numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
sum_all= sum(numbers[:4]+numbers[5:])
new_number = sum_all / len(numbers)
numbers[4] = new_number
new_list = numbers[:]
print('Измененный список:', new_list)