from dog import Dog
from pet import Pet

# Separate instance of a dog class
aussie_mix = Dog("Australian Shepherd Mix")

# Passing the instance of a dog into Pet so it can be named
murph = Pet("Murphis", aussie_mix)

# Adding an owner to this pet
murph.set_owner("The Sheps", "555-555-1234")

print(murph)