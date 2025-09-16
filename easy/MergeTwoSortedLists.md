
```python

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        return dummy.next

```

<img width="1436" height="1189" alt="image" src="https://github.com/user-attachments/assets/092110c5-06af-46f3-a1c2-ebcaf7538656" />
