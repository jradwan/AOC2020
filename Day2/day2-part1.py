# Advent of Code 2020
# Day 2, Part 1
# December 3, 2020

file_name = "day2-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()
   valid_cnt  = 0

   for idx in range(len(line_content)):
      curr_line = line_content[idx].rstrip()

      # split current line into
      # - mix/max occurrences
      # - character
      # - password
      loc1  = curr_line.find('-')
      loc2  = curr_line.find(' ')
      loc3  = curr_line.find(':')

      min_cnt   = int(curr_line[:loc1])
      max_cnt   = int(curr_line[loc1+1:loc2])
      char_rule = curr_line[loc2+1:loc3]
      passwd    = curr_line[loc3+2:]
      char_cnt  = passwd.count(char_rule)

      # debugging block
      #print('Line: ', curr_line)
      #print('Loc1: ', loc1)
      #print('Loc2: ', loc2)
      #print('Loc3: ', loc3)
      #print('Min:  ', min_cnt)
      #print('Max:  ', max_cnt)
      #print('Char: ', char_rule)
      #print('Pwd:  ', passwd)
      #print('Ocurs:', char_cnt, end = "")

      # check password against rule and keep count of valid passwords
      if ((char_cnt >= min_cnt) and (char_cnt <= max_cnt)):
         #print('  Valid!\n')  
         valid_cnt += 1
      else:
         #print('  ** INVALID **\n')
         pass
      
   print('\nThe total # of valid passwords is: ', valid_cnt, '\n')

