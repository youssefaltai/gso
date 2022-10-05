# Actions
An `Action` is an object that has a `name` describing its intent (what it is trying to change in application state), and a `payload` that has all the information needed by the application state to make this change.

# Observables
An `Observable` is a piece of data that your applications UI depends on. It is encapsulated with a list of `Observer`s that should be notified with any changes in the `Observable`s `value`.

# Observers
An `Observer` is any object that should update its state to sync with an `Observable`s state. It is usually a UI component but it can be any type of object, even an `Observable` if needed.
