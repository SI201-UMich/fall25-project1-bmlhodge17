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

import csv
import pprint

def read_penguins_data(csv_file):
    base_path = os.path.abspath(os.path.dirname(__file__))
    full_path = os.path.join(base_path, csv_file)
    # use this 'full_path' variable as the file that you open
    with open(full_path, 'r') as file:
        r = csv.reader(file)
        rows = list(r) #skips the header
        #print(rows)

    penguins = {} #empty dictionary
    for r in rows[1:]:
        penguin_number = int(r[0])
        species = r[1]
        island = r[2]
        bill_length_mm = r[3]
        sex = r[7]
        if bill_length_mm == 'NA' or sex == 'NA':
            continue
        bill_length_mm = float(bill_length_mm)
        penguins[penguin_number] = {'species': species, 'island': island, 'bill_length_mm': bill_length_mm, 'sex': sex}
    pprint.pprint(penguins)
    return penguins



import os
import unittest

def average_bill_length(penguins):
    average_lengths = {}
    count = {} #keys are the species and values are the number of penguins in that species
    for k, v in penguins.items():
        if v['species'] not in average_lengths:
            average_lengths[v['species']] = v['bill_length_mm']
            count[v['species']] = 1
        else:
            average_lengths[v['species']] += v['bill_length_mm']
            count[v['species']] += 1
    for species in average_lengths:
        len_species = average_lengths[species]
        total_count = count[species]
        all_averages = len_species / total_count 
        average_lengths[species] = round(all_averages, 2)

    return average_lengths

    # example output = {species1 : 10. species2: 20}

def island_female_percentage(penguins):
    pass

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

    def setUp(self):
        self.data1 =  {342: {'bill_length_mm': 49.6,
       'island': 'Dream',
       'sex': 'male',
       'species': 'Chinstrap'},
 343: {'bill_length_mm': 50.8,
       'island': 'Dream',
       'sex': 'male',
       'species': 'Chinstrap'},
 344: {'bill_length_mm': 50.2,
       'island': 'Dream',
       'sex': 'female',
       'species': 'Chinstrap'}} #usual
        
        #usual
        self.data2 = 

        
        #unusual
        self.data3 = 

        #unusual 
        self.data4 = 


    def test_average_bill_length(self):
        a = average_bill_length(self.data1)
        data1_output = {'Chinstrap': 50.2}

        self.assertEqual(a, data1_output, 2)

        

        

        

'''
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
   
'''
def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
'''
d = read_penguins_data('penguins.csv')
a = average_bill_length(d)
pprint.pprint(a)
'''