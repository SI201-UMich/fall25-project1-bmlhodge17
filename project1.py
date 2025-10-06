#Student name: Brianna Hodge
#Student ID: 50873856
#email: bmlhodge@umich.edu
#Collaborators/GenAI: No student collaborators, ChatGPT
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
#test two general/usual cases
#test two edge cases?
import unittest
class TestUnittest(unittest.TestCase):

    def setUp(self):
        

    def test_average_bill_length(self):
        p1 = average_bill_length()
        p2 = 

        self.assertEqual(p1, p2)


'''
chatgpt notes about test cases
Edge Cases: Test with empty lists, lists containing only True, only False, and a mix of both.
Typical Cases: Include lists with a representative mix of True and False values.
Floating Point Precision: Account for potential precision issues with assertAlmostEqual when dealing with percentages that are not whole numbers.
'''

    def test_female_percentage(self):


        self.assertEqual()
        #should I use assertAlmostEqual if the percentage is a float? 

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()