'''
Author: Scott Field
Version: 1.00
Date: 2/28/2023
Program Name: Transformers_Class_Storage
Program Purpose: Stores The Classes For The Tkinter Window For The Transformers TCG_Deck_Builder.py file
This program is called by the TranformersTCG_Deck_Builder.py file
'''

from tkinter import *
from tkinter.ttk import *
from Transformers_Card_Data import *


#Class For Displaying Labels That Need To Store Numbers
class ThemedLabel(Label):
    def __init__(self,frame,text,current_number,total_number = None):
        #get the frame the label will deploy in
        self.frame = frame

        #get the number value that represents how much has been added
        self.current_number = current_number
        #get the number value that represents the max to be added
        self.total_number = total_number

        #convert current number to string for output
        self.current_string = str(current_number)
        #convert max number value to string for output
        self.total_string = str(total_number)

        #format the output total
        if (self.total_number!= None):
            self.total = " " + "(" + self.current_string + "/" + self.total_string + ")"
        else:
            self.total = " " + "(" + self.current_string + ")"

        #add the output text to class
        self.text = text
        #add the text and ouput total to the output string
        self.output = self.text + self.total

        #Inherit attributes of label
        Label.__init__(self,frame,text = self.output)

    #return the current number
    def getCurrentNumber(self):
        return self.current_number
    
    #return the total number
    def getTotalNumber(self):
        return self.total_number
    
    #return the complete text 
    def getText(self):
        return self.output
    
    def setCurrentNumber(self,number):
        #increase current displayed number by number
        self.current_number = number
        self.current_string = str(self.current_number)
        #format the output total
        #if their is a total number set total to format 1
        if (self.total_number!= None):
            #set format 1
            self.total = " " + "(" + self.current_string + "/" + self.total_string + ")"
        #if their is not a total number set total to format 2
        else:
            #set format 2
            self.total = " " + "(" + self.current_string + ")"
        #add the output text to the current text
        self.output = self.text + self.total
        self.config(text = self.output)


#Change The Colors Of All ttk buttons
class ThemedButton(Button):
    #initailize class
    def __init__(self,frame,text,Mybackground,command):
        self.frame = frame
        self.text = text
        #Mybackground distinguishes which background is the parameter
        self.background = Mybackground
        self.command = command
        #Inherit attributes of ttk.button
        Button.__init__(self,self.frame,text = self.text, command = self.command)

        #Create New Style For Button
        self.style = Style()
        #Set Style To Alternate
        self.style.theme_use('alt')
        #Configure New Style Name & Color
        self.style.configure('TButton', background = Mybackground)

    #method to change color to provided color
    def changeColor(self,color):
         #change the style
         self.style.configure('TButton', background = color)
         #map the style to the button
         self.style.map('TButton',background = [('active',color)])
    #method to change text to provided text
    def setText(self,newText):
        #configure text equal to the new text
        self.configure(text = newText)


    
        



        




        
    
