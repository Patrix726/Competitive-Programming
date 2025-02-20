class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start_indexes = [
            ind for ind, (gain, lose) in enumerate(zip(gas, cost)) if gain >= lose
        ]
        tank = 0
        stuck_ind = 0
        for i in start_indexes:
            traveled_ind = 0
            tank = 0
            if i < stuck_ind:
                continue
            while tank >= 0 and traveled_ind < len(gas):
                cur_ind = (i + traveled_ind) % len(gas)
                tank += gas[cur_ind]
                tank -= cost[cur_ind]
                if tank < 0:
                    break
                traveled_ind += 1
            if traveled_ind == len(gas):
                return i
            else:
                stuck_ind = i + traveled_ind

        return -1


"""
Much faster solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        n = len(gas)

        cg = 0
        c_start = 0
        for start in range(n):
            cg += gas[start]-cost[start]
            if cg<0:
                c_start = start+1
                cg = 0
        return c_start
"""
