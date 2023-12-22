sum = 0
copied_cards = 0
local_matches = 0
match_list = []
reversed_list = []
match_dict = {}
copies_dict = {}

def get_matches(i,card_string):
    matched = []
    ltotal = 0
    number_of_matches = 0
    my_numbers = []
    total = 0
    test = card_string.split(':')
    list = test[1].split('|')
    winning_numbers = list[0].split(' ')
    winning_numbers = [i for i in winning_numbers if i]
    my_numbers = list[1].split(' ')
    my_numbers = [i for i in my_numbers if i]
    count = 0
    for l in my_numbers:
        if l in winning_numbers:
                count += 1
                matched.append(l)
    number_of_matches = count
    return(number_of_matches)

def get_card_number(card):
    card_id = card.split(':')
    card_number_list = card_id[0].split(' ')
    card_number = int(card_number_list[-1])
    return(card_number)

with open('/day4/day4-part1-data.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]
    original_card_total = len(lines)
    for i,card in enumerate(lines):          
        matches = get_matches(i,card)
        match_list.append(matches)
    for i, count in enumerate(match_list):
         match_dict[i+1] = count
#    print(match_dict)

    matches = 0
    card = ''
    
    reversed_list = lines[::-1]
 #   print(reversed_list)
    for card in reversed_list:
        number = get_card_number(card)
        matches = match_dict[number]
        if matches == 0:
            copies_dict[number]=0
 # this section caused me some grief!!!
 #       elif matches == 1:
 #           copied_cards += matches
 #           copies_dict[number] = 1
        else:
            local_matches = matches
            copied_cards += matches
            for count in range(1,matches+1):
                matches = copies_dict[number + count]
                local_matches += matches
                copied_cards += matches
            copies_dict[number] = local_matches               
print(f"original card_total: {original_card_total}")
print(f"copied card total: {copied_cards}")
total_cards = original_card_total + copied_cards
print(f"total cards = {total_cards}") 
