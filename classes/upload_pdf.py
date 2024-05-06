import requests

def upload_to_github(token, repo_owner, repo_name, file_path, file_content="bill", branch='add-cli'):
    headers = {
        'Authorization': 'token ' + token,
        'Content-Type': 'application/json',
    }

    # Get the current commit SHA for the branch
    get_branch_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/branches/{branch}'
    response = requests.get(get_branch_url, headers=headers)
    commit_sha = response.json()['commit']['sha']

    # Create a new file on GitHub
    create_file_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
    payload = {
        'message': 'Upload file',
        'content': file_content,
        'branch': branch,
        'sha': commit_sha
    }
    response = requests.put(create_file_url, headers=headers, json=payload)

    if response.status_code == 201:
        print("\n\nFile uploaded successfully.")
    else:
        print("\n\nError uploading file:")
        print(response.json())