import random


def randomSearch(items: list, target) -> int:
    """
    Randomly choose items until the target is found.
    Prints the number of tries and returns the index.
    """
    if target not in items:
        print("Target not found in list")
        return -1

    tries = 0
    indices = list(range(len(items)))
    checked = set()

    while True:
        tries += 1
        # Choose a random index we haven't checked yet
        available = [i for i in indices if i not in checked]
        random_index = random.choice(available)
        checked.add(random_index)

        if items[random_index] == target:
            print(f"Random search took {tries} tries")
            return random_index


def linearSearch(items: list, target) -> tuple[int, int]:
    """
    Implements linear search.
    Returns (index, number_of_checks).
    """
    checks = 0

    for i in range(len(items)):
        checks += 1
        if items[i] == target:
            return (i, checks)

    # Target not found
    return (-1, checks)


def binarySearch(items: list, target) -> tuple[int, int]:
    """
    Implements binary search (requires sorted list).
    Returns (index, number_of_checks).
    """
    checks = 0
    left = 0
    right = len(items) - 1

    while left <= right:
        checks += 1
        mid = (left + right) // 2

        if items[mid] == target:
            return (mid, checks)
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Target not found
    return (-1, checks)

