class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.strip('.').split('.')
        v2 = version2.strip('.').split('.')
        
        v1 = [str(int(i)) for i in v1]
        v2 = [str(int(i)) for i in v2]
        
        nv1 = len(v1)
        nv2 = len(v2)
        
        if nv1 > nv2:
            v2.append('0'*(nv1-nv2))
        elif nv1 < nv2:
            v1.append('0'*(nv2-nv1))
            
        v1 = int(''.join(v1))
        v2 = int(''.join(v2))
        
        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
        else:
            return 0
        
