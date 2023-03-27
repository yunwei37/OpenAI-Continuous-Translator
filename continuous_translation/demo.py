import os
import pygit2
import openai
import logging
import re
import time

# 配置日志
logging.basicConfig(level=logging.INFO)

# 配置
git_repo_url = "https://github.com/promptslab/Awesome-Prompt-Engineering"
source_language = "en"
target_language = "zh"
api_key = "xxx"

# 设置 OpenAI API 密钥
openai.api_key = api_key

local_repo_path = "local_repo"

# 检查目录是否存在
if not os.path.exists(local_repo_path):
    logging.info("Cloning repository...")
    # 克隆仓库
    repo = pygit2.clone_repository(git_repo_url, local_repo_path)
    repo_path = repo.workdir
    logging.info(f"Repository cloned to {local_repo_path}.")
else:
    logging.warning("local_repo already exists, skipping the clone process.")
    repo_path = local_repo_path

def translate(text):
    retries = 3
    while retries > 0:
        try:
            time.sleep(3)  # Sleep for 3 seconds before each API call
            # 调用 ChatGPT API
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that translates English to Chinese. Your task is to translate structured text such as Markdown, HTML, and code comments, while preserving the original formatting, including inline elements like links and images. Make sure to ignore HTML tags and code blocks, but translate code comments. Be cautious when translating Markdown links, images, and headings."
                    },
                    {
                        "role": "user",
                        "content": f'Translate the following English text to Chinese while maintaining the original formatting: "{text}". Return only the translated content, not including the original text.'
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
            return t_text.strip()
        except Exception as e:
            retries -= 1
            wait_time = 60
            logging.warning(f"Error occurred: {e}. Waiting for 60 seconds. Retries remaining: {retries}.")
            time.sleep(wait_time)

    logging.error("Failed to translate text after 3 retries.")
    return None  # Return None if all retries have been exhausted

# 遍历文件
for root, _, files in os.walk(repo_path):
    for file in files:
        # 根据文件类型过滤
        if file.endswith((".txt", ".md", ".rst")):
            file_path = os.path.join(root, file)
            logging.info(f"Processing file: {file_path}")
            with open(file_path, "r") as f:
                content = f.read()

            # 将文本拆分为段落
            paragraphs = re.split(r'\n{2,}', content)

            translated_paragraphs = []
            for paragraph in paragraphs:
                translated_paragraph = translate(paragraph)
                translated_paragraphs.append(translated_paragraph)
                logging.info(f"Translated paragraph: {translated_paragraph}")

            # 将翻译好的段落拼接回文本
            t_text = '\n\n'.join(translated_paragraphs)
            logging.info("Translation completed.")

            # 保存翻译后的文件
            translated_file_path = os.path.join(root, f"{file}")
            logging.info(f"Saving translated file: {translated_file_path}")
            with open(translated_file_path, "w") as f:
                f.write(t_text)
            logging.info("File saved.")
