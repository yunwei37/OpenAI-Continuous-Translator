import os
from unittest import TestCase
from continuous_translation.config import load_config

class TestConfig(TestCase):
    def test_config_values(self):
        os.environ["INPUT_GIT_REPO_URL"] = "https://github.com/test/test-repo.git"
        os.environ["INPUT_SOURCE_LANGUAGE"] = "en"
        os.environ["INPUT_TARGET_LANGUAGE"] = "zh"
        os.environ["INPUT_API_KEY"] = "test-api-key"
        os.environ["INPUT_ADDITIONAL_PROMPT"] = "translate this"

        config = load_config()

        self.assertEqual(config["GIT_REPO_URL"], "https://github.com/test/test-repo.git")
        self.assertEqual(config["SOURCE_LANGUAGE"], "en")
        self.assertEqual(config["TARGET_LANGUAGE"], "zh")
        self.assertEqual(config["API_KEY"], "test-api-key")
        self.assertEqual(config["ADDITIONAL_PROMPT"], "translate this")
