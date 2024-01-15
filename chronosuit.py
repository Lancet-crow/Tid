class Chronosuit:
    maximum_rate = 10  # максимальный ход времени
    minimum_rate = 0  # минимальный ход времени

    rate_change = 1  # изменение хода времени

    maximum_usages = 4  # максимальное кол-во использований

    counter_of_usages = 0  # кол-во изменений

    def __init__(self):
        self.current_rate = 1
        self.old_rate = 1

    # счетчик с проверкой(return None если количество использований максимально возможное)
    def dec_counter(func):
        def internal(cls, *args, **kwargs):
            if cls.counter_of_usages >= cls.maximum_usages:
                return None
            result = func(cls, *args, **kwargs)
            cls.increases_counter_renames()
            return result

        return internal


    @classmethod
    def increases_counter_renames(cls):
        cls.counter_of_usages += 1

    @dec_counter
    def stop_time(self):
        self.current_rate = 0

    @dec_counter
    def start_time(self):
        self.current_rate = self.old_rate

    @dec_counter
    def change_time(self, n):
        self.current_rate += Chronosuit.rate_change * n
        if self.current_rate < Chronosuit.minimum_rate:
            self.current_rate = Chronosuit.minimum_rate
        elif self.current_rate > Chronosuit.maximum_rate:
            self.current_rate = Chronosuit.maximum_rate
        self.old_rate = self.current_rate

    def take_rate(self):
        return self.current_rate

    def take_usages(self):
        return Chronosuit.counter_of_usages
