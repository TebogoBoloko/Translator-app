#Pig Latin transaltor Version 0.1

#My imports
import tkinter as tk

#GUI-Creating the window
window = tk.Tk()
window.title("Pig Latin Translator")
window.geometry("600x300")

#GUI-Creating my labels
label1 = tk.Label(text="Enter the sentence you wish to translate: ")
label1.grid(column=0,row=0)

#GUI-Creating my entry
entry1 = tk.Entry()
entry1.grid(column=2,row=0)

#----function that does the actual translating----
def trans():
    #User input 
    user_input = str(entry1.get())
    
    
    #Splitting my string to put it inside a list
    #Creating a new list as well...
    my_list = user_input.split()
    newList = [' ']*len(my_list)

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
    
    #Pasting my results in the entry point
    results = tk.Text(master=window,height=10,width=30)
    results.grid(column=0,row=4)
    results.insert(tk.END,full_sen)
    
    

#GUI-Button
button1 = tk.Button(text="Translate", command=trans)
button1.grid(column=0,row=3)

#GUI-Executing the main loop function
window.mainloop()