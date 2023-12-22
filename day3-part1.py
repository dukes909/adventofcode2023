import re
num=0
sum = 0
with open('day3-data.txt', 'r') as file:
    lines = file.readlines()
#    print(lines)
    previous_line = None  # Initialize to None for first iteration
    current_line = None
    next_line = None
    
    for i, line in enumerate(lines):
        num = 0

 #       print(f"Line is: {line}")
        numbers = re.findall(r"(\d+)+", line)
        if numbers:       # There is at least one number on current line
            
            current_line = line
            if i > 0:
                previous_line = lines[i - 1]
            if i < len(lines) - 1:  # Update next_line if it exists
                next_line = lines[i + 1]
            else:
                next_line = None

 #           print(f"Previous line is {previous_line}")
 #           print(f"Next line is {next_line}")
            
            numbers_iterable = re.finditer(r"(\d+)+", line)
            number_indices = [m.span() for m in numbers_iterable] # Create a list of 
            for tuples in number_indices:                         # tuples that are the
                start_pos = tuples[0]                             # indices of number
                end_pos = tuples[1]
 #               print(f"Range to check is: {tuples}")
                foundachar = False

                
                if start_pos == 0:                   # If number is at very start of line
                    char_after = str(line[end_pos])  # only check spot after number
 #                   print(f"char after: {char_after}")                    
                    if re.match(r"[^\w.]", char_after):
 #                       print(f"ADDING {int(numbers[num])}\n")
                        print(int(numbers[num]))
 #                       print("Matched!")
                        sum += int(numbers[num])
 #                       print(f"Sum is {sum}")
                        foundachar = True
                elif end_pos == 140:                     # If number is at end of line
                    char_before = str(line[start_pos-1]) # only check position before number
 #                   print(f"char before: {char_before}")                    
                    if re.match(r"[^\w.]", char_before):
 #                       print("Matched!")
                        print(int(numbers[num]))
 #                       print(f"ADDING {int(numbers[num])}\n")
                        sum += int(numbers[num])
 #                       print(f"Sum is {sum}")
                        foundachar = True
                else:
                    char_before = str(line[start_pos-1])  
 #                   print(f"char before: {char_before}")  # Case where number is 
                    char_after = str(line[end_pos])       # anywhere but start 
 #                   print(f"char after: {char_after}")    # end of line               
                    if re.match(r"[^\w.]", char_before) or re.match(r"[^\w.]", char_after):
 #                       print("Matched!")         # Found a special character!
                        print(int(numbers[num]))

 #                       print(f"ADDING {int(numbers[num])}\n")
                        sum += int(numbers[num])  # Add it to running total
 #                       print(f"Sum is {sum}")
                        foundachar = True

    # Now check previous line
                
                if previous_line != None and not foundachar:
                    if start_pos == 0:  # If number is at very start of line
                        for position in range(0,end_pos+1):
                            char_after = str(previous_line[position])  # only check spot after number
#                            print(f"char after: {char_after}")                    
                            if re.match(r"[^\w.]", char_after):
 #                               print("Previous line matched!!!")
                                print(int(numbers[num]))

 #                               print(f"ADDING {int(numbers[num])}\n")
                                sum += int(numbers[num])
 #                               print(f"Sum is {sum}")
                                foundachar = True

                                break
                    elif end_pos == 140:                     # If number is at end of line
                        for position in range(start_pos - 1,139):
                            char = str(previous_line[position]) #  check 2 positions before number
#                            print(f"char before: {char}")                    
                            if re.match(r"[^\w.]", char):
 #                               print("Previous line matched!!")
                                print(int(numbers[num]))

 #                               print(f"ADDING {int(numbers[num])}\n")
                                sum += int(numbers[num])
 #                               print(f"Sum is {sum}")
                                foundachar = True

                                break
                    else:                         # Middle of line
                        for position in range(start_pos - 1,end_pos+1):
                            char = str(previous_line[position])
#                            print(f"char before: {char}")  # Case where number is
                            if re.match(r"[^\w.]", char):
 #                               print(f"Previous line matched!")     # Found a special character!
                                print(int(numbers[num]))

#                                print(f"ADDING {int(numbers[num])}\n")
                                sum += int(numbers[num])           # Add it to running total
 #                               print(f"Sum is {sum}")

                                break
                                foundachar = True

                            else:
                                pass
                            
        ### Now check following line, if there is one
                            
                if next_line != None and not foundachar:
#                    print("checking next line")
                    if start_pos == 0:  # If number is at very start of line
                        for position in range(0,end_pos+1):
                            char = str(next_line[position])  # only check spot after number
 #                           print(f"checking position {position} char: {char}")                    
                            if re.match(r"[^\w.]", char):
 #                               print("Next line matched!!!")
 #                               print(f"ADDING {int(numbers[num])}\n")
                                print(int(numbers[num]))

                                sum += int(numbers[num])
 #                               print(f"Sum is {sum}")
                                foundachar = True

                                break
                    elif end_pos == 140:                     # If number is at end of line
                        for position in range(start_pos - 1,139):
                            char = str(next_line[position]) #  check 2 positions before number
 #                           print(f"char before: {char}")                    
                            if re.match(r"[^\w.]", char):
 #                               print("Next line matched!!")
                                print(int(numbers[num]))

#                                print(f"ADDING {int(numbers[num])}\n")
                                sum += int(numbers[num])
 #                               print(f"Sum is {sum}")
                                foundachar = True

                                break
                    else:                         # Middle of line
                        for position in range(start_pos - 1,end_pos+1):
                            char = str(next_line[position])
#                            print(f"char before: {char}")  # Case where number is
                            if re.match(r"[^\w.]", char):
 #                               print(f"Next line matched!")     # Found a special character!
 #                               print(f"ADDING {int(numbers[num])}\n")
                                print(int(numbers[num]))

                                sum += int(numbers[num])           # Add it to running total
 #                               print(f"Sum is {sum}")
                                foundachar = True
                                break
                            else:
                                pass
                num += 1
        else:
            print("Skipping...")   # No numbers on this line
            if i > 0:
                previous_line = lines[i - 1]
            if i < len(lines) - 1:  # Update next_line if it exists
                next_line = lines[i + 1]
            pass


print(f"Sum is {sum}")


