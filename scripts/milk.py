import sys
import cowsay

if __name__ == "__main__":
    msg = F''
    for word in sys.argv[2:]:
        msg += F'{word} '

    command = f'cowsay.{sys.argv[1]}("{msg}")'
    exec(command)
