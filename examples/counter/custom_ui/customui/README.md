## Custom UI

This is a dummy library included for demonstration purposes only.

You will find a folder named `ui` that contains a folder named `base`. The `base` folder contains the abstract UI classes and interfaces that the examples in custom UI use.

For simplicity, Custom UI is CLI-based, and it has only one abstract class `View` that every visible UI element will implement.

Every subclass of `View` should implement its single abstract method `show()` that describes how the UI element will be displayed in the terminal.
