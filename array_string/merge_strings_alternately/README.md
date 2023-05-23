# 1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

## Example 1:

```
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
```

## Example 2:

```
Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
```

## Example 3:

```
Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
```

## Constraints:

- `1 <= word1.length, word2.length <= 100`
- `word1 and word2 consist of lowercase English letters.`


# What did I learn?

Between the first and second solution, I like the second solution more. I think that the second solution is just a little bit more cleaner as we're able to remove the variable `iterations` and the `if` conditionals that came with it. There is another solution that one could perform that utilizes `min()` instead of `max()`. If one were to do that, you'd be able to remove the 2 `if` conditionals and use slicing to ensure you grab the remaining characters if one word is longer than the other. I've provided a possibility of said third solution below.


```
# Possible third solution

class ThirdSolution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        count = 0
        while count < min(len(word1), len(word2)):
            merged += word1[count]
            merged += word2[count]

            count += 1

        return merged + word1[count:] + word2[count:]
```

I personally think `SecondSolution` is better as it's more friendly to more novice programmers (easier to understand) and executes just as fast.