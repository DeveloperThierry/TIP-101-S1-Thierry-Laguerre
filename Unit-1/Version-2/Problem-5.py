# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#What should be returned if list is empty?
#Can the list contain negative numbers?

### P - Plan

#2. Write out in plain English what you want to do: 
#Find the biggest and smallest number in the array and return the difference.

#3. Translate each sub-problem into pseudocode:
#if list is empty return 0
#if set max value equals max of list 
#if set min value equals min of list 
#return max value minus min value

### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def max_difference(lst):
    mx=max(lst)
    mn=min(lst)
    return mx-mn
lst = [5,22,8,10,2]
max_diff = max_difference(lst)
print(max_diff)
