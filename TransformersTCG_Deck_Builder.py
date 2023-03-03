'''
Author: Scott Field
Version: 0.75
Date: 2/26/2023
Program Name: Transformers Trading Card Game Deck Builder
Program Purpose: Create a Transformers TCG Deck Builder That Will Eventually Be Capable of Listing all 700 Cards in the Tranformers TCG
'''

#Import Libraries
from tkinter import *
from tkinter import ttk   
from Transformers_Card_Data import *


#Acquire Program Data From Transformer_Card_Data.py
List_All_Transformer = Assemble_Transformer_List()
List_All_Battle = Assemble_Battle_List()

#Display Transfoermer Card Data In Treeview
def Display_Transformers(treeview,card_data):
    '''The Purpose Of This Function Is To Display A List Of Transformer Cards To a Treeview Widget'''
    #get card data size equal to number of transformers
    card_data_size = len(card_data)
    #create new transformer
    bot = Transformer_Card({})
    #initialize cost string
    cost_string = ""
    #iterate through card data, output transformer name, subname, cost, and affiliation (through color)
    for index in range(card_data_size):
        #get item from card data
        bot = card_data[index]
        #get image string for when the treeview item is selected
        image_location = bot.image_path
        #convert cost into string for display purpose
        cost_string = str(bot.cost)
        #insert item into treeview, assign tags to each item
        treeview.insert('', '0',image_location, text = bot.name + "    " + bot.sub_name + "   " + cost_string, tags = (bot.loyalty))

    #configure red background for Autbots and purple background for Decepticons
    treeview.tag_configure("Autobot", background = "red")
    treeview.tag_configure("Decepticon", background = "purple")

    return treeview

#Display Battle Card Data In Treeview
def Display_Battle(treeview,card_data):
    '''The Purpose Of This Function Is To Display A List Of Battle Cards To a Treeview Widget'''
    #get card data size equal to number of transformers
    card_data_size = len(card_data)
    #create new transformer
    battle = Battle_Card({})
    #initialize cost string
    cost_string = ""
    #iterate through card data, output battle card name, cost, and type (through color)
    for index in range(card_data_size):
        #get item from card data
        battle = card_data[index]
        #create image location for treeview item
        image_location = battle.image_path
        #convert cost into string for display purpose
        cost_string = str(battle.cost)
        #insert item into treeview, assign tags to each item
        treeview.insert('', '0',image_location, text = battle.name + "    " + cost_string, tags = (battle.type))

    #configure magenta background for Action Cards, and grey background for Upgrades
    treeview.tag_configure("Action", background = "magenta")
    treeview.tag_configure("Upgrade", background = "grey")

    return treeview


#Get Image From Selection
def Retrieve_Image(treeview):
    '''This function requires the treeview as a parameter in order to retrieve the image location string of the selected Battle or Transformer Card'''
    #Treeview Selection Returns a Tuple Which Must Be Converted Into a String To Turn Into An Image
    selection_tuple = treeview.selection()
    #Convert Tuple To String For Image Selection (image path is located at index 0 of the tuple)
    selection_string = selection_tuple[0]
    #Print To Verify What Program Has Retrieved
    print(selection_string)
    #Define Image amd Image Path
    image = PhotoImage(file = selection_string)
    return image




#Main Function
def main():
    """This Function Is Where The Program Layout Is Assembled"""
    #Create Program Window
    window = Tk()
    #Create The Program Title
    window.title("Transformers TCG Card Editor")

    #Create the Top Menu
    menubar = Menu(window)
    #Configure The Top Menu as a Menu Bar
    window.config(menu=menubar)
    #Resize window geometry based on widgets added to window
    window.geometry("")
    #File Menu Contains: New, Open, Save, Save As, Exit
    #Create The (File) Menu Within the Menu Bar (No tearoff menu must remain bound to program)
    file_menu = Menu(menubar, tearoff = False)
    #File Menu Options:
    file_menu.add_command(label = "New", command = None)
    file_menu.add_command(label = "Open", command = None)
    file_menu.add_command(label = "Save", command = None)
    file_menu.add_command(label = "Save As", command = None)
    file_menu.add_command(label = 'Exit', command = window.destroy)
    #Add The (File Menu To the Menu Bar)
    menubar.add_cascade(label = "File",menu = file_menu)

    #Creating The Various Frames To Place In The Window (Remember To Increase Their Size Based On the Widgets They Contain)
    card_list_section = ttk.Frame(window,width = 500, height = 500) #Contains Tabs For Displaying Treeviews Of Transformer and Battle Cards (and scrollbar)
    search_section = ttk.Frame(window) #Contains Search Bar and Filter Buttons
    battle_cards_section = ttk.Frame(window) #Contains Selected Battle Cards (and scrollbar)
    transformer_cards_section = ttk.Frame(window) #Contains Selected Transformer Cards (and scrollbar)
    card_preview_section = ttk.Frame(window,width = 1000, height = 1000) #Contains the image for previewing card images after they have been selected

    #CARD LIST SECTION START
    card_list_section.pack(side = "top", fill = "both", expand = True)

    #Add Notebook to store Tabs To Switch Between Viewing Transformer and Battle Cards
    #Add the tab_book to the card_list_section Frame
    tab_book = ttk.Notebook(card_list_section)
    tab_book.pack()

    #Add Tabs To Switch Between Viewing Transformer and Battle Cards
    tab_transformer = ttk.Frame(tab_book,width = 500, height = 500)
    tab_battle = ttk.Frame(tab_book,width = 500, height = 500)

    #Add text to tabs, add tabs to tab_book
    tab_book.add(tab_transformer, text = 'Transformer Cards')
    tab_book.add(tab_battle, text = 'Battle Cards')

    #Add Treeviews To Display Transformer Cards Within Respective Tab
    treeview_transformer = ttk.Treeview(tab_transformer)
    #Add transformers from list to treeview
    Display_Transformers(treeview_transformer, List_All_Transformer)
    treeview_transformer.pack(side = "top", fill = "both", expand = True)

    #Add Treeview To Display Battle Cards Within Respective Tab
    treeview_battle = ttk.Treeview(tab_battle)
    #Add battle cards from list to treeview
    Display_Battle(treeview_battle,List_All_Battle)
    treeview_battle.pack(side = "top", fill = "both", expand = True)

    #pack must be called with these three arguments to ensure that the widget expands with the window, it is anchored 'e' to align it left
    tab_book.pack(side = "top", fill = "both", expand = True, anchor = 'e')

    #IMAGE PREVIEW SECTION START

    #Set Card Preview Frame
    #pack must be called with these three arguments to ensure that the widget expands with the window,
    card_preview_section.pack(side = "top", fill = "both", expand = True)
    #Stop Frame From Shrinking To Fit Its Initial Contents
    card_preview_section.pack_propagate(False)

    #initialize label to display initial image

    #set a variable class to display an image string in the card_preview_section frame
    image_string = StringVar(card_preview_section,"Reckless-Charge.gif")
    #set the image equal to the variable class string
    card_image = PhotoImage(file = image_string.get())
    image_label = Label(card_preview_section,image = card_image)
    image_label.pack()
    
    #Command Bindings For Treeview (Print Current Selection, and Display Image To Frame)

    #Function Should Retrieve The Image (From TreeviewSelect), Then Display The Image Using a Label)
    treeview_battle.bind('<<TreeviewSelect>>', lambda e:  image_label.config(image = Retrieve_Image(treeview_battle)))
    treeview_transformer.bind('<<TreeviewSelect>>', lambda e: image_label.config(image = Retrieve_Image(treeview_transformer)))


    #CARD LIST SECTION END

    


    #Open Window
    window.mainloop()

#main loop
if __name__ == "__main__":
    
    main()

