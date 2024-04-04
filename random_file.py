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
        
    def connect(self, person2):
        if person2 not in self.connections:
            self.connections.add(person2)
            person2.connect(self)
            
    def store_name(self,name):
        self.store = list()
        self.store.append(name)
        
    def display_connections(self):
        if self.connection_names:
            print(f"Connections of {self.name}:")
            for name in self.connection_names:
                print(name)
        else:
            print(f"{self.name} has no connections yet.")
        
        