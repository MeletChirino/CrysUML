""" main package from crysuml"""
class Actor():
    def __init__(self, type, name, note, *args, **kwargs):
        if type:
            self.type = "human"
        else:
            self.type = type
        self.name = name
        if note:
            self.note = ""
        else:
            self.note = note

    def __str__(self):
        return F"ACTOR = {self.name}"
class UseCase():
    def __init__(self, name, description, note, link, *args, **kwargs):
        self.name = name
        self.description = ""
        self.note = ""
        self.link = link
    def __str__(self):
        return F"USE CASE = {self.name}"

class UseCaseDiagram():
    def __init__(self, use_case, notes_on, *args, **kwargs):
        self.use_case = use_case
        if notes_on:
            self.notes_on = notes_on
        else:
            self.notes_on = False


    def create(self):
        #create use case diagram with plantuml
        print("Creating diagram")
        for case in self.use_case:
            for link in case.link:
                for key in link:
                    if not (key == "type"):
                        print(F"{case.name} --> {link[key]}")
        return case
