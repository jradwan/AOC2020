# Advent of Code 2020
# Day 8, Part 1
# December 13, 2020

file_name = "day8-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # intialize variables and file length
   curr_row = 0
   accum    = 0
   executed = set()
   length   = len(line_content) - 1

   while curr_row <= length:
      curr_line = line_content[curr_row].rstrip()
      #print(curr_line)

      instr = curr_line[:curr_line.find(' ')]
      incr  = int(curr_line[curr_line.find(' '):])
      #print(instr)
      #print(incr)
      if (curr_row in executed):
         #print('duplicate! infinite loop imminent!')
         curr_row = length + 1
      else:
         executed.add(curr_row)
         #print(executed)

         # evaluate current instruction
         if (instr == 'nop'): 
            curr_row += 1

         if (instr == 'acc'):
            accum = accum + incr
            curr_row += 1

         if (instr == 'jmp'):
            curr_row = curr_row + incr
         
   print('\nThe accumulator was at',accum,'when an infinite loop was detected.')        


