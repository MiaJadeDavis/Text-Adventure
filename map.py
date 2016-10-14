class Room:
    def __init__(self, description):
        self.description = ""
        self.exits = {}
        self.items = []
        self.people = {}

# sector building floor roomname

rooms = {
    "NAME" : {
        "name" : "KNOWNNAME",
        "unknown name" : "UNKNOWNNAME",
        "description" : "DESCRIPTION",
        "exits" : {}
        }

    "GYR_housingblocko_1_room6" : {
        "name" : "Room 6",
        "unknown name" : "Room 6",
        "description" : "DESCRIPTION",
        "exits" : {}
        }
    
    "IGY_hq_4_briefing2" : {
        "name" : "Briefing Room 2",
        "unknown name" : "",
        "description" : ""
        },
    
    "IGY_hq_4_hallway" : {}
    }

"""IGY_hq_4_briefing2 = Room()
IGY_hq_4_briefing2.exits = {"Hallway" : "IGY_hq_4_hallway"}

IGY_hq_4_hallway = Room()
IGY_hq_4_hallway.exits = {"Briefing Room 2" : "IGY_hq_4_briefing"}"""
