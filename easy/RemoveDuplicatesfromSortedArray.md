
```python

class Solution(object):
    def removeDuplicates(self, nums):
        k = 1
        last = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            if val != last:
                nums[k] = val
                last = val
                k += 1
        return k

```

<img width="1255" height="1188" alt="image" src="https://github.com/user-attachments/assets/e7acaa03-3b79-4966-9942-92c45b65a46e" />
