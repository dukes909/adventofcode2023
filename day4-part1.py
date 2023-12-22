sum = 0
with open('/day4/day4-part1-data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    for card in lines:          
        my_numbers = []
        total = 0
        test = card.split(':')
        list = test[1].split('|')
        winning_numbers = list[0].split(' ')
        winning_numbers = [i for i in winning_numbers if i]
        print(winning_numbers)
        my_numbers = list[1].split(' ')
        my_numbers = [i for i in my_numbers if i]
        count = 0
        for l in my_numbers:
            if l in winning_numbers:
                print(l)
                count += 1
            if count != 0:
                total = 2 ** (count-1)
        print(f"Total: {total}")
        sum += total
    print(f"Sum: {sum}")
