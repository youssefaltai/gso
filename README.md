# Global State Observer

GSO is an open-source Python library for managing state. It provides simple interfaces that UI elements can easily
implement to sync with application state.

GSO is based on the [Observer pattern](https://refactoring.guru/design-patterns/observer), it is inspired
by [Redux.js](https://redux.js.org/).

GSO was originally designed to facilitate the synchronization between application state and GUIs built
with [PySide](https://en.wikipedia.org/wiki/PySide)/[PyQt](https://en.wikipedia.org/wiki/PyQt), but it should work with
any GUI library since it is very abstract.

⚠ **Please note that GSO is currently under development and is far from usable.**

## How to use

UI elements should implement the `Observer` interface, and override the `notify(action)` method, to update their UI state based on the `action`.

Application state should be encapsulated in a class called `State`. 
It should hold all observable pieces of data and have a single
method: `dispatch(action)`.

The `dispatch(action)` method on the `State` class should be called from the UI elements as a result of a user interaction.

An `Action` is an object that describes a UI event that is fired with the intent of changing application state.

An observable piece of data is any value in the application state that UI elements depend on.

Any piece of observable data should implement the `Observable` interface, and have any number of methods for updating
their values, by updating the protected member of the `Observable`
interface: `_value`.

Every update method on an observable piece of data should call the protected method of the `Observable`
interface: `notify(action)`, to notify all the attached observers with the update, and call their `notify(action)` methods.