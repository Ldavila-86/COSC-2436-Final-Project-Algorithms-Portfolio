from typing import List

def countdown(i: int) -> None:
    if i <= 0:
        print(0)
        return
    print(i)
    countdown(i - 1)

def fact(x: int) -> int:
    if x == 1:  # Base case
        return 1
    return x * fact(x - 1)  # Recursive case

def recursive_sum(arr: List[int]) -> int:
    if len(arr) == 0:  # Base case
        return 0
    return arr[0] + recursive_sum(arr[1:])  # Recursive case

def recursive_count(arr: List) -> int:
    if len(arr) == 0:  # Base case
        return 0
    return 1 + recursive_count(arr[1:])  # Recursive case

def recursive_max(arr: List[int]) -> int:
    if len(arr) == 1:  # Base case
        return arr[0]
    rest_max = recursive_max(arr[1:])  # Recursive call
    return arr[0] if arr[0] > rest_max else rest_max
