
```python

class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n

```

<img width="1189" height="1193" alt="image" src="https://github.com/user-attachments/assets/9d233aca-e1ff-4e2b-9860-7dee8240c02e" />
