#PF-Prac-26
def check_occurence(string):
    string=string.lower()
    if(string.count("mat")==string.count("jet")):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))