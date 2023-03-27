import os
from unittest import TestCase
from continuous_translation.config import load_config

class TestConfig(TestCase):
    def test_config_values(self):
        os.environ["GIT_REPO_URL"] = "https://github.com/test/test-repo.git"
        os.environ["SOURCE_LANGUAGE"] = "en"
        os.environ["TARGET_LANGUAGE"] = "zh"
        os.environ["API_KEY"] = "test-api-key"

        config = load_config()

        self.assertEqual(config["GIT_REPO_URL"], "https://github.com/test/test-repo.git")
        self.assertEqual(config["SOURCE_LANGUAGE"], "en")
        self.assertEqual(config["TARGET_LANGUAGE"], "zh")
        self.assertEqual(config["API_KEY"], "test-api-key")