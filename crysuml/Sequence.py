from .functions import *

class Sequence():
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.file_name = F"diagrams/{self.name}_sequence.txt"
        self.links = kwargs['links']
        self.actors = kwargs['actors']
        self.sequence = kwargs['sequence_list']

    def create(self):
        print("Creating Sequance diagram")
        create_uml_file(self.file_name)
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
    return F"{final_string}\n"

