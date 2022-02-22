import os

from atlassian import Jira
from dotenv import load_dotenv
from flask import Flask, render_template

from app.models.report.report import Report

app = Flask(__name__)
load_dotenv()
jira = Jira(
    url=os.environ.get('JIRA_URL'),
    username=os.environ.get('JIRA_USERNAME'),
    password=os.environ.get('JIRA_API_TOKEN'),
    cloud=True
)


@app.route("/")
def report_page():
    jql_query = os.environ.get('JQL_QUERY')
    start_at = 0
    issues = []
    while True:
        request = jira.jql(jql_query, start=start_at, limit=200)
        issues = issues + request['issues']
        start_at = request['startAt']
        max_results = request['maxResults']
        total = request['total']
        if start_at + max_results < total:
            start_at = start_at + max_results
        else:
            break
    report = Report(issues, jql_query)
    return render_template('report.html', data=report)
