import pandas as pd
from imbu_dataclass import (
    void, crit, vamp, mlvl, ice_protection
)
from imbu_items import making


def sort_imbu(imbu_recipe):
    the_cheapest = sorted(imbu_recipe, key=calculate_the_cost)[0]
    return the_cheapest


def calculate_the_cost(recipe):
    cost = 0
    for ingredient in recipe:
        cost += ingredient.item.cost * ingredient.quantity

    return cost


def cost_per_hour(all_imbu_cost, final_imbu_amount):
    cost_per_hour = total_cost(all_imbu_cost, final_imbu_amount) / 20
    return int(cost_per_hour)


def total_cost(all_imbu_cost, final_imbu_amount):
    total = final_imbu_amount * making.cost + all_imbu_cost
    return total


def total_items(needed_items, size):
    needed_items_array = []
    items_dict = {}

    while len(needed_items) > size:
        piece = needed_items[:size]
        needed_items_array.append(piece)
        needed_items = needed_items[size:]
    needed_items_array.append(needed_items)

    for value, name in needed_items_array:
        items_dict[name] = items_dict.get(name, 0) + value

    return items_dict


def show_items(the_cheapest):
    needed_items = ()

    for ingredient in the_cheapest:
        needed_items += ingredient.quantity, ingredient.item.name

    return needed_items


def without_price(imbu):
    for recipes in imbu:
        for ingredient in recipes:
            if ingredient.item.cost is None:
                ingredient.item.cost = int(input(f'{ingredient.item.name} price: '))


def without_token(imbu, all_imbu_cost, needed_items, ):
    all_imbu_cost += calculate_the_cost(imbu.recipes)
    needed_items += show_items(imbu.recipes)

    return all_imbu_cost, needed_items


def with_token(imbu, all_imbu_cost, needed_items):
    without_price(imbu.recipes)
    the_cheapest_imbu = sort_imbu(imbu.recipes)
    all_imbu_cost += calculate_the_cost(the_cheapest_imbu)
    needed_items += show_items(the_cheapest_imbu)

    return all_imbu_cost, needed_items


def start():
    all_imbu_cost = 0
    needed_items = ()
    imbu_with_tokens = {"mana": void, "crit": crit, 'vamp': vamp}
    imbu_without_tokens = {"mlvl": mlvl, "ice protection": ice_protection}

    imbu_amount = int(input('How much imbu do you want to make?:'))

    final_imbu_amount = imbu_amount

    while imbu_amount > 0:
        imbu_amount -= 1

        imbu = input('What kind of imbu do you want to do: crit/ice protection/mana/mlvl/vamp: ')

        if imbu in imbu_with_tokens:
            all_imbu_cost, needed_items = with_token(imbu_with_tokens[imbu], all_imbu_cost, needed_items)

        elif imbu in imbu_without_tokens:
            all_imbu_cost, needed_items = without_token(imbu_without_tokens[imbu], all_imbu_cost, needed_items)

        else:
            print("There is no such imbu")
            imbu_amount += 1

    total_needed_items = total_items(needed_items, 2)

    return all_imbu_cost, final_imbu_amount, total_needed_items


def main():
    all_imbu_cost, final_imbu_amount, total_needed_items = start()

    print("Total cost of imbu: ", total_cost(all_imbu_cost, final_imbu_amount))

    print("Cost per hour: ", cost_per_hour(all_imbu_cost, final_imbu_amount))

    print("Needed items:\n",
          pd.DataFrame(total_needed_items, index=["amount"]).T.sort_index().reset_index().rename({'index': 'item'},
                                                                                                 axis=1))


if __name__ == '__main__':
    main()
