#!/usr/bin/env python
# coding: utf-8

# Class: CMSC 201 
# Discussion section: 62
# Year: Fall 2020 
# Title: Project 3 
# File name: Project 3 CMSC201 
# Date: 11/24/2020 

# In[1]:


pip install plotnine 


# In[2]:


from plotnine import * 
import pandas as pd


# In[3]:


#STEP 8: read in the data file 
#read in the project 3 file 
dataframe = pd.read_csv("~/Downloads/Project3_data.csv", encoding="ISO-8859-1")
dataframe


# In[4]:


#Step 8: convert the dataframe into a 2d list 
df = dataframe.values.tolist()
df


# In[5]:


#STEP 9: extract only the candidate votes for sorting algorithms 
candidate_votes = [] 
for i in df: 
    candidate_votes.append(i[14])
    
candidate_votes 
#candidate_votes = i[14]
#candidate_votes.split() 
#[i[14] for i in df] 


# In[6]:


#STEP 9: Implement selection sort algorithm with the largest values first 
#display the run time of the algorithm

import time 

def selection_sort(list): 
    start = time.time_ns() 
    #selection sort uses the minimum value to sort through the list 
    for i in range(0, len(list)-1): 
        min_value = i 
        
        for j in range(i+1, len(list)): 
            if list[j] > list[min_value]: 
                min_value = j 
                
        if min_value != i: 
            list[min_value], list[i] = list[i], list[min_value]
            
    finish = time.time_ns()
    print('Elapsed time = ', finish-start)
    return(list)

print(selection_sort(candidate_votes))


# In[7]:


#STEP 9: Implement quick sort algorithm with the largest values first 
#display the run time of the algorithm
start = time.time_ns() 
candidate_votes = [] 
for i in df: 
    candidate_votes.append(i[14])
    
candidate_votes 

#import time module to calculate run time 

def quick_sort(sequence):
    
    #we will apply this to first sequence and the subsequences that we create
    #BASE CASE: if the list has a length greater than 1
    length = len(sequence)
    if length <= 1:
        return(sequence)
    else:
        #pop will remove the last element and then return it
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    #splitting the items into two lists
    for item in sequence:
        if item < pivot:
            items_greater.append(item)

        else:
            items_lower.append(item)
            
   
 
    return(quick_sort(items_lower) + [pivot] + quick_sort(items_greater))
finish = time.time_ns()
print("ending value =", finish - start)
print(quick_sort(candidate_votes))


# Results: implementing a descending selection sort and quick sort algorithm requires us to change the relationship between the item and the pivot so that we have a descending value of candidate votes. Insertion sort is an algorithm which has a worst case time complexity of 0(n^2) and a best case scenario of Omega(n^2) however, quicksort is faster with a worst case time complexity of 0(n^2) and a best case scenario of Omega(nlogn). 

# 

# Next step: Create a new 2Dlist for the Republican, Democrat, Bernie Sanders, and Angus Caine candidates with information of year, code, name, party, and votes. We want to create the list containing the specific rows and columns for graphical analysis 

# In[8]:


#print out the first ten lines of the dataframe we've created 
for i in range(5): 
    print(df[i])


# Our next step will parse out the necessary data 
# by only showing the democrat, republican, Bernie Sanders, and Angus Caine information

# In[9]:


#STEP 10: Data analysis and visualization 
#Print out the last 10 rows of this new list to prove that your code works correctly 


Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
new_2d_list = [] 

for i in range(len(df)): 
    if df[i][Party] == "democrat" or df[i][Party] == "republican" or df[i][Name] == 'Bernie Sanders' or df[i][Name] == "Angus S. King, Jr.": 
            temp = [] 
            for j in l: 
                temp.append(df[i][j])
            new_2d_list.append(temp)

        
print(new_2d_list[-10:len(new_2d_list)])


# Purpose: the above code assigns certain colums to a variable within the 2d list then if a candidate is a democrat or republican or is Angus S. King, Jr. or Bernie Sanders, will extract the information of the year, state, name, party, amount of votes into respective columns 

# In[6]:


#STEP 11: Create a new ggplot object and draw a bar chart with candidates 
#on the x axis and the y axis showing the number of votes 

#repeat this to show the number of democratic candidates per year  

Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
republicans = [] 

for i in range(len(df)): 
    if df[i][Party] == "republican": 
        temp = [] 
        for j in l: 
            temp.append(df[i][j])
        republicans.append(temp)
        
republican_data = pd.DataFrame(republicans)
republican_data.columns=["Year", "State", "Candidate", "Party", "Votes"]
republican_data


# In[12]:


republican_data = pd.DataFrame(republican_data, columns=["Year", "State", "Candidate", "Party", "Votes"])

(ggplot(republican_data) + geom_col(aes(x='Year', y = 'Votes')))


# In[14]:


republican_data = pd.DataFrame(republican_data, columns=["Year", "State", "Candidate", "Party", "Votes"])

(ggplot(republican_data) + geom_col(aes(x='Year', y = 'Votes', color="State")))


# The color reveals the how many votes came from each state. 

# In[8]:


Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
democrats = [] 

for i in range(len(df)): 
    if df[i][Party] == "democrat" or df[i][Party] =="Bernie Sanders" or df[i][Party] =="Angus S. King, Jr.": 
        temp = [] 
        for j in l: 
            temp.append(df[i][j])
        democrats.append(temp)
        
democrat_data = pd.DataFrame(democrats)
democrat_data.columns=["Year", "State", "Candidate", "Party", "Votes"]
democrat_data


# In[34]:


democrat_data = pd.DataFrame(democrat_data, columns=["Year", "State", "Candidate", "Party", "Votes"])

(ggplot(democrat_data) + geom_col(aes(x='Year', y = 'Votes')))


# In[9]:


democrat_data = pd.DataFrame(democrat_data, columns=["Year", "State", "Candidate", "Party", "Votes"])

(ggplot(democrat_data) + geom_col(aes(x='Year', y = 'Votes', color='State')))


# In[18]:


Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
new_2d_list = [] 

for i in range(len(df)): 
    if df[i][Party] == "democrat" or df[i][Party] == "republican" or df[i][Name] == 'Bernie Sanders' or df[i][Name] == "Angus S. King, Jr.": 
            temp = [] 
            for j in l: 
                temp.append(df[i][j])
            new_2d_list.append(temp)

        
print(new_2d_list)

 


# In[12]:


from plotnine import ggplot, geom_col, aes 
(ggplot(dataframe, aes('year', 'candidatevotes'))) + geom_col() 


# In[13]:


from plotnine import ggplot, geom_col, aes 
(ggplot(dataframe, aes('year', 'candidatevotes', color='factor(year)'))) + geom_col()


# All of the black squares inside of the bars depicts the percentage of each state during the election year 
# 

# Horizontal bar chart stacks the data to show the count on the x-axis and the year on the y-axis. Overtime, candidate votes average has steadily grown. 

# In[10]:


#STEP 12: Votes per party, per election over time 

states = ['MD', 'PA', 'VA']
parties = ["republican", "democrat", "Bernie Sanders", "Angus S. King, Jr."]
Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
mvp = [] 

for i in range(len(df)): 
    #if df[i][State] == "MD"or df[i][State] == "PA" or df[i][State] == "VA": 
    if df[i][State] in states and df[i][Party] in parties:
        temp = [] 
        for j in l: 
            temp.append(df[i][j])
        mvp.append(temp)


# In[11]:


mvp


# In[13]:


new_mvp = pd.DataFrame(mvp, columns=["Year", "State", "Candidate", "Party", "Votes"])
new_mvp.head() 


# In[17]:


#STEP 12: Make a line plot showing the percentage of votes for each party
#in each election for the states of Maryland, Pennsylvania, and Virginia 

from plotnine import geom_line, geom_col 
(ggplot(new_mvp, aes('Year', 'Votes', color='Votes')) + geom_line())
#fill is not a line chart command so we must change it to color 
#plots the points of how many votes the candidate got for each party 


# 

# In[23]:


#STEP 12: Votes per party, per election over time 

states = ['MD', 'PA', 'VA']
parties = ["republican"]
Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
mvp = [] 

for i in range(len(df)): 
    #if df[i][State] == "MD"or df[i][State] == "PA" or df[i][State] == "VA": 
    if df[i][State] in states and df[i][Party] in parties:
        temp = [] 
        for j in l: 
            temp.append(df[i][j])
        mvp.append(temp)

(ggplot(new_mvp, aes(x='State', y ='Votes '))) + geom_point() 


# This scatter plot reveals that Pennsylvania leads with the most amount of republican votes with Virginia and Maryland following. 

# In[43]:


#STEP 12: Votes per party, per election over time 

states = ['AK', 'CA', 'TX']
parties = ["republican"]
Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
mvp = [] 

for i in range(len(df)): 
    #if df[i][State] == "MD"or df[i][State] == "PA" or df[i][State] == "VA": 
    if df[i][State] in states and df[i][Party] in parties:
        temp = [] 
        for j in l: 
            temp.append(df[i][j])
        mvp.append(temp)

(ggplot(new_mvp, aes(x='Year', y ='Votes', color='State'))) + geom_col() 


# This bar chart shows the number of republican votes per year in the biggest states in the US. 

# In[40]:


states = ['CA', 'TX', 'AK']
parties = ["democrat"]
Year = 0 
State = 2 
Name = 10 
Party = 11 
Votes = 14 

l = [Year, State, Name, Party, Votes]
mvp = [] 

for i in range(len(df)): 
    #if df[i][State] == "MD"or df[i][State] == "PA" or df[i][State] == "VA": 
    if df[i][State] in states and df[i][Party] in parties:
        temp = [] 
        for j in l: 
            temp.append(df[i][j])
        mvp.append(temp)

new_mvp = pd.DataFrame(mvp, columns=["Year", "State", "Candidate", "Party", "Votes"])


# In[41]:


new_mvp


# In[42]:


(ggplot(new_mvp, aes(x='State', y ='Votes '))) + geom_point() 


# This scatterplot shows the amount of votes for democrats from 1976-2018 for some of the biggest states in the US. 
