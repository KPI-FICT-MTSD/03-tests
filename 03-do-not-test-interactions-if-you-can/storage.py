from typing import List, Optional


class Storage:

    def __init__(self):
        self._kv = {}

    def put(self, account: dict):
        # username = account["username"]
        # if username not in self._kv:
        #     self._kv[username] = account
        pass

    def find_by_username(self, username: str) -> Optional[dict]:
        return self._kv.get(username)

    def list_all(self) -> List[dict]:
        return list(self._kv.values())
