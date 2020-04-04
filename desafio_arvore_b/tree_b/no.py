class Node:
    def __init__(self, value, right=None, left=None, my_page=None):
        self.value = value
        self.right = right
        self.left = left
        self.my_page = my_page

    def __eq__(self, other):
        if type(other) == Node:
            return self.value == other.value
        return self.value == other

    def __lt__(self, other):
        if type(other) == Node:
            return self.value < other.value
        return self.value < other

    def __gt__(self, other):
        if type(other) == Node:
            return self.value > other.value
        return self.value > other

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.__str__()
