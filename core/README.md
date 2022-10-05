# Actions
An action is an object that has a `name` describing its intent, and a `payload` that has all the information the applications state needs to update accordingly.

# Observables
An observable is a wrapper around any piece of data that your applications UI depends on. It keeps a list of `observers` that should be notified with any changes in the observables `value`.

# Observers
An observer is any object that should update its state to sync with an `Observable`s state. It is usually a UI component but it can be any type of object, even an `Observable` if needed.
