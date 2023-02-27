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

#Display Card Data In Treeview
def Display_Transformers(treeview,card_data):
    #get card data size equal to number of transformers
    card_data_size = len(card_data)
    #create new transformer
    bot = Transformer_Card({})
    #iterate through card data, output transformer name, subname, cost, and affiliation (through color)
    for index in range(card_data_size):
        #get item from card data
        bot = card_data[index]
        #create index for treeview item
        string_index = str(index)
        location = "item" + string_index
        #insert item into treeview
        treeview.insert('', '0',location, text = bot.name + "    " + bot.sub_name, tags = (bot.loyalty))

    #configure red background for Autbots and purple background for Decepticons
    treeview.tag_configure("Autobot", background = "red")
    treeview.tag_configure("Decepticon", background = "purple")

    #For some reason this function only adds some of the autobots to the treeview, why is unknown for now.
    return treeview

#Main Function
def main():
    #Create Program Window
    window = Tk()
    #Create The Program Title
    window.title("Transformers TCG Card Editor")

    #Create the Top Menu
    menubar = Menu(window)
    #Configure The Top Menu as a Menu Bar
    window.config(menu=menubar)

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

    #Creating The Various Frames To Place In The Window
    card_list_section = ttk.Frame(window) #Contains Tabs For Displaying Treeviews Of Transformer and Battle Cards (and scrollbar)
    card_list_section.config(height = 1000, width = 1000)
    search_section = ttk.Frame(window) #Contains Search Bar and Filter Buttons
    battle_cards_section = ttk.Frame(window) #Contains Selected Battle Cards (and scrollbar)
    transformer_cards_section = ttk.Frame(window) #Contains Selected Transformer Cards (and scrollbar)
    card_preview_section = ttk.Frame(window) #Contains the image for previewing card images after they have been selected

    #Create The card_list_section content
    card_list_section.pack()

    #Add Tabs To Switch Between Viewing Transformer and Battle Cards
    tab_book = ttk.Notebook(card_list_section)
    tab_book.pack()

    tab_transformer = ttk.Frame(tab_book)
    tab_battle = ttk.Frame(tab_book)

    tab_book.add(tab_transformer, text = 'Transformer Cards')
    tab_book.add(tab_battle, text = 'Battle Cards')

    #Add Treeviews To Display Transformer and Battle Cards Within Respective Tabs
    treeview_transformer = ttk.Treeview(tab_transformer)
    #Add transformers from list to treeview
    Display_Transformers(treeview_transformer, List_All_Transformer)
    treeview_transformer.pack()

    treeview_battle = ttk.Treeview(tab_battle)
    treeview_battle.pack()

    tab_book.pack()

    #Open Window
    window.mainloop()

#main loop
if __name__ == "__main__":
    
    main()

