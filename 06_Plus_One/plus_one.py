digits = [1,2,3]        
        
val = ''

for i in range(len(digits)):
    val = val+str(digits[i])

val = int(val) + 1

new_digits = []

for value in str(val):
    new_digits.append(int(value))

print(new_digits)