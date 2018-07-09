# Main Steps for this exercise
* Give a pet its own prop of name
* Give it a property of animal_type
* animal_type needs to be an instance of a dog
* Assign an owner via a method
* \_\_str\_\_ return a string with pet's name, # of legs, and what it says

# Requirements for the other Classes:
### dog.py:
Create a Dog class that:
* Inherits from Animal
* Has its own prop of "breed"
* 1 initializes the Animal class with'species', 'leg_num' and 'domesticated' attributes

### main.py:
* Instantiate a new Dog and print out the results of making it speak
Then...when you're done with making your Pet class
* Create an instance of the Pet class and compose the Dog instance into it by adding the dog as a property of the new Pet
* Add an owner by calling your pet's set_owner method (or whatever you called it)
* Print a human-readable output thanks to our the __str__ method you defined in Pet