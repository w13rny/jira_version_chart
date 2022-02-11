import os
from typing import Optional

from app.models.jira.jiraissuetype import JiraIssueType


class JiraEpic:
    key: str = ''
    summary: str = ''
    issue_type: Optional[JiraIssueType] = None

    def __init__(self, raw: dict):
        self.key = raw['key']
        self.issue_type = JiraIssueType(raw['fields']['issuetype'])
        self.summary = raw['fields']['summary']

    @property
    def url(self) -> str:
        return os.environ.get('JIRA_URL') + '/browse/' + self.key
