import random


class Elephant:
    
    def __init__(self, fnc):
        
        self._fnc = fnc
        self._memory = []
        
    def __call__(self):
        
        retval = self._fnc()
        self._memory.append(retval)
        return retval
    
    def memory(self):
        
        return self._memory


@Elephant
def random_odd_digit():
    
    return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())
print(random_odd_digit.memory())
print(random_odd_digit())
print(random_odd_digit.memory())