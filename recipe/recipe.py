# Recipe



class Recipe:

    def __init__(self):
        self.ingredients = ["2 avocados", "1 lime", "2 tsp salt"]
        self.instructions = ["chop avocados", "chop onion",
                "squeeze lime", "add salt", "mix well"]

        print("Welcome....!!!!")

        pass
    def print_ingredients(self):
        count=0
        for ingredient in self.ingredients:
            count+=1
            print(f"ingredient num {count} is {ingredient}")
        pass

    def print_instructions(self):
        count=0
        for instruction in self.instructions:
            count+=1
            print(f"instruction num {count} is {instruction}")
        pass

    def add_ingredient(self, ingredient):
        print("Successful Adding {ingredient}")
        pass
    def add_instructions(self, instructions):
        print("Successful Adding {instructions}")

        pass
recipe=Recipe()
print()    
recipe.print_ingredients()
print()
recipe.print_instructions()