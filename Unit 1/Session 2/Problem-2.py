# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#What if the list is empty, what should we return?
#Are there constraints on the size of the integers?

### P - Plan
#2. Write out in plain English what you want to do: 
# I want to loop through the array and multiply each integer by two and print the result on a newline.

#3. Translate each sub-problem into pseudocode:
#function doubled(lst):
    #loop num in lst
        #multiply by two
        #print result


### I - Implement
#4. Translate the pseudocode into Python and share your final answer:

def doubled(lst):
    for n in lst:
        print(n * 2)
lst = [1,2,3]
doubled(lst)
