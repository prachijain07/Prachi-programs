#PF-Prac-6
def list123(nums):
    for i in range(0,len(nums)-2):
        if(nums[i]==1 and nums[i+1]==2 and nums[i+2]==3):
            return True
        else:
            continue
    return False
            
nums=[1,2,3,4,5]
print(list123(nums))