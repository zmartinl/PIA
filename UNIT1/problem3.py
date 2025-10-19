def analyze_sets(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    union = set1 | set2
    symmetric_difference = set1 ^ set2
    result = {
        "intersection": intersection,
        "union": union,
        "symmetric_difference": symmetric_difference
    }
    return result

if __name__ == "__main__":
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    
    result = analyze_sets(list_a, list_b)
    
    print("Intersection:", result["intersection"])
    print("Union:", result["union"])
    print("Symmetric difference:", result["symmetric_difference"])
