#Student name: Brianna Hodge
#Student ID: 50873856
#email: bmlhodge@umich.edu
#Collaborators/GenAI: No student collaborators, ChatGPT, https://www.w3schools.com/python/ref_stat_mean.asp#gsc.tab=0 
#How I used ChatGPT: Asked Chatgpt what lines in a code chunk was doing from discussion (importing a csv file), gave Chatgpt a few lines of data and asked it to create another example of code for me using the example provided. 

'''
x student info/collaborators/etc
x import libraries 
create a function to read in penguins csv file, use 'r' 
define two analysis functions that create and populate(add key, values to) a dictionary, and calcuates 
create a function that outputs the results in a new text or csv file (use text for a dictionary, or use csv for calculation/if output looks more like a "list")
create a class for unittest cases
define main function that calls in the testcases
'''

import os
import unittest

'''
to write test cases function
write four testcases per function (8 total)
we don't have a function written yet so its a "black box"
for testcase function reference discussion 5 SLIDES

https://www.geeksforgeeks.org/python/unit-testing-python-unittest/
#test example
class TestUnitest(unittest):
    def test_functionname(self):
        a = functionname(6,3)
        b = 2
        self.assertEqual(a, b) #checks if a and b are equal
        
'''
#function returns list of bill lengths for specified species
def get_species_data(species, csv_file):
    bill_lengths = []
    for row in csv_file:
        if row['species'] == species:
            bill_lengths.append(float(row['bill_length_mm']))
    return bill_lengths

#function returns list of penguins gender based on a specified island 
def get_island_data(island, csv_file):
    island_sex = []
    for row in csv_file:
        if row['island'] == island:
            island_sex.append(row['sex'])
    return island_sex

#test two general/usual cases
#test two edge cases?
import unittest
import statistics
class TestUnittest(unittest.TestCase):

    def test_average_bill_length(self):
        bill_lengths = get_species_data(self.species, self.csv_file)

        p1 = self.average_length
        p2 = statistics.mean(bill_lengths)

        self.assertEqual(p1, p2)


    def test_female_percentage(self):
        island_sex = get_island_data(self.island, self.csv_file)

        i1 = self.female_percentage
        i2 = 

        self.assertEqual(i1, i2)
         

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()