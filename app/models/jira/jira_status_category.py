from typing import Optional


class JiraStatusCategory:
    id: Optional[int] = None
    key: Optional[str] = None
    color_name: Optional[str] = None
    name: Optional[str] = None
    self_url: Optional[str] = None

    def __init__(self, raw: dict):
        if raw['id']:
            self.id = int(raw['id'])
        if raw['key']:
            self.key = raw['key']
        if raw['colorName']:
            self.color_name = raw['colorName']
        if raw['name']:
            self.name = raw['name']
        if raw['self']:
            self.self_url = raw['self']
