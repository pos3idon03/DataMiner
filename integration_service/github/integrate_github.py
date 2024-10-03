import subprocess
import os

def clone_repo(repo_url) -> None:
    print(repo_url)
    try:
        system_name = repo_url.split("/")[-1]
        if not os.path.exists(f"./repos/{system_name}"):
            os.makedirs(f"./repos/{system_name}")
            print(f"Created folder: ./repos/{system_name}")
            subprocess.run(['git', 'clone', repo_url, f"./repos/{system_name}"], check=True)
            print("clone done")
            remove_repo(system_name)
            print("repo deleted")
        else:
            print(f"Folder ./repos/{system_name} already exists.")
            remove_repo(system_name)
            print("repo deleted")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository '{repo_url}': {e}")

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