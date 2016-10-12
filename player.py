import random

class Player():
    def __init__(self):
        self.name = ""
        self.clone_number = 1
        self.security_clearance = "R"

        self.service_group = None
        self.mutant_power = None
        self.secret_society = None

        self.attributes = {
            "strength" : None,
            "agility" : None,
            "dexterity" : None,
            "endurance" : None,
            "moxie" : None,
            "chutzpah" : None,
            "mechanical aptitude" : None,
            "power" : None
        }
        
        self.skills = {}
        
        self.skills["agility"] = {
                "force sword" : None,
                "grenade" : None,
                "neurowhip" : None,
                "primitive melee weapon" : None,
                "truncheon" : None,
                "unarmed" : None
            }
        
        self.skills["dexterity"] = {
                "energy weapons" : None,
                "field weapons" : None,
                "laser weapons" : None,
                "primitive missile weapon" : None,
                "projectile weapons" : None,
                "vehicle armed weapons" : None,
                "vehicle field weapons" : None,
                "vehicle launched weapons" : None
            }
        
        self.skills["chutzpah"] = {
                "bootlicking" : None,
                "bribery" : None,
                "con" : None,
                "fast talk" : None,
                "forgery" : None,
                "interrogation" : None,
                "intimidation" : None,
                "motivation" : None,
                "oratory" : None,
                "psychescan" : None,
                "spurious logic" : None
            }
        
        self.skills["moxie"] = {
                "biochemical therapy" : None,
                "biosciences" : None,
                "chemical engineering" : None,
                "data analysis" : None,
                "data search" : None,
                "demolition" : None,
                "electronic engineering" : None,
                "mechanical engineering" : None,
                "medical" : None,
                "nuclear engineering" : None,
                "security" : None,
                "stealth" : None,
                "surveillance" : None,
                "survival" : None
            }
        
        self.skills["mechanical"] = {
                "autocar operation and maintenance" : None,
                "copter operation and maintenance" : None,
                "crawler operation and maintenance" : None,
                "docbot operation and maintenance" : None,
                "flybot operation and maintenance" : None,
                "habitat engineering" : None,
                "hover operation and maintenance" : None,
                "jackobot operation and maintenance" : None,
                "scrubot operation and maintenance" : None,
                "transbot operation and maintenance" : None,
                "vulturecraft operation and maintenance" : None
            }
