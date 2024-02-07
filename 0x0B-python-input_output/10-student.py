class Student:
    """ A student blueprint """
    def __init__(self, first_name, last_name, age):
        """initialiser for student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self, attrs = None):
            """Returns a json representation of the object"""
            if attrs is type(list):

            return class_to_json(self)
