from typing import List, Dict
from collections import defaultdict

def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:
    new_d = {}
    for i,x in zip(names,scores):
        new_d = {i,x}
    return new_d


# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
