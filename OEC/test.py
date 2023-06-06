import requests
import argparse

def get_cli_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--git_secret', required=True, dest='git_secret', help='GIT_TOKEN'
    )
    return parser.parse_args()


def main():
    args = get_cli_args()
    git_secret = args.git_secret
    print("in")
    # Perform checks and determine which workflow to trigger
    chosen_workflow = "test1.yml"

    # Trigger the chosen workflow using the GitHub API
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {git_secret}"
    }
    repo_owner = "OfirBador"
    repo_name = "testing"
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{chosen_workflow}/dispatches"
    response = requests.post(api_url, headers=headers)

    if response.status_code == 204:
        print("Workflow run triggered successfully.")
    else:
        print("Failed to trigger the workflow run.")

if __name__ == '__main__':
    main()
