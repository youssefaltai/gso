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

