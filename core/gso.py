def update(*actions):
    """
    Decorate all your observables' update methods with this decorator function.
    """

    def inner_update(func):
        def inner(observable, *args, **kwargs):
            func(observable, *args, **kwargs)
            observable._Observable__notify(*actions)

        return inner

    return inner_update
