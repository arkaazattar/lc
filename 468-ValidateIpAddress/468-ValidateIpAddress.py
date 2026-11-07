# Last updated: 11/7/2026, 10:34:07 AM
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = queryIP.split(".")
        ipv6 = queryIP.split(":")
        valid_ipv4, valid_ipv6 = True, True

        if len(ipv4) != 4:
            valid_ipv4 = False
        
        if len(ipv6) != 8:
            valid_ipv6 = False

        if not valid_ipv6 and not valid_ipv4:
            return "Neither" 

        if valid_ipv4:
            for segment in ipv4:
                if len(segment) > 4:
                    return "Neither"
                if segment > "255":
                    return "Neither"
                if not segment.isnumeric():
                    return "Neither"
                if segment[0] == '0' and len(segment) != 1:
                    return "Neither"
            return "IPv4"

        elif valid_ipv6:
            for segment in ipv6:
                if len(segment) > 4 or len(segment) == 0:
                    return "Neither"

                for ch in segment:
                    if ch not in "0123456789abcdefABCDEF":
                        return "Neither"

            return "IPv6"
            
        