"""Super should be used only in cases where you have a diamond shaped
inheritance case, like this:"""

class Avi:
    def __init__(self):
        print('Avi')

class Tali(Avi):
    def __init__(self):
        print('Tali')
        Avi.__init__(self)

class Shai(Avi):
    def __init__(self):
        print('Shai')
        Avi.__init__(self)

class Moshe(Shai, Tali):
    def __init__(self):
        print('Moshe')
        Tali.__init__(self)
        Shai.__init__(self)

moshe = Moshe()

"""The python solution is:"""

class Avi:

    def __init__(self):

        print('Avi')

class Tali(Avi):

    def __init__(self):

        print('Tali')
        super().__init__()

class Shai(Avi):

    def __init__(self):

        print('Shai')
        super().__init__()

class Moshe(Shai, Tali):

    def __init__(self):

        print('Moshe')
        super().__init__()

moshe = Moshe()