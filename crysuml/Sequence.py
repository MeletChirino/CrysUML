from .functions import *

class Sequence():
    def __init__(self, **kwargs):
        """
        Those are options of sequence diagram
message(
    starts=starting_actor[Actor],
    ends=endind_actor[Actor],
    message="message string"[string],
    categorie="Logical Categorie"[string]
    )

def reponse(
    starts=starting_actor[Actor],
    ends=endind_actor[Actor],
    message="message string"[string],
    categorie="Logical Categorie"[string]
    )

def activate(actor=activated_actor[Actor])

def deactivate(actor=activated_actor[Actor])

def loop(condition="loop condition"[string])
def alt(condition="loop condition"[string])
def elsif(condition="loop condition"[string])

def end():

def ref(ref_sequence=sequence_diagram[Sequence], over=[actor1, actor2, ...][Actor]):

def divider():
        """
        self.name = kwargs['name']
        self.file_name = F"docs/diagrams/{self.name}_sequence.txt"
        self.links = kwargs['links']
        self.actors = kwargs['actors']
        self.sequence = kwargs['sequence_list']

    def create(self):
        print("Creating Sequance diagram")
        create_uml_file(self.file_name)
        for actor in self.actors:
            if(actor.type != "component"):
                write_file(
                        file_name = self.file_name,
                        string = F"{actor.type} {actor.name}\n",
                        )
        for etape in self.sequence:
            write_file(
                    file_name = self.file_name,
                    string = seq_to_string(etape)
                    )
        end_file(self.file_name)
        draw_plantuml(self.file_name)

def seq_to_string(message):
    message_type = message['type']
    if message_type == "message":
        final_string = F"{message['starts'].name} -> {message['ends'].name} : {message['message']}"
    elif message_type == 'reponse':
        final_string = F"{message['starts'].name} --> {message['ends'].name} : {message['message']}"
    elif message_type == 'activate':
        final_string = F"activate {message['actor'].name}"
    elif message_type == 'deactivate':
        final_string = F"deactivate {message['actor'].name}"
    elif message_type == 'loop':
        final_string = F"loop {message['condition']}"
    elif message_type == 'alt':
        final_string = F"alt {message['condition']}"
    elif message_type == 'else':
        final_string = F"else {message['condition']}"
    elif message_type == 'end':
        final_string = F"end"
    elif message_type == 'divider':
        final_string = F"==== {message['title']} ===="
    elif message_type == 'ref':
        final_string = F"ref :{message['ref_sequence']}"
    return F"{final_string}\n"

