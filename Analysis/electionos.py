#!/usr/bin/env python
# coding: utf-8

# In[14]:



import pandas as pd
import os
import csv

file_to_load = os.path.join(r'/Users/bigd/Downloads/election_results.csv')
file_to_save = os.path.join(r'/Users/bigd/Downloads/election_results.csv')
print (file_to_load)

with open(file_to_load) as election_data:
    print(election_data)
    
# read the file object with the reader function.
    file_reader = csv.reader(election_data)
    for row in file_reader: 
        print(row)
# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_county = 0
winning_percentage = 0
winning_c_percentage = 0

# 2: Track the largest county and county voter turnout.
lrg_turnout_county = ""
lrg_turn_count = 0


# In[22]:


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
    candidate_name = row[2]

        # 3: Extract the county name from each row.
    county_name = row[1]
        


# In[ ]:




