from typing import Optional


class JiraProject:
    id: Optional[int] = None
    key: Optional[str] = None
    name: Optional[str] = None
    project_type_key: Optional[str] = None
    simplified: Optional[bool] = None
    self_url: Optional[str] = None

    def __init__(self, raw: dict):
        if raw['id']:
            self.id = int(raw['id'])
        if raw['key']:
            self.key = raw['key']
        if raw['name']:
            self.name = raw['name']
        if raw['projectTypeKey']:
            self.project_type_key = raw['projectTypeKey']
        if raw['simplified']:
            self.simplified = bool(raw['simplified'])
        if raw['self']:
            self.self_url = raw['self']

