from core.globalstate import GlobalState
from examples.counter.state.counterstate import CounterState
from ui.MainUI import MainUI


def main():
    GlobalState.set("counter", CounterState())

    main_ui = MainUI()
    main_ui.loop()


if __name__ == '__main__':
    main()
