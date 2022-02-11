# Jira Version Chart

This script creates website with basic stats of each component in your Jira project.

All you must do is provide Jira data (URL, user name & API token) and JQL query for issues which will be used for creating stats page.


## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Configuration

Create .env file in main directory and fill it with following data:

```
# JIRA URL - e.g. 'https://company.atlassian.net/'
export JIRA_URL=''

# JIRA_USERNAME - e.g. 'john.smith@company.com'
export JIRA_USERNAME=''

# JIRA_API_TOKEN - get it from https://id.atlassian.com/manage-profile/security/api-tokens
export JIRA_API_TOKEN=''

# JQL_QUERY - e.g. 'project = "Example Project" AND fixVersion = MVP AND issuetype not in (Sub-task, Sub-Bug) ORDER BY Rank ASC'
export JQL_QUERY=''
```

## Run script
### Run Flask for develop
```
$ python wsgi.py
```
Website shoud run on ``http://127.0.0.1:5000``
