class Solution:
    def romanToInt(self, s: str) -> int:

        #Initialize dictionary 
        value_dict = {'I':1, 'V':5, 'X':10, 'L': 50, 'C': 100, 'D':500, 'M': 1000}
        
        sum = 0
        prev = None
        # Loop through string to accumulate sum according to rules
        for char in s:
            curr = char

            # If current symbol has smaller value than previous
            # Extract 2 times of previous value
            # Because we have added it once, but we want curr=prev
            # Hence we have sum = sum - 2*prev + curr

            if prev is not None and value_dict[prev] < value_dict[curr]:
                sum -= 2 * value_dict[prev]                
            sum += value_dict[curr]
            prev = curr
        return sum