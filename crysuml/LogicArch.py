'''Logic Architecture'''
from crysuml.functions import *
def get_categorie_list(sequences_list):
    '''This function search for categories in messages of sequence diagrams and saves them.'''
    categorie_list = ["default",]
    for instance in sequences_list:
        for message_dict in instance.sequence:
            if message_dict.get('categorie'):
                new_cat = message_dict['categorie']
                if not(new_cat in categorie_list):
                    categorie_list.append(new_cat)
    return categorie_list

def get_messages_list(sequences_list):
    '''This function gets all messages of a sequences diagrams list'''
    categorie_list = get_categorie_list(sequences_list)
    final_list = []
    temp_list = []
    for categorie in categorie_list:
        for instance in sequences_list:
            for message_dict in instance.sequence:
                if message_dict.get('categorie'):
                    if message_dict['categorie'] == categorie:
                        if message_dict.get('message'):
                            temp_list.append(message_dict['message'])
                        elif message_dict.get('reponse'):
                            temp_list.append(message_dict['message'])
                elif message_dict.get('message') or message_dict.get('reponse'):
                    if categorie == "default":
                        if message_dict.get('message'):
                            temp_list.append(message_dict['message'])
                        elif message_dict.get('reponse'):
                            temp_list.append(message_dict['message'])
        temp_dict = {"categorie": categorie, "messages": temp_list}
        final_list.append(temp_dict)
        temp_list = []
        temp_dict = {}
    return final_list

def logic_architecture_diagram(sequences_list):
    '''This function creates the logic architecture diagram based on sequence diagrams'''
    messages_list = get_messages_list(sequences_list)
    file_name = F"docs/diagrams/logic_architecture.iuml"
    create_uml_file(file_name)
    #print(messages_list)
    for element in messages_list:
        #print(element)
        write_file(
                file_name = file_name,
                string = F"""
class {element['categorie']} {{\n
                    """
                )
        for message in element['messages']:
           write_file(
               file_name = file_name,
               string = f"{message}\n"
               )
        write_file(file_name=file_name, string=f"}}\n")
        if not element['categorie'] == 'default':
            write_file(
                    file_name = file_name,
                    string=f"{element['categorie']} -- default\n"
                    )
    end_file(file_name)
    draw_plantuml(file_name)
