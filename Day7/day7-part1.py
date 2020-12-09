# Advent of Code 2020
# Day 7, Part 1
# December 7, 2020

def bag_recursion(bag_color):

   global rules
   global bags

   #print('\nLooking for bag colors that can contain',bag_color,'bags:')
   for curr_rule in rules:
      if (curr_rule.find(bag_color) != -1):
         outer_bag_color = curr_rule[:curr_rule.find(',')]
         #print('Checking bag color:', outer_bag_color)
         # ignore the bag color we're actually looking for, count the others
         if (outer_bag_color != bag_color):
            #print('Recursion ...')
            bag_recursion(outer_bag_color)
         else:
            #print('Final outer bag: ', outer_bag_color)
            bags.add(outer_bag_color)

# end bag_recursion()   


# *** main program begins here ***

file_name = "day7-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # initialize variables and set file length
   rule_cnt  = 0
   curr_row  = 0
   bag_cnt   = 0   
   rules     = set()
   bags      = set()
   bag_color = 'shiny gold'
   length    = len(line_content) - 1

   # load in and parse the rules
   while curr_row <= length:
      curr_rule = line_content[curr_row].rstrip()
      # strip ending period
      curr_rule = curr_rule.rstrip('.')
      # remove the word 'bags' or 'bag'
      curr_rule = curr_rule.replace(' bags', '')
      curr_rule = curr_rule.replace(' bag', '')
      # replace 'contains'
      curr_rule = curr_rule.replace(' contain', ',')
      #print('Rule #', rule_cnt + 1, ': ', curr_rule)
      # add the current, revised rule to the set
      rules.add(curr_rule)

      rule_cnt += 1
      curr_row += 1

   #print('\nTotal # of rules loaded and parsed: ', rule_cnt) 

   # recurse through all the bag colors to determine which colors can 
   # contain the bag_color we're interested in
   bag_recursion(bag_color)

   # remove the bag color we're looking for from the final set 
   bags.remove(bag_color)

   #print('\nBag colors: ', bags)
   print('\nTotal # of bag colors that can contain a',bag_color,'bag:', len(bags), '\n')
