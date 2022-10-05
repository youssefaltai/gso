# Examples of using GSO with a custom UI

The examples here demonstrate how you would use GSO with a completely custom UI library.

## Custom UI

You will find a folder named `ui` that contains a folder named `base`. The `base` folder contains the abstract UI classes and interfaces that the examples use.

For simplicity, the custom UI is CLI-based, and it has only one class `View`, which is an abstract class that every visible UI element should implement.

Every subclass of `View` should implement its single abstract method `show()` that describes how the UI element will be displayed in the terminal.

### Examples
**More practical examples on how you would use GSO with a custom UI are yet to be added soon.**
1. [Color switcher](./example_1)
