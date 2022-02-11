# Jira Version Chart

This app creates simple web page that shows basic stats for components in your Jira project.


All you must do is provide Jira data (URL, user name & API token) and JQL query for all issues you want to analyse.


## Installation
### Quick way

Just clone this repository and install with pip:

```
git clone https://github.com/w13rny/jira_version_chart.git
pip install -r requirements.txt
```

### Reccomended way

Use `virtualenv` to create isolated Python environment for this app.

1. Install `virtualenv` if you don't have it:

```
pip install virtualenv
```

2. Clone this repository and create a virtual environment:

```
git clone https://github.com/w13rny/jira_version_chart.git
cd jira_version_chart
virtualenv venv
```

3. Activate virtual environment and install the python dependencies:

```
source venv/bin/activate
pip install -r requirements.txt
```

## Configuration

Create `.env` file in main directory and fill it with following data:

```
# JIRA URL - e.g. 'https://company.atlassian.net/'
JIRA_URL=''

# JIRA_USERNAME - e.g. 'john.smith@company.com'
JIRA_USERNAME=''

# JIRA_API_TOKEN - get it from https://id.atlassian.com/manage-profile/security/api-tokens
JIRA_API_TOKEN=''

# JQL_QUERY - e.g. 'project = "Example Project" AND fixVersion = MVP AND issuetype not in (Sub-task, Sub-Bug) ORDER BY Rank ASC'
JQL_QUERY=''
```

## Run app
### Run Flask for develop
```
$ python wsgi.py
```
Website should run on `http://127.0.0.1:5000`
