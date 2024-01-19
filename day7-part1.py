from ordered_set import OrderedSet
import itertools


card_dict = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "6" : 7,
    "7" : 8,
    "8" : 9,
    "9" : 10,
    "T" : 11,
    "J" : 12,
    "Q" : 13,
    "K" : 14,
    "A" : 15

}

def count_chars(s):
    templist = []
    templist2 = []
    templist3 = s.split(' ')
    string = list(s)
    orderedset = OrderedSet(s)
    count = {}
    for i, char in enumerate(string):
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1
    for char in orderedset:
        templist.append(count[char])
        templist2.append(char)
    templist.sort()
    maxvalue = max(templist)
    if maxvalue == 1:
        return templist3, "high"
    elif maxvalue == 2:
        if templist[-2] == 1:
            return templist3, "one"
        else:
            return templist3, "two"
    elif maxvalue == 3:
        if templist[-2] == 1:
            return templist3, "three"
        else:
            return templist3, "full"
    elif maxvalue == 4:
        return templist3, "four"
    else:
        return templist3, "five"
    


total = 0

count_list = []

five_list = []
four_list = []
full_list = []
three_list = []
two_list = []
one_list = []
high_list = []
original_dict = {}
with open('/home/opalko/Desktop/Python Projects/Advent of Code 2023/day7/day7-data.txt', 'r') as file:
    hands_list = [line.strip() for line in file.readlines()]
    for line in hands_list:
        total = 0
        temp_list = []
        hand_bid = line.split(' ')
        hand = hand_bid[0]
        value = hand_bid[1]
        original_dict[hand] = value
        temp_list, maxv = count_chars(hand)
        if maxv == "five":
            five_list.append(hand)
        elif maxv == "four":
            four_list.append(hand)
        elif maxv =="full":
            full_list.append(hand)
        elif maxv == "three":
            three_list.append(hand)
        elif maxv == "two":
            two_list.append(hand)
        elif maxv == "one":
            one_list.append(hand)
        else:
            high_list.append(hand)
print(original_dict)
big_list = []
hand_dict = { "high_list": high_list,
              "one_list": one_list,
              "two_list": two_list,
              "three_list": three_list,
              "full_list": full_list,
              "four_list": four_list,
              "five_list": five_list }
print(one_list)

for name, h_list in hand_dict.items():
    h_len = len(h_list)
    if h_len > 1:
        for i in range(h_len):
            for h in range (0, h_len-i-1):
                current_hand = h_list[h]
                next_hand = h_list[h + 1]
#                print(f"currently on: {current_hand} {next_hand}")
                for card1, card2 in zip(current_hand,next_hand):
#                    print(f"--checking: {card1} {card2}")
                    if card_dict[card1] > card_dict[card2]:
#                        print(f"----switching {current_hand} and {next_hand}")
                        h_list[h],h_list[h + 1] = h_list[h + 1],h_list[h]
#                        print(f"----now {hands_list}")
                        break
                    elif card_dict[card1] == card_dict[card2]:
#                        print(f"same value at {card1} {card2}")
                        card1, card2 = next(itertools.islice(zip(current_hand, next_hand), 1, None))
#                        print(f"now at {card1} {card2}")
                    else:
                        break
        print(f"Currently: {name}\n")
 #       print(h_list)
        print("\n")
        big_list.append(h_list)
    else:
        big_list.append(h_list)
merged_list = [item for sublist in big_list for item in sublist]
print(merged_list)
final_list = []
counter = 0
total_amount = 0
for val, sorted_hand in enumerate(merged_list):
    counter = val + 1
    print(counter,sorted_hand,original_dict[sorted_hand])
    total_amount = total_amount + int(original_dict[sorted_hand]) * counter
print(total_amount)