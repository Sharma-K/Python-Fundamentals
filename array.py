nums = [1]
print(nums)

nums2 =  [x for x in range(3)]
print(nums2)

nums3 = [1,2]
nums3.append(4)
nums3.insert(1,6) # insert at index 1
print(nums3)

nums3[len(nums3):] = [5]
print(nums3)