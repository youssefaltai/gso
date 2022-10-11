from examples.counter.action.update_number import UpdateNumber


class DecrementNumber(UpdateNumber):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount

    def __call__(self, num):
        super().__call__(num)
        return num - self.amount
