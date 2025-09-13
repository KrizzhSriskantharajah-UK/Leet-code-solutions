
```python

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data, columns = ["student_id", "age"])
    return df

```

[submission details](https://leetcode.com/submissions/detail/1768943186/)



