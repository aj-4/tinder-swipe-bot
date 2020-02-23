import os
import random
from enum import Enum
from typing import List, Tuple


RANDOM_MATCH_CHANCE = 0.7


class MatchMaker:
    def __init__(self):
        self._whitelist = None
        self._blacklist = None

    def _read_preferences(self, filename) -> List[str]:
        pref_path = os.path.join(os.getcwd(), filename)
        with open(pref_path, "r") as f:
            terms = f.read().split("\n")[:-1]
        return terms

    @property
    def whitelist(self) -> List[str]:
        if self._whitelist is None:
            self._whitelist = self._read_preferences("whitelist.txt")
        return self._whitelist

    @property
    def blacklist(self) -> List[str]:
        if self._blacklist is None:
            self._blacklist = self._read_preferences("blacklist.txt")
        return self._blacklist

    def should_like(self, bio: str) -> Tuple[bool, str]:
        if not bio:
            return False, f"Has no bio"

        for term in self.blacklist:
            if term in bio:
                return False, f'Info matches blacklist term: "{term}"'

        for term in self.whitelist:
            if term in bio:
                return True, f'Info matches whitelist term: "{term}"'

        if random.random() < RANDOM_MATCH_CHANCE:
            return True, f"Random chance success"
        else:
            return False, f"Random chance fail"
