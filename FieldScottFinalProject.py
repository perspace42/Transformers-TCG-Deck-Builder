'''
Author: Scott Field
Version: 1.00
Date: 3/06/2023
Program Name: Transformers Trading Card Game Deck Builder
Program Purpose: Create a Transformers TCG Deck Builder That Will Eventually Be Capable of Listing all 700 Cards in the Tranformers TCG
'''

#Import Libraries
from tkinter import *
from tkinter import ttk   
from Transformers_Card_Data import *
from Transformers_Class_Storage import *

#Acquire Program Data From Transformer_Card_Data.py
List_All_Transformer = Assemble_Transformer_List()
List_All_Battle = Assemble_Battle_List()

#Display Transfoermer Card Data In Treeview
def Display_Transformers(treeview,card_data):
    '''The Purpose Of This Function Is To Display A List Of Transformer Cards To a Treeview Widget
    Args:
    treeview (ttk.treeview): The treeview where the list of bot cards from card_data is to be displayed
    card_data (list): The list containing the Transformer_Card classes to be converted into treeview rows
    '''
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
        treeview.insert('', END,image_location, text = bot.name + "    " + bot.sub_name, values =(bot.name + "   " + bot.sub_name,cost_string), tags = (bot.loyalty))

    #configure red background for Autbots and purple background for Decepticons based on the inserted tag
    treeview.tag_configure("Autobot", background = "red")
    treeview.tag_configure("Decepticon", background = "purple")

    #return the treeview back to the main program
    return treeview

#Display Battle Card Data In Treeview
def Display_Battle(treeview,card_data,third_column_value = None):
    '''The Purpose Of This Function Is To Display A List Of Battle Cards To a Treeview Widget
    Args:
    treeview (ttk.treeview): The treeview where the list of battle cards from card_data is to be displayed
    card_data (list): The list containing the Battle_Card classes to be converted into treeview rows
    third_column_value = None: If not == None, indicates that the battle card treeview contains a third column (a quantity column) that must have a value assigned to it in the treeview.insert() function
    '''
    #get card data size equal to number of transformers
    card_data_size = len(card_data)
    #create new transformer
    battle = Battle_Card({})
    #initialize cost string
    cost_string = ""
    #iterate through card data, output battle card name, cost, and type (through color)
    if (third_column_value == None):
        for index in range(card_data_size):
            #get item from card data
            battle = card_data[index]
            #create image location for treeview item
            image_location = battle.image_path
            #convert cost into string for display purpose
            cost_string = str(battle.cost)
            #insert item into treeview, assign tags to each item
            treeview.insert('', END,image_location, text = battle.name, values = (battle.name,cost_string), tags = (battle.type))

    #else if there is a third column, iterate through card data, output battle card name, cost, type (through color), and set quantity to the value provided
    else:
        for index in range(card_data_size):
            #get item from card data
            battle = card_data[index]
            #create image location for treeview item
            image_location = battle.image_path
            #convert cost into string for display purpose
            cost_string = str(battle.cost)
            #insert item into treeview, assign tags to each item
            treeview.insert('', END,image_location, text = battle.name, values = (battle.name,cost_string,third_column_value), tags = (battle.type))


    #configure cyan background for Action Cards, and green background for Upgrades based on the inserted tag
    treeview.tag_configure("Action", background = "cyan")
    treeview.tag_configure("Upgrade", background = "green")

    return treeview

#Get Image From Selection
def Retrieve_Image(treeview, label):
    '''This function requires the treeview as a parameter in order to retrieve the image location string of the selected Battle or Transformer Card
    Args:
    treeview (ttk.treeview): The treeview from which, the selected row contains the image string as the index of the selected row
    label (tkinter label): The label to which the image string will be added as a photoimage
    '''
    #Ensure that there is still a row from which to select an image (row can be removed from selected transformer card or selected battle cards by left clicking a selected row)
    if (len(treeview.selection()) > 0):
        #Treeview Selection Returns a Tuple Which Must Be Converted Into a String To Turn Into An Image
        selection_tuple = treeview.selection()
        #Convert Tuple To String For Image Selection (image path is located at index 0 of the tuple)
        selection_string = selection_tuple[0]
        #Print To Verify What Program Has Retrieved
        print(selection_string)
        #Define Image amd Image Path
        image = PhotoImage(file = selection_string)
        # update label
        label.config(image=image)
        label.image = image  # store the reference of the image
        #It is not necessary to return anything as the label being referenced has already been defined under the main() function

#Change Button Color and Text Depending On Selected Tab
def Change_Style(tab_book,filter_one,filter_two):
    """The purpose of this function is to rewrite the colors and text of a list of the filter buttons when the next tab is selected to reflect their function
    Args:
    tab_book (ttk.Notebook): The notebook that contains the tabs (frame widgets) that display the available bot and battle cards,
                             In this function it is used to determine which tab is currently active (displayed to user)
    filter_one: (ThemedButton): The first button whose color and text will be changed depending on which tab is currently active
    filter_two: (ThemedButton): The second button whose color and text will be changed depending on which tab is currently active
    """

    if (tab_book.index('current')) == 0: #when tab_book.index('current')==0 then the transformer tab is selected
        filter_one.changeColor('grey') #and therefore the buttons should all have their style changed to grey
        filter_one.setText("Filter Autobots") #set the first button to filter upgrades
        filter_two.setText("Filter Decepticons") #set the second button to filter actions
    else: #otherwise the battle card tab is selected
        filter_two.changeColor('orange') #and all transformers should have their color changed to orange
        filter_one.setText("Filter Upgrades") #set the first button to filter upgrades
        filter_two.setText("Filter Actions") #set the second button to filter actions

#Removes All of a Treeviews Items Or A Single One If An Index Is Specified
def Clear_Treeview(treeview, image_tuple = None):
    '''Purpose of this function is to remove one or all items from a treeview, depending on function parameters
    Args:
    treeview(ttk.Treeview): The treeview from which an item (row) is to be removed if a path string within a tuple is provided, if not all items (rows) are removed
    image_tuple(tuple): default None, if not None posesses an image string to be used as an index for a row within treeview to be removed.
    '''
    #remove a selected item from the treeview
    if image_tuple != None:
        #get the image string from provided tuple
        index = image_tuple[0]
        #remove item from treeview, using image string
        treeview.delete(index)
    #remove each item from the treeview if none is specified
    else:
        for item in treeview.get_children():
            #delete that item
            treeview.delete(item)

#Find either a transformer card or battle card by its image
def Find_Card(given_image_path,card_data):
    '''This function takes advantage of the fact that the .image_path method for Battle_Card and Transformer_Card are one and the same.
    The goal of this function is return the correct Class object (either Battle_Card or Transformer_Card) by searching using that objects image
    Args:
    given_image_path (string): contains the image path to be searched
    card_data(list): contains a list of battle cards or bot cards to be searched by the given_image_path
    '''
    #find the length of data to be searched
    length = len(card_data)
    #search until desired image string is found
    for index in range(length):
        #once desired image string is found
        if (card_data[index].image_path == given_image_path):
            #return image string
            return card_data[index]
    #otherwise return nothing to the main program and inform the user that the image path is incorrect
    print(given_image_path, "Not Found!!!")
    return None

#Add a card from a treeview to another treeview
def Add_Card(tab_book,first_treeview,second_treeview, Transformer_List = List_All_Transformer, Battle_List = List_All_Battle):
    """Purpose of this function is to add a card from selected cards, to the selected card list
    Args:
    tab_book(ttk.Notebook): Displays which frame (tab) is currently selected and therfore which type of class is contained within the treeview (Transformer_Card if active tab 0, Battle_Card if active tab 1)
    first_treeview(ttk.Treeview): The treeview from which the image string for a card is to be taken
    second_treeview(ttk.Treeview): The treeview to which the  found card is to be added
    Transformer_List(list): A list of bot cards that is searched by using the image_string from the first treeview to find a card (if active tab == 0)
    Battle_List(list): A list of batte cards that is searched by using the image_string from the first treeview to find a card (if active tab == 1)
    """

    #Find which tab is currently open (only data from a treeview within an open tab can be added)
    active_tab = tab_book.index('current')
    #Find the tuple that holds the image path
    selection_tuple = first_treeview.selection()
    #Assign the tuples string that holds the image path to a variable
    image_string = selection_tuple[0]
    #initialize the list that will hold the Transformer or Battle Card Class
    output_list = []

    #If the transformer tab is currently open
    if (active_tab == 0):
       #If an exception is raised this means that the same battle card has been attempted to be added to the transformer display treeview, this can be safely ignored by the program
       #(by treeview widget logic the same item cannot be added twice, and by the transformers trading card game rules two of the exact same transformer card is forbidden in the same deck)
       try:
        #Set Bot Equal To The Transformer Card That Contains The Image String
        bot = Find_Card(image_string,Transformer_List)
        #Using a list in order to reuse the Display Transformers Function
        output_list.append(bot)
        Display_Transformers(second_treeview,output_list)
        #therefore the exception ignores the error
       except:
           pass 

    #If the battle tab is currently open
    else:
       #Set battle Equal To The Battle Card That Contains The Image String
       battle = Find_Card(image_string,Battle_List)
       #Using a list in order to reuse the Display Battle Function
       output_list.append(battle)
       
       #If an exception is raised this means that the same battle card has been attempted to be added to the second_treeview, this is acceptable up to 3 times in the battle cards treeview
       #Therefore the function will add a number to the card name to denote how many have been added
       try:
           Display_Battle(second_treeview,output_list,"1")
       #If the same cards have been detected count how many, then if the number counted is < 3 add 1 more To The Quantity Tab
       except:
           #get the values contained within the treeview row tuple
           second_treeview_text = second_treeview.item(battle.image_path,"values")
           print(second_treeview_text)

           #set variables equal to the tuple strings
           name = second_treeview_text[0]
           cost_string = second_treeview_text[1]
           quantity_string = "1"

           #check if row contains a quantity
           if (len(second_treeview_text) > 2):
               #if so, set the quantity string to it
               quantity_string = second_treeview_text[2]

           #convert quantity to int to check if the number of cards added is equal to 3
           quantity = int(quantity_string)
           if (quantity == 3):
               print(battle.name,"has already been added three times")
           #if the card has not been added three times, change the values of the treeview row to reflect the new quantity

           else:
                #increment quantity by 1
                quantity += 1
                #convert quantity to a string
                quantity_string = str(quantity)
                #add the quantity to the item
                second_treeview.item(battle.image_path,values = (name,cost_string,quantity_string))

#Remove a card from a treeview
def Remove_Card(treeview):
    """The purpose of this function is to remove a card from a selected card treeview
    Args:
    treeeview (ttk.Treeview): the treeview from which a row containing information for a card is to be removed.
    """
    #get the tuple containing the image path
    selection_tuple = treeview.selection()
    #If anything has been selected continue, otherwise do nothing
    if (len(selection_tuple) > 0):
        #get image path from tuple
        image_string = selection_tuple[0]
        #get list of values from treeview row
        row_tuple = treeview.item(image_string,"values")
        #get the name of the card from the tuple
        name = row_tuple[0]
        #get the cost of the card in string form from the tuple
        cost_string = row_tuple[1]

        #if row does not have a quantity column
        if (len(row_tuple) < 3):
            #quantity must be 1, and program should simply remove the row
            Clear_Treeview(treeview,selection_tuple)
        
        #else reduce the value in the quantity column of the row by 1
        else:
            #set quantity = rows current quantity
            quantity_string = row_tuple[2]
            #get quantity in integer form
            quantity = int(quantity_string)
            #decrease quantity by one
            quantity -= 1
            #if quantity is now 0
            if (quantity == 0):
                #remove the row from the treeview
                Clear_Treeview(treeview,selection_tuple)
            #add the new quantity back to the treeview
            else:
                #convert quantity back to string form
                quantity_string = str(quantity)
                #add quantity back to the row (along with the other values)
                treeview.item(image_string,values = (name,cost_string,quantity_string))
    

#Filter Cards In A Treeview Depending On The Filter And Tab User Selected
def Filter_Cards(tab_book,treeview_transformer,treeview_battle,filter = None, Transformer_List = List_All_Transformer, Battle_List = List_All_Battle):
    '''The purpose of this funtion is to change the results displayed within the card list view treeview depending on the buttons the user selects
    Args:
    tab_book(ttk.Notebook): provides a means to check which tab (frame) containing cards has been currently selected by the user
    treeview_transformer(ttk.Treeview): provides all of the rows to display filtered bot card data if the tab containing their treeview is active
    treeview_battle(ttk.Treeview): provides all of the rows to display filtered battle card data if the tab containing their treeview is active
    filter(string): provides the argument for the program to filter the active card treeview by (if None show all cards)
    Transformer_List(list): contains all bot cards within the program, the filter will be applied to this data if the bot treeview is active
    Battle_List(list): contains all bot cards within the program, the filter will be applied to this data if the bot treeview is active
    '''
    #determines which tab has been selected,( 0 = transformer cards or 1 = battle cards), and therefore which treeview to filter
    active_tab = tab_book.index('current')
    #initialization of the variable that stores the filtered results
    output_list = []
    
    #Filter by Transformer Card
    if (active_tab == 0): #If the transformer tab is the currently selected tab

        #Check to see which transformer loyalty the program should filter 
        if (filter == "Autobot&Upgrade"):
            #Set Filter = Autobot since the transformer tab has been selected and the filter item is Autobots&Upgrade
            filter = "Autobot"
        elif(filter == "Decepticon&Action"):
            #Set Filter = Decepticon since the transformer tab has been selected and the filter item is Decepticon&Action
            filter = "Decepticon"
        else:
            #Set Filter = None since the transformer tab has been selected and the filter item is Show All
            filter = None

        #Clear The Transformer Treeview
        Clear_Treeview(treeview_transformer)
        #If There Is a Filter Item, Filter The Data
        if (filter != None):
            #get the length of the data
            card_data_size = len(Transformer_List)
            #for each card in the card data
            for index in range(card_data_size):
                #get the current card
                current_card = Transformer_List[index]
                #get the current cards loyalty
                card_loyalty = current_card.loyalty
                #check if filter matches current card loyalty
                if (card_loyalty == filter):
                    #if it does add the card to the now filtered output list
                    output_list.append(current_card)

            #Because There is a filter item display with the output list rather than the total list
            Display_Transformers(treeview_transformer,output_list)

        #If there is no Filter Item, Display All Cards Within The Treeview (Show All Selected)
        else:
            #Display All Cards
            Display_Transformers(treeview_transformer,Transformer_List)
            
    #Filter by Battle Card
    else: #If the battle tab is the currently selected tab

        #Check to see which transformer loyalty the program should filter 
        if (filter == "Autobot&Upgrade"):
            #Set Filter = Upgrade since the transformer tab has been selected and the filter item is Autobot&Upgrade
            filter = "Upgrade"
        elif (filter == "Decepticon&Action"):
            #Set Filter = Action since the battle tab has been selected and the filter item is Decepticon&Action
            filter = "Action"
        else:
            #Set Filter = None since the battle tab has been selected and the filter item is None
            filter = None

        #Clear The Battle Treeview
        Clear_Treeview(treeview_battle)
        #If There Is a Filter Item, Filter The Data
        if (filter != None):
            #get the length of the data
            card_data_size = len(Battle_List)
            #for each card in the card data
            for index in range(card_data_size):
                #get the current card
                current_card = Battle_List[index]
                #get the current cards type
                card_type = current_card.type
                #check if filter matches current card type
                if (card_type == filter):
                    #if it does add the card to the now filtered output list
                    output_list.append(current_card)

            #Because There is a filter item
            Display_Battle(treeview_battle,output_list)

        #If there is no Filter Item, Display All Cards
        else:
            #Display All Cards
            Display_Battle(treeview_battle,Battle_List)

#Returns A Tuple Containing The Total Cost & Number Of Cards Within A Treeview
def Get_Totals(treeview,columns):
    """Using the numeber of columns within the treeview determine whether the selected transformers treeview
      or selected battle treeview has been passed as a parameter, then find the amount of cards that treeview contains
    and the total cost of all the cards within that treeview
    Args:
    treeview(ttk.Treeview): contains the rows and values from which the cost and number of cards represented by the treeview widget will be returned
    columns(int): if 3 reveals that the parameter treeview contains a quantity column that must be factored into the calculation 
    of the number of cards and cost of cards, if not 3 reveals that their is not quantity column
    """
    #initialization
    spent_points = 0
    total_cards = 0
    quantity = 1

    #if the selected treeview displays transformers
    if (columns < 3):
        #for each row in the treeview
        for child in treeview.get_children():
            #get the tuple displaying all of the rows values
            child_tuple = treeview.item(child)["values"]
            #get the cost from that value
            child_string = child_tuple[1]
            child_cost = int(child_string)
            #add the cost to spent points
            spent_points += child_cost
            #increment total cards by 1
            total_cards += 1

    else:
        for child in treeview.get_children():
            #get the tuple displaying all of the rows values
            child_tuple = treeview.item(child)["values"]
            #get the cost from that value
            child_string = child_tuple[1]
            child_cost = int(child_string)
            #get the quantity from that value
            quantity_string = child_tuple[2]
            quantity = int(quantity_string)
            #add the cost * quantity to spent points
            spent_points += child_cost * quantity
            #add the card * quantity to total cards
            total_cards += 1 * quantity

    return [spent_points,total_cards]

#Adjust SubTotal Point Count Based On How Many Cards Were Added To Parameter Treeview
def Update_Subtotals(treeview,columns,tree_cost_label,number_cards_label):
    """Using the provided number of columns (if 2 selected transformers treevieww, if 3 selected battle cards treeview) 
    find which type of card has been added to the treeview, then get the treeview current cost (and quantity if applicable)
    After which point update the total_cost_label and number_cards_label
    Args:
    treeview(ttk.Treeview): reveals which treeview has been updated (either a card has been added or a card has been removed)
    columns(int): reveals whether or not the treeview to be updated contains a quantity column, if columns = 2 it does not, otherwise it does
    and must be factored into the toal point and card count
    tree_cost_label(ThemedLabel): The label that displays the total cost of all cards within a single treeview
    number_cards_label(ThemedLabel): The label that displays the total number of cards within a single treeview
    """
    
    #Initialization
    #stores list of treeview totals
    treeview_total = []
    
    #if the selcted transformers card tab is the one being updated (contains 2 columns)
    if (columns == 2):
        treeview_total = Get_Totals(treeview,2)
    #if the selected battle card tab is the one being updated (contains 3 columns)
    else:
        treeview_total = Get_Totals(treeview,3)

    #access amounts from treeview total
    treeview_cost = treeview_total[0]
    treeview_cards = treeview_total[1]


    #Set Label Text
    tree_cost_label.setCurrentNumber(treeview_cost)
    number_cards_label.setCurrentNumber(treeview_cards)

#Adjust Total Point Count Based On Amounts In Each Subtotal
def Update_Total(left_label,right_label,total_label):
    """This function is to add together both subtotals of the card selection section into the total spent points section
    Args:
    left_label(ThemedLabel): The label that provides the left (Bot Treeview) cost subtotal
    right_label(ThemedLabel): The label that provides the right (Battle Treeview) cost subtotal)
    total_label(ThemedLabel): The label that displays the result of: left_label subtotal + right_label subtotal
    """
    #get the number currently being displayed by the left label
    left_number = left_label.getCurrentNumber()
    #get the number currently being displayed by the right label
    right_number = right_label.getCurrentNumber()
    #update the total label
    total_label.setCurrentNumber(left_number + right_number)

#Create A New Window That Contains All Of The Program Functions & Capabilities 
def New_Window(window):
    """Upon the 'New' file menu option being selected, create a new window with the same format as the old one 
    Args:
    window(Tk()): provides the root window from which a new window can be created using the main(window) function
    """
    #Define new window on top of the old window
    next_window = Toplevel(window)
    #Create widgets within new window so that it looks and functions just like the old one on startup
    main(next_window)

#Main Function
def main(window):
    """This Function Is Where The Program Layout Is Assembled
    Args:
    window(Tk()): provides the root window from which the first window can be created
    """
    #Create The Program Title
    window.title("Transformers TCG Deck Builder")
    #Resize window geometry based on widgets added to window
    window.geometry("")
    
    #Creating The Various Frames To Place In The Window (Remember To Increase Their Size Based On the Widgets They Contain)
    card_list_section = ttk.Frame(window) #Contains Tabs For Displaying Treeviews Of Transformer and Battle Cards 
    search_section = ttk.Frame(window) #Contains Filter Buttons
    selection_section = ttk.Frame(window) #Contains Selected Transformer & Battle Cards 
    card_preview_section = ttk.Frame(window) #Contains the image for previewing card images after they have been selected

    #SELECTION SECTION START

    transformer_label = Label(selection_section,text = "Selected Transformer Cards")

    #set the selected transformer treeview equal to original treeview
    selected_transformer = ttk.Treeview(selection_section, column = ("c1", "c2"), show = 'headings', height = 10)
    #Anchor Column #1 (Transformer Name Column) West and set its width to 275
    selected_transformer.column("# 1", anchor = W, width = 275)
    selected_transformer.heading("# 1", text = "Transformer Card Name")
    selected_transformer.column("# 2", anchor = CENTER, width = 100)
    selected_transformer.heading("# 2", text = "Cost")

    battle_label = Label(selection_section,text = "Selected Battle Cards")

    #set the selected battle treeview equal to original treeview
    selected_battle = ttk.Treeview(selection_section, column = ("c1", "c2","c3"), show = 'headings', height = 10)
    #Anchor Column #1 (Battle Name Column) West and set its width to 275
    selected_battle.column("# 1", anchor = W, width = 275)
    selected_battle.heading("# 1", text = "Batle Card Name")
    selected_battle.column("# 2", anchor = CENTER, width = 50)
    selected_battle.heading("# 2", text = "Cost")
    selected_battle.column("# 3", anchor = CENTER, width = 50)
    selected_battle.heading("# 3", text = "Quantity")

    #Set a label to store the cost of transformers
    transformer_cost_label = ThemedLabel(selection_section, text = "Transformer Points:", current_number = 0)
    #Set a label to store the cost of battle cards
    battle_cost_label = ThemedLabel(selection_section, text = "Battle Card Points:", current_number = 0)
    #Set a label to store total points spent (max 25, on initialization 0 have been spent)
    total_cost_label = ThemedLabel(selection_section, text = "Total Spent Points:", current_number = 0, total_number = 25)
    #Set a label to store number of transformers used (max 6, on initialization 0 have been spent)
    number_bots_label = ThemedLabel(selection_section, text = "Used Transformers:", current_number = 0, total_number = 6)
    #Set a label to store number of cards added (max 40, on initialization 0 have been added)
    number_battle_label = ThemedLabel(selection_section, text = "Added Cards:", current_number = 0, total_number = 40)

    #row 0 widgets placement
    transformer_label.grid(row = 0, column = 0)
    battle_label.grid(row = 0, column = 1)

    #row 1 widgets placement
    number_bots_label.grid(row = 1,column = 0)
    number_battle_label.grid(row = 1,column = 1)

    #row 2 widgets placement
    transformer_cost_label.grid(row = 2, column = 0)
    battle_cost_label.grid(row = 2, column = 1)

    #row 3 widgets placement (extend across 2 columns)
    total_cost_label.grid(row = 3,column = 0, columnspan = 2)

    #row 4 widgets placement
    selected_transformer.grid(row = 4, column = 0)
    selected_battle.grid(row = 4, column = 1)

    #command bindings
    #remove the selected card from the treeview when right click is selected
    #remove from selected battle cards treeview, then update the battle subtotal label and total label
    selected_battle.bind('<Button-3>',lambda e: [Remove_Card(selected_battle),
                                                 Update_Subtotals(selected_battle,3,battle_cost_label,number_battle_label),
                                                 Update_Total(transformer_cost_label,battle_cost_label,total_cost_label)])
    #remove from selected transformer cards treeview, then update the transformer subtotal label total label
    selected_transformer.bind('<Button-3>',lambda e: [Remove_Card(selected_transformer),
                                                      Update_Subtotals(selected_transformer,2,transformer_cost_label,number_bots_label),
                                                      Update_Total(transformer_cost_label,battle_cost_label,total_cost_label)])

    #SELECTION SECTION END

    #CARD LIST DISPLAY SECTION START

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
    #Configure Treeview To Contain Two Columns, Show Heading Text On Each, And To Display 10 Lines Of Transformers At One Time
    treeview_transformer = ttk.Treeview(tab_transformer, column = ("c1", "c2"), show = 'headings', height = 10)
    #Anchor Column #1 (Transformer Name Column) West and set its width to 275
    treeview_transformer.column("# 1", anchor = W, width = 275)
    treeview_transformer.heading("# 1", text = "Transformer Card Name")
    treeview_transformer.column("# 2", anchor = CENTER, width = 100)
    treeview_transformer.heading("# 2", text = "Cost")
    
    #Add transformers from list to treeview
    Display_Transformers(treeview_transformer, List_All_Transformer)
    treeview_transformer.pack()

    #Add Treeview To Display Battle Cards Within Respective Tab
    treeview_battle = ttk.Treeview(tab_battle, column = ("c1", "c2"), show = 'headings', height = 10)
    #Configure Multiple Columns Within Treeview
    treeview_battle.column("# 1",anchor = W, width = 275)
    treeview_battle.heading("# 1", text = "Battle Card Name")
    treeview_battle.column("# 2", anchor = CENTER, width = 100)
    treeview_battle.heading("# 2", text = "Cost")

    #Add battle cards from list to treeview
    Display_Battle(treeview_battle,List_All_Battle)
    #print treeview to tab
    treeview_battle.pack()

    #print tab_book to window
    tab_book.pack()

    #set am empty string to display an image string in the card_preview_section frame 
    image_string = ""
    #set the image equal to the variable class string
    card_image = PhotoImage(file = image_string)
    #define the label to hold the image
    image_label = Label(card_preview_section,image = card_image)
    #print the label to the tkinter frame
    image_label.pack()
    
    #On double click of a treeview transformer item, add the card to a display treeview and adjust the totals
    treeview_transformer.bind("<Double-1>", lambda e: [Add_Card(tab_book,treeview_transformer,selected_transformer),
                                                       Update_Subtotals(selected_transformer,2,transformer_cost_label,number_bots_label),
                                                       Update_Total(transformer_cost_label,battle_cost_label,total_cost_label)])
    #On double click of a treeview battle item, add the card to a display treeview and adjust the totals
    treeview_battle.bind("<Double-1>", lambda e: [Add_Card(tab_book,treeview_battle,selected_battle),
                                                  Update_Subtotals(selected_battle,3,battle_cost_label,number_battle_label),
                                                  Update_Total(transformer_cost_label,battle_cost_label,total_cost_label)])

    #Function Retrieves The Image (From Mouse Button 1 Being Released) Then Displays The Image Using The Label
    #Mouse release is used here instead of mouse click in order to avoid conflict between Mouse Click and Double Click
    treeview_battle.bind('<ButtonRelease-1>', lambda e:  Retrieve_Image(treeview_battle,image_label))
    treeview_transformer.bind('<ButtonRelease-1>', lambda e: Retrieve_Image(treeview_transformer,image_label))
    
    #Function To Retrieve Image When a Selected Card Is Picked
    #The binding is different for the selected cards because double click is not used in the CARD SELECTION SECTION
    selected_battle.bind('<<TreeviewSelect>>', lambda e:  Retrieve_Image(selected_battle,image_label))
    selected_transformer.bind('<<TreeviewSelect>>', lambda e: Retrieve_Image(selected_transformer,image_label))

    #IMAGE PREVIEW SECTION END
    #CARD LIST DISPLAY SECTION END

    #SEARCH SECTION START
    
    #Confiugre A Button To Filter Autobot Cards & Battle Cards Depending On Which Treeview Is Selected (Starts With Default Of Filtering Autbot Cards)
    filter_one = ThemedButton(search_section, text = "Filter Autobots", Mybackground = '', command = lambda: Filter_Cards(tab_book,treeview_transformer,treeview_battle,"Autobot&Upgrade"))
    filter_one.pack(side = LEFT)
    
    filter_two = ThemedButton(search_section, text = "Filter Decepticons", Mybackground = '', command = lambda: Filter_Cards(tab_book,treeview_transformer,treeview_battle,"Decepticon&Action"))
    filter_two.pack(side = LEFT)
    #filter_threes text is never changed therefore it is necessary to set it here
    filter_three = ThemedButton(search_section, text = "Show All", Mybackground = '', command = lambda: Filter_Cards(tab_book,treeview_transformer,treeview_battle))
    filter_three.pack(side = LEFT)

    #Check If The Tab Has Been Changed Then When It Is Check To See Which Tab Is Displaying, Then Change Filter Buttons Appropriately (The third button never changes its text)
    tab_book.bind('<<NotebookTabChanged>>', lambda e: Change_Style(tab_book,filter_one,filter_two))

    #SEARCH SECTION END
    
    #ORGANIZE THE FRAMES SECTION START
    search_section.grid(row = 0, column = 0, sticky = W)
    card_list_section.grid(row = 1, column = 0, sticky = N)
    card_preview_section.grid(row = 2, column = 1, sticky = W)
    selection_section.grid(row = 1,column = 1, sticky = W)
    #ORGANIZE THE FRAMES SECTION END

    #FILE MENU CONFIGURATION SECTION START
    #File Menu Currently Contains: New, Exit

    #Create the Top Menu
    menubar = Menu(window)
    #Configure The Top Menu as a Menu Bar
    window.config(menu=menubar)
    #Create The (File) Menu Within the Menu Bar (No tearoff menu must remain bound to program)
    file_menu = Menu(menubar, tearoff = False)
    # Create File Menu Options:
    # Option To Create A New Window
    file_menu.add_command(label = "New", command = lambda: New_Window(window))
    #Option To Delete A Window
    file_menu.add_command(label = 'Exit', command = window.destroy)
    
    #Add The (File Menu To the Menu Bar)
    menubar.add_cascade(label = "File",menu = file_menu)
    #FILE MENU CONFIGURATION SECTION END

    #Loop Window
    window.mainloop()

#main loop
if __name__ == "__main__":
    #Create Program Window
    window = Tk()
    #Loop window
    main(window)

