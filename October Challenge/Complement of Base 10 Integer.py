class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)
        new = '0b'
        
        for bit in binary[2:]:
            if bit == '0':
                new += '1'
            else:
                new += '0'
               
        return int(new,2)
        
        
