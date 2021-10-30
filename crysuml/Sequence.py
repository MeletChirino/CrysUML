'''Sequence diagram library'''
from .functions import link

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

        reponse(
            starts=starting_actor[Actor],
            ends=endind_actor[Actor],
            message="message string"[string],
            categorie="Logical Categorie"[string]
            )

        activate(actor=activated_actor[Actor])

        deactivate(actor=activated_actor[Actor])

        loop(condition="loop condition"[string])
        alt(condition="if condition"[string])
        elsif(condition="new condition"[string])
        opt(condition="optional condition")

        end():

        ref(ref_sequence=sequence_diagram[Sequence], over=[actor1, actor2, ...][Actor]):

        divider():
        """
        self.name = kwargs['name']
        self.file_name = F"docs/diagrams/{self.name}_sequence.txt"
        if kwargs.get('links'): self.links = kwargs['links']
        self.actors = kwargs['actors']
        self.sequence = kwargs['sequence_list']

    def create(self):
        '''This method has no arguments, it creates the sequence diagram'''
        #print("Creating Sequance diagram")
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
    """This function writes in text file the sequence of the diagram in plantuml format"""
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
    elif message_type == 'opt':
        final_string = F"opt {message['condition']}"
    elif message_type == 'else':
        final_string = F"else {message['condition']}"
    elif message_type == 'end':
        final_string = F"end"
    elif message_type == 'divider':
        final_string = F"==== {message['title']} ===="
    elif message_type == 'ref':
        final_string = F"ref over "
        final_string += F"{message['over'][0].name}"
        for actor in message['over'][1:]:
            final_string += F", {actor.name}"
        final_string += F"\n{message['ref_sequence'].name}"
    return F"{final_string}\n"

