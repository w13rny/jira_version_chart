from typing import List, Optional

from app.models.jira.jira_issue import JiraIssue


class IssueList:
    issues: List[JiraIssue] = None
    name: str = None

    def __init__(self, name: str, issues: List[JiraIssue] = None):
        self.issues = sorted(issues, key=lambda x: x.status_category.key)
        self.name = name

    @property
    def all_story_points(self) -> float:
        value = 0.0
        for issue in self.issues:
            if issue.story_points:
                value += issue.story_points
        return value

    @property
    def resolved_story_points(self) -> float:
        value = 0.0
        for issue in self.issues:
            if issue.story_points and issue.resolution_date:
                value += issue.story_points
        return value

    @property
    def story_points_in_progress(self) -> float:
        value = 0.0
        for issue in self.issues:
            if issue.story_points and issue.status_category.key.upper() not in ['NEW', 'DONE']:
                value += issue.story_points
        return value

    @property
    def percent_resolved(self) -> Optional[float]:
        if self.all_story_points == 0:
            return 100.0
        else:
            return self.resolved_story_points/self.all_story_points*100
