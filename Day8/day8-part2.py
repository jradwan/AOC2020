# Advent of Code 2020
# Day 8, Part 2
# December 13, 2020

file_name = "day8-input2.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # intialize variables and file length
   curr_row = 0
   accum    = 0
   executed = set()
   length   = len(line_content) - 1

   while curr_row <= length:
      curr_line = line_content[curr_row].rstrip()
      print(curr_line)

      instr = curr_line[:curr_line.find(' ')]
      incr  = int(curr_line[curr_line.find(' '):])
      #print(instr)
      #print(incr)
      if (curr_row in executed):
         print('duplicate! infinite loop imminent!')
         curr_row = length + 2
      else:
         executed.add(curr_row)
         print(executed)

         # evaluate current instruction
         if (instr == 'nop'): 
            # would this nop cause the next line to be executed a second time?
            # if so, change it to a jmp instead
            if ((curr_row + 1) in executed):
               print('switchinbg nop to jmp on line',curr_row + 1)
               curr_row = curr_row + incr 
            else:
               curr_row += 1

         if (instr == 'acc'):
            accum = accum + incr
            curr_row += 1

         if (instr == 'jmp'):
            # would this jmp cause the next line to be executed a second time?
            # if som change it to a nop instead
            if ((curr_row + incr) in executed):
               print('switchinbg jmp to nop on line',curr_row + 1)
               curr_row += 1
            else:
               curr_row = curr_row + incr

   #print(curr_row)
   if ((curr_row - 1) == length):
      print ('\nThe program terminated successfully. The accumulator was ',accum)
   else:         
     print('\nThe accumulator was ',accum,'when an infinite loop was detected.')        


