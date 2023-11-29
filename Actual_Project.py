import random
from designer import *
from dataclasses import dataclass

OBSTACLE1_SPEED = 3
OBSTACLE2_SPEED = 5
OBSTACLE3_SPEED = 1
OBSTACLE4_SPEED = 5

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
    saturn_list: list[DesignerObject]
    list_of_shields: list[Shield]
    shield_status: DesignerObject
    shield_amount: int

def create_world() -> World:
    """
    Creates the world

    Args: None

    Return: The World dataclass, with values for each field, which will be
    updated throughout the game
    """
    return World(choose_character(),
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

def choose_character() -> DesignerObject:
    """
    Asks the player to input a word to play as. If the word is not valid, will ask the player
    to try again. If valid, will generate the character as the emoji of the word entered.

    Args: None

    Return (DesignerObject): The emoji which the player will play as
    """
    valid_name = False
    first_input = input("What do you want to play as?" "\n"
                        "Type in a word")
    try:
        emoji(first_input.lower().strip())
        final_input = first_input.lower().strip()
        valid_name = True
    except:
        valid_name = False
    while not valid_name:
        try:
            inputed_character = input("Invalid word" "\n"
                                      "Try another word")
            formatted_input = inputed_character.lower().strip()
            try_input = emoji(formatted_input)
            final_input = formatted_input
            valid_name = True
        except:
            valid_name = False

    created_character = emoji(final_input)
    return created_character

def create_timer(world: World):
    """
    Creates the timer

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function updates the game timer but does not return anything
    """
    world.game_time.text = "Timer: " + str(world.game_time_value)


def increase_timer(world: World):
    """
    Increase the in_game timer every second (or every 30 frames)

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function updates the frame timer and the game time, but does
        not return anything
    """
    world.frame_timer += 1
    if world.frame_timer % 30 == 0:
        world.game_time_value += 1

def enable_endless() -> bool:
    """
    The function asks the player whether they want to play on endless mode

    Args: None

    Return:
        bool: Whether or not endless mode should be enabled
    """
    toggle = input("Endless Mode?" "\n"
                   "yes / no")
    if toggle.lower().strip() == "yes":
        print("Endless mode enabled." "\n"
              "Start dodging!")
        return True
    else:
        print("Endless mode disabled." "\n"
              "Start dodging!")
        return False

def move_character(world: World):
    """
    Establishes continuous movement for the character

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but continuously moves the
        character in a certain direction
    """
    world.character.x += world.character_speed_x
    world.character.y += world.character_speed_y


def head_left(world: World):
    """
    Allows character to move left

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the character speed
        so that they can only move to the left
    """
    world.character_speed_x = -5
    world.character_speed_y = 0


def head_right(world: World):
    """
    Allows character to move right

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the character speed
        so that they can only move to the right
    """
    world.character_speed_x = 5
    world.character_speed_y = 0


def head_up(world: World):
    """
    Allows character to move upwards

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the character speed
        so that they can only move upwards
    """
    world.character_speed_x = 0
    world.character_speed_y = -5


def head_down(world: World):
    """
    Allows character to move downwards

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the character speed
        so that they can only move downwards
    """
    world.character_speed_x = 0
    world.character_speed_y = 5


def character_direction(world: World, key: str):
    """
    Combines the earlier direction functions in order to bind it to a key input

    Args:
        world (World): The world dataclass created during the start of the game
        key (str): The name of the key being pressed (determines direction)

    Return:
        None: The function does not return anything, but decides which direction the
        character moves based on which key is pressed.
    """
    if key == "right":
        head_right(world)
    if key == "left":
        head_left(world)
    if key == "up":
        head_up(world)
    if key == "down":
        head_down(world)


def character_wall(world: World):
    """
    Establishes how character interacts with the wall (bounces off in opposite direction

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, instead decides which direction the
        character goes depending on which border was struck.
    """
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
    """
    Decides whether the shield powerup should spawn, set for every 40 seconds

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        bool: Whether a shield should spawn (by testing if it's been exactly
        40 seconds)
    """
    should_shield = False
    if not world.frame_timer % 1200:
        should_shield = True
    return should_shield

def create_shield(world: World):
    """
    Creates the actual shield powerup

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but creates the shield and adds
        it to a list of all shields currently in game.
    """
    shield = emoji("shield")
    shield.x = random.randint(0, get_width())
    shield.y = random.randint(0, get_height())
    world.list_of_shields.append(Shield(shield, 0, 0))

def shield_bobbing(world: World):
    """
    Makes it so that the shield bobs up and down

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but scales the shield up and
        down, creating the bobbing effect.
    """
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
    """
    Updates text stating how much shield the player still has

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but updates the shield_status
        field in the World instance every update to how much shield they have.
    """
    world.shield_status.text = "Shield: " + str(world.shield_amount) + "x"

def character_hits_shield(world: World) -> bool:
    """
    Determines whether the character has hit the shield

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        bool: whether or not the shield is within the range of coordinates established
        for the character. This boolean enables later functions.
    """
    hits_shield = False
    for shield in world.list_of_shields:
        if (world.character.x + 20) > shield.shield_itself.x > (world.character.x - 20):
            if (world.character.y + 20) > shield.shield_itself.y > (world.character.y - 20):
                hits_shield = True
                destroy(shield.shield_itself)
                world.list_of_shields.remove(shield)
    return hits_shield

def character_gets_shield(world: World):
    """
    Adds shield to the player's total

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but adds 20 shield to the field
        in "world" which describes how much shield the player has.
    """
    world.shield_amount += 20

# //////////////////////// end of shield powerup /////////////////////


# ////////////////////////////Obstacle 1////////////////////////////////


def create_obstacles1(world: World):
    """
    Creates the obstacles for level 1

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but adds the obstacles to the game
        every 3 seconds (3 total) to the list containing each obstacle for level 1.
    """
    if world.frame_timer == 90:
        microbe = emoji("microbe")
        obstacle1_1 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_1.obstacle_itself.x = 0
        obstacle1_1.obstacle_itself.y = get_height() / 4
        world.obstacle1_list.append(obstacle1_1)
    if world.frame_timer == 180:
        microbe = emoji("microbe")
        obstacle1_2 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_2.obstacle_itself.x = 0
        obstacle1_2.obstacle_itself.y = (get_height() * 2) / 4
        world.obstacle1_list.append(obstacle1_2)
    if world.frame_timer == 270:
        microbe = emoji("microbe")
        obstacle1_3 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_3.obstacle_itself.x = 0
        obstacle1_3.obstacle_itself.y = (get_height() * 3) / 4
        world.obstacle1_list.append(obstacle1_3)


def level_one_title(world: World):
    """
    Creates the title for level 1

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the level_title text
        to level 1 when a second has passed.
    """
    if world.game_time_value == 1:
        world.level_title.text = "Level 1"


def obstacle1_movement(world: World):
    """
    Determines movement for the level 1 obstacles

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but makes it so that the
        obstacles move from left to right.
    """
    for obstacle in world.obstacle1_list:
        obstacle.obstacle_itself.x += obstacle.obstacle_speed


def obstacle1_wall(world: World):
    """
    Makes the obstacles bounce off wall and move in the opposite direction

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the obstacle speed
        to the opposite direction.
    """
    for obstacle in world.obstacle1_list:
        if obstacle.obstacle_itself.x > get_width():
            obstacle.obstacle_speed = -obstacle.obstacle_speed
        if obstacle.obstacle_itself.x < 0:
            obstacle.obstacle_speed = -obstacle.obstacle_speed


# ///////////////////end of obstacle 1/////////////////////////////

# ///////////////////obstacle 2///////////////////////////////////
def level_two_title(world: World):
    """
    Creates the title for level 2

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the title text to
        level 2 when 15 seconds has passed.
    """
    if world.game_time_value == 15:
        world.level_title.text = "Level 2"


def create_obstacles2(world: World):
    """
    Creates the obstacles for level 2

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but creates frisbees which
        move up and down on the screen. These frisbees are added to a list for
        all level 2 obstacles.
    """
    if world.frame_timer == 450:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_1 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_1.obstacle_itself.x = get_width() / 5
        obstacle2_1.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_1)
    if world.frame_timer == 540:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_2 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_2.obstacle_itself.x = (get_width() * 2) / 5
        obstacle2_2.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_2)
    if world.frame_timer == 630:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_3 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_3.obstacle_itself.x = (get_width() * 3) / 5
        obstacle2_3.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_3)
    if world.frame_timer == 720:
        frisbee = emoji("🥏")
        frisbee.scale_x = 1.5
        frisbee.scale_y = 1.5
        obstacle2_4 = Obstacle(frisbee, OBSTACLE2_SPEED)
        obstacle2_4.obstacle_itself.x = (get_width() * 4) / 5
        obstacle2_4.obstacle_itself.y = 0
        world.obstacle2_list.append(obstacle2_4)


def obstacle2_movement(world: World):
    """
    Establishes up and down movement of the frisbee

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the y value of
        the frisbees so that they move vertically.
    """
    for obstacle in world.obstacle2_list:
        obstacle.obstacle_itself.y += obstacle.obstacle_speed


def obstacle2_wall(world: World):
    """
    Establishes collision interaction between frisbee and the wall

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the obstacle
        speed so that it moves in the opposite direction.
    """
    for obstacle in world.obstacle2_list:
        if obstacle.obstacle_itself.y > get_height():
            obstacle.obstacle_speed = -OBSTACLE2_SPEED
        if obstacle.obstacle_itself.y < 0:
            obstacle.obstacle_speed = OBSTACLE2_SPEED


# //////////////////end of obstacle 2////////////////////////////

# /////////////////start of obstacle 3///////////////////////////
def level_three_title(world: World):
    """
    Updates the level text to level 3

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but changes the text of
        level_title to level 3.
    """
    if world.game_time_value == 30:
        world.level_title.text = "Level 3"


def create_obstacle3(world: World):
    """
    Creates the obstacle for level 3.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything, but creates the obstacle and adds
        it to the obstacle 3 list.
    """
    if world.frame_timer == 900:
        plane = emoji("airplane")
        plane.scale_y = 3
        plane.scale_x = 3
        obstacle3_1 = Obstacle(plane, OBSTACLE3_SPEED)
        obstacle3_1.obstacle_itself.x = 0
        obstacle3_1.obstacle_itself.y = 0
        world.obstacle3_list.append(obstacle3_1)


def obstacle3_movement(world: World):
    """
    Determines movement for obstacle 3. This one homes towards the player after taking
    in the player's coordinates relative to its own.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. The obstacle compares xy coordinates
        with the player and moves towards the player.
    """
    for obstacle in world.obstacle3_list:
        if world.character.x < obstacle.obstacle_itself.x:
            if world.character.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.character.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed + 0.45
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed + 0.45
            else:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
        if world.character.x > obstacle.obstacle_itself.x:
            if world.character.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed + 0.40
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed + 0.40
            if world.character.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed + 0.90
                obstacle.obstacle_itself.y += obstacle.obstacle_speed + 0.90
            else:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
        else:
            if world.character.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.character.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed


# /////////////////end of obstacle 3////////////////////////////

# /////////////////obstacle 4//////////////////////////////////
def level_four_title(world: World):
    """
    Updates the level to level 4

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. Updates the text of level_title
        to level 4.
    """
    if world.game_time_value == 45:
        world.level_title.text = "Level 4"


def create_obstacle4(world: World):
    """
    Creates the obstacles for level 4. These move around the border of the screen.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. Creates obstacles every 5
        seconds and adds them to the obstacle 4 list.
    """
    if world.frame_timer == 1350:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_1 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_1.obstacle_itself.x = 20
        obstacle4_1.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_1)
    if world.frame_timer == 1500:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_2 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_2.obstacle_itself.x = 20
        obstacle4_2.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_2)
    if world.frame_timer == 1650:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_3 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_3.obstacle_itself.x = 20
        obstacle4_3.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_3)
    if world.frame_timer == 1800:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_4 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_4.obstacle_itself.x = 20
        obstacle4_4.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_4)
    if world.frame_timer == 1950:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_5 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_5.obstacle_itself.x = 20
        obstacle4_5.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_5)
    if world.frame_timer == 2100:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_6 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_6.obstacle_itself.x = 20
        obstacle4_6.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_6)
    if world.frame_timer == 2250:
        satellite = emoji("satellite")
        satellite.scale_y = 3
        satellite.scale_x = 3
        obstacle4_7 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_7.obstacle_itself.x = 20
        obstacle4_7.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_7)

def obstacle4_horz_movement(world: World):
    """
    Determines the horizontal movement for level 4 obstacles. Changes direction when they
    hit the corner.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. When the obstacle reaches a certain corner,
        its speed updates in order to continue moving across the border.
    """
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
    """
    Determines the vertical movement for level 4 obstacles. Changes direction when they
    hit the corner.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. When the obstacle reaches a certain corner,
        its speed updates in order to continue moving across the border.
    """
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
    """
    Updates the level title to level 5

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. Updates the text of level_title
        to level 5
    """
    if world.game_time_value == 80:
        world.level_title.text = "Level 5"


def level_five(world: World):
    """
    For level 5, obstacles in level 1, 2, and 3 have their speed increased

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. When 80 seconds has passed,
        runs through obstacle lists and increases their speeds
    """
    if world.frame_timer == 2400:
        for obstacle in world.obstacle1_list:
            if obstacle.obstacle_speed > 0:
                obstacle.obstacle_speed += 3
            if obstacle.obstacle_speed < 0:
                obstacle.obstacle_speed += -3
        for obstacle in world.obstacle2_list:
            if obstacle.obstacle_speed > 0:
                obstacle.obstacle_speed += 3
            if obstacle.obstacle_speed < 0:
                obstacle.obstacle_speed += -3
        for obstacle in world.obstacle3_list:
            obstacle.obstacle_speed += 0.5

# ////////////////end of level 5/////////////////////////////

# ///////////////end screen/////////////////////////////////
def level_six_title(world: World):
    """
    Updates the level title to level 6

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. When the time reaches 90 seconds,
        the text of level_title and game_time are updated accordingly.
    """
    if world.frame_timer == 2700:
        if not world.endless_mode:
            world.level_title.text = "Level 6"
            world.game_time.text = "Reach Saturn before 100 seconds!"

def create_saturn(world: World):
    """
    Creates the saturn emoji, which the player needs to reach to win the game

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. When 90 seconds have passed,
        creates the saturn emoji at the center of the screen.
    """
    if world.frame_timer == 2700:
        if not world.endless_mode:
            saturn = emoji("🪐")
            saturn.scale_x = 5
            saturn.scale_y = 5
            saturn.x = get_width() / 2
            saturn.y = get_height() / 2
            world.saturn_list.append(saturn)

def character_hits_saturn(world: World) -> bool:
    """
    Determines whether the player character has hit saturn, which triggers
    the win screen

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        bool: Whether the character has reached saturn
    """
    wins_game = False
    for saturn in world.saturn_list:
        if (world.character.x + 50) > saturn.x > (world.character.x - 50):
            if (world.character.y + 50) > saturn.y > (world.character.y - 50):
                wins_game = True
    return wins_game


def win_screen(world: World):
    """
    Creates the win screen for the game, updating text and hiding all obstacles
    on screen.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. updates the text of game_time
        to the win text and hides all obstacles on screen
    """
    world.game_time.text = "Congratulations! Your Score: " + str(world.game_time_value)
    hide_obstacles(world)

# ///////////////end of end screen/////////////////////////

def character_hits_obstacle(world: World) -> bool:
    """
    Determines whether the character has hit an obstacle, which decides whether they
    lose the game. Player also loses if 100 seconds have passed since the start of the game.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        bool: Whether any obstacles have entered into range of the character or if
        100 seconds have passed. Will also decrease shield if the player has any (or else they lose).
    """
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
    if world.game_time_value >= 100:
        is_game_over = True
    return is_game_over

def hide_obstacles(world: World):
    """
    Hides all obstacles on screen

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. The hide function runs through
        each obstacle list and removes them from screen.
    """
    for obstacle in world.obstacle1_list:
        hide(obstacle.obstacle_itself)
    for obstacle in world.obstacle2_list:
        hide(obstacle.obstacle_itself)
    for obstacle in world.obstacle3_list:
        hide(obstacle.obstacle_itself)
    for obstacle in world.obstacle4_list:
        hide(obstacle.obstacle_itself)
def game_over(world: World):
    """
    The game over screen for the game. Occurs when the player hits an obstacle with
    0 shield or 100 seconds have passed since the start of the game.

    Args:
        world (World): The world dataclass created during the start of the game

    Return:
        None: The function does not return anything. updates the game_time text and
        hides all obstacles on screen.
    """
    world.game_time.text = "Game Over! Score: " + str(world.game_time_value)
    hide_obstacles(world)

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
when("updating", create_saturn)
# level6
# shield
when(should_shield_spawn, create_shield)
when("updating", shield_bobbing)
when("updating", update_shield_status)
when(character_hits_shield, character_gets_shield)
# shield
when("typing", character_direction)
when(character_hits_saturn, pause, win_screen)
when(character_hits_obstacle, pause, game_over)
start()
