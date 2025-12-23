nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

def evenSum(nums):
    evenSumVal = 0
    start = 0
    end = len(nums)-1
    while start <= end:
        evenSumVal += nums[start]
        start += 2
    return evenSumVal

def oddSum(nums):
    oddSumVal = 0
    start = 1
    end = len(nums)-1
    while start <= end:
        oddSumVal += nums[start]
        start += 2
    return oddSumVal

def evenMinusOdd(nums):
    return (evenSum(nums)-oddSum(nums))

print(evenSum(nums))
print(oddSum(nums))
print(evenMinusOdd(nums))