import os
import random
import re
from enum import Enum
from typing import List, Tuple


RANDOM_MATCH_CHANCE = 0.95  # ~95% chance


class MatchMaker:
    def __init__(self):
        self._whitelist = None
        self._starlist = None
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
    def starlist(self) -> List[str]:
        if self._starlist is None:
            self._starlist = self._read_preferences("starlist.txt")
        return self._starlist

    @property
    def blacklist(self) -> List[str]:
        if self._blacklist is None:
            self._blacklist = self._read_preferences("blacklist.txt")
        return self._blacklist

    def _bio_has_term(self, bio: str, term: str) -> bool:
        pattern = re.compile(rf"\b{term}\b")
        return pattern.search(bio) is not None

    def should_like(self, bio: str) -> Tuple[bool, str]:
        if not bio:
            return False, f"Has no bio"

        for term in self.blacklist:
            if self._bio_has_term(bio, term):
                return False, f'Info matches blacklist term: "{term}"'

        for term in self.whitelist:
            if self._bio_has_term(bio, term):
                return True, f'Info matches whitelist term: "{term}"'

        if random.random() < RANDOM_MATCH_CHANCE:
            return True, f"Random chance success"
        else:
            return False, f"Random chance fail"

    def should_super_like(self, bio: str) -> Tuple[bool]:
        if not bio:
            return False, f"Has no bio"

        for term in self.starlist:
            if self._bio_has_term(bio, term):
                return True, f'Info matches starlist term: "{term}"'

        return False, f"Does not match starlist terms"
