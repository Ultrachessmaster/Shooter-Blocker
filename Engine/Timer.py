class Timer:
    def __init__(self, secs, func):
        self._secs = secs
        self._func = func
    def UpdateAndIsDone(self, deltasecs):
        self._secs -= deltasecs
        if self._secs < 0:
            self._func()
            return True
        return False