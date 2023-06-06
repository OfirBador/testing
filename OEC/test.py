import requests

# Perform checks and determine which workflow to trigger
chosen_workflow = "test1.yml"

# Trigger the chosen workflow using the GitHub API
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "Bearer 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"
}
repo_owner = "OfirBador"
repo_name = "testing"
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/actions/workflows/{chosen_workflow}/dispatches"
response = requests.post(api_url, headers=headers)

if response.status_code == 204:
    print("Workflow run triggered successfully.")
else:
    print("Failed to trigger the workflow run.")
