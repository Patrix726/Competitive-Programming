class Solution:
    def findAllRecipes(
        self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]
    ) -> list[str]:
        recipe_set = set(recipes)
        supply_set = set(supplies)

        roots = set()
        possible = set()
        for i, ingredient in enumerate(ingredients):
            ing_set = set(ingredient)
            diff = ing_set.difference(supply_set)
            if len(diff) == 0:
                roots.add(recipes[i])
            elif len(diff) == len(ing_set.intersection(recipe_set)):
                possible.add(i)
        output = [root for root in roots]
        while len(roots) > 0:
            cur = set()
            for i in possible:
                intersect = set(ingredients[i]).intersection(recipe_set)
                if roots.issuperset(intersect):
                    cur.add(i)
                    output.append(recipes[i])
            if len(cur)>0:
                roots.update(output)
                possible = possible.difference(cur)
            else:
                break
        return output
