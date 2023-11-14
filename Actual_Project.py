from designer import *
from dataclasses import dataclass

OBSTACLE1_SPEED = 3
OBSTACLE2_SPEED = 5

@dataclass
class Obstacle:
    obstacle_itself: DesignerObject
    obstacle_speed: int
@dataclass
class World:
    egg: DesignerObject
    egg_speedx: int
    egg_speedy: int
    game_time: DesignerObject
    game_time_value: int
    level_title: DesignerObject
    frame_timer: int
    obstacle1_list: [Obstacle]
    obstacle2_list: [Obstacle]

def create_world() -> World:
    "Creating World"
    return World(create_egg(),
                 0,
                 0,
                 text("black", "Time: ", 24, get_width() / 2, 20),
                 0,
                 text("black", "", 24, 50 , 20),
                 0,
                 [],
                 []
                 )

def create_egg() -> DesignerObject:
    "Create the Egg"
    egg = emoji("egg")
    egg.y = get_height() * (1 / 2)
    return egg


def create_timer(world: World):
    "Creating the timer"
    world.game_time.text = "Timer: " + str(world.game_time_value)


def increase_timer(world: World):
    "Increase an in-game timer that increases over time"
    world.frame_timer += 1
    if world.frame_timer % 30 == 0:
        world.game_time_value += 1


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


"////////////////////////////Obstacle 1////////////////////////////////"


def create_obstacles1(world: World):
    "Obstacle from frame_time 0 - 900"
    if world.frame_timer == 1:
        microbe = emoji("microbe")
        obstacle1_1 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_1.obstacle_itself.x = 0
        obstacle1_1.obstacle_itself.y = get_height() / 5
        world.obstacle1_list.append(obstacle1_1)
    if world.frame_timer == 300:
        microbe = emoji("microbe")
        obstacle1_2 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_2.obstacle_itself.x = 0
        obstacle1_2.obstacle_itself.y = (get_height() * 2) / 5
        world.obstacle1_list.append(obstacle1_2)
    if world.frame_timer == 600:
        microbe = emoji("microbe")
        obstacle1_3 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_3.obstacle_itself.x = 0
        obstacle1_3.obstacle_itself.y = (get_height() * 3) / 5
        world.obstacle1_list.append(obstacle1_3)
    if world.frame_timer == 900:
        microbe = emoji("microbe")
        obstacle1_4 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_4.obstacle_itself.x = 0
        obstacle1_4.obstacle_itself.y = (get_height() * 4) / 5
        world.obstacle1_list.append(obstacle1_4)

def level_one_title(world: World):
    if world.game_time_value == 1:
        world.level_title.text = "Level 1"

def obstacle1_movement(world: World):
    "to move the obstacles"
    for obstacle in world.obstacle1_list:
        obstacle.obstacle_itself.x += obstacle.obstacle_speed

def obstacle1_wall(world: World):
    "to make obstacles bounce off wall"
    for obstacle in world.obstacle1_list:
        if obstacle.obstacle_itself.x > get_width():
            obstacle.obstacle_speed = -OBSTACLE1_SPEED
        if obstacle.obstacle_itself.x < 0:
            obstacle.obstacle_speed = OBSTACLE1_SPEED

#///////////////////end of obstacle 1/////////////////////////////

#///////////////////obstacle 2///////////////////////////////////
def level_two_title (world: World):
    "creating title for level 2"
    if world.game_time_value == 60:
        world.level_title.text = "Level 2"

def create_obstacles2(world: World):
    "creating obstacles for level 2"
    if world.frame_timer == 1830:
        frisbee = emoji("🥏")
        obstacle2_1 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_1.obstacle_itself.x = get_width() / 5
        obstacle2_1.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_1)
    if world.frame_timer == 1980:
        frisbee = emoji("🥏")
        obstacle2_2 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_2.obstacle_itself.x = (get_width() * 2) / 5
        obstacle2_2.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_2)
    if world.game_time_value == 2130:
        frisbee = emoji("🥏")
        obstacle2_3 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_3.obstacle_itself.x = (get_width() * 3) / 5
        obstacle2_3.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_3)
    if world.game_time_value == 2280:
        frisbee = emoji("🥏")
        obstacle2_4 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_4.obstacle_itself.x = (get_width() * 4) / 5
        obstacle2_4.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_4)

def obstacle2_movement(world: World):
    "moving the obstacles"
    for obstacle in world.obstacle2_list:
        obstacle.obstacle_itself.y += obstacle.obstacle_speed
def obstacle2_wall(world: World):
    "bouncing obstacles off wall"
    for obstacle in world.obstacle2_list:
        if obstacle.obstacle_itself.y > get_height():
            obstacle.obstacle_speed = -OBSTACLE2_SPEED
        if obstacle.obstacle_itself.y < 0:
            obstacle.obstacle_speed = OBSTACLE2_SPEED
#//////////////////end of obstacle 2////////////////////////////


def egg_hits_obstacle(world: World) -> bool:
    "determines whether one loses the game"
    has_collision_happened = False
    for obstacle in world.obstacle1_list:
        if obstacle.obstacle_itself.x < (world.egg.x + 20) and obstacle.obstacle_itself.x > (world.egg.x - 20):
            if obstacle.obstacle_itself.y < (world.egg.y + 20) and obstacle.obstacle_itself.y > (world.egg.y - 20):
                has_collision_happened = True
    for obstacle in world.obstacle2_list:
        if obstacle.obstacle_itself.x < (world.egg.x + 20) and obstacle.obstacle_itself.x > (world.egg.x - 20):
            if obstacle.obstacle_itself.y < (world.egg.y + 20) and obstacle.obstacle_itself.y > (world.egg.y - 20):
                has_collision_happened = True
    return has_collision_happened


def game_over(world: World):
    "shows game over message"
    world.game_time.text = "Game Over! Score: " + str(world.game_time_value)


when("starting", create_world)
when("updating", move_egg)
when("updating", egg_wall)
when("updating", create_timer)
when("updating", increase_timer)
when("updating", create_obstacles1)
when("updating", obstacle1_movement)
when("updating", obstacle1_wall)
when("updating", level_one_title)
when("updating", level_two_title)
when("updating", create_obstacles2)
when("updating", obstacle2_movement)
when("updating", obstacle2_wall)
when("typing", egg_direction)
when(egg_hits_obstacle, game_over, pause)
start()

