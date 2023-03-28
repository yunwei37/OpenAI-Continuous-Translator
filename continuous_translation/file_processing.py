import os
import logging
import re
from continuous_translation.translation import get_prompt_based_on_file_type, translate

# 合并较小的段落
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

# 翻译文件
def translate_files(repo_path, config):
    return process_files(repo_path, config, translate)

# 处理文件并翻译
def process_files(repo_path: str, config, translate_func: str):
    source_language: str = config["SOURCE_LANGUAGE"]
    target_language: str = config["TARGET_LANGUAGE"]
    api_key: str = config["API_KEY"]
    additional_prompt: str = config["ADDITIONAL_PROMPT"]
    # 遍历文件
    for root, _, files in os.walk(repo_path):
        for file in files:
            if re.match(config["FILE_PATHS_FILTER"], file) is None:
                continue
            if not file.endswith(tuple(config["FILE_TYPES"].split(","))):
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

# remove .git folder and move files to root
def move_files_to_target(repo_path, target_path):
    os.system(f"rm -rf {repo_path}/.git && mv {repo_path}/* {target_path} && rm -rf {repo_path}")
