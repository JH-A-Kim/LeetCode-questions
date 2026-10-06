import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # so first we need to remove the non alphanumeric characters, remove all spaces and then we need to go from outside in 2 pointers and compare the values resulting in a O(n) solution But also what if something is inbetween? Should be ok without because we are simply not considering those values in our input.
        cleaned_text = re.sub(r'[\W_]', '', s).replace(" ", "").lower()

        i = 0
        j = len(cleaned_text)-1

        while i <= j:
            if cleaned_text[i] == cleaned_text[j]:
                i+=1
                j-=1
                continue
            else:
                return False

        return True


        