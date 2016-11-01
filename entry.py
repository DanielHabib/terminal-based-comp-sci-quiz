class Entry:
    def __init__(self, **kwargs):
        self.__dict__.update({x:y for x, y in kwargs.items() if x != 'self'})
        self.userAnswer = 0
        self.grade = 0
