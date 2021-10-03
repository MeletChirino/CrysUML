'''General functions for crysuml'''
import gc
import plantuml

def create_md(**kwargs):
    ''' This function writes a mark down file
    kwargs:
        - name
        - description
        - instance_list
        - footer
    '''
    file_name = F"docs/{kwargs['name']}.md"
    f = open(file_name, 'w')
    f.write(F"{kwargs['name']} markdown File!\n")

    if kwargs.get('description'):
        f.write(F"\n{kwargs['description']}\n\n")
    for instance in kwargs['instance_list']:
        try:
            if instance.get("verbose_name"):
                f.write(F'\n- {instance["verbose_name"]}')
            else:
                f.write(F'\n- {instance["name"]}')
            if not(instance['description'] == ""):
                f.write(F': {instance["description"]}')
        except:
            #print("Instance list were a dict list")
            pass

        try:
            if hasattr(instance, "verbose_name"):
                f.write(F'\n- {instance.verbose_name}')
            else:
                f.write(F'\n- {instance.name}')

            if not(instance.description == ""):
                f.write(F': {instance.description}')
        except:
            #print("Instance list were a instance list")
            pass

    if kwargs.get('diagram_name'):
        diagram_file = class_diagram(
                kwargs['instance_list'],
                name = kwargs['diagram_name']
                )
        f.write(F"\n\n![alt text]({diagram_file})\n")


    if kwargs.get('footer'):
        f.write(F"\n\n{kwargs['footer']}")

    f.close()

def draw_plantuml(file_name):
    try:
        diagram = plantuml.PlantUML(
                url='http://www.plantuml.com/plantuml/img/',
                )
        diagram.processes_file(file_name)
        return diagram
    except Exception as e:
        print(e)

def get_list(class_name):
    trash = gc.get_objects()
    class_list = []
    for obj in trash:
        if isinstance(obj, class_name):
            class_list.append(obj)

    return class_list

def link_type(string):
    switcher = {
            "simple": ["--", ""],
            "include": [".>", ": include"],
            "extends": ["<.", ": extends"],
            }
    return switcher[string]

def check_kwargs(string, kwargs, **default):
    if string in kwargs and kwargs[string]:
        return kwargs[string]
    elif 'default' in default and default['default']:
        return default['default']
    else:
        return ""

#functions for writing files
def create_uml_file(file_name):
    f = open(file_name, 'w')
    f.write("@startuml\n")
    f.close()

def write_file(**kwargs):
    f = open(kwargs['file_name'], 'a')
    f.write(kwargs['string'])
    f.close()

def end_file(file_name):
    f = open(file_name, 'a')
    f.write("\n@enduml")
    f.close()

#functions for exigence file
def class_diagram(dict_list, **kwargs):
    name = kwargs['name']
    file_name = F"docs/diagrams/{kwargs['name']}_class.txt"

    #write clases
    create_uml_file(file_name)
    for element in dict_list:
        write_file(
                file_name = file_name,
                string = F"""
                    class {element['name']} {{
                    .. name ..
                    {element['verbose_name']}
                    .. description ..
                    {element['description']}
                    }}\n
                    """
                )
    # now we write the links
    for element in dict_list:
        if element.get("links"):
            for link in element['links']:
                write_file(
                        file_name = file_name,
                        string = F'{element["name"]} {link_element(link, "exigence")}\n'
                        )
    end_file(file_name)
    draw_plantuml(file_name)
    return F"diagrams/{kwargs['name']}_class.png"


def link_element(link, kw):
    if link['type'] == 'simple':
        return F"-- {link[kw]}"
    elif link['type'] == 'extension':
        return F"--|> {link[kw]}"
    elif link['type'] == 'composition':
        return F"*-- {link[kw]}"
    elif link['type'] == 'agregation':
        return F"--o {link[kw]}"


#functions for linking and write properties to diagrams and objects
def link(**kwargs):
    return kwargs

def message(**kwargs):
    kwargs['type'] = 'message'
    return kwargs

def reponse(**kwargs):
    kwargs['type'] = 'reponse'
    return kwargs

def activate(**kwargs):
    kwargs['type'] = 'activate'
    return kwargs

def deactivate(**kwargs):
    kwargs['type'] = 'deactivate'
    return kwargs

def loop(**kwargs):
    kwargs['type'] = 'loop'
    return kwargs

def alt(**kwargs):
    kwargs['type'] = 'alt'
    return kwargs

def end(**kwargs):
    kwargs['type'] = 'end'
    return kwargs

def ref(**kwargs):
    kwargs['type'] = 'ref'
    return kwargs

def divider(**kwargs):
    kwargs['type'] = 'divider'
    return kwargs
