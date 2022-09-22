def find_bigest_num(nums):
    bigest = nums[0]
    for i in nums:
        if i > bigest:
            bigest = i
        return (bigest)
    
listnum = [4, 5, 17, 3, 2, 9]

def find_three_sum(nums):
    numeric = 0
    for i in nums:
        if i % 3 == 0:
            numeric += i
            
    return numeric

print(find_bigest_num(listnum))
print(max(listnum))
print(min(listnum))
print(find_three_sum(listnum))