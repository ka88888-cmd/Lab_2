def find_min(lst):
    if not lst:
        return None
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

if __name__ == "__main__":
    print(find_min([3, 1, 4, 1, 5, 9, 2, 6]))
