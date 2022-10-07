import sys

from core.globalstate import GlobalState
from examples.counter.state.counterstate import CounterState
from ui.MainUI import MainUI


def main():
    GlobalState.create(counter=CounterState())

    main_ui = MainUI()

    def process(command):
        match command:
            case "inc":
                main_ui.inc_button.click()
            case "dec":
                main_ui.dec_button.click()
            case "exit":
                sys.exit()
            case other:
                raise Exception(f"Unknown command: {other}")

    while True:
        main_ui.show()
        process(command=input("> "))


if __name__ == '__main__':
    main()
