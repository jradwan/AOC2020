# Advent of Code 2020
# Day 7, Part 2
# December 13, 2020

def bag_contains(bag_color, bag_cnt):

   global rules
   global total_bags
   global recur_level

   outer_bag_cnt = 0
   temp_bag_cnt  = 0

   print('\nLooking for bag colors contained in',bag_cnt,' ',bag_color,'bags:')
   for curr_rule in rules:
      if (curr_rule.find(bag_color) == 0):
         #print(curr_rule)
         # strip off the first bag color to get the list of remaining bag colors
         new_rule = curr_rule[curr_rule.find(':') + 2:]
         #print(new_rule)
         # recurse through the list of bag colors contained in the current bag color
         while new_rule != '':
            loc1 = new_rule.find(',')
            if (loc1 != -1):
               loc2 = new_rule.find(' ')
               outer_bag_cnt = new_rule[:loc2]
               outer_bag_color = new_rule[loc2 + 1:new_rule.find(',')]
               temp_bag_cnt = temp_bag_cnt + int(new_rule[:loc2])
               print(new_rule)
               #print(outer_bag_cnt)
               #print(outer_bag_color)
               recur_level += 1
               print('entering recursion level ',recur_level,'for ',outer_bag_cnt,outer_bag_color,' bags')
               #bag_contains(outer_bag_color, outer_bag_cnt)
               total_bags = total_bags + int(bag_cnt) + (int(bag_cnt) * (bag_contains(outer_bag_color, int(outer_bag_cnt))))
               print('total',total_bags)
               print('back from recursion level',recur_level)
               recur_level += -1
               new_rule = new_rule[loc1+2:]
            else:
               # handle the last bag color 
               loc1 = len(new_rule)
               loc2 = new_rule.find(' ')
               outer_bag_cnt = new_rule[:loc2]
               outer_bag_color = new_rule[loc2 + 1:]
               temp_bag_cnt = temp_bag_cnt + int(new_rule[:loc2])
               print(new_rule)
               #print(outer_bag_cnt)
               #print(outer_bag_color)
               recur_level += 1
               print('entering recursion level ',recur_level,'for ',outer_bag_cnt,outer_bag_color,' bags')
               #bag_contains(outer_bag_color, outer_bag_cnt)
               total_bags = total_bags + int(bag_cnt) + (int(bag_cnt) * (bag_contains(outer_bag_color, int(outer_bag_cnt))))
               print('total',total_bags)
               print('back from recursion level',recur_level)
               recur_level += -1
               new_rule = ''
         if (temp_bag_cnt == 0): 
            # the current bag color contained no other bags
            print('returning 1')
            return bag_cnt
         else:
            print('returning ',temp_bag_cnt)
            return (temp_bag_cnt * bag_cnt)

         #if (recur_level != 0):
         #print('bag color:',bag_color)
         #print('total bags:',total_bags)
         #print('temp_bag_cnt:',temp_bag_cnt)
         #print('bag_cnt:',bag_cnt)
         #total_bags = total_bags + (int(bag_cnt) * temp_bag_cnt)
         #print('**leaving recursion ',recur_level,'for ',bag_color,', total bags = ',total_bags)
         #else:
         #   print('total bags:',total_bags)
         #   print('temp_bag_cnt:',temp_bag_cnt)
         #   print('bag_cnt:',bag_cnt)
         #   total_bags = total_bags * bag_cnt
         #   print('leaving recursion ',recur_level,'for ',bag_color,', total bags = ',total_bags)

# end bag_contains()   


# *** main program begins here ***

file_name = "day7-input2.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # initialize variables and set file length
   rule_cnt   = 0
   curr_row   = 0
   bag_cnt    = 1   
   total_bags = 0
   recur_level   = 0
   rules      = set()
   bag_color  = 'shiny gold'
   length     = len(line_content) - 1

   # load in and parse the rules
   while curr_row <= length:
      curr_rule = line_content[curr_row].rstrip()
      # strip ending period
      curr_rule = curr_rule.rstrip('.')
      # remove the word 'bags' or 'bag'
      curr_rule = curr_rule.replace(' bags', '')
      curr_rule = curr_rule.replace(' bag', '')
      # replace 'contains'
      curr_rule = curr_rule.replace(' contain', ':')
      # replace 'no other'
      curr_rule = curr_rule.replace(' no other', '')
      #print('Rule #', rule_cnt + 1, ': ', curr_rule)
      # add the current, revised rule to the set
      rules.add(curr_rule)

      rule_cnt += 1
      curr_row += 1

   #print('\nTotal # of rules loaded and parsed: ', rule_cnt) 

   bag_color = input('\nBag color: ')

   # recurse through all the bag colors contained in the bag we're interested in
   bag_contains(bag_color, bag_cnt)

   #print('\nBag colors: ', bags)
   print('\nTotal # of bags contained in ',bag_cnt,' ',bag_color,'bag(s):', total_bags, '\n')
