#PF-Prac-4
def find_nine(nums):
    if 9 in nums[:4]:
        return True
    else:
        return False
    

nums=[1,9,4]
print(find_nine(nums))