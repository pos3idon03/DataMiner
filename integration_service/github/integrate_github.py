import subprocess
import os
import logging
import git

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clone_repo(repo_url) -> None:
    logger.info(f"Starting clone task for: {repo_url}")
    try:
        system_name = repo_url.split("/")[-1]
        repo_path = os.path.join(f"./github/repos/{system_name}")
        log_path = os.path.join(f"./github/logs/{system_name}")
        if not os.path.exists(repo_path):
            logger.info(f"Repo {repo_url} not found")
            subprocess.run(["mkdir", "-p", repo_path], check=True)
            subprocess.run(["mkdir", "-p", log_path], check=True)
            subprocess.run(['git', 'clone', repo_url], cwd=repo_path, check=True)
            logger.info(f"Cloned repository: {repo_url}")
            export_log(repo_path, system_name)       
            logger.info(f": {repo_url}")
            #remove_repo(system_name)
            #logger.info(f"Deleted repository: {repo_url}")
        else:
            logger.info(f"Repo {repo_url} found")
            #remove_repo(system_name)
            #logger.info(f"Deleted repository: {repo_url}")
        return repo_path
    except subprocess.CalledProcessError as e:
        logger.info(f"Error cloning repository '{repo_url}': {e}")


def export_log(repo_path, system_name):
    log_file = os.path.join(f"./github/logs/{system_name}/{system_name}.log")
    with open(log_file, 'w') as log_file:
        subprocess.run(['git', 'log'], cwd=repo_path, stdout=log_file, stderr=subprocess.PIPE, check=True)
        # g = git.Git(os.path.join(f"{repo_path}/{system_name}"))
        # log_file.write(
        #     g.log(
        #         '--pretty=format:"%h - %an, %ad : %s" --date=short',
        #         '--numstat',
        #         '--summary',
        #         '--no-merges'
        #     )
        # )
    logger.info(f"Log exportedfor system: {system_name}")

def check_for_system(system_name):
    log_path = os.path.join(f"./github/logs/{system_name}")
    if not os.path.exists(log_path):
        logger.info(f"Log {system_name} not found")
        return False
    else:
        logger.info(f"Log {system_name} found")
        return True

def remove_repo(system_name)-> None:
    try:
        if os.path.exists(f"./repos/{system_name}"):
            subprocess.run(['rm', '-rf', f"./repos/{system_name}"])
            print(f"Removed folder: ./repos/{system_name}")
        else:
            print(f"Folder ./repos/{system_name} does not exist.")
    except Exception as e:
        print(f"Error removing repository '{system_name}': {e}")
        
# repo_url = "https://github.com/Software-Improvement-Group/sigridci"