import sys

unsortedList = raw_input("Enter the strings to be sorted separated by space :")
unsortedList = unsortedList.split(" ") # Split string into words
unsortedList.sort()

print(unsortedList)

#hardcoded list for sorting 
listOfGreekGods = ['Notus', 'Momus', 'Nereus', 'Glaucus', 'Heracles', 
'Eurus', 'Aether', 'Phosphorus', 'Zelus', 'Tartarus']

# Sorting list in order
listOfGreekGods.sort()

#print sorted list  
print(listOfGreekGods)