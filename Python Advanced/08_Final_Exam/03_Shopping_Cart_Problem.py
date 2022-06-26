def shopping_cart(*args, **kwargs):
    linesep = "\n"
    meals_limit_dict = {
        "Soup": 3,
        "Pizza": 4,
        "Dessert": 2
    }
    meals_dict = {
        "Soup": [],
        "Pizza": [],
        "Dessert": []
    }

    for products in args:
        if products == "Stop":
            break
        meal, product = products
        if product not in meals_dict[meal] and len(meals_dict[meal]) < meals_limit_dict[meal]:
            meals_dict[meal].append(product)

    sorted_meals = dict(sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0])))

    # Sort products alphabetically and turn them to line separated strings
    for meal, products in sorted_meals.items():
        sorted_meals[meal] = linesep.join([f" - {product}" for product in sorted(products)])

    # result = linesep.join([f"{meal}:{linesep}{products}" for meal, products in sorted_meals.items()])
    result = ""
    for meal, products in sorted_meals.items():
        result += f"{meal}:{linesep}"
        if products:
            result += f"{products}{linesep}"

    if not any([v for v in meals_dict.values()]):
        return "No products in the cart!"
    return result.strip()


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print("----------------------")
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print("----------------------")
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
print("----------------------")
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Pizza', 'ham'),
    ('Pizza', 'ham'),
    ('Pizza', 'ham'),
    ('Pizza', 'ham'),
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))



