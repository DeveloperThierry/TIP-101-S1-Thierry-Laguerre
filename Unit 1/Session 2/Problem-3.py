# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#What should we return in case of empty list?
#Should we handle other data types?

### P - Plan
#2. Write out in plain English what you want to do: 
#Initalize new array. Loop through each integer and multiply by two and append to new list and return.

#3. Translate each sub-problem into pseudocode:
#function doubled(lst):
    #set arr
    #for each num in lst:
        #append num * 2
    #return arr


### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def doubled(lst):
    arr = []
    for n in lst:
        arr.append(n * 2)
    return arr
lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
