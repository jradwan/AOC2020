# Advent of Code 2020
# Day 3, Part 2
# December 5, 2020

file_name = "day3-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # intialize coordinates, tree count, map width and length
   curr_row = 0
   curr_col = 0
   tree_cnt = 0
   width    = len(line_content[0].rstrip()) - 1
   length   = len(line_content) - 1

   # prompt for slope
   print('\nEnter slope to calculate')
   right = int(input('Right: '))
   down  = int(input('Down:  '))

   while curr_row < length:
      # advance down and proceed if we haven't gone past the bottom of the map
      curr_row += down
      if (curr_row <= length):
         curr_line = line_content[curr_row].rstrip()
         wrapped = bool(False)

         # advance right, wrap around if needed
         if ((curr_col + right) > width):
            wrapped = bool(True)
            curr_col = (curr_col - width) + (right - 1) 
         else:
            curr_col += right

         # check for a tree, keep count
         curr_char = curr_line[curr_col]      
         if (curr_char == '#'):
            tree_cnt += 1

      # debugging block
      print('\nLine', curr_row + 1, ': ', curr_line)
      print('Col:  ', curr_col, end='')
      if wrapped:
         print(' (wrapped around)')
      else:
         print('')
      print('Char: ', curr_char)

   print('\nThe total # of trees encountered for slope ', right, '/', down, ' is: ', tree_cnt, '\n')

