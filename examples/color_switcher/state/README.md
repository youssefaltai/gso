## [`state.py`](state.py)
Contains the central [`State`](#class-state) class.

### `class State`
Acts as a singleton object that holds and provides all application state (i.e. all observable pieces of data).

**Fields**
#### `number: Number`
The only observable piece of data in this example.

**Methods**
#### `def dispatch(action: Action) -> None`
Updates the application state based on the `action`.

## [`number.py`](number.py)
Contains the [`Number`](#class-numberobservable) observable class.

### `class Number(Observable)`
An observable integer.

**Methods**
#### `def update_number(new_number: int) -> None`
Updates the integers value and notifies all observers with this update.