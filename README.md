# GSO (Global State Observer)

GSO is an open-source Python library for managing application state.
It uses the 
[Observer pattern](https://en.wikipedia.org/wiki/Observer_pattern) 
to sync UI state with application state.

GSO was originally designed to work with 
[PySide](https://wiki.qt.io/Qt_for_Python)/
[PyQt](https://riverbankcomputing.com/software/pyqt/),
but it works well with pretty much every class-based UI library out there.

## How to use

You will find a lot of 
[examples](https://github.com/youssef-attai/gso/tree/main/examples)
that can help you get started.
The examples are very simple, they are focused on 
the pattern that works best with GSO.

You are encouraged to clone the ones that use the UI library you are working with
and have a closer look.

### Flow

In GSO, application state is encapsulated in observables.

An observable is like a wrapper around the actual state or variable.

All an observable brings to the table is that it keeps references to 
objects (usually UI components) that are interested in knowing when 
the wrapped state changes.

Observables force notification of observers when encapsulated state changes, 
so whenever application state changes, UI components can instantly update
accordingly.

All UI components that depend on at least one variable in
application state should implement the `Observer` interface,
and each of these variables should be encapsulated in
an `Observable`. 

That was the **O** in GSO, the _Observer pattern_.

You might be thinking, how do UI components reach
state? Well, that's where the **GS** comes to play.

The `GlobalState` class is used to group all application state variables
and make them globally available everywhere in your code, 
so that UI components can easily request state updates
and observe application state. It acts as a singleton, and stores
all the observables in a Python `dict`.

As you already know, an observable can have multiple observers,
and an observer can observe multiple observables.

In other words, one variable in application state
can have multiple UI components depending on it,
and one UI component can have it's state depend on multiple
variables in application state, which is why
the `notify_state_changed()` method on `Observer`s
accepts the parameter `action`.

If you are familiar with [Redux](https://redux.js.org/), you probably
 have an idea what actions are, they are pretty similar in GSO,
but they are **not** the same.

In both Redux and GSO, actions are objects that describe what kind of update 
should take place in application state.

In Redux, every action has a unique name, and a payload that
has all what is needed to make the corresponding update properly.

However, in GSO, actions are distinct objects that encapsulate
state update logic. They are used by `Observable`s in their `apply()`
method to update encapsulated state using the encapsulated logic.

**If you found any of this confusing or unclear, please refer to the examples.**

## How to install

Make sure you have `pip` installed, then open a terminal window, and type:
```
pip install gso
```
