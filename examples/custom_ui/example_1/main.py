import sys

from ui.MainView import MainView


def main():
    main_ui = MainView()

    def process(command):
        match command:
            case "click":
                main_ui.container_view.number_button_view.click()
            case "exit":
                sys.exit()
            case other:
                raise Exception(f"Unknown command: {other}")

    while True:
        main_ui.show()
        process(command=input("> "))


if __name__ == '__main__':
    main()
