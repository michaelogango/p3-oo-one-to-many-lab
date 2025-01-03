class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")

        self.name = name
        self.pet_type = pet_type
        self.owner = None

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of the Owner class.")
            self.owner = owner

        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of the owner's pets."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to the owner, ensuring the pet is a Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return a list of the owner's pets sorted by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)
