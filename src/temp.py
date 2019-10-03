class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to= None
        self.e_to = None
        self.w_to = None
#temp file for testing         
class Plyer:
     def __init__(self, name, starting_room):
         self.name = name
         self.current_room = starting_room
         
         
room = {
        'outside':  Room("outside Cave Entrace",
                         "North of you, the cave mount backons"),
        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),
        
        'overlook': Room("Grand Overlook",  """A steep cliff appers before youm falls into the darkness. Ahed to the north, a light flickers in 
                         the distance, but there is no way across the chasm."""),
        
        'narrow' : Room ("Narrow Passage", """The narrow passage bens here form the west to north. The smell of gold permeates the air."""),
        
        'treasure' : Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by
                          earlier adventures. The only exit is to the south."""),
                          
        }         



rooom['outside'].n_to = room['foyer']
rooom['foyer'].s_to = room['outside']
rooom['foyer'].n_to = room['overlook']
rooom['foyer'].n_to = room['narrow']
rooom['overlook'].n_to = room['foyer']
rooom['narrow'].n_to = room['foyer']
rooom['narrow'].n_to = room['treasure']
rooom['treasure'].n_to = room['narrow']

player = Player ("Pablo", room['outside'])

while True:
    #pritn the current room title and description
    
    current_room = player.current_room
    print(player.current_room.title)
    print(player.current_room.decription)
    #wait for user input
    cmd = input("-> ")
    #Parse user inputs (n, s ,w, e,q)
    
    if cmd == "n" and:
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
        else:
            print("You cannot go that way")
            
            elif cmd == "s" and:
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
        else:
            print("You cannot go that way")
            
             elif cmd == "e" and:
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
        else:
            print("You cannot go that way")
            
             elif cmd == "w" and:
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
        else:
            print("You cannot go that way")
        
    elif cmd == "q":
        
        print("goodbye")
        
        break
    else print("I did not recognized that commend")
    
    

