import heapq
class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        busy = []
        available = [(weight, i) for i, weight in enumerate(servers)]
        heapq.heapify(available)
        rsp = []
        j = 0
        t = 0

        for i, task in enumerate(tasks):
            t = max(t, i)
            
            if not available:
                t = max(t, busy[0][0])
            
            while busy and busy[0][0] <= t:
                    cur_server = heapq.heappop(busy)
                    heapq.heappush(available, (cur_server[1], cur_server[2]))
                
            if available:
                cur_server = heapq.heappop(available)
                heapq.heappush(busy, (t + task, cur_server[0], cur_server[1]))
                rsp.append(cur_server[1])
        
        return rsp
