import sys
import pygame
import plantuml
from os import system, getcwd, path
from time import sleep
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

global file_path, file_modified
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        global file_path, file_modified
        if event.src_path == F"{file_path}":
            file_modified = True

class Vizio:
    def __init__(self, img):
        self.screen_size = (600, 600)
        self.screen = pygame.display.set_mode((1,1))

        pygame.display.set_caption("CrysUML render")
        self.running = True
        self.img = img


    def show(self):
        draw_uml(self.img)
        background_image = pygame.image.load(F"{self.img}.png").convert()
        size = background_image.get_size()
        self.screen = pygame.display.set_mode(
                size
                )
        self.screen.blit(background_image, [0, 0])
        pygame.display.update()

    def finish_render(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

def draw_uml(file_name):
    try:
        diagram = plantuml.PlantUML(
                url='http://www.plantuml.com/plantuml/img/',
                )
        diagram.processes_file(F"{file_name}.iuml")
    except Exception as e:
        print(F"Error in plantuml:{e}\nTrying offline")
        res = system(F"plantuml {file_name}.iuml")
        #if not res == 0: raise Exception('Plantuml Syntax Error')

def create_file(file_name):
    f = open(file_name, 'w')
    f.write("@startuml\n@enduml")
    f.close()

if __name__ == "__main__":
    global file_path, file_modified
    file_modified = True
    file_name = sys.argv[1]
    file_path = F"{getcwd()}/{file_name}.iuml"
    if not path.isfile(file_path):
        create_file(file_path)

    render = Vizio(file_name)
    # watchdog 
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=f'{getcwd()}', recursive=True)
    observer.start()
    while(render.running):
        render.finish_render()
        if file_modified:
            file_modified = False
            render.show()
        #sleep(3)
    observer.stop()
    observer.join()

