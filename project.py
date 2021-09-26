from usecase import *
from exigences import *
from crysuml.matrix import matrix

def main():
    use_case_diagram.create()
    matrix(cases_list, exigences_list, 'exigence')
    return 0

main()
