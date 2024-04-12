
dict_data = {
    1: {"name": "Bronson", "money": "$0.05"},
    2: {"name": "Masha", "money": "$3.66"},
    3: {"name": "Roscoe", "money": "$1.14"}

}



list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"},}

for number in list_data:
    print(number*2)

for number2 in embedded_lists:
    print(number2)

    for single_number in number2:
        print(single_number)

for number3 in dict_data:
    print(number3)

for number4 in dict_data:
    for value in dict_data[number4].values():
        print(value)

for number5 in dict_data.values():
        print(number5["money"])

