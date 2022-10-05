# Example 1 (Color switcher)

In this example, the application state consists of only one observable type of data: `Number`,

and the UI consists of three parts:
* A `ColoredView` on the left.
* A `ColoredView` on the right.
* A `ButtonView` in the middle.

`ColoredView`s will change their color based on the `Number`.


The left `ColoredView` will turn red if the `Number` is even, and blue if it is odd.
The right `ColoredView` will do the exact opposite.

The `ButtonView` in the middle is used to increment the `Number` in the application state. The text displayed on the button should update to show the current value of the `Number`.

# Details

## [`ui/`](ui)
Module that has all UI elements used in the example.

## [`state/`](../state)
Module that has the central `State` class and all the application-specific observable types.

## [`main.py`](main.py)
The example's entry point. Run this file to test the example.

**Contains:**
* [`main()`](#def-main---none)

### `def main() -> None`
Called when the application is executed.

**Contains:**
* [`process()`](#def-processcommand-str---none)
* [Main loop](#main-loop)

### `def process(command: str) -> None`
Helper function for processing user input.

**Parameters:**

#### `command: str` 
User command that they input via the command line.

**Possible values:**
* "click"
* "exit"

### Main loop
Goes as follows:
1. Wait for the users command,
2. process it,
3. update state and UI,
4. rerender the UI.
