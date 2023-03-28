import pytest
import os
from continuous_translation import git_integration

# 配置
git_repo_url = "https://github.com/radi-cho/awesome-gpt4"
local_repo_path = "test_repo"

@pytest.fixture(scope="module")
def repo():
    if os.path.exists(local_repo_path):
        git_integration.delete_local_repository(local_repo_path)
    git_integration.clone_repository(git_repo_url, local_repo_path)
    git_integration.delete_local_repository(local_repo_path)
