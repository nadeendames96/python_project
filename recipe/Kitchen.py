from recipe import Recipe



class Kitchen:
    
    recipe=Recipe("Cake",2)
    my_recipes=[]
    def __init__(self,ingredient,instruction):
      self.ingredient=ingredient
      self.instruction=instruction
      pass
    def info_recipe(self,ingredient,instruction):
        self.recipe.add_ingredient(ingredient)
        self.recipe.add_instructions(instruction)
        self.my_recipes.append(self.recipe)
#kitchen=Kitchen("ingredient","instruction")
#kitchen.info_recipe()self.recipe.print_ingredients()
#    recipe.print_ingredients()
    #recipe.print_instructions()
