import os
import logging
from continuous_translation.translation import get_prompt_based_on_file_type, translate


def merge_paragraphs(paragraphs, max_length):
    merged = []
    current_paragraph = ""

    for paragraph in paragraphs:
        if len(current_paragraph) + len(paragraph) + 1 <= max_length:
            current_paragraph += paragraph + "\n"
        else:
            merged.append(current_paragraph.strip())
            current_paragraph = paragraph + "\n"

    if current_paragraph.strip():
        merged.append(current_paragraph.strip())

    return merged


def translate_files(repo_path, source_language, target_language, api_key, additional_prompt=""):
    return process_files(repo_path, source_language, target_language, api_key, translate, additional_prompt)

def process_files(repo_path: str, source_language: str, target_language: str, api_key: str, translate_func: str, additional_prompt: str):
    # 遍历文件
    for root, _, files in os.walk(repo_path):
        for file in files:
            if not file.endswith((".md", ".rst", ".txt", ".py", ".js", ".json", ".html", ".cpp", ".c", ".ipynb")):
                continue
            file_path = os.path.join(root, file)
            logging.info(f"Processing file: {file_path}")
            with open(file_path, "r") as f:
                content = f.read()

            file_type_prompt = get_prompt_based_on_file_type(
                file_path) + additional_prompt

            # 将文本拆分为段落并跟踪换行符数量
            paragraphs = content.split("\n")

            # 合并较小的段落
            merged_paragraphs = merge_paragraphs(paragraphs, 2048)

            translated = ""
            for merged_paragraph in merged_paragraphs:
                translated_merged_paragraph = translate_func(
                    merged_paragraph, source_language, target_language, api_key, file_type_prompt)
                # 合并的翻译段落
                translated += translated_merged_paragraph

            logging.info("Translation completed.")

            # 保存翻译后的文件
            translated_file_path = os.path.join(root, f"{file}")


            logging.info(f"Saving translated file: {translated_file_path}")
            with open(translated_file_path, "w") as f:
                f.write(translated)
            logging.info("File saved.")
