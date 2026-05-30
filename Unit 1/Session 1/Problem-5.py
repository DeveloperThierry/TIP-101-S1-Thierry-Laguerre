# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#How should the function handle negative numbers and zero?
#Is there a number range that Python can't handle (overflow issues?    

### P - Plan
#2. Write out in plain English what you want to do: 
#I want to define product function accepting two ints. Inside it I want to multiply these two values and return product.

#3. Translate each sub-problem into pseudocode:
#function product(a,b)
    #set result = a * b
    #return result
#call product using arguments a and b


### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def product(a, b):
    return a * b
print(product(5, 5))
