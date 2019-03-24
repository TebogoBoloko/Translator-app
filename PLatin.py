#Pig-latin translator for sentences

#User input 
user_input = str(input('Enter the sentence you wish to translate! \n'))

#Splitting my string to put it inside a list
#Creating a new list as well to store new values...
my_list = user_input.split()
newList = [' ']*len(my_list)

#Function that does the processes
def trans():
    #For loop to iterate through the list
    for i in my_list:
        
        first_letter = i[0]
        
        #if statement to check if the first_letter starts with a vowels
        if first_letter in 'aeiuo':
            word = i + 'ay'
        else:
            last_letters = i[1:]
            word = last_letters + first_letter + 'ay'
        
        #Removing the " " inside the list and re-inserting updated values
        newList.pop(0)
        newList.append(word)
    
    #Now I'm merging values from the list to be one string
    full_sen = " ".join(newList)
    print(full_sen)

#Calling function
trans()