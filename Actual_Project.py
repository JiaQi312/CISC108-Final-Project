from designer import *
from dataclasses import dataclass

OBSTACLE1_SPEED = 3
OBSTACLE2_SPEED = 5
OBSTACLE3_SPEED = 1
OBSTACLE4_SPEED = 2
OBSTACLE6_SPEED = 7


@dataclass
class Obstacle:
    obstacle_itself: DesignerObject
    obstacle_speed: int


@dataclass
class World:
    egg: DesignerObject
    egg_speed_x: int
    egg_speed_y: int
    game_time: DesignerObject
    game_time_value: int
    level_title: DesignerObject
    frame_timer: int
    obstacle1_list: list[Obstacle]
    obstacle2_list: list[Obstacle]
    obstacle3_list: list[Obstacle]
    obstacle4_list: list[Obstacle]
    obstacle6_list: list[Obstacle]


def create_world() -> World:
    """Creating World"""
    return World(create_egg(),
                 0,
                 0,
                 text("black", "Time: ", 24, get_width() / 2, 20),
                 0,
                 text("black", "", 24, 50, 20),
                 0,
                 [],
                 [],
                 [],
                 [],
                 []
                 )


def create_egg() -> DesignerObject:
    """Create the Egg"""
    egg = emoji("egg")
    egg.y = get_height() * (1 / 2)
    return egg


def create_timer(world: World):
    """Creating the timer"""
    world.game_time.text = "Timer: " + str(world.game_time_value)


def increase_timer(world: World):
    """Increase an in-game timer that increases over time"""
    world.frame_timer += 1
    if world.frame_timer % 30 == 0:
        world.game_time_value += 1


def move_egg(world: World):
    """Regular movement of the egg"""
    world.egg.x += world.egg_speed_x
    world.egg.y += world.egg_speed_y


def head_left(world: World):
    """egg heads left"""
    world.egg_speed_x = -5
    world.egg_speed_y = 0


def head_right(world: World):
    """egg heads right"""
    world.egg_speed_x = 5
    world.egg_speed_y = 0


def head_up(world: World):
    """egg heads up"""
    world.egg_speed_x = 0
    world.egg_speed_y = -5


def head_down(world: World):
    """egg heads down"""
    world.egg_speed_x = 0
    world.egg_speed_y = 5


def egg_direction(world: World, key: str):
    """Determining which direction egg moves"""
    if key == "right":
        head_right(world)
    if key == "left":
        head_left(world)
    if key == "up":
        head_up(world)
    if key == "down":
        head_down(world)


def egg_wall(world: World):
    """to make egg bounce off wall"""
    if world.egg.x > get_width():
        head_left(world)
    if world.egg.x < 0:
        head_right(world)
    if world.egg.y < 0:
        head_down(world)
    if world.egg.y > get_height():
        head_up(world)


# ////////////////////////////Obstacle 1////////////////////////////////


def create_obstacles1(world: World):
    """Obstacle from frame_time 0 - 900"""
    if world.frame_timer == 1:
        microbe = emoji("microbe")
        obstacle1_1 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_1.obstacle_itself.x = 0
        obstacle1_1.obstacle_itself.y = get_height() / 5
        world.obstacle1_list.append(obstacle1_1)
    if world.frame_timer == 150:
        microbe = emoji("microbe")
        obstacle1_2 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_2.obstacle_itself.x = 0
        obstacle1_2.obstacle_itself.y = (get_height() * 2) / 5
        world.obstacle1_list.append(obstacle1_2)
    if world.frame_timer == 300:
        microbe = emoji("microbe")
        obstacle1_3 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_3.obstacle_itself.x = 0
        obstacle1_3.obstacle_itself.y = (get_height() * 3) / 5
        world.obstacle1_list.append(obstacle1_3)
    if world.frame_timer == 450:
        microbe = emoji("microbe")
        obstacle1_4 = Obstacle(microbe, OBSTACLE1_SPEED)
        obstacle1_4.obstacle_itself.x = 0
        obstacle1_4.obstacle_itself.y = (get_height() * 4) / 5
        world.obstacle1_list.append(obstacle1_4)


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
        obstacle3_1 = Obstacle(plane, OBSTACLE3_SPEED)
        obstacle3_1.obstacle_itself.x = 0
        obstacle3_1.obstacle_itself.y = 0
        world.obstacle3_list.append(obstacle3_1)


def obstacle3_movement(world: World):
    """movement for obstacle 3, want to make it home towards character"""
    for obstacle in world.obstacle3_list:
        if world.egg.x > obstacle.obstacle_itself.x:
            if world.egg.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.egg.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed
            else:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
        elif world.egg.x < obstacle.obstacle_itself.x:
            if world.egg.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.egg.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed
            else:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
        else:
            if world.egg.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.egg.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed


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
        obstacle4_1 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_1.obstacle_itself.x = 20
        obstacle4_1.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_1)
    if world.frame_timer == 3000:
        satellite = emoji("satellite")
        obstacle4_2 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_2.obstacle_itself.x = 20
        obstacle4_2.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_2)
    if world.frame_timer == 3150:
        satellite = emoji("satellite")
        obstacle4_3 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_3.obstacle_itself.x = 20
        obstacle4_3.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_3)
    if world.frame_timer == 3300:
        satellite = emoji("satellite")
        obstacle4_4 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_4.obstacle_itself.x = 20
        obstacle4_4.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_4)
    if world.frame_timer == 3450:
        satellite = emoji("satellite")
        obstacle4_5 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_5.obstacle_itself.x = 20
        obstacle4_5.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_5)
    if world.frame_timer == 3600:
        satellite = emoji("satellite")
        obstacle4_6 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_6.obstacle_itself.x = 20
        obstacle4_6.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_6)
    if world.frame_timer == 3750:
        satellite = emoji("satellite")
        obstacle4_7 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_7.obstacle_itself.x = 20
        obstacle4_7.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_7)
    if world.frame_timer == 3900:
        satellite = emoji("satellite")
        obstacle4_8 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_8.obstacle_itself.x = 20
        obstacle4_8.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_8)
    if world.frame_timer == 4050:
        satellite = emoji("satellite")
        obstacle4_9 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_9.obstacle_itself.x = 20
        obstacle4_9.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_9)
    if world.frame_timer == 4200:
        satellite = emoji("satellite")
        obstacle4_10 = Obstacle(satellite, OBSTACLE4_SPEED)
        obstacle4_10.obstacle_itself.x = 20
        obstacle4_10.obstacle_itself.y = 20
        world.obstacle4_list.append(obstacle4_10)


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
    if world.game_time_value == 150:
        world.level_title.text = "Level 5"


def level_five(world: World):
    """speeding obstacles up"""
    if world.frame_timer == 4500:
        for obstacle in world.obstacle1_list:
            obstacle.obstacle_speed += 2
        for obstacle in world.obstacle2_list:
            obstacle.obstacle_speed += 2
        for obstacle in world.obstacle3_list:
            obstacle.obstacle_speed += 1
        for obstacle in world.obstacle4_list:
            obstacle.obstacle_speed += 2


# ////////////////end of level 5/////////////////////////////

# ///////////////end screen/////////////////////////////////
def level_six_title(world: World):
    """creating title for level 6"""
    if world.frame_timer == 4800:
        world.level_title.text = "Level 6"
        world.game_time.text = "Reach Saturn!"


def create_obstacle6(world: World):
    """creating obstacle 6"""
    if world.frame_timer == 4800:
        saturn = emoji("🪐")
        saturn.scale_x = 3
        saturn.scale_y = 3
        obstacle6_1 = Obstacle(saturn, OBSTACLE4_SPEED)
        obstacle6_1.obstacle_itself.x = 0
        obstacle6_1.obstacle_itself.y = 0
        world.obstacle6_list.append(obstacle6_1)


def obstacle6_movement(world: World):
    """defining obstacle 6 movement"""
    for obstacle in world.obstacle6_list:
        if world.egg.x > obstacle.obstacle_itself.x:
            if world.egg.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.egg.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed
            else:
                obstacle.obstacle_itself.x += obstacle.obstacle_speed
        elif world.egg.x < obstacle.obstacle_itself.x:
            if world.egg.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.egg.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed
            else:
                obstacle.obstacle_itself.x -= obstacle.obstacle_speed
        else:
            if world.egg.y > obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y += obstacle.obstacle_speed
            if world.egg.y < obstacle.obstacle_itself.y:
                obstacle.obstacle_itself.y -= obstacle.obstacle_speed


def egg_hits_saturn(world: World) -> bool:
    """determines whether one wins the game"""
    wins_game = False
    for obstacle in world.obstacle6_list:
        if (world.egg.x + 30) > obstacle.obstacle_itself.x > (world.egg.x - 30):
            if (world.egg.y + 30) > obstacle.obstacle_itself.y > (world.egg.y - 30):
                wins_game = True
    return wins_game


def win_screen(world: World):
    """Shows win screen"""
    world.game_time.text = "Congratulations! Your Score: " + str(world.game_time_value)

# ///////////////end of end screen/////////////////////////

def egg_hits_obstacle(world: World) -> bool:
    """determines whether one loses the game"""
    is_game_over = False
    for obstacle in world.obstacle1_list:
        if (world.egg.x + 20) > obstacle.obstacle_itself.x > (world.egg.x - 20):
            if (world.egg.y + 20) > obstacle.obstacle_itself.y > (world.egg.y - 20):
                is_game_over = True
    for obstacle in world.obstacle2_list:
        if (world.egg.x + 40) > obstacle.obstacle_itself.x > (world.egg.x - 40):
            if (world.egg.y + 40) > obstacle.obstacle_itself.y > (world.egg.y - 40):
                is_game_over = True
    for obstacle in world.obstacle3_list:
        if (world.egg.x + 20) > obstacle.obstacle_itself.x > (world.egg.x - 20):
            if (world.egg.y + 20) > obstacle.obstacle_itself.y > (world.egg.y - 20):
                is_game_over = True
    for obstacle in world.obstacle4_list:
        if (world.egg.x + 20) > obstacle.obstacle_itself.x > (world.egg.x - 20):
            if (world.egg.y + 20) > obstacle.obstacle_itself.y > (world.egg.y - 20):
                is_game_over = True
    return is_game_over


def game_over(world: World):
    """shows game over message"""
    world.game_time.text = "Game Over! Score: " + str(world.game_time_value)


when("starting", create_world)
when("updating", move_egg)
when("updating", egg_wall)
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
when("updating", obstacle6_movement)
# level6
when("typing", egg_direction)
when(egg_hits_saturn, win_screen, pause)
when(egg_hits_obstacle, game_over, pause)
start()
