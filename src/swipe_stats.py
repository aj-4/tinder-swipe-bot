import json
import os
from typing import Dict, List


class SwipeStats:
    def __init__(self):
        self._swipes = None

    def _read_file(self, filename) -> List[str]:
        pref_path = os.path.join(os.getcwd(), filename)
        with open(pref_path, "r") as f:
            lines = f.read().split("\n")[:-1]
        return lines

    @property
    def swipes(self):
        if not self._swipes:
            swipes = []
            for idx, json_line in enumerate(self._read_file("swipes.log")):
                try:
                    swipe = json.loads(json_line)
                    swipes.append(swipe)
                except json.decoder.JSONDecodeError:
                    # I originally forgot to json.dumps(). Skip bad dumps.
                    print(f"[{idx+1}] {json_line}\n")
                    pass
            self._swipes = swipes
        return self._swipes

    def get_stats(self) -> Dict:
        total = len(self.swipes)
        avg_age = sum([s["age"] for s in self.swipes if s["age"] >= 0]) / total
        pct_likes = sum([1 for s in self.swipes if s["like"]]) / total
        pct_super_likes = (
            sum([1 for s in self.swipes if s["super_like"]]) / total
        )
        pct_no_bio = (
            sum([1 for s in self.swipes if s["reason"] == "Has no bio"])
            / total
        )

        return {
            "total": total,
            "avg_age": avg_age,
            "pct_likes": pct_likes,
            "pct_super_likes": pct_super_likes,
            "pct_no_bio": pct_no_bio,
        }


if __name__ == "__main__":
    stats = SwipeStats()
    print(stats.get_stats())
