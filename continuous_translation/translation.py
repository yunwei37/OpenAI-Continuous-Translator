import logging
import time
import openai

MARKDOWN_PROMPT = """
Your task is to translate a Markdown file, while preserving the original formatting,
including inline elements like links and images. Make sure to ignore HTML tags and code blocks,
but translate code comments. Be cautious when translating Markdown links,
Markdown images, and Markdown headings. Make sure TOC links like (#content) are translated.
"""

RST_PROMPT = """
Your task is to translate reStructuredText files, while preserving the original formatting,
including inline elements like links and images. Make sure to ignore HTML tags and code blocks,
but translate code comments. Be cautious when translating reStructuredText links,
reStructuredText images, and reStructuredText headings.
"""

HTML_PROMPT = """
Your task is to translate an HTML file, while preserving the original structure and formatting.
Make sure to translate the content inside HTML tags, but leave the tag names and attributes unchanged.
Be cautious when translating links, images, and headings.
"""

NOTEBOOK_PROMPT = """
Your task is to translate a Jupyter Notebook file, while preserving the original structure and formatting.
Make sure to translate the content in Markdown and raw text cells, but leave the code cells unchanged,
except for code comments, which should be translated. Be cautious when translating links, images, and headings.
"""

PYTHON_CODE_PROMPT = """
Your task is to translate code comments, while preserving the original code formatting.
Make sure to translate the content inside code comments, but leave the code unchanged.
Be cautious when translating imports, variables, and keywords.
"""

CODE_PROMPT = """
Your task is to translate code comments, while preserving the original code formatting.
Make sure to translate the content inside code comments, but leave the code unchanged.
Be cautious when translating imports, variables, and keywords.
"""

def get_prompt_based_on_file_type(file_path: str) -> str:
    if file_path.endswith(".txt"):
        return "Your task is to translate structured text. This is a txt file."
    elif file_path.endswith((".md", ".mdx")):
        return MARKDOWN_PROMPT
    elif file_path.endswith(".rst"):
        return RST_PROMPT
    elif file_path.endswith(".html") or file_path.endswith(".htm"):
        return HTML_PROMPT
    elif file_path.endswith(".ipynb"):
        return NOTEBOOK_PROMPT
    elif file_path.endswith(".py"):
        return PYTHON_CODE_PROMPT
    else:
        return CODE_PROMPT + f"The file name is {file_path}. You can infer the file type from the file name."

def translate(text: str, source_language: str, target_language: str, api_key: str, file_prompt="") -> str:
    openai.api_key = api_key
    retries = 3
    while retries > 0:
        try:
            system_prompt = f"You are a helpful assistant that translates {source_language} to {target_language}. {file_prompt}"
            user_prompt = f"""Instructions: Translate the following {source_language} text to {target_language} 
while maintaining the original formatting: "{text}".
format: Return only the translated content, not including the original text."""
            logging.info(f"Translating paragraphs: {text}")
            logging.info(f"System prompt: {system_prompt}")
            logging.info(f"User prompt: {user_prompt}")

            time.sleep(3)  # Sleep for 3 seconds before each API call
            # 调用 ChatGPT API
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    }
                ],
            )
            t_text = (
                completion["choices"][0]
                .get("message")
                .get("content")
                .encode("utf8")
                .decode()
            )
            result = t_text.strip()
            logging.info(f"Translated paragraphs: {result}")
            return result
        except Exception as e:
            retries -= 1
            wait_time = 60
            logging.warning(
                f"Error occurred: {e}. Waiting for 60 seconds. Retries remaining: {retries}.")
            time.sleep(wait_time)

    logging.error(
        "Failed to translate text after 3 retries due to rate limit.")
    return None  # Return None if all retries have been exhausted
