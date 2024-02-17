from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(int)
        for i in range(len(cpdomains)):
            sentence = cpdomains[i].split()
            l1 = sentence[1].split('.')
            for i in range(len(l1)):
                domains['.'.join(l1[i:len(l1)])] += int(sentence[0])
        ans = []
        for v,k in domains.items():
            ans.append(f"{str(k)} {v}")
        return (ans)
            
            

        
