class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB_sum = {}
        CD_sum = {}
        cnt = 0

        for i in A:
            for j in B:
                if i+j not in AB_sum:
                    AB_sum[i+j] = 0
                AB_sum[i+j] += 1

        for i in C:
            for j in D:
                if i+j not in CD_sum:
                    CD_sum[i+j] = 0
                CD_sum[i+j] += 1

        for i in AB_sum:
            if -i in CD_sum:
                cnt += AB_sum[i] * CD_sum[-i]
        return cnt
