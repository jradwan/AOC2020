# Advent of Code 2020
# Day 5, Part 2
# December 6, 2020

from collections import Counter

def process_group():

   global ans_cnt
   global curr_grp

   # count occurences of each character
   grp_sum = Counter(curr_grp)

   #print('Counter: ', grp_sum)
   for curr_char in grp_sum:
      #print(curr_char, ':', grp_sum[curr_char])
      if (grp_sum[curr_char] == ind_cnt):
         ans_cnt += 1

# end process_group


# *** main program begins here ***

file_name = "day6-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # initialize variables and set file length
   grp_cnt   = 0
   ind_cnt   = 0
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
         #print('Group #', grp_cnt, ' (line ', first_row, ', members: ', ind_cnt, '): ', ''.join(sorted(curr_grp)))
         # count number of occurences of characters in the group
         process_group()
         # clear out group info for next set of data
         curr_grp = ''
         ind_cnt  = 0
         first_row = curr_row +2
      else:
         curr_grp = curr_grp + curr_line
         ind_cnt += 1

      curr_row += 1

   # don't forget to include the count from the last group!
   #print('Group #', grp_cnt, ' (line ', first_row, ', members: ', ind_cnt, '): ', ''.join(sorted(curr_grp)))
   process_group()
   
   print('\nTotal # of groups processed: ', grp_cnt)  
   print('Sum of ''yes'' questions by all members in a group is: ', ans_cnt, '\n')
