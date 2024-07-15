#The basic idea is that we keep track of the symbols in the string that we have looked
#at and the then iterate size by 1 if that symbol is not in the substring. if it is in 
#the substring we simply change biggest to size if size is bigger than biggest and set 
# size to 1.
def length_of_longest_substring(s: str) -> int:
    # Your code here
    size=0 #size variable keeps track of current size of the longest substring
    biggest=0 #biggest variable keeps track of the biggest size encountered
    if len(s)==1: #if string is only one character, return 1
        return 1
    for i in range (len(s)): #the for loop iterates through all elements of the string
        if s[i] not in s[:i]:#this checks if the element is not in the substring before 
                            #the current element and if it is not,it will add 1 to size 
            size+=1 #increment by 1 
        elif size>biggest:#comparison of size and if it is bigger than the biggest
                          #value then they will swap and set size to be equal to 1
            biggest=size
            size=1 #changed to 1 because because we have already incremented the first 
                   #variable in this substring.
        else: #if size is not bigger size still has to be set to 1
            size=1
    if size>biggest: #final check if biggest is still the biggest value and if not swap
        biggest=size
    return biggest

# Example test cases
print(length_of_longest_substring("abcabcbb"))  # Expected output: 3
print(length_of_longest_substring("bbbbb"))     # Expected output: 1
print(length_of_longest_substring("pwwkew"))    # Expected output: 3
print(length_of_longest_substring("a"))         # Expected output:1
print(length_of_longest_substring("abcdefghijklmnopqrstuvwxyz"))    # Expected output:26
print(length_of_longest_substring("abcdefghijklmnopqrstuvwxyza"))   # Expected output:26
print(length_of_longest_substring("AbA"))         # Expected output:2
print(length_of_longest_substring("$@#$"))        # Expected output:3
print(length_of_longest_substring("abcaABA12345"))  # Expected output:6


