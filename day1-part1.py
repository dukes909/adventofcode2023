# Day 1: Trebuchet?
# Part 1:
#qzjggk1one
#two2seven7
#vszthreetwo6threethree4two3
def get_numbers_if_any(string):
    number_list = []
    for character in string:
        if character.isdigit():
            number_list.append(int(character))
    print(number_list)
    if len(number_list) > 1:
        local_sum = int(str(number_list[0]) + str(number_list[-1]))
        print(local_sum)
    else:
        local_sum = int(str(number_list[0]) + str(number_list[0]))
        print(local_sum)
    return(local_sum)   

file = open("day1-data.txt", "r")
total = 0
for line in file:
    total += get_numbers_if_any(line)
print(f"Sum is: {total}")