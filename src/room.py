# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def__init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to= None
        self.e_to = None
        self.w_to = None
        
 class Plyer:
     def__init__(selfm name, starting_room):
         self.name = name
         self.current_room = starting_room