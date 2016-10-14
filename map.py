class Room:
    def __init__(self, *args, **kwargs):
        self.exits = {}
        self.items = []

# sector building floor roomname

IGY_hq_4_briefing2 = Room()
IGY_hq_4_briefing2.exits = {"Hallway" : "IGY_hq_4_hallway"}

IGY_hq_4_hallway = Room()
IGY_hq_4_hallway.exits = {"Briefing Room 2" : "IGY_hq_4_briefing"}
