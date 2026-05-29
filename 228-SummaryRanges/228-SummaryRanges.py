# Last updated: 5/29/2026, 5:54:51 PM
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        rsp = []
        cur_range = []
        for num in nums:
            if not cur_range:
                cur_range.append(num)
            
            elif num != cur_range[-1] + 1:
                if len(cur_range) == 1:
                    rsp.append(f"{cur_range[0]}")
                else: 
                    rsp.append(f"{cur_range[0]}->{cur_range[-1]}")
                
                cur_range.clear()
                cur_range.append(num)

            else:
                cur_range.append(num)
        
        if cur_range:
            if len(cur_range) == 1:
                    rsp.append(f"{cur_range[0]}")
            else: 
                rsp.append(f"{cur_range[0]}->{cur_range[-1]}")

        return rsp
