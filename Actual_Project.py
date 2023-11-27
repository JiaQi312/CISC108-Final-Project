import random
from designer import *
from dataclasses import dataclass

OBSTACLE1_SPEED = 3
OBSTACLE2_SPEED = 5
OBSTACLE3_SPEED = 1
OBSTACLE4_SPEED = 5
OBSTACLE6_SPEED = 0

@dataclass
class Obstacle:
    obstacle_itself: DesignerObject
    obstacle_speed: int

@dataclass
class Shield:
    shield_itself: DesignerObject
    bobbing_toggle: int
    shield_timer: int

@dataclass
class World:
    character: DesignerObject
    character_speed_x: int
    character_speed_y: int
    game_time: DesignerObject
    game_time_value: int
    level_title: DesignerObject
    frame_timer: int
    endless_mode: bool
    obstacle1_list: list[Obstacle]
    obstacle2_list: list[Obstacle]
    obstacle3_list: list[Obstacle]
    obstacle4_list: list[Obstacle]
    obstacle6_list: list[Obstacle]
    list_of_shields: list[Shield]
    shield_status: DesignerObject
    shield_amount: int

def create_world() -> World:
    """Creating World"""
    return World(create_character(choose_character()),
                 0,
                 0,
                 text("black", "Time: ", 24, get_width() / 2, 20),
                 0,
                 text("black", "", 24, 60, 20),
                 0,
                 enable_endless(),
                 [],
                 [],
                 [],
                 [],
                 [],
                 [],
                 text("black", "", 24, 70, 50),
                 0
                 )

def choose_character() -> str:
    """Now one can choose their character!"""
    valid_names = ["egg", "rocket", "rock", "cat", "dog", "winking"]
    valid_name = False
    choose_your_character = input("What do you want to play as?" "\n"
                                  "egg, rocket, rock, cat, dog, winking")
    if choose_your_character.strip().lower() in valid_names:
        valid_name = True
    while not valid_name:
        choose_your_character = input("Invalid character. Type in one of these" "\n"
                                      "egg, rocket, rock, cat, dog, winking")
        if choose_your_character.strip().lower() in valid_names:
            valid_name = True
    return choose_your_character.strip().lower()
def create_character(name: str) -> DesignerObject:
    """Create the Character"""
    character = emoji(name)
    character.y = get_height() * (1 / 2)
    print("all set, start dodging!")
    return character


def create_timer(world: World):
    """Creating the timer"""
    world.game_time.text = "Timer: " + str(world.game_time_value)


def increase_timer(world: World):
    """Increase an in-game timer that increases over time"""
    world.frame_timer += 1
    if world.frame_timer % 30 == 0:
        world.game_time_value += 1

def enable_endless() -> bool:
    toggle = input("Endless Mode?" "\n"
                   "yes / no")
    if toggle.lower().strip() == "yes":
        return True
    if toggle.lower().strip() == "no":
        return False
    else:
        return False



def move_character(world: World):
    """Regular movement of the character"""
    world.character.x += world.character_speed_x
    world.character.y += world.character_speed_y


def head_left(world: World):
    """character heads left"""
    world.character_speed_x = -5
    world.character_speed_y = 0


def head_right(world: World):
    """character heads right"""
    world.character_speed_x = 5
    world.character_speed_y = 0


def head_up(world: World):
    """character heads up"""
    world.character_speed_x = 0
    world.character_speed_y = -5


def head_down(world: World):
    """character heads down"""
    world.character_speed_x = 0
    world.character_speed_y = 5


def character_direction(world: World, key: str):
    """Determining which direction character moves"""
    if key == "right":
        head_right(world)
    if key == "left":
        head_left(world)
    if key == "up":
        head_up(world)
    if key == "down":
        head_down(world)


def character_wall(world: World):
    """to make character bounce off wall"""
    if world.character.x > get_width():
        head_left(world)
    if world.character.x < 0:
        head_right(world)
    if world.character.y < 0:
        head_down(world)
    if world.character.y > get_height():
        head_up(world)

# /////////////////////////shield powerup/////////////////////////////
def should_shield_spawn(world: World) -> bool:
    """deciding if the powerup should spawn"""
    should_shield_spawn = False
    if not world.frame_timer % 1350:
        should_shield_spawn = True
    return should_shield_spawn

def create_shield(world: World):
    """creating the shield powerup"""
    shield = emoji("shield")
    shield.x = random.randint(0, get_width())
    shield.y = random.randint(0, get_height())
    world.list_of_shields.append(Shield(shield, 0, 0))

def shield_bobbing(world: World):
    """allowing the shield to bob up and down in scale"""
    for shield in world.list_of_shields:
        if shield.bobbing_toggle == 0:
            shield.shield_itself.scale_x += -0.01
            shield.shield_itself.scale_y += -0.01
            shield.shield_timer += 1
            if shield.shield_timer == 30:
                shield.bobbing_toggle = 1
        if shield.bobbing_toggle == 1:
            shield.shield_itself.scale_x += 0.01
            shield.shield_itself.scale_y += 0.01
            shield.shield_timer += -1
            if shield.shield_timer == 0:
                shield.bobbing_toggle = 0
def update_shield_status(world: World):
    """updating current amount of shield available"""
    world.shield_status.text = "Shield: " + str(world.shield_amount) + "x"

def character_hits_shield(world: World) -> bool:
    """collision interaction between character and shield"""
    hits_shield = False
    for shield in world.list_of_shields:
        if (world.character.x + 20) > shield.shield_itself.x > (world.character.x - 20):
            if (world.character.y + 20) > shield.shield_itself.y > (world.character.y - 20):
                hits_shield = True
                destroy(shield.shield_itself)
                shield.bobbing_toggle = 2
                world.list_of_shields.remove(shield)
    return hits_shield

def character_gets_shield(world: World):
    """Giving character shield when the shield emoji is hit"""
    world.shield_amount += 20

# //////////////////////// end of shield powerup /////////////////////


# ////////////////////////////Obstacle 1////////////////////////////////


def create_obstacles1(world: World):
    """Obstacle from frame_time 0 - 900"""
    if world.frame_timer == 150:
        microbe = emoji("microbe")
        obstacle1_1 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_1.obstacle_itself.x = 0
        obstacle1_1.obstacle_itself.y = get_height() / 4
        world.obstacle1_list.append(obstacle1_1)
    if world.frame_timer == 300:
        microbe = emoji("microbe")
        obstacle1_2 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_2.obstacle_itself.x = 0
        obstacle1_2.obstacle_itself.y = (get_height() * 2) / 4
        world.obstacle1_list.append(obstacle1_2)
    if world.frame_timer == 450:
        microbe = emoji("microbe")
        obstacle1_3 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_3.obstacle_itself.x = 0
        obstacle1_3.obstacle_itself.y = (get_height() * 3) / 4
        world.obstacle1_list.append(obstacle1_3)


def level_one_title(world: World):
    """create level 1 title"""
    if world.game_time_value == 1:
        world.level_title.text = "Level 1"


def obstacle1_movement(world: World):
    """to move the obstacles"""
    for obstacle in world.obstacle1_list:
        obstacle.obstacle_itself.x += obstacle.obstacle_speed


def obstacle1_wall(world: World):
    """to make obstacles bounce off wall"""
    for obstacle in world.obstacle1_list:
        if obstacle.obstacle_itself.x > get_width():
            obstacle.obstacle_speed = -OBSTACLE1_SPEED
        if obstacle.obstacle_itself.x < 0:
            obstacle.obstacle_speed = OBSTACLE1_SPEED


# ///////////////////end of obstacle 1/////////////////////////////

# ///////////////////obstacle 2///////////////////////////////////
def level_two_title(world: World):
    """creating title for level 2"""
    if world.game_time_value == 30:
        world.level_title.text = "Level 2"


def create_obstacles2(world: World):
    """creating obstacles for level 2"""
    if world.frame_timer == 1050:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_1 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_1.obstacle_itself.x = get_width() / 5
        obstacle2_1.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_1)
    if world.frame_timer == 1200:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_2 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_2.obstacle_itself.x = (get_width() * 2) / 5
        obstacle2_2.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_2)
    if world.frame_timer == 1350:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_3 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_3.obstacle_itself.x = (get_width() * 3) / 5
        obstacle2_3.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_3)
    if world.frame_timer == 1500:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_4 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_4.obstacle_itself.x = (get_width() * 4) / 5
        obstacle2_4.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_4)


def obstacle2_movement(world: World):
    """moving the obstacles"""
    for obstacle in world.obstacle2_list:
        obstacle.obstacle_itself.y += obstacle.obstacle_speed


def obstacle2_wall(world: World):
    """bouncing obstacles off wall"""
    for obstacle in world.obstacle2_list:
        if obstacle.obstacle_itself.y > get_height():
            obstacle.obstacle_speed = -OBSTACLE2_SPEED
        if obstacle.obstacle_itself.y < 0:
            obstacle.obstacle_speed = OBSTACLE2_SPEED


# //////////////////end of obstacle 2////////////////////////////

# /////////////////start of obstacle 3///////////////////////////
def level_three_title(world: World):
    """creating title for level 3"""
    if world.game_time_value == 60:
        world.level_title.text = "Level 3"


def create_obstacle3(world: World):
    """creating obstacle for level 3"""
    if world.frame_timer == 1950:
        plane = emoji("airplane")
        plane.scale_y = 3
        plane.scale_x = 3
        obstacle3_1 = Obstacle(plane, OBSTACLE3_SPEED)
        obstacle3_1.obstacle_itself.x = 0
        obstacle3_1.obstacle_itself.y = 0
        world.obstacle3_list.append(obstacle3_1)


def obstacle3_movement(world: World):
    """movement for obstacle 3, want to make it home towards character"""
    for obstacle in world.obstacle3_list:
        if world.character.x > obstacle.obstacle_itself.x:
            if world.character.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.character.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
                obstacle.obstacle_itself.y += -obstacle.obstacle_speed
            else:
                obstacle.obstacle_itself.x += (obstacle.obstacle_speed * 1.5)
        elif world.character.x < obstacle.obstacle_itself.x:
            if world.character.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += -obstacle.obstacle_speed
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.character.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += -obstacle.obstacle_speed
                obstacle.obstacle_itself.y += -obstacle.obstacle_speed
            else:
                obstacle.obstacle_itself.x += -(obstacle.obstacle_speed * 1.5)
        else:
            if world.character.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y += (obstacle.obstacle_speed * 1.5)
            if world.character.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y += -(obstacle.obstacle_speed * 1.5)


# /////////////////end of obstacle 3////////////////////////////

# /////////////////obstacle 4//////////////////////////////////
def level_four_title(world: World):
    """creating title for level 4"""
    if world.game_time_value == 90:
        world.level_title.text = "Level 4"


def create_obstacle4(world: World):
    """creating obstacles for level 4"""
    if world.frame_timer == 2850:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_1 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_1.obstacle_itself.x = 20
        obstacle4_1.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_1)
    if world.frame_timer == 3000:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_2 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_2.obstacle_itself.x = 20
        obstacle4_2.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_2)
    if world.frame_timer == 3150:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_3 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_3.obstacle_itself.x = 20
        obstacle4_3.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_3)
    if world.frame_timer == 3300:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_4 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_4.obstacle_itself.x = 20
        obstacle4_4.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_4)
    if world.frame_timer == 3450:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_5 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_5.obstacle_itself.x = 20
        obstacle4_5.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_5)
    if world.frame_timer == 3600:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_6 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_6.obstacle_itself.x = 20
        obstacle4_6.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_6)
    if world.frame_timer == 3750:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_7 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_7.obstacle_itself.x = 20
        obstacle4_7.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_7)

def obstacle4_horz_movement(world: World):
    """defining horizontal movement for obstacle 4"""
    for obstacle in world.obstacle4_list:
        if obstacle.obstacle_itself.y == get_height() - 20:
            if obstacle.obstacle_itself.x == get_width() - 20:
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed
            obstacle.obstacle_itself.x += obstacle.obstacle_speed
        if obstacle.obstacle_itself.y == 20:
            if obstacle.obstacle_itself.x == 20:
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            obstacle.obstacle_itself.x -= obstacle.obstacle_speed


def obstacle4_vert_movement(world: World):
    """defining vertical movement for obstacle 4"""
    for obstacle in world.obstacle4_list:
        if obstacle.obstacle_itself.x == 20:
            if obstacle.obstacle_itself.y == get_height() - 20:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
            obstacle.obstacle_itself.y += obstacle.obstacle_speed
        if obstacle.obstacle_itself.x == get_width() - 20:
            if obstacle.obstacle_itself.y == 20:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
            obstacle.obstacle_itself.y -= obstacle.obstacle_speed


# /////////////////end of obstacle 4//////////////////////////

# ////////////////level 5/////////////////////////////////////
def level_five_title(world: World):
    """creating title for level 5"""
    if world.game_time_value == 140:
        world.level_title.text = "Level 5"


def level_five(world: World):
    """speeding obstacles up"""
    if world.frame_timer == 4200:
        for obstacle in world.obstacle1_list:
            obstacle.obstacle_speed += 2
        for obstacle in world.obstacle2_list:
            obstacle.obstacle_speed += 2
        for obstacle in world.obstacle3_list:
            obstacle.obstacle_speed += 0.5
        for obstacle in world.obstacle4_list:
            obstacle.obstacle_speed += 2


# ////////////////end of level 5/////////////////////////////

# ///////////////end screen/////////////////////////////////
def level_six_title(world: World):
    """creating title for level 6"""
    if world.frame_timer == 4500:
        if not world.endless_mode:
            world.level_title.text = "Level 6"
            world.game_time.text = "Reach Saturn!"


def create_obstacle6(world: World):
    """creating obstacle 6"""
    if world.frame_timer == 4500:
        if not world.endless_mode:
            saturn = emoji("🪐")
            saturn.scale_x = 5
            saturn.scale_y = 5
            obstacle6_1 = Obstacle(saturn, OBSTACLE6_SPEED)
            obstacle6_1.obstacle_itself.x = get_width() / 2
            obstacle6_1.obstacle_itself.y = get_height() / 2
            world.obstacle6_list.append(obstacle6_1)

def character_hits_saturn(world: World) -> bool:
    """determines whether one wins the game"""
    wins_game = False
    for obstacle in world.obstacle6_list:
        if (world.character.x + 50) > obstacle.obstacle_itself.x > (world.character.x - 50):
            if (world.character.y + 50) > obstacle.obstacle_itself.y > (world.character.y - 50):
                wins_game = True
    return wins_game


def win_screen(world: World):
    """Shows win screen"""
    world.game_time.text = "Congratulations! Your Score: " + str(world.game_time_value)

# ///////////////end of end screen/////////////////////////

def character_hits_obstacle(world: World) -> bool:
    """determines whether one loses the game"""
    is_game_over = False
    for obstacle in world.obstacle1_list:
        if (world.character.x + 20) > obstacle.obstacle_itself.x > (world.character.x - 20):
            if (world.character.y + 20) > obstacle.obstacle_itself.y > (world.character.y - 20):
                if world.shield_amount == 0:
                    is_game_over = True
                else:
                    world.shield_amount += -1
    for obstacle in world.obstacle2_list:
        if (world.character.x + 30) > obstacle.obstacle_itself.x > (world.character.x - 30):
            if (world.character.y + 30) > obstacle.obstacle_itself.y > (world.character.y - 30):
                if world.shield_amount == 0:
                    is_game_over = True
                else:
                    world.shield_amount += -1
    for obstacle in world.obstacle3_list:
        if (world.character.x + 50) > obstacle.obstacle_itself.x > (world.character.x - 50):
            if (world.character.y + 50) > obstacle.obstacle_itself.y > (world.character.y - 50):
                if world.shield_amount == 0:
                    is_game_over = True
                else:
                    world.shield_amount += -1
    for obstacle in world.obstacle4_list:
        if (world.character.x + 50) > obstacle.obstacle_itself.x > (world.character.x - 50):
            if (world.character.y + 50) > obstacle.obstacle_itself.y > (world.character.y - 50):
                if world.shield_amount == 0:
                    is_game_over = True
                else:
                    world.shield_amount += -1
    return is_game_over


def game_over(world: World):
    """shows game over message"""
    world.game_time.text = "Game Over! Score: " + str(world.game_time_value)

when("starting", create_world)
when("updating", move_character)
when("updating", character_wall)
when("updating", create_timer)
when("updating", increase_timer)
# level1
when("updating", create_obstacles1)
when("updating", obstacle1_movement)
when("updating", obstacle1_wall)
when("updating", level_one_title)
# level1
# level2
when("updating", level_two_title)
when("updating", create_obstacles2)
when("updating", obstacle2_movement)
when("updating", obstacle2_wall)
# level2
# level3
when("updating", level_three_title)
when("updating", create_obstacle3)
when("updating", obstacle3_movement)
# level3
# level4
when("updating", level_four_title)
when("updating", create_obstacle4)
when("updating", obstacle4_vert_movement)
when("updating", obstacle4_horz_movement)
# level4
# level5
when("updating", level_five_title)
when("updating", level_five)
# level5
# level6
when("updating", level_six_title)
when("updating", create_obstacle6)
# level6
# shield
when(should_shield_spawn, create_shield)
when("updating", shield_bobbing)
when("updating", update_shield_status)
when(character_hits_shield, character_gets_shield)
# shield
when("typing", character_direction)
when(character_hits_saturn, win_screen, pause)
when(character_hits_obstacle, game_over, pause)
start()
