"""
There are N gas stations along a circular route, where the amount of
gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas
to travel from station i to its next station (i+1). You begin the journey
with an empty tank at one of the gas stations.
Return the starting gas station's index if you can travel around the
circuit once, otherwise return -1.
Problem found here:
http://oj.leetcode.com/problems/gas-station/
"""


"""
My initial solution, this is correct but for very long examples it is too slow
as its worst case is O(n^2) for n gas stations.
"""
class Solution1:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        val_per_station = [x - y for x, y in zip(gas, cost)] 
        if sum(val_per_station) < 0:
            return -1
        start = 0
        gas_total = val_per_station[start]
        current = (start + 1) % len(val_per_station)
        for i in xrange(len(val_per_station)*2):
            if val_per_station[i] > 0:
                if self.traverse(i, val_per_station):
                    return i
        return -1
        
    def traverse(self, starting_index, val_per_station):
        cur_val = val_per_station[starting_index]
        index = (starting_index + 1) % len(val_per_station)
        while index != starting_index:
            if cur_val < 0:
                return False
            cur_val += val_per_station[index]
            index += 1
            index = index % len(val_per_station)
        return True

"""
My improved solution, this was accepted.  Now the worst case runtime is
2N.
"""
class Solution2:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        val_per_station = [x - y for x, y in zip(gas, cost)] 
        if sum(val_per_station) < 0:
            return -1
        start = 0
        gas_total = val_per_station[start]
        current = (start + 1) % len(val_per_station)
        for i in xrange(len(val_per_station)*2):
            if current == start and gas_total >= 0:
                return start
            if gas_total <= 0:
                start = current
                gas_total = 0
            gas_total += val_per_station[current]
            current = (current + 1) % len(val_per_station)
        return -1


#test
sol = Solution1()
gas = [8,5,4,3,2,1]
cost = [8,5,4,3,3,0]
print 'given gas available of: ', gas
print 'and cost of traversing of: ', cost
print 'the expected starting point is: ', 5,
print ' and our system returns: ', sol.canCompleteCircuit(gas, cost)
