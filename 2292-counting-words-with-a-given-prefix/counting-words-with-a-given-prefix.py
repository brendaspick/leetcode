class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        n = len(pref)
        answer = 0

        for word in words:
            if word[:n] == pref:
                answer += 1
        
        return answer
        