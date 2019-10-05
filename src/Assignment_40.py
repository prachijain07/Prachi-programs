#PF-Assgn-40
def is_palindrome(word):
    word=word.upper()
    if len(word)<1:
        return True
    else:
        if word[0]==word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return False
   
    
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
    

#word=word.upper()
#rev=word[::-1]
#if rev==word
#True
#else False