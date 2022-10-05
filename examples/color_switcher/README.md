# Example 1 (Color switcher)

In this example, the application state consists of only one user-defined observable type of data: `Number`,

and the UI generally consists of three parts:

* A colored view on the left.
* A colored view on the right.
* A button in the middle.

colored views will change their color based on the `Number`.

The left colored view will turn red if the `Number` is even, and blue if it is odd.
The right colored view will do the exact opposite.

The button in the middle is used to increment the `Number` in the application state. The text displayed on the button
should update to show the current value of the `Number`.

### Using

* [Custom UI](./custom_ui)
* [PySide6](./pyside6)
