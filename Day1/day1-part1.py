# Advent of Code 2020
# Day 1, Part 1
# December 1, 2020

file_name = "day1-input.dat"

with open(file_name) as file_contents:
   list1 = file_contents.readlines()
   list2 = list1

   for line1 in range(len(list1)):
      val1 = int(list1[line1].rstrip())
      
      for line2 in range(len(list2)):
         val2 = int(list2[line2].rstrip())
         val_sum  = val1 + val2

         if val_sum == 2020:
            print("\nFound the pair that equals 2020:")
            print("{} + {} = {}".format(val1, val2, val_sum))
            print("\nSo the answer is:")
            aoc_answer = val1 * val2
            print("{} * {} = {}\n".format(val1, val2, aoc_answer))
            quit()  
