class Solution:
    def isPrefixAndSuffix(self, str1: str, str2: str) -> bool:
        if len(str1) > len(str2):
            return False

        n = len(str1)
        if str2[:n] == str1 and str2[-n:] == str1:
            return True
        return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1, n):
                if self.isPrefixAndSuffix(words[i], words[j]):
                    answer += 1
        return answer
                
        