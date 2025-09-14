
```python 

class Solution(object):
    def generate(self, numRows):
        if numRows == 0:
            return []
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
            triangle.append(row)
        return triangle

```

<img width="1178" height="1190" alt="image" src="https://github.com/user-attachments/assets/e402b8bd-58ea-496b-a433-1544abd2b2e6" />
