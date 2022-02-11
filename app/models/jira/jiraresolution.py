from typing import Optional


class JiraResolution:
    description: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    self_url: Optional[str] = None

    def __init__(self, raw: dict):
        if raw['description']:
            self.description = raw['description']
        if raw['id']:
            self.id = raw['id']
        if raw['name']:
            self.name = raw['name']
        if raw['self']:
            self.self_url = raw['self']
