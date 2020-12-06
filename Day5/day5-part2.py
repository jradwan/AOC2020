# Advent of Code 2020
# Day 5, Part 2
# December 5, 2020

def process_boarding_pass():

   global curr_pass
   global high_seat
   global seat_list

   # determine row_num
   row_id = curr_pass[:7]
   #print('Row ID: ', row_id)

   # convert to binary string
   row_num = row_id.replace('F', '0')
   row_num = row_num.replace('B', '1')
   #print('Row ID in binary: ', row_num)

   # convert to decimal
   row_num = int(row_num, 2)
   #print('Row ID in decimal: ', row_num)

   # determine col_num
   col_id = curr_pass[7:]
   #print('Col ID: ', col_id)

   # convert to binary string
   col_num = col_id.replace('L', '0')
   col_num = col_num.replace('R', '1')
   #print('Col ID in binary: ', col_num)
  
   # convert to decimal
   col_num = int(col_num, 2)
   #print('Col ID in decimal: ', col_num)

   # calculate seat_id
   seat_id = (row_num * 8) + col_num
   #print('Seat ID: ', seat_id)
   if (seat_id > high_seat):
      high_seat = seat_id

   # store seat id in a list for later
   seat_list.append(seat_id)

# end process_boarding_pass


# *** main program begins here ***

file_name = "day5-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # initialize variables and set file length
   curr_row  = 0
   first_row = 0
   row_id    = 0
   row_num   = 0
   col_id    = 0
   col_num   = 0
   seat_id   = 0
   high_seat = 0
   seat_list = []
   length    = len(line_content) - 1

   while curr_row <= length:
      curr_pass = line_content[curr_row].rstrip()
      first_row = curr_row + 1
      #print('\nBoarding pass #', first_row, ': ', curr_pass)
      process_boarding_pass()
      curr_row += 1

   # sort the list of assigned seats
   seat_list.sort()

   # find the unassigned seat
   seat_cnt  = 0
   while seat_cnt < len(seat_list) - 1:
      #print('\ncurr seat: ', seat_list[seat_cnt])
      if ((seat_list[seat_cnt] + 1) != seat_list[seat_cnt + 1]):
         missing_seat = seat_list[seat_cnt] + 1
      seat_cnt +=1

   print('\nYour assigned seat is: ', missing_seat, '\n')
