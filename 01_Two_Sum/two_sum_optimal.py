def twosum(my_list, target):
    n = len(my_list)

    hash_map = {}

    for i in range(0, n):
        remaining = target - my_list[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
    
        hash_map[my_list[i]] = i

n = int(input("How many items do you want to enter? "))
my_list = []

for i in range(n):
    item = int(input(f"Enter item {i+1}: "))
    my_list.append(item)

target = int(input("Enter the target number: "))

result = twosum(my_list, target)
print(result)