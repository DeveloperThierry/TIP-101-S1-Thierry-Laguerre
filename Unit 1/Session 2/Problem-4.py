# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#Should we return new array or modify it in place?
#How should we handle an empty list?

### P - Plan
#2. Write out in plain English what you want to do: 
#Create new list. Loop through array and multiply each number by -1 and append it to array and return.

#3. Translate each sub-problem into pseudocode:
#init new array
#loop input list
    #multiply by -1 and append to new array
#return new array

### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def flip_sign(lst):
    arr = []
    for n in lst:
        arr.append(n*-1)
    return arr
lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
