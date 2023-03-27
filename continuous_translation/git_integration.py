import os
import pygit2
import logging

def clone_repository(repo_url, local_path):
    """
    克隆远程仓库到本地路径。
    """
    if not os.path.exists(local_path):
        logging.info("Cloning repository...")
        repo = pygit2.clone_repository(repo_url, local_path)
        logging.info(f"Repository cloned to {local_path}.")
    else:
        logging.warning("local_repo already exists, skipping the clone process.")
        repo = pygit2.Repository(local_path)
    return repo

def commit_changes(repo, commit_message):
    """
    提交本地仓库的更改，并将它们推送到远程仓库。
    """
    repo.index.add_all()
    repo.index.write()

    user = repo.default_signature
    tree = repo.index.write_tree()
    oid = repo.create_commit('refs/heads/master', user, user, commit_message, tree, [repo.head.target])

def delete_local_repository(local_path):
    """
    删除本地仓库。
    """
    if os.path.exists(local_path):
        if os.name == 'nt':  # 如果是 Windows 系统
            os.system(f'rmdir /s /q "{local_path}"')
        else:
            os.system(f'rm -rf "{local_path}"')
