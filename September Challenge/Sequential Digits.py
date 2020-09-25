class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digit = 1
        result = []
        while digit < 10:
            num = digit
            new_digit = digit
            while num <= high and new_digit < 10:
                if num >= low and num <= high:
                    result.append(num)
                new_digit += 1
                num = num*10 + new_digit
            digit += 1
            
        return sorted(result)
