#PF-Assgn-31
def check_palindrome(word):
    
    status=0
    a=word[::-1]
    if(a==word):
        status=1
    
    return status
        
    

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")