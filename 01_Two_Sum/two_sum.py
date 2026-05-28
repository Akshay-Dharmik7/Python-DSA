
def twosum(my_list, target):
    n = len(my_list)
    for i in range(n-1):
        for j in range(i+1, n):
            if my_list[i] + my_list[j] == target:
                return [i, j]

n = int(input("How many items do you want to enter? "))
my_list = []

for i in range(n):
    item = int(input(f"Enter item {i+1}: "))
    my_list.append(item)

target = int(input("Enter the target number: "))

result = twosum(my_list, target)
print(result)