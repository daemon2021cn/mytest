class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0 for i in range(n)]

        for person_a, person_b in trust:
            count[person_a-1] -= 1
            count[person_b-1] += 1
        trust_max = max(count)

        return count.index(trust_max)+1 if trust_max == n-1 else -1
