#!/usr/bin/env python3
'''simple.py'''


class Singleton:
    _instance = None
    _initialised = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self.__class__._initialised:
            self._score = 0
            self.__class__._initialised = True

    def set_score(self, score):
        self._score = score

    def get_score(self):
        return self._score

    def incr_score(self, n):
        self._score += n

    def decr_score(self, n):
        self._score -= n
        if self._score < 0:
            self._score = 0


def main():
    a = Singleton()
    a.set_score(10)

    b = Singleton()
    b.incr_score(32)

    print(a is b)

    print(b.get_score())

    print(love())

    return 0


def love():
    return "I 💖 Python!"


if __name__ == "__main__":
    main()
