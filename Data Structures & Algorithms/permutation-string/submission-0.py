class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        need = len(count)
        size = len(s1)

        for index, char in enumerate(s2):
            count[char] -= 1
            if count[char] == 0:
                need -= 1
            if index >= size:
                left = s2[index - size]
                count[left] += 1
                if count[left] == 1:
                    need += 1
            if need == 0:
                return True
        return False
        