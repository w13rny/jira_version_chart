import os
from datetime import datetime
from typing import Optional, List
import arrow

from app.models.jira.jira_component import JiraComponent
from app.models.jira.jira_epic import JiraEpic
from app.models.jira.jira_issue_type import JiraIssueType
from app.models.jira.jira_project import JiraProject
from app.models.jira.jira_resolution import JiraResolution
from app.models.jira.jira_status import JiraStatus
from app.models.jira.jira_status_category import JiraStatusCategory


class JiraIssue:
    key: str = ''
    summary: str = ''
    status: Optional[JiraStatus] = None
    status_category: Optional[JiraStatusCategory] = None
    story_points: Optional[float] = None
    issue_type: Optional[JiraIssueType] = None
    resolution: Optional[JiraResolution] = None
    resolution_date: Optional[datetime] = None
    components: Optional[List[JiraComponent]] = None
    parent: Optional[JiraEpic] = None
    project: Optional[JiraProject] = None

    def __init__(self, raw: dict):
        self.key = raw['key']
        self.issue_type = JiraIssueType(raw['fields']['issuetype'])
        self.summary = raw['fields']['summary']
        if raw['fields']['status']:
            self.status = JiraStatus(raw['fields']['status'])
        if raw['fields']['status']['statusCategory']:
            self.status_category = JiraStatusCategory(raw['fields']['status']['statusCategory'])
        if raw['fields']['customfield_10014']:
            self.story_points = raw['fields']['customfield_10014']
        if raw['fields']['resolution']:
            self.resolution = JiraResolution(raw['fields']['resolution'])
        if raw['fields']['resolutiondate']:
            parsed_data = arrow.get(raw['fields']['resolutiondate'])
            self.resolution_date = parsed_data.datetime
        if raw['fields']['components']:
            self.components = []
            for component in raw['fields']['components']:
                self.components.append(JiraComponent(component))
        try:
            if raw['fields']['parent'] and not self.issue_type.subtask:
                self.parent = JiraEpic(raw['fields']['parent'])
        except KeyError:
            self.parent = None
        if raw['fields']['project']:
            self.project = JiraProject(raw['fields']['project'])

    @property
    def url(self) -> str:
        return os.environ.get('JIRA_URL') + '/browse/' + self.key
