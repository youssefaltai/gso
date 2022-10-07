# GSO (Global State Observer)

GSO is an open-source Python library for managing application state.
It uses a modified version of the [Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) 
to sync UI state with application state.

GSO was originally designed to work with [PySide](https://wiki.qt.io/Qt_for_Python)/[PyQt](https://riverbankcomputing.com/software/pyqt/),
but it works well with pretty much every class-based UI library out there.

## How to use

You will find a lot of [examples](https://github.com/youssef-attai/gso/tree/main/examples)
that can help you get started.
The examples are very simple, they are all focused on 
the pattern you should follow when you use GSO.
You are encouraged to clone the ones that use the UI library you are working with
and have a closer look.

### Flow

In GSO, application state is encapsulated in 
user-defined observables. An observable is like
a wrapper around the actual state or variable, that
helps make application state and UI state synced together.

All an observable does is keep references to objects that are
interested in knowing when the wrapped state changes.

Observables provide one way to update encapsulated state, and
in this way, observers are notified after the update happens so
that they can update accordingly.

All UI components that depend on at least one variable in
application state should implement the `Observer` interface.
This variable of interest should be encapsulated in a class that
extends the `Observable` class. 

Then, The UI component should observe the observable it
depends on, using the `observe()` method on `Observer`
instances (or `attach_observer()` on `Observable` instances),
and implement the `notify_state_changed()` method to react
accordingly when the observable state changes.

If you are familiar with class diagrams, this might be useful: 

![GSO Class Diagram](./gso-class-diagram.svg)