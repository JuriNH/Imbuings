from dataclasses import dataclass
import imbu_items


@dataclass
class Item:
    name: str
    cost: int


@dataclass
class Imbu:
    name: str
    recipes: list


@dataclass
class Ingredient:
    quantity: int
    item: Item


crit = Imbu(name="crit",
            recipes=[
                [Ingredient(quantity=20, item=imbu_items.protective_charm),
                 Ingredient(quantity=25, item=imbu_items.sabretooth),
                 Ingredient(quantity=5, item=imbu_items.vexclaw_talon)],

                [Ingredient(quantity=2, item=imbu_items.token),
                 Ingredient(quantity=25, item=imbu_items.sabretooth),
                 Ingredient(quantity=5, item=imbu_items.vexclaw_talon)],

                [Ingredient(quantity=4, item=imbu_items.token),
                 Ingredient(quantity=5, item=imbu_items.vexclaw_talon)],

                [Ingredient(quantity=6, item=imbu_items.token)],
            ])

vamp = Imbu(name="vamp",
            recipes=[
                [Ingredient(quantity=25, item=imbu_items.vampire_teeth),
                 Ingredient(quantity=15, item=imbu_items.bloody_pincers),
                 Ingredient(quantity=5, item=imbu_items.piece_of_dead_brain)],

                [Ingredient(quantity=2, item=imbu_items.token),
                 Ingredient(quantity=15, item=imbu_items.bloody_pincers),
                 Ingredient(quantity=5, item=imbu_items.piece_of_dead_brain)],

                [Ingredient(quantity=4, item=imbu_items.token),
                 Ingredient(quantity=5, item=imbu_items.piece_of_dead_brain)],

                [Ingredient(quantity=6, item=imbu_items.token)],
            ])

void = Imbu(name="void",
            recipes=[
                [Ingredient(quantity=25, item=imbu_items.rope_belt),
                 Ingredient(quantity=25, item=imbu_items.silencer_claw),
                 Ingredient(quantity=5, item=imbu_items.grimleach_wing)],

                [Ingredient(quantity=2, item=imbu_items.token),
                 Ingredient(quantity=25, item=imbu_items.silencer_claw),
                 Ingredient(quantity=5, item=imbu_items.grimleach_wing)],

                [Ingredient(quantity=4, item=imbu_items.token),
                 Ingredient(quantity=5, item=imbu_items.grimleach_wing)],

                [Ingredient(quantity=6, item=imbu_items.token)],
            ])

ice_protection = Imbu(name='ice',
                      recipes=[Ingredient(quantity=25, item=imbu_items.winter_wolf_fur),
                               Ingredient(quantity=15, item=imbu_items.thick_fur),
                               Ingredient(quantity=15, item=imbu_items.deepling_warts)])

mlvl = Imbu(name='magic_level',
            recipes=[Ingredient(quantity=25, item=imbu_items.elvish_talisman),
                     Ingredient(quantity=15, item=imbu_items.broken_shamanic_staff),
                     Ingredient(quantity=15, item=imbu_items.medusa_hair)])
