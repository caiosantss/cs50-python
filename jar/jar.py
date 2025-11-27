class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError()
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError()
        if self._size + n > self._capacity:
            raise ValueError()
        self._size += n

    def withdraw(self, n):
        if n < 0 or n > self._size:
            raise ValueError()
        self._size -= n

    #Getter capacity
    @property
    def capacity(self):
        print("Getting capacity...")
        return self._capacity

    #Getter size
    @property
    def size(self):
        print("Getting size...")
        return self._size


Cookie_Jar = Jar()
print(Cookie_Jar.capacity)
Cookie_Jar.deposit(5)
print(Cookie_Jar.size)
Cookie_Jar.withdraw(2)
print(Cookie_Jar.size)
print(Cookie_Jar)
