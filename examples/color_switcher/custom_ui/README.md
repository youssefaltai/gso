## [`ui/`](ui)
Module that has all UI components used in the example.

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
