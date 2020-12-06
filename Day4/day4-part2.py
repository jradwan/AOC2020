# Advent of Code 2020
# Day 4, Part 2
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
      # the passport has all the required fields, so validate them
      if validate_passport(byr, iyr, eyr, hgt, hcl, ecl, pid):
         val_cnt += 1

# end check_passport


def validate_passport(byr, iyr, eyr, hgt, hcl, ecl, pid):

   global curr_pass

   # initialize variables
   valid_pass = True

   # byr (Birth Year) - four digits; at least 1920 and at most 2002.
   #print('\nbyr: ', byr)
   byr_val = extract_field(byr)
   if not (check_year(byr_val, 4, 1920, 2002)):
      valid_pass = False

   # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
   #print('iyr: ', iyr)
   iyr_val = extract_field(iyr)
   if not (check_year(iyr_val, 4, 2010, 2020)):
      valid_pass = False

   # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
   #print('eyr: ', eyr)
   eyr_val = extract_field(eyr)
   if not (check_year(eyr_val, 4, 2020, 2030)):
      valid_pass = False
   
   # hgt (Height) - a number followed by either cm or in:
   #  If cm, the number must be at least 150 and at most 193.
   #  If in, the number must be at least 59 and at most 76.
   #print('hgt: ', hgt)
   hgt_val = extract_field(hgt)
   hgt_cm  = hgt_val.find('cm')
   hgt_in  = hgt_val.find('in')
   if (hgt_cm == -1 and hgt_in == -1):
      #print('hgt units not in or cm, or missing altogether')
      valid_pass = False
   else:
      hgt_len = len(hgt_val) - 2
      hgt_uni = hgt_val[hgt_len:]
      hgt_num = int(hgt_val[:hgt_len])
      #print('hgt: ', hgt_num, '-', hgt_uni)
      if (hgt_uni == 'cm'):
         if (hgt_num < 150 or hgt_num > 193):
            #print('cm not between 150-193')
            valid_pass = False
      if (hgt_uni == 'in'):
         if (hgt_num < 59 or hgt_num > 76):
            #print('in not between 59-76')
            valid_pass = False

   # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
   #print('hcl: ', hcl)
   hcl_val = extract_field(hcl)
   if (len(hcl_val) != 7):
      #print('hcl is not 7 digits')
      valid_pass = False
   else:
      if (hcl_val[0] != '#'):
         #print('hcl doesn''t start with a #')
         valid_pass = False
      else:
         hcl_val = hcl_val[1:]
         #print('new hcl val: ', hcl_val)
         if not (all(char in '0123456789abcdef' for char in hcl_val)):
            #print('hcl contains non-hex characters')
            valid_pass = False

   # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
   #print('ecl: ', ecl)
   ecl_val = extract_field(ecl)
   if (ecl_val not in ['amb','blu','brn','gry','grn','hzl','oth']):
      #print('ecl of ', ecl_val, ' is not valid')
      valid_pass = False

   # pid (Passport ID) - a nine-digit number, including leading zeroes.
   #print('pid: ', pid)
   pid_val = extract_field(pid)
   if (len(pid_val) != 9):
      #print('pid is not 9 characters')
      valid_pass = False
   else:
      if not (all(char in '0123456789' for char in pid_val)):
         #print('non-numeric char in pid')
         valid_pass = False 

   if (valid_pass):
      return True
   else:
      #print('Invalid passport!')
      return False

# end validate_passport


def extract_field(pass_field):

   global curr_pass

   next_space = curr_pass.find(' ', pass_field)
   if (next_space == -1):
      next_space = len(curr_pass)
   check_field = curr_pass[pass_field + 4:next_space]
   #print('field: ',check_field)

   return check_field

# end extract_field


def check_year(year, length, year_from, year_to):

   if (len(year) != length):
      #print('year not ', length, ' digits')
      return False
   else:
      if (int(year) < int(year_from) or int(year) > int(year_to)):
         #print('year not between ', year_from, '-', year_to)
         return False
      else:
         return True
   
# end check_year


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
         #print('\nPassport starting on line ', first_row, ': ', curr_pass, end='')
         check_passport()
         # clear out current passport for next set of data
         curr_pass = ''
         first_row = curr_row + 2
      else:
         curr_pass = curr_pass + ' ' + curr_line

      curr_row += 1

   # don't forget to process the last passport!
   #print('\nPassport starting on line ', first_row, ': ', curr_pass, end='')
   check_passport()

   print('\nTotal # of passports processed: ', pass_cnt)
   print('Total # of valid passports: ', val_cnt, '\n')


