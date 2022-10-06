****
⚠️ **This documentation is outdated.**
****

## [`MainView.py`](MainView.py)

Contains the [`MainView`](#class-mainviewview) class.

### `class MainView(View)`

The applications main UI component, it is the outermost container.

**Fields:**

#### `self.container_view: ContainerView`

Container for the `ColoredView` and the `ButtonView`

## [`ContainerView.py`](ContainerView.py)

Contains the [`ContainerView`](#class-containerviewview) class.

### `class ContainerView(View)`

Container for the `ColoredView` and the number `ButtonView`.

**Fields:**

#### `self.colored: ColoredView`

A view that changes its color based on the application states `Number`.
Turns red when the `Number` is even, blue otherwise.

#### `self.number_button_view: ButtonView`

A button used to increment the application states `Number`. It displays the `Number`s current value as the buttons text.

## [`ColoredView.py`](ColoredView.py)

Contains the [`ColoredView`](#class-coloredviewview) class.

### `class ColoredView(View)`

A view that changes its color based on the application states `Number`.

**Fields:**

#### `self.parity: str`
Determines when the view should change its color to red with respect to the `Number`s parity.

**Possible values:**
* "even"
* "odd"

#### `self.color: str`
The views color.

## [`TextView.py`](TextView.py)
Contains the [`TextView`](#class-coloredviewview) class.

### `class TextView(View)`
A view that displays some text.

**Fields:**

#### `self.text: str`
The text displayed.

**Methods:**

#### `def update_text(self, new_text: str) -> None`
Updates the displayed text.

## [`ButtonView.py`](ButtonView.py)
Contains the [`ButtonView`](#class-buttonviewview) class.

### `class ButtonView(View, Observer)`
A button that displays some text and dispatches an `updateNumber` `Action` when clicked.

It implements the `Observer` interface since its UI state depends on the `Number`.

**Fields:**

#### `self.TextView: str`
The text displayed on the button.

#### `self.on_click_handlers: list[function]`
A list of handler functions that are executed when the button is clicked.

**Methods:**

#### `def add_on_click_listener(self, handler: function) -> None`
Adds a handler function that gets executed when the button is clicked.

#### `def click(self) -> None`
Clicks the button, calling all the `on_click_handlers`.

#### `def notify(action: Action)`
Updates the buttons UI state (the buttons text in this case) when the action is `updateNumber`.
