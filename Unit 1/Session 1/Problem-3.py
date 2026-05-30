# Tech Fellow Task Instructions 
#For each problem in your assigned task, write out the UPI solution by answering questions 1-4.

# Template Questions
### U - Understand 
#1. Share 2 questions you would ask to help understand the question:
#Can I pass a string emoji as params or should I place it in variable?
#Should we consider rendering it dynamically in case of different menu items.

### P - Plan
#2. Write out in plain English what you want to do: 
#I want to call print_menu with a specific emoji string and have it concatenated in a string and printed

#3. Translate each sub-problem into pseudocode:
#function print_menu(menu):
    #print lunch is menu
#call print_menu with argument pizza

### I - Implement
#4. Translate the pseudocode into Python and share your final answer:
def print_menu(menu):
    print("Lunch today is: " + menu)
print_menu("🍕")
