class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # the sorted anagrams will have the same order -> use it as key
        res = defaultdict(list) # when a key first time comes up, create a list
        for s in strs:
            # "eat" -> "aet"
            sortedS = ''.join(sorted(s))
            # put it in correspond bucket
            # res = {
            #    "aet": ["eat", "tea", "ate"],
            #    "ant": ["tan", "nat"],
            #    "abt": ["bat"]
            # }
            res[sortedS].append(s)
        # use list() to extract dict.value()
        return list(res.values())