from typing import List

from app.models.jira.jira_component import JiraComponent
from app.models.report.issue_list import IssueList
from app.models.jira.jira_issue import JiraIssue


def has_component(issue: JiraIssue, component_name: str) -> bool:
    if issue.components:
        for component in issue.components:
            if component.name == component_name:
                return True
        return False
    else:
        return False


class Report:
    jql_query: str = None
    all_components: List[JiraComponent] = None
    all_issues: IssueList = None
    issues_with_components: List[IssueList] = None
    issues_without_components: IssueList = None

    def __init__(self, issues: dict, jql_query: str):
        self.jql_query = jql_query
        self.all_components = []

        all_issues_list = []
        for issue in issues:
            obj = JiraIssue(issue)
            all_issues_list.append(obj)
            if obj.components:
                for component in obj.components:
                    if component not in self.all_components:
                        self.all_components.append(component)

        self.all_issues = IssueList('Wszystkie zadania', all_issues_list)

        self.issues_with_components = []
        for component in self.all_components:
            issue_filter = filter(lambda x: has_component(x, component.name), all_issues_list)
            self.issues_with_components.append(IssueList(component.name, list(issue_filter)))

        issues_without_components_filter = filter(lambda x: not x.components, all_issues_list)
        self.issues_without_components = IssueList('Zadania bez komponentów', list(issues_without_components_filter))
