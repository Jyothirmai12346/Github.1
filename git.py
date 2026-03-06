import requests

# GitHub API URL for Microsoft repositories
url = "https://api.github.com/orgs/microsoft/repos"

# Send GET request to GitHub API
response = requests.get(url)

# Convert response to JSON format
repos = response.json()

# Print repository names
print("Microsoft Open Source Repositories:\n")

for repo in repos:
    print(repo["name"])
