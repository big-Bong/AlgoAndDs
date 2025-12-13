from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    grouping = {}

    for word in strs:
        key = "".join(sorted(word))
        if key in grouping:
            grouping[key].append(word)
        else:
            grouping[key] = [word]

    output = []
    for val in grouping.values():
        output.append(val)

    return output

def groupAnagrams_cleaner(strs: List[str]) -> List[List[str]]:
    grouping = defaultdict(list)

    for word in strs:
        key = "".join(sorted(word))
        grouping[key].append(word)
    
    return list(grouping.values())

if __name__ == "__main__":
    #strs = ["eat","tea","tan","ate","nat","bat"]
    strs = ["a"]
    print(groupAnagrams(strs=strs))