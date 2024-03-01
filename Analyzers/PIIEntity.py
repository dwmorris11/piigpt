class PIIEntity:
    def __init__(self, text: str, category: str, subcategory: str, offset: int, length: int):
        self.text = text
        self.category = category
        self.subcategory = subcategory
        self.offset = offset
        self.length = length

    def __str__(self):
        return f"Text: {self.text}, Category: {self.category}, Subcategory: {self.subcategory}, Offset: {self.offset}, Length: {self.length}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.text == other.text and self.category == other.category and self.subcategory == other.subcategory and self.offset == other.offset and self.length == other.length

    def __hash__(self):
        return hash((self.text, self.category, self.subcategory, self.offset, self.length))

    def __lt__(self, other):
        return self.offset < other.offset

    def __le__(self, other):
        return self.offset <= other.offset

    def __gt__(self, other):
        return self.offset > other.offset

    def __ge__(self, other):
        return self.offset >= other.offset

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return self.offset + other.offset

    def __sub__(self, other):
        return self.offset - other.offset

    def __mul__(self, other):
        return self.offset * other.offset

    def __truediv__(self, other):
        return self.offset / other.offset

    def __floordiv__(self, other):
        return self.offset // other.offset

    def __mod__(self, other):
        return self.offset % other.offset

    def __divmod__(self, other):
        return divmod(self.offset, other.offset)

    def __pow__(self, other):
        return self.offset ** other.offset

    def __lshift__(self, other):
        return self.offset << other.offset

    def __rshift__(self, other):
        return self.offset >> other.offset

    def __and__(self, other):
        return self.offset & other.offset

    def __xor__(self, other):
        return self.offset ^ other.offset

    def __or__(self, other):
        return self.offset | other.offset