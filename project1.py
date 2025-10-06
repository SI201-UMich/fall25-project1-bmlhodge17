#Student name: Brianna Hodge
#Student ID: 50873856
#email: bmlhodge@umich.edu
#Collaborators/GenAI: No student collaborators, ChatGPT
#How I used ChatGPT: Asked Chatgpt what lines in a code chunk was doing from discussion (importing a csv file), gave Chatgpt a few lines of data and asked it to create another example of code for me using the example provided. 

'''
student info/collaborators/etc
import libraries 
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