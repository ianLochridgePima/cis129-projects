# CIS129
# Ian Lochridge
# 4/11/25
# This program determines if a string is a palindrome 
# (the same forwards and backwards)

def is_palindrome(palindromeString): 
    strippedPalindromeString = strip_string(palindromeString)  #call function to strip string
    stack = []  #instantiate empty stack

    for x in range (len(strippedPalindromeString)):  #iterate through length of strippedPalindromeString
        stack.append(strippedPalindromeString[x])  #add each char to stack

    for x in range (len(strippedPalindromeString)):  #iterate through length of strippedPalindromeString
        currentChar = stack.pop()  #pop stack
        if currentChar != strippedPalindromeString[x]:  #compare popped value to adjacent value in strippedPalindromeString
            return False  #return if not equal
    return True  
    
def strip_string(palindromeString):
    punctuationCharacters = "?.!,@#$%^&*()></}~`-_"  #establish invalid chars
    strippedPalindromeString = palindromeString.replace(" ", "")  #remove all spaces in the string
    strippedPalindromeString = strippedPalindromeString.lower()  #convert string to all lower case

    for x in range (len(strippedPalindromeString) - 1, -1, -1):  #iterate through string in reverse
        if strippedPalindromeString[x] in punctuationCharacters:  #if char is a punctuation mark
            strippedPalindromeString = strippedPalindromeString[:x] + strippedPalindromeString[x+1:]  #remove char
    return strippedPalindromeString  

def main():
    print("Enter a string:")  #prompt user for a string
    palindromeString = input("")  #gather user input
    palindromeBoolean = is_palindrome(palindromeString)  #call function
    if (palindromeBoolean):  #print result
        print(f"({palindromeString}) is a Palindrome")
    else:
        print(f"({palindromeString}) is not a Palindrome")
main()

