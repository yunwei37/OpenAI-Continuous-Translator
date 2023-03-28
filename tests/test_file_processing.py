import os
import tempfile
from unittest import TestCase
from continuous_translation import file_processing

# 定义简单的翻译函数
def simple_translate(text, source_language, target_language, api_key, prompt):
    return text.replace("test", "测试").replace("Test", "测试")

CONFIG_TEST = {
    "SOURCE_LANGUAGE": "en",
    "TARGET_LANGUAGE": "zh",
    "API_KEY": "test",
    "I18N_SURFIX": "",
    "ADDITIONAL_PROMPT": "",
    "FILE_PATHS_FILTER": ".*",
    "FILE_TYPES": "md,rst,txt,py,js,json,html,cpp,c,ipynb"
}

class TestFileProcessing(TestCase):

    def test_process_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # 创建用于测试的文件
            test_files = {
                "test.txt": "This is a test file.",
                "test.md": "# This is a test markdown file\n\nThis is a test paragraph.",
                "test.rst": "Test\n====\n\nThis is a test reStructuredText file.",
                "test.py": "# This is a test Python file\nprint('Hello, World!')",
                "test.js": "// This is a test JavaScript file\nconsole.log('Hello, World!');"
            }

            for filename, content in test_files.items():
                file_path = os.path.join(tmpdir, filename)
                with open(file_path, "w") as f:
                    f.write(content)
            # 调用 process_files 函数
            file_processing.process_files(tmpdir, CONFIG_TEST, simple_translate)

            # 检查翻译后的文件是否存在并验证其内容
            for filename, original_content in test_files.items():
                translated_file_path = os.path.join(tmpdir, filename)
                self.assertTrue(os.path.exists(translated_file_path))

                # 检查翻译后的文件内容
                with open(translated_file_path, "r") as f:
                    content = f.read()
                expected_content = original_content.replace(
                    "test", "测试").replace("Test", "测试")
                self.assertEqual(content, expected_content)

    def test_process_files_complex(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # 创建用于测试的文件
            test_file = "test_complex.md"
            test_file_path = os.path.join(tmpdir, test_file)
            with open(test_file_path, "w") as f:
                f.write(
                    "This is a test file.\n\n\nThis is another paragraph.\n\nThis is a third paragraph.")

            # 调用 process_files 函数
            file_processing.process_files(
                tmpdir, CONFIG_TEST, simple_translate)

            # 检查翻译后的文件是否存在
            translated_file_path = os.path.join(tmpdir, test_file)
            self.assertTrue(os.path.exists(translated_file_path))

            # 检查翻译后的文件内容
            with open(translated_file_path, "r") as f:
                content = f.read()
            self.assertEqual(
                content, "This is a 测试 file.\n\n\nThis is another paragraph.\n\nThis is a third paragraph.")

    def test_file_path_filter(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # 创建用于测试的文件
            test_files = {
                "test.md": "This is a test file.",
                "test.jpg": "This is a test image file.",
                ".gitignore": "This is a test gitignore file.",
                "ssss": "This is a test file.",
            }

            for filename, content in test_files.items():
                file_path = os.path.join(tmpdir, filename)
                with open(file_path, "w") as f:
                    f.write(content)

            # 调用 process_files 函数
            file_processing.process_files(
                tmpdir, CONFIG_TEST, simple_translate)

            # 检查翻译后的文件是否存在并验证其内容
            for filename, original_content in test_files.items():
                translated_file_path = os.path.join(tmpdir, filename)
                if filename.endswith(".md"):
                    self.assertTrue(os.path.exists(translated_file_path))

                    # 检查翻译后的文件内容
                    with open(translated_file_path, "r") as f:
                        content = f.read()
                    expected_content = original_content.replace(
                        "test", "测试").replace("Test", "测试")
                    self.assertEqual(content, expected_content)
                else:
                    with open(translated_file_path, "r") as f:
                        content = f.read()
                    self.assertEqual(content, original_content)
