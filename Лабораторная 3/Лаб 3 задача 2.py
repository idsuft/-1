# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=","):
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)
    common = set(participants1) & set(participants2)
    return sorted(common)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
print("С разделителем по умолчанию (запятая):")
test_group1 = "Иванов,Петров,Сидоров"
test_group2 = "Петров,Сидоров,Смирнов"
result1 = find_common_participants(test_group1, test_group2)
print(f"Общие участники: {result1}")
# Проверка с разделителем "|" как в примере
print("\nС разделителем '|':")
result2 = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общие участники: {result2}")
# Проверка с другими разделителями
print("\nС разделителем ';':")
test_group3 = "Иванов;Петров;Сидоров"
test_group4 = "Петров;Сидоров;Смирнов"
result3 = find_common_participants(test_group3, test_group4, ";")
print(f"Общие участники: {result3}")