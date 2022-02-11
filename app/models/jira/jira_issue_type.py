from typing import Optional


class JiraIssueType:
    description: Optional[str] = None
    hierarchy_level: Optional[int] = None
    icon_url: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    self_url: Optional[str] = None
    subtask: Optional[bool] = None

    def __init__(self, raw: dict):
        if raw['description']:
            self.description = raw['description']
        if raw['hierarchyLevel']:
            self.hierarchy_level = raw['hierarchyLevel']
        if raw['iconUrl']:
            self.icon_url = raw['iconUrl']
        if raw['id']:
            self.id = raw['id']
        if raw['name']:
            self.name = raw['name']
        if raw['self']:
            self.self_url = raw['self']
        if raw['subtask']:
            self.subtask = raw['subtask']
