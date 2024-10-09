import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clone_repo(repo_url) -> None:
    logger.info(f"Starting clone task for: {repo_url}")
    try:
        system_name = repo_url.split("/")[-1]
        if not os.path.exists(f"./gitlab/repos/{system_name}"):
            logger.info(f"Repo {repo_url} not found")
            subprocess.run(["mkdir", "-p", f"./gitlab/repos/{system_name}"], check=True)
            subprocess.run(['git', 'clone', repo_url], cwd=f"./gitlab/repos/{system_name}", check=True)
            logger.info(f"Cloned repository: {repo_url}")
            #remove_repo(system_name)
            #logger.info(f"Deleted repository: {repo_url}")
        else:
            logger.info(f"Repo {repo_url} found")
            #remove_repo(system_name)
            #logger.info(f"Deleted repository: {repo_url}")
        
    except subprocess.CalledProcessError as e:
        logger.info(f"Error cloning repository '{repo_url}': {e}")

def remove_repo(system_name)-> None:
    try:
        if os.path.exists(f"./repos/{system_name}"):
            subprocess.run(['rm', '-rf', f"./gitlab/repos/{system_name}"])
            print(f"Removed folder: ./gitlab/repos/{system_name}")
        else:
            print(f"Folder ./gitlab/repos/{system_name} does not exist.")
    except Exception as e:
        print(f"Error removing repository '{system_name}': {e}")