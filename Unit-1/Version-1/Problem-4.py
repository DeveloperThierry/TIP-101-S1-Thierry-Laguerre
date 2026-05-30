# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#Should output be string or int?
#Can we use sum() multiple times?

### P - Plan
#2. Write out in plain English what you want to do: 
#I want to call the sum function passing in two int parameters and store result in variable. I want to pass that stored variable in the sum function twice and print the result.

#3. Translate each sub-problem into pseudocode:
#store the result of sum(a,b) in variable
#store result of sum(var, var) in new variable
#print result of new variable


### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def sum(a, b):
    return a + b
x = sum(10, 10)
y = sum(x, x)
print(y)
