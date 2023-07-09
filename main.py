workingHours = []
array=0
salary = 0
for i in range(7):
    workingHours.append(int(input()))
    array+= workingHours[i]
    salary += (workingHours[i] * 100)
    if workingHours[i] > 8:
        salary += (workingHours[i] % 8) * 15
if workingHours[0]:
    salary += (workingHours[0] * 100) // 2
if workingHours[6]:
    salary += (workingHours[6] * 100) // 4
if array>40:
    salary += (array-40) *25
print(int(salary))
