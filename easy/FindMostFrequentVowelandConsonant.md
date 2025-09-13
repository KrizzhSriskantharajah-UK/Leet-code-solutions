
```python
class Solution(object):
    def maxFreqSum(self, s):
        vowel_indices = set([ord(c) - 97 for c in 'aeiou'])
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - 97] += 1

        max_vowel = 0
        max_consonant = 0

        for i, count in enumerate(freq):
            if count == 0:
                continue
            if i in vowel_indices:
                if count > max_vowel:
                    max_vowel = count
            else:
                if count > max_consonant:
                    max_consonant = count

        return max_vowel + max_consonant
```

<img width="1170" height="1188" alt="image" src="https://github.com/user-attachments/assets/e538e5a5-b280-48e5-8fd0-e8bdb4ef7b5c" />
