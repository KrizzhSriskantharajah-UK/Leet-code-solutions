
```python

class Solution(object):
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

```

<img width="1278" height="1187" alt="image" src="https://github.com/user-attachments/assets/7329c621-8dc0-45fb-8b78-fb4329ba5617" />
