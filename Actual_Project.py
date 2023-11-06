from designer import *
from dataclasses import dataclass


@dataclass
class World:
    egg: DesignerObject
    egg_speedx: int
    egg_speedy: int


def create_world() -> World:
    "Creating World"
    return World(create_egg(), 0, 0)


def create_egg() -> DesignerObject:
    "Create the Egg"
    egg = emoji("egg")
    egg.y = get_height() * (1 / 2)
    return egg


def move_egg(world: World):
    "Regular movement of the egg"
    world.egg.x += world.egg_speedx
    world.egg.y += world.egg_speedy


def head_left(world: World):
    world.egg_speedx = -5
    world.egg_speedy = 0


def head_right(world: World):
    world.egg_speedx = 5
    world.egg_speedy = 0


def head_up(world: World):
    world.egg_speedx = 0
    world.egg_speedy = -5


def head_down(world: World):
    world.egg_speedx = 0
    world.egg_speedy = 5


def egg_direction(world: World, key: str):
    if key == "right":
        head_right(world)
    if key == "left":
        head_left(world)
    if key == "up":
        head_up(world)
    if key == "down":
        head_down(world)


def egg_wall(world: World):
    "to make egg bounce off wall"
    if world.egg.x > get_width():
        head_left(world)
    if world.egg.x < 0:
        head_right(world)
    if world.egg.y < 0:
        head_down(world)
    if world.egg.y > get_height():
        head_up(world)


when("starting", create_world)
when("updating", move_egg)
when("updating", egg_wall)
when("typing", egg_direction)
start()


