from menu import menu
from counter import Counter

def run():
    with Counter() as counter:
        menu(counter)

if __name__ == '__main__':
    run()