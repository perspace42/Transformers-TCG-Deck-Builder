'''
Author: Scott Field
Version: 1.0
Date: 2/26/2023
Program Name: Transformers_Card_Data
Program Purpose: Create Classes and Functions For Displaying Card Data
This program is called by the TranformersTCG_Deck_Builder.py file
'''

#Define Battle Card
class Battle_Card():
    '''Purpose of this class is to store the data contained within a Transformers TCG battle card'''
    #define class 

    def __init__(self,battle_dict):
        #card name
        self.name = battle_dict.get("name",None)

        #whether card is 'action' or 'upgrade'
        self.type = battle_dict.get("type",None)

        #only equipment battle cards will contain a subtype (gear, weapon, armor)
        self.subtype = battle_dict.get("subtype",None)
        #icon is short for the battle icons that appear in the top right of battle cards (some contain none)
        self.icon = battle_dict.get("icon",None)

        #card effect text
        self.text = battle_dict.get("text",None)

        #card stat bonus (whether the card boosts the stats of the transformer it is attached to) if not bonus is 0
        self.bonus_attack = battle_dict.get("b_attack",0)
        self.bonus_defense = battle_dict.get("b_defense",0)

        #battle cards with a cost of nothing will have their cost set to 0
        self.cost = battle_dict.get("cost", 0)

        #Store the path to the card image, display an error image if not found
        self.image_path = battle_dict.get("image_path","error.gif")

    #Print Function
    def __str__(self):
        #return a string containing all items
        return(str(self.__dict__))

#Define Transformer Card
class Transformer_Card():
    '''Purpose of this class is to store the data contained within a Transformers TCG bot card'''
    def __init__(self,transform_dict):
        #self,name,sub_name,bot_mode,alt_mode,star_cost,affiliation
        self.name = transform_dict.get("name",None)
        self.sub_name = transform_dict.get("sub_name",None)

        #individual bot_stats
        self.bot_attack = transform_dict.get('bot_attack',None)
        self.bot_health = transform_dict.get('bot_health',None)
        self.bot_defense = transform_dict.get('bot_defense',None)
        self.bot_text = transform_dict.get("bot_text",None)

        #traits are stored in a list
        self.bot_traits = transform_dict.get("bot_traits",None)

        #individual vehicle_stats (if vehicle stats are not specified then the vehcile stat is the same as the bot stat except for text and traits)
        self.vehicle_attack = transform_dict.get('vehicle_attack',self.bot_attack)
        self.vehicle_health = transform_dict.get('vehicle_health', self.bot_health)
        self.vehicle_defense = transform_dict.get('vehicle_defense',self.bot_defense)

        #card effect
        self.vehicle_text = transform_dict.get("vehicle_text", None)

        #traits are stored in a list
        self.vehicle_traits = transform_dict.get("vehicle_traits",None)

        #loyalty displays if a transformer is either an autobot or a decepticon
        self.loyalty = transform_dict.get('loyalty')

        #transformer cards with a cost of nothing will have their cost set to 404 to display that cost was entered incorrectly
        self.cost = transform_dict.get("cost", 404)

        #Store the path to the card image, display an error image if not found
        self.image_path = transform_dict.get("image_path","error.gif")
    
    #Print Function
    def __str__(self):
        #return a string containing all items
        return(str(self.__dict__))

#Place List of Transformer Card Test Data Here
def Assemble_Transformer_List():
    '''The Purpose Of This Function Is To Provide A List of Tranformer Cards For The TransformersTCG_Deck_Builder.py File.'''
    Transformer_Data = []
    #Autbots Card List Start
    Transformer_Data.append(Transformer_Card({"name":"Bumblebee",
                                              "sub_name":"Courageous Scout",
                                              "bot_traits": ["Specialist"],

                                              "bot_attack": 6,
                                              "bot_health": 10,
                                              "bot_defense": 2,
                                              "bot_text": "When this attacks or defends and you flip at least <white><white><arrow> Flip 2 more battle cards",

                                              "vehicle_traits": ["Car","Specialist"],
                                              "vehicle_attack": 5,
                                              "vehicle_text": "When you flip to this mode <arrow> Draw a card. Then put a card from your hand on top of your deck",

                                              "loyalty":"Autobot",
                                              "cost": 9,
                                              "image_path":"Autobot-Bumblebee.gif"
                                              }))

    Transformer_Data.append(Transformer_Card({"name":"Arcee",
                                              "sub_name":"Skilled Fighter",
                                              "bot_traits": ["Specialist"],

                                              "bot_attack": 1,
                                              "bot_health": 9,
                                              "bot_defense": 1,
                                              "bot_text": "This has Pierce equal to her <attack> (Do at least <attack> damage when attacking)",

                                              "vehicle_traits": ["Motorcycle","Specialist"],
                                              "vehicle_attack": 2,
                                              "vehicle_text": "When you flip to this mode <arrow> Repair 1 damage from eacy of your characters",

                                              "loyalty":"Autobot",
                                              "cost": 5,
                                              "image_path":"Autobot-Arcee.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Autobot Cosmos",
                                              "sub_name":"Recon & Communication",
                                              "bot_traits": ["Specialist"],

                                              "bot_attack": 2,
                                              "bot_health": 21,
                                              "bot_defense": 1,
                                              "bot_text": "When you reshuffle your deck while this is attacking <arrow> KO the defender if it has 12<cost> or fewer.",

                                              "vehicle_traits": ["Spaceship","Specialist"],
                                              "vehicle_attack": 1,
                                              "vehicle_text": "When you flip to this mode <arrow> Scrap all cards from your hand. Then draw that many cards.",

                                              "loyalty":"Autobot",
                                              "cost": 11,
                                              "image_path":"Autobot-Cosmos.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Autobot Mirage",
                                              "sub_name":"Lone Wolf",
                                              "bot_traits": ["Ranged"],

                                              "bot_attack": 5,
                                              "bot_health": 12,
                                              "bot_defense": 2,
                                              "bot_text": "When this attacks for the first time each turn and you flip at least <white><white><white> <arrow> Untap this.",

                                              "vehicle_traits": ["Car","Melee"],
                                              "vehicle_attack": 4,
                                              "vehicle_text": "When you flip to this mode <arrow> You may play an Action.",

                                              "loyalty":"Autobot",
                                              "cost": 9,
                                              "image_path":"Autobot-Mirage.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Optimus Prime",
                                              "sub_name":"Battlefield Legend",
                                              "bot_traits": ["Leader","Ranged"],

                                              "bot_attack": 8,
                                              "bot_health": 14,
                                              "bot_defense": 2,
                                              "bot_text": "After you flip battle cards for this characters attack and before defense flips <arrow> you may play one of the Actions that you flipped.",

                                              "vehicle_traits": ["Leader","Truck","Melee"],
                                              "vehicle_attack": 6,
                                              "vehicle_defense": 3,
                                              "vehicle_text": "When you flip to this mode <arrow> Return an Action from your scrap pile to hand.",

                                              "loyalty":"Autobot",
                                              "cost": 13,
                                              "image_path":"Autobot-Optimus_Prime.gif"
                                              }))
    #Autobots Card List End
    
    #Decepticon Card List Start
    Transformer_Data.append(Transformer_Card({"name":"Flamewar",
                                              "sub_name":"Veteran Decepticon",
                                              "bot_traits": ["Specialist"],

                                              "bot_attack": 3,
                                              "bot_health": 10,
                                              "bot_defense": 1,
                                              "bot_text": "Each of your characters has Tough 1. (Flip 1 more battle card when defending.)",

                                              "vehicle_traits": ["Motorcycle","Specialist"],
                                              "vehicle_text": "When you flip to this mode <arrow> Each of your characters gets Bold 1 until end of turn (Flip 1 more battle card when attacking.)",

                                              "loyalty":"Decepticon",
                                              "cost": 5,
                                              "image_path":"Decepticon-Flamewar.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Megatron",
                                              "sub_name":"Living Weapon",
                                              "bot_traits": ["Leader","Ranged"],

                                              "bot_attack": 7,
                                              "bot_health": 14,
                                              "bot_defense": 2,
                                              "bot_text": "This can be upgraded with a weapon in his armor and/or Utility slots.",

                                              "vehicle_attack": 5,
                                    
                                              "vehicle_traits": ["Leader","Tank","Ranged"],
                                              "vehicle_text": "When you flip to this mode <arrow> Return a weapon from your scrap pile to your hand.)",

                                              "loyalty":"Decepticon",
                                              "cost": 13,
                                              "image_path":"Decepticon-Megatron.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Nemesis Prime",
                                              "sub_name":"Dark Clone",
                                              "bot_traits": ["Melee"],

                                              "bot_attack": 7,
                                              "bot_health": 16,
                                              "bot_defense": 2,
                                              "bot_text": "When you reshuffle your scrap pile into your deck <arrow> put the bottom card of your deck face down under this. This has 3<attack> for each card under him.",

                                              "vehicle_attack": 6,
                                    
                                              "vehicle_traits": ["Truck","Melee"],
                                              "vehicle_text": "When you flip to this mode <arrow> Your opponent chooses one of their characters and does 2 damage to it.",

                                              "loyalty":"Decepticon",
                                              "cost": 12,
                                              "image_path":"Decepticon-Nemesis_Prime.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Decepticon Shockwave",
                                              "sub_name":"Cybertron Commander",
                                              "bot_traits": ["Leader","Specialist"],

                                              "bot_attack": 4,
                                              "bot_health": 11,
                                              "bot_defense": 3,
                                              "bot_text": "When a card is scrapped from your opponents hand <arrow> Your opponent chooses one of their characters and does 1 damage to it",

                                              "vehicle_attack": 6,
                                    
                                              "vehicle_traits": ["Leader","Spaceship","Specialist"],
                                              "vehicle_text": "When you flip to this mode <arrow> Each player draws 2 cards.",

                                              "loyalty":"Decepticon",
                                              "cost": 11,
                                              "image_path":"Decepticon-Shockwave.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Starscream",
                                              "sub_name":"Air Commander",
                                              "bot_traits": ["Leader","Ranged"],

                                              "bot_attack": 4,
                                              "bot_health": 13,
                                              "bot_defense": 2,
                                              "bot_text": "Bold 2 (Flip 2 more battle cards when attacking.)",

                                              "vehicle_attack": 3,
                                              "vehicle_defense": 1,
                                    
                                              "vehicle_traits": ["Leader","Plane","Ranged"],
                                              "vehicle_text": "When you flip to this mode <arrow> Do damage to an enemy equal to the number ",

                                              "loyalty":"Decepticon",
                                              "cost": 11,
                                              "image_path":"Decepticon-StarScream1.gif"
                                              }))
    
    Transformer_Data.append(Transformer_Card({"name":"Starscream",
                                              "sub_name":"Scheming Second-In-Command",
                                              "bot_traits": ["Leader","Ranged"],

                                              "bot_attack": 5,
                                              "bot_health": 14,
                                              "bot_defense": 1,
                                              "bot_text": "Tough 1 (Flip 1 more battle card when defending.)",

                                              "vehicle_traits": ["Leader","Plane","Ranged"],
                                              "vehicle_text": "Bold 1 (Flip 1 more battle card when attacking.)",

                                              "loyalty":"Decepticon",
                                              "cost": 10,
                                              "image_path":"Decepticon-StarScream2.gif"
                                              }))
    #Decepticon Card List End

    #Return Card List
    return Transformer_Data

#Place List of Battle Card Test Data Here
def Assemble_Battle_List():
    '''The Purpose Of This Function Is To Provide A List of Battle Cards For The TransformersTCG_Deck_Builder.py File.'''
    Battle_Data = []

    #Upgrade Cards
    Battle_Data.append(Battle_Card({"name": "Armored Plating",
                        "icon": "<blue>",
                        "type": "Upgrade",
                        "subtype": "Armor",
                        "b_defense": 1,
                        "image_path": "Armored-Plating.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Backup Beam",
                        "icon": "<blue><green>",
                        "type": "Upgrade",
                        "subtype": "Weapon",
                        "text": "Bold 2(Flip 2 more battle cards when attacking)",
                        "image_path": "Backup-Beam.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Enforcement Batons",
                        "icon": "<orange><green>",
                        "type": "Upgrade",
                        "subtype": "Weapon",
                        "text": "When you put this on a character <arrow> Scrap an enemy Weapon.",
                        "b_attack": 1,
                        "image_path": "Enforcement-Batons.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Grenade Launcher",
                        "icon": "<orange>",
                        "type": "Upgrade",
                        "subtype": "Weapon",
                        "text": "After the upgraded character attacks <arrow> Scrap this card.",
                        "b_attack": 4,
                        "image_path": "Grenade-Launcher.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Handheld Blaster",
                        "icon": "<blue><blue>",
                        "type": "Upgrade",
                        "subtype": "Weapon",
                        "text": "Bold 1 (Flip 1 more battle card when attacking)",
                        "image_path": "Handheld-Blaster.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Improvised Shield",
                        "icon": "<orange><orange>",
                        "type": "Upgrade",
                        "subtype": "Armor",
                        "text": "Tough 1 (Flip 1 more battle card when defending)",
                        "image_path": "Improvised-Shield.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Primary Laser",
                        "icon": "<orange><orange>",
                        "type": "Upgrade",
                        "subtype": "Weapon",
                        "b_attack": 2,
                        "image_path": "Primary-Laser.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Security Console",
                        "icon": "<white>",
                        "type": "Upgrade",
                        "subtype": "Utility",
                        "text": "When the upgraded character defends <arrow> Draw a card. Then Plan 1. (You may put 1 card from your hand on top of your deck.)",
                        "image_path": "Security-Console.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Sparring Gear",
                        "icon": "<orange><green>",
                        "type": "Upgrade",
                        "subtype": "Armor",
                        "text": "Tough 2 (Flip 2 more battle cards when defending.)",
                        "image_path": "Sparring-Gear.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Stealthiness",
                        "icon": "<orange>",
                        "type": "Upgrade",
                        "subtype": "Utility",
                        "text": "Stealth (Enemies attack other characters if able)",
                        "image_path": "Stealthiness.gif"
                        }))
    
    #Action Cards
    Battle_Data.append(Battle_Card({"name": "Equipment Enthusiast",
                        "icon": "<white>",
                        "type": "Action",
                        "text": "Draw a card for each of your upgrades.",
                        "image_path": "Equipment-Enthusiast.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Inferno Breath",
                        "icon": "<blue>",
                        "type": "Action",
                        "text": "Tap one of your untapped characters that has 5<cost> or more <arrow> Do 3 damage to an enemy",
                        "image_path": "Inferno-Breath.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Leap of Faith",
                        "icon": "<white>",
                        "type": "Action",
                        "text": "Scrap the top card of your deck. You may play that card. Then scrap another card from the top of your deck. You may play that card (Your team and deck can have 25<cost> total)",
                        "cost": 1,
                        "image_path": "Leap-Of-Faith.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "New Designs",
                        "icon": "<orange>",
                        "type": "Action",
                        "text": "You may play an Upgrade",
                        "image_path": "New-Designs.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Pep Talk",
                        "icon": "<blue>",
                        "type": "Action",
                        "text": "Draw 2 cards",
                        "image_path": "Pep-Talk.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Reckless Charge",
                        "icon": "<orange>",
                        "type": "Action",
                        "text": "One of your characters gets +4<attack> until end of turn. At end of turn, do 3 damage to it.",
                        "image_path": "Reckless-Charge.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Rest and Relaxation",
                        "icon": "<green>",
                        "type": "Action",
                        "text": "Repair 1 damage from one of your characters. (After each battle <arrow> You may swap 1 card from your hand with one of your flipped <green> cards)",
                        "image_path": "Rest-And-Relaxation.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Strafing Run",
                        "type": "Action",
                        "text": "Do 1 damage to each enemy",
                        "image_path": "Strafing-Run.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Supercharge",
                        "icon": "<orange>",
                        "type": "Action",
                        "text": "One of your characters gets Bold 3 until end of turn. (Flip 3 more battle cards when atacking.)",
                        "image_path": "SuperCharge.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Surprise Attack",
                        "icon": "<white>",
                        "type": "Action",
                        "text": "One of your characters gets Pierce 3 until end of turn. (Do at least 3 damage when attacking, but not more than <attack> total. Pierce numbers add together)",
                        "image_path": "Surprise-Attack.gif"
                        }))
    
    Battle_Data.append(Battle_Card({"name": "Vaporize",
                        "icon": "<blue>",
                        "type": "Action",
                        "text": "Scrap an enemy Upgrade",
                        "image_path": "Vaporize.gif"
                        }))
    
    return Battle_Data