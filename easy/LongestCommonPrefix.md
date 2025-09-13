
```python

class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
```

<img width="1233" height="1190" alt="image" src="https://github.com/user-attachments/assets/6acc69e4-2529-42a9-b3a8-bec8a3da3b1e" />
