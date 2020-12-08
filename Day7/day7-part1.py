# Advent of Code 2020
# Day 7, Part 1
# December 7, 2020

file_name = "day7-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()

   # initialize variables and set file length
   rule_cnt  = 0
   curr_row  = 0
   bag_cnt   = 0   
   rules     = set()
   bags      = set()
   bag_type  = 'shiny gold'
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
      print('Rule #', rule_cnt + 1, ': ', curr_rule)
      # add the current, revised rule to the set
      rules.add(curr_rule)

      rule_cnt += 1
      curr_row += 1

   #print(rules)
   print('\nTotal # of rules loaded and parsed: ', rule_cnt) 

   # find the initial outer bag colors that contain the bag color we're interested in
   print('\nOuter bag colors that can contain', bag_type, 'bags:')
   for curr_rule in rules:
      if (curr_rule.find(bag_type) != -1):
         bag_clr = curr_rule[:curr_rule.find(',')]
         # ignore the bag color we're actually looking for, count the others
         if (bag_clr != bag_type):
            print(bag_clr)
            bags.add(bag_clr)
            bag_cnt += 1
            
   print('Total: ', bag_cnt)
   #print(bags)

   # now, for each of those outer bags, count the combinations of other bag colors
   # that can contain THOSE bag colors 
   for curr_bag in bags:
      print('\nChecking which bags can contain a', curr_bag, 'bag ...')
      for curr_rule in rules:
         if (curr_rule.find(curr_bag) != -1):
            bag_clr = curr_rule[:curr_rule.find(',')]
            if (bag_clr != curr_bag):
               print(bag_clr)
               #bags.add(bag_clr)
               bag_cnt += 1
               #print(curr_rule)


   print('\nTotal # of bag colors that could contain a',bag_type,':', bag_cnt, '\n')
