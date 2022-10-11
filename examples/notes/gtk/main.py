from core.globalstate import GlobalState


def main():
    GlobalState.set("notes", NotesState())


if __name__ == '__main__':
    main()
