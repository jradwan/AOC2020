# Advent of Code 2020
# Day 5, Part 1
# December 6, 2020

file_name = "day6-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # initialize variables and set file length
   grp_cnt   = 0
   ans_cnt   = 0
   curr_row  = 0
   first_row = 1
   curr_grp  = ''
   length    = len(line_content) - 1

   while curr_row <= length:
      curr_line = line_content[curr_row].rstrip()
      # check for next group (blank line)
      if (curr_line == ''):
         grp_cnt += 1
         #print('Group #', grp_cnt, ' (line ', first_row, '): ', curr_grp)
         #print('Unique # of characters: ', len(set(curr_grp)))
         # count unique number of characters in the group
         ans_cnt = ans_cnt + len(set(curr_grp))
         # clear out group for next set of data
         curr_grp = ''
         first_row = curr_row +2
      else:
         curr_grp = curr_grp + curr_line

      curr_row += 1

   # don't forget to include the count from the last group!
   #print('Group #', grp_cnt, ' (line ', first_row, '): ', curr_grp)
   ans_cnt = ans_cnt + len(set(curr_grp))
   
   print('\nTotal # of groups processed: ', grp_cnt)  
   print('Sum of ''yes'' questions of all groups is: ', ans_cnt, '\n')
