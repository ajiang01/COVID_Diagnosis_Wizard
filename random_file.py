class Person:
    """ A person in the social network
    
        Attributes:
        name(str): the person's name
        connections (set of Person): other people in the social network who
        knows this person
    """
    def __init__(self, name):
        "Initializes a new Person object."
        self.name = name
        self.connections = set()    