def process_list(num):
    num = [n for n in num if n >= 0]
    num = list(set(num))
    
    num.sort()
    return num

listNum = [4, -1, 2, 4, 3, -5, 2]
result = process_list(listNum)
print(result)