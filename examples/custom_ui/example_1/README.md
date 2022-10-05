# Example 1 (Color switcher)

In this example, the application state consists of only one observable type of data: `Number`

The UI consists of three parts:
* A `ColoredView` on the left.
* A `ColoredView` on the right.
* A `ButtonView` in the middle.

`ColoredView`s will change their color based on the `Number`.


The left `ColoredView` will turn red if the `Number` is even, and blue if it is odd.
The right `ColoredView` will do the exact opposite.

The `ButtonView` in the middle is used to increment the `Number` in the application state. The text displayed on the button should update to show the current value of the `Number`.

## `main.py`
The example's entry point. Run this file to test the example.

Contains:
* [`main()`](#def-main)

### `def main() -> None`
Called when the application is executed.

Contains:
* [`process()`](#def-processcommand-str---none)
* [Main loop](#main-loop)

### `def process(command: str) -> None`
Helper function for processing user input.

#### `command: str`
User command that they input via the command line.

Possible values:
* click
* exit

### Main loop
Goes as follows:
1. Wait for user commands,
2. process them,
3. update state and UI,
4. rerender the UI.