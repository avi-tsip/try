class MyClass:
    """Can modify object instances state
       Can modify class state"""
    def method(self):
        return 'instance method called', self


    """CAN'T modify object instances state
       Can modify class state"""
    @classmethod
    def classmethod(cls):
        return 'class method called', cls

    """CAN'T modify object instances state
       CAN'T modify class state"""
    @staticmethod
    def staticmethod():
        return 'static method called'