import sys

from ui import MainUI


def main():
    main_ui = MainUI("Parity Colors")

    def process(cmd):
        if cmd == "click":
            main_ui.container.number.click()
        elif cmd == "exit":
            sys.exit()
        else:
            raise Exception("Unknown command")

    while True:
        print(main_ui)
        process(input("> "))


if __name__ == '__main__':
    main()
