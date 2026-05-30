# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#What if the input list is empty?
#Are we guanranteed all elements in list are strings?

### P - Plan
#2. Write out in plain English what you want to do: 
#I want to loop through each item one by one and print each item on newline

#3. Translate each sub-problem into pseudocode:
#function print_list
    #loop iteem in items
        #print item


### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def print_list(lst):
    for item in lst:
        print(item)
print_list(['batman', 'robin', 'joker'])
