## [`MainView.py`](./MainView.py)

Contains the [`MainView`](#class-mainviewview) class.

### `class MainView(View)`

The applications main UI component, it is the outermost container.

**Fields:**

#### `self.container_view: ContainerView`

Container for the `ColoredView`s and the `ButtonView`

## [`ContainerView.py`](./ContainerView.py)

Contains the [`ContainerView`](#class-containerviewview) class.

### `class ContainerView(View)`

Container for the left and right `ColoredView`s and the number `ButtonView`.

**Fields:**

#### `self.left_view: ColoredView`

A view that changes its color based on the application states `Number`.
Turns red when the `Number` is even, blue otherwise.

#### `self.number_button_view: ButtonView`

A button used to increment the application states `Number`. It displays the `Number`s current value as the buttons text.

#### `self.right_view: ColoredView`

A view that changes its color based on the application states `Number`.
Turns blue when the `Number` is even, red otherwise.


## [`ColoredView.py`](./ColoredView.py)

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