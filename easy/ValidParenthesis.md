
```python

class Solution(object):
    def isValid(self, s):
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0

```

<img width="1207" height="1198" alt="image" src="https://github.com/user-attachments/assets/458eb529-91a7-446a-903d-e05bb0fa9480" />
