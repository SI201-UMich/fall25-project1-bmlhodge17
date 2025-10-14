#Student name: Brianna Hodge
#Student ID: 50873856
#email: bmlhodge@umich.edu
#Collaborators/GenAI: No student collaborators, ChatGPT, office hours
#How I used ChatGPT: Asked Chatgpt what lines in a code chunk was doing from discussion (importing a csv file), gave Chatgpt a few lines of data and asked it to create another example of code for me using the example provided. 
# Checked expected test cases output with Chatgpt and asked it to explain my second function code to me in order to debug and make changes. 

'''
x student info/collaborators/etc
x import libraries 
x create a function to read in penguins csv file, use 'r' 
define two analysis functions that create and populate(add key, values to) a dictionary, and calcuates 
create a function that outputs the results in a new text or csv file (use text for a dictionary, or use csv for calculation/if output looks more like a "list")
x create a class for unittest cases
x define main function that calls in the testcases
'''

import csv
import pprint
import unittest
import os


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
    island_females = {}
    for k, v in penguins.items():
        island = v['island']
        sex = v['sex']
    total_female_count(island_females, island, sex) #call helper function total_female_count
    island_percentages = {}
    for island, totals in island_females.items():
        num_females = totals.get('num_females', 0)
        total = totals['total']
        percent_female = num_females / total * 100
        island_percentages[island] = round(percent_female, 2)
        #percent_female = totals['num_females'] / totals['total']
        #write to csv or text file
        return island_percentages


def total_female_count(island_females, island, sex):
#acts as a helper function for island_female_percentage
    if island not in island_females:
        island_females[island] = {}
    island_females[island]['total'] = island_females[island].get('total', 0) + 1
    if sex == 'female':
        island_females[island]['num_females'] = island_females[island].get('num_females', 0) + 1
    

#{‘islandname’: {‘total’: 1, ‘num_females’: 0}}

#output (23%) #returns female count//total count x 100

# example output = {island: 23%, island2: 42%}

'''
office hours notes
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


class TestUnittest(unittest.TestCase):

    def setUp(self):
        #usual
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
       'species': 'Chinstrap'}} 
        
        #usual
        self.data2 =  {276: {'bill_length_mm': 49.9,
       'island': 'Biscoe',
       'sex': 'male',
       'species': 'Gentoo'},
 277: {'bill_length_mm': 46.5,
       'island': 'Dream',
       'sex': 'female',
       'species': 'Chinstrap'},
 278: {'bill_length_mm': 50.0,
       'island': 'Dream',
       'sex': 'male',
       'species': 'Chinstrap'}}

        #unusual
        self.data3 =  {188: {'bill_length_mm': NA, #unusual case --> NA for bill length value
       'island': 'Biscoe',
       'sex': 'male',
       'species': 'Gentoo'},
 189: {'bill_length_mm': 42.6,
       'island': 'Biscoe',
       'sex': 'female',
       'species': 'Gentoo'},
 190: {'bill_length_mm': 44.4,
       'island': 'Biscoe',
       'sex': 'male',
       'species': 'Gento'}, #unusual case --> spelling mistake
 191: {'bill_length_mm': 44.0,
       'island': 'Biscoe',
       'sex': 'female',
       'species': 'Gentoo'}}

        #unusual 
        self.data4 =  {44: {'bill_length_mm': 44.1,
      'island': 'Dream',
      'sex': 'male',
      'species': 'Adelie'},
 45: {'bill_length_mm': NA, #NA value for unusual test case
      'island': 'Dream',
      'sex': 'female',
      'species': 'Adelie'},
 46: {'bill_length_mm': 39.6,
      'island': 'Dream',
      'sex': 'male',
      'species': 'adelie'}} #lowercase A


    def test_average_bill_length(self):
        a = average_bill_length(self.data1)
        data1_output = {'Chinstrap': 50.2}

        b = average_bill_length(self.data2)
        print(b)
        data2_output = {'Gentoo': 49.9, 'Chinstrap': 48.25}

        c = average_bill_length(self.data3)
        data3_output = {'Gentoo': 43.5}

        d = average_bill_length(self.data4)
        data4_output = {'Adelie': 44.1, 'adelie': 39.6}

        self.assertEqual(a, data1_output, 2) #usual
        self.assertEqual(b, data2_output, 2) #usual
        self.assertEqual(c, data3_output, 2) #unusual
        self.assertEqual(d, data4_output, 2) #unusual


    def island_female_percentage(self):

        def setUp(self):
            #usual
            self.percent1 = {1: {'bill_length_mm': 39.1,
     'island': 'Torgersen',
     'sex': 'male',
     'species': 'Adelie'},
 2: {'bill_length_mm': 39.5,
     'island': 'Torgersen',
     'sex': 'female',
     'species': 'Adelie'}}

            #usual
            self.percent2 =  {324: {'bill_length_mm': 49.0,
       'island': 'Dream',
       'sex': 'male',
       'species': 'Chinstrap'},
 325: {'bill_length_mm': 51.5,
       'island': 'Dream',
       'sex': 'male',
       'species': 'Chinstrap'},
 326: {'bill_length_mm': 49.8,
       'island': 'Dream',
       'sex': 'female',
       'species': 'Chinstrap'}}

            #unusual
            self.percent3 =  {107: {'bill_length_mm': 38.6,
       'island': 'Biscoe',
       'sex': 'female',
       'species': 'Adelie'},
 108: {'bill_length_mm': 38.2,
       'island': 'Biscoe',
       'sex': 'NA', #NA for unusual test case
       'species': 'Adelie'},
 109: {'bill_length_mm': 38.1,
       'island': 'Biscoe',
       'sex': 'femal', #spelled female wrong for unusual test case
       'species': 'Adelie'}}

            #unusual
            self.percent4 =  {281: {'bill_length_mm': 52.7,
       'island': 'Dream',
       'sex': 'male',
       'species': 'Chinstrap'},
 282: {'bill_length_mm': 45.2,
       'island': 'Dream',
       'sex': 'male', #changed to male for unusual test case
       'species': 'Chinstrap'},
 283: {'bill_length_mm': 46.1,
       'island': 'Dream',
       'sex': 'fmale', #change spelling for unusual test case
       'species': 'Chinstrap'}}


        percent1 = island_female_percentage(self.percent1)
        percent1_output = {'Torgersen': 50.0}

        percent2 = island_female_percentage(self.percent2)
        percent2_output = {'Dream': 33.33}

        percent3 = island_female_percentage(self.percent3)
        percent3_output = {'Biscoe': 33.33}

        percent4 = island_female_percentage(self.percent4)
        percent4_output = {'Dream': 0.0}

        self.assertEqual(percent1, percent1_output, 2) #usual
        self.assertEqual(percent2, percent2_output, 2) #usual
        self.assertEqual(percent3, percent3_output, 2) #unusual
        self.assertEqual(percent4, percent4_output, 2) #unusual
 

def main():
    d = read_penguins_data('penguins.csv')
    a = average_bill_length(d)
    p = island_female_percentage(d)
    pprint.pprint(a)
    pprint.pprint(p)
    #unittest.main()

if __name__ == '__main__':
    main()
'''
d = read_penguins_data('penguins.csv')
a = average_bill_length(d)
pprint.pprint(a)
'''