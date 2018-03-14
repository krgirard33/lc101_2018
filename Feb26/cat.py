class Cat:
    ''' Cat class for demonstrating my cat class, and my cat style. '''

    def __init__(self, name, color, weight, voice):
        ''' Create a new point at the origin '''
        self.name = name
        self.color = color
        self.weight = weight
        self.voice = voice
    
    def name_print(self):
        '''Print the name of the cat.'''
        print("They call me %s." % self.name)
    
    def make_sound(self):
        print(self.name, 'goes "'+str(self.voice)+'"')
        
    def cat_weighs(self):
        print(self.name, 'weighs', self.weight)
    
    def cat_colors(self):
        print(self.name, 'is', self.color)
        
    def cat_description(self):
        print(self.name,'is', self.color.lower(), ", weighs", self.weight, "lbs, and sounds like", self.voice)
        
        

mrpaws = Cat("Mr. Paws","Black with white paws", 4.7, "Meow!")
sally = Cat("Sally","Long white hair", 3.0, "mew")
'''
mrpaws.name = "Mr. Paws"
mrpaws.color = "Black with white paws"
mrpaws.weight = 4.7
mrpaws.voice = "Meow!"
mrpaws.Cat("Mr. Paws","Black with white paws", 4.7, "Meow!")
'''
mrpaws.name_print()
sally.make_sound()
mrpaws.cat_description()

class Older_Cat(Cat):
    '''A Cat aged over 8 years with name, color, weight, voice, and illness components.'''

    def __init__(self, name, color, weight, voice, illness):
        '''A new Older_Cat with a name (string), color (string) and weight (float).'''

        Cat.__init__(self, name, temperament, weight)
        self.illness = illness

    def has_illness(self):
        '''Describes if the Older_Cat has any health conditions.'''
        if self.illness != "none":
            print "%s has %s. Please consult care plan." \
            % (self.name, self.illness)
        else:
            print "%s has no health conditions." % self.name

rosebud = Older_Cat("Rosebud", "Thin gray and brown hair", 4, "arthritis")
print(rosebud)