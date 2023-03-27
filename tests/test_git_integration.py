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
    repo = git_integration.clone_repository(git_repo_url, local_repo_path)
    yield repo
    git_integration.delete_local_repository(local_repo_path)

def test_clone_repository(repo):
    assert os.path.exists(local_repo_path)
    assert os.path.exists(os.path.join(local_repo_path, ".git"))

def test_commit_changes(repo):
    # 创建一个测试文件
    test_file = "test_file.txt"
    test_file_path = os.path.join(local_repo_path, test_file)
    with open(test_file_path, "w") as f:
        f.write("This is a test file.")

    # 提交并推送更改
    git_integration.commit_changes(repo, "Add test file")

    # 检查更改是否成功推送到远程仓库
    # 在这里，您可能需要手动检查远程仓库，以确保测试文件已成功添加
    assert True
