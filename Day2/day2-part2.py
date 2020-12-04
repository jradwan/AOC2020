# Advent of Code 2020
# Day 2, Part 2
# December 3, 2020

file_name = "day2-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()
   valid_cnt  = 0

   for idx in range(len(line_content)):
      curr_line = line_content[idx].rstrip()

      # split current line into
      # - character positions
      # - character
      # - password
      loc1  = curr_line.find('-')
      loc2  = curr_line.find(' ')
      loc3  = curr_line.find(':')

      char_pos1 = int(curr_line[:loc1])
      char_pos2 = int(curr_line[loc1+1:loc2])
      char_rule = curr_line[loc2+1:loc3]
      passwd    = curr_line[loc3+2:]
      char_cnt  = 0

      # debugging block
      #print('Line: ', curr_line)
      #print('Loc1: ', loc1)
      #print('Loc2: ', loc2)
      #print('Loc3: ', loc3)
      #print('Pos1: ', char_pos1)
      #print('Pos2: ', char_pos2)
      #print('Char: ', char_rule)
      #print('Pwd:  ', passwd)
      #print('Ocurs:', char_cnt, end = "")

      # check for character location in the two positions
      # subtract one from the position to account for index zero in string
      if (passwd[char_pos1-1] == char_rule):
         #print(char_rule, ' occurs at position ', char_pos1)
         char_cnt = char_cnt + 1
         #print(char_cnt)
      if (passwd[char_pos2-1] == char_rule):
         #print(char_rule, ' occurs at position ', char_pos2)
         char_cnt = char_cnt + 1
         #print(char_cnt)
    
      # character is only allowed to occur in one of the two positions, so
      # check for a valid password and keep count 
      if (char_cnt == 1):
         #print('Valid!\n')  
         valid_cnt += 1
      else:
         #print('** INVALID **\n')
         pass
      
   print('\nThe total # of valid passwords is: ', valid_cnt, '\n')

