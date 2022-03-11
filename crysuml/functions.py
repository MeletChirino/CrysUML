'''General functions for crysuml'''
import gc
import plantuml
from .matrix import matrix
from os import system, path, makedirs, getcwd

def create_md(**kwargs):
    ''' This function writes a mark down file
    kwargs:
        - name
        - description
        - instance_list
        - footer
    '''
    folder_name = F"{getcwd()}/docs"
    file_name = F"{folder_name}/{kwargs['name']}.md"
    if not path.exists(folder_name): makedirs(folder_name)
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
                f.write(F': {instance["description"].lstrip()}')
        except:
            #print("Instance list were a dict list")
            pass

        try:
            if hasattr(instance, "verbose_name"):
                f.write(F'\n- {instance.verbose_name}')
            else:
                f.write(F'\n- {instance.name}')

            if not(instance.description == ""):
                f.write(F': {instance.description.lstrip()}')
        except:
            pass
    if(kwargs.get('matrix')):
        table = matrix(
                kwargs['matrix'][0],
                kwargs['matrix'][1],
                kwargs['matrix'][2],
                kwargs['matrix'][3],
                )
        i = 0
        f.write("\n\n| |")
        for row in kwargs['matrix'][1]:
            f.write(F" {row['verbose_name']} |");
        f.write("\n| --- |")
        for row in kwargs['matrix'][1]:
            f.write(F" --- |");
        f.write("\n")
        for column in kwargs['matrix'][0]:
            try:
                f.write(F"| {column.name} |")
            except:
                f.write(F"| {column['verbose_name']} |")
            j = 0
            for row in kwargs['matrix'][1]:
                if(table[i, j] == 1):
                    f.write(" X |")
                else:
                    f.write(" |")
                j += 1
            i += 1
            f.write("\n")


    if kwargs.get('diagram_name'):
        diagram_file = class_diagram(
                kwargs['instance_list'],
                name = kwargs['diagram_name'],
                type = kwargs['name'],
                )
        f.write(F"\n\n![alt text]({diagram_file})\n")


    if kwargs.get('footer'):
        f.write(F"\n\n{kwargs['footer']}")

    f.close()

def draw_plantuml(file_name):
    '''This function writes a uml diagram if there is a file written in plantuml format
    :params string file_name: file's path
    '''
    try:
        diagram = plantuml.PlantUML(
                url='http://www.plantuml.com/plantuml/img/',
                )
        diagram.processes_file(file_name)
        return diagram
    except Exception as e:
        print(F"Looks like a pantuml Error:\n{e}\nIf you didn't get it you can try to compile the file in plantuml web compiler")
        print("Trying offline")
        res = system(F"plantuml {file_name}")
        if not res == 0:
            # aqui intento compilar la imagen offline pero puede que tenga errores
            raise ValueError(F'{res} Plantuml error ')
        else:
            print("You can see your error on the pic")

def get_list(class_name):
    '''This function gets a list of all instances of a single class.'''
    trash = gc.get_objects()
    class_list = []
    for obj in trash:
        if isinstance(obj, class_name):
            class_list.append(obj)

    return class_list

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
    '''This function creates a class diagram of a list of dictionaries'''
    name = kwargs['name']
    file_name = F"docs/diagrams/{kwargs['name']}_class.iuml"

    #write clases
    create_uml_file(file_name)
    write_file(
            file_name = file_name,
            string = F"""
            title {name}
            scale 1024 width
            scale 768 height
            \n
                """
            )
    for element in dict_list:
        write_file(
                file_name = file_name,
                string = F"""
                    class {element['name']} {element['color']}{{
                    .. name ..
                    {element['verbose_name']}
                    .. description ..
                    {element['description']}
                    }}\n
                    """
                )
    # now we write the links
    if kwargs['type'] == "Exigences":
        for element in dict_list:
            if element.get("links"):
                for link in element['links']:
                    if link.get('exigence'):
                        write_file(
                                file_name = file_name,
                                string = F'{element["name"]} {link_element(link, "exigence")}\n'
                                )
    elif kwargs['type'] == 'Specifications':
        for element in dict_list:
            if element.get("links"):
                for link in element['links']:
                    if link.get('spec'):
                        write_file(
                                file_name = file_name,
                                string = F'{element["name"]} {link_element(link, "spec")}\n'
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
