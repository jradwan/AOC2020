# Advent of Code 2020
# Day 4, Part 1
# December 5, 2020

def check_passport():

   global pass_cnt
   global val_cnt
   global curr_pass

   # initialize variables
   byr = -1
   iyr = -1
   eyr = -1
   hgt = -1
   hcl = -1
   ecl = -1
   pid = -1
   cid = -1

   pass_cnt += 1

   # find location of fields
   byr = curr_pass.find('byr:') # birth year
   iyr = curr_pass.find('iyr:') # issue year
   eyr = curr_pass.find('eyr:') # expiration year
   hgt = curr_pass.find('hgt:') # height
   hcl = curr_pass.find('hcl:') # hair color
   ecl = curr_pass.find('ecl:') # eye color
   pid = curr_pass.find('pid:') # passport id
   cid = curr_pass.find('cid:') # country id (optional)

   if ( byr >= 0 and
        iyr >= 0 and
        eyr >= 0 and
        hgt >= 0 and
        hcl >= 0 and
        ecl >= 0 and
        pid >= 0):
      val_cnt += 1

# end check_passport()


# *** main program begins here ***

file_name = "day4-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # initialize variables and set file length
   pass_cnt  = 0
   val_cnt   = 0
   curr_row  = 0
   first_row = 1
   curr_pass = ''
   length    = len(line_content) - 1

   while curr_row <= length:
      curr_line = line_content[curr_row].rstrip()
      # check for next passport (blank line)
      if (curr_line == ''):
         # process current passport
         #print('Passport starting on line ', first_row, ': ', curr_pass, end='')
         check_passport()
         # clear out current passport for next set of data
         curr_pass = ''
         first_row = curr_row + 2
      else:
         curr_pass = curr_pass + ' ' + curr_line

      curr_row += 1

   # don't forget to process the last passport!
   #print('Passport starting on line ', first_row, ': ', curr_pass, end='')
   check_passport()

   print('\nTotal # of passports processed: ', pass_cnt)
   print('Total # of valid passports: ', val_cnt, '\n')


