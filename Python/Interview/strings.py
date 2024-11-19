class MString:
    def __init__(self, value):
        self.value = value

    def isEquivalent(self, other_string):
        return self.value == other_string.value

# Example usage:
str1 = MString("Hello")
str2 = MString("Hello")
str3 = MString("World")
str4 = MString("hell")

print(str1.isEquivalent(str2))  # Output: True
print(str1.isEquivalent(str3))
print(str1.isEquivalent(str4))