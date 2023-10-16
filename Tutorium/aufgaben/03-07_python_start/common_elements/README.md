## Common Elements in Lists

Write a Python function called *find_common_elements* that takes two lists of integers as arguments and returns a new list containing the common elements that appear in both lists. The returned list should not contain any duplicates, and the elements should be in the same order as they appear in the first list.

``` python
>>> find_common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8])
[4, 5]
>>> find_common_elements([1, 2, 3, 4, 5], [5, 6, 7, 8])
[5]
>>> find_common_elements([1, 2, 3, 4, 5], [])
[]
>>> find_common_elements([], [4, 5, 6, 7, 8])
[]
>>> find_common_elements([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
[1, 2, 3, 4, 5]
```

[Zurück](../README.md)