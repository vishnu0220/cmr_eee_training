nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tar = int(input("Enter your target to find in the list : ")) # Takes input from the user

def binarySearch(nums, tar):
    low = 0
    high = len(nums)-1
    
    while low <= high:
        mid = (low+high)//2
        if nums[mid] == tar:
            return True
        elif nums[mid] < tar:
            low = mid+1
        else:
            high = mid-1
    return False

print(binarySearch(nums, tar))