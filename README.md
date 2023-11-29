### Title: 90 Seconds

Dodging compounding obstacles which scale in size and speed

### About
Following the theme of SCALE, I will be attempting to create
a game in which the player will control a character and dodge 
projectiles and obstacles (of increasing scale). The player will move on to 
different levels, in which additional obstacles will be added on top of the 
already existing obstacles. This continues until the player reaches the final 
phase and wins the game by reaching the end. If the player is in endless mode,
they will aim to achieve the largest score possible. 

### Game Demo: https://youtu.be/Z2mcJ_HuehY

### Instructions:
 - Pre-Game
   - Prompt will come up in terminal
     - Choose character to play (type in word)
       - Will be asked to enter another word if no character exists
     - choose yes / no for endless mode 
     - Then good to go!
 - Dodge the obstacles
 - Control character with the **arrow** keys 
 - Collect the shields which pop up throughout the game
   - Each shield allows you to collide obstacles for 20 frames without losing
 - When you lose, the game will pause
   - Will need to rerun the code to play again

### Authors:
 - Jia Qi (qijia@udel.edu)

### Acknowledgements
 - These helped A LOT:
   - Designer Function List
   - Example Firefighter Game (Designer Tutorial)
 - My professor and TAs!

## Development Progress
### Phase 1: Figuring things out
 - [x] Creating the character
 - [x] Setting character movement (with arrow keys)
 - [x] Creating a timer
 - [x] Determining how many levels I need (Currently: 5)
 - [x] Creating a Level
   - Creating obstacle
     - [x] Decide where obstacle spawns
     - [x] Size of obstacle
     - [x] Speed of obstacle
     - [x] Direction of obstacle
     - [x] Obstacle - wall interactions
   - [x] Creating collision interactions between objects and character
     - [x] Lose screen
 - Phase 1 demo video: https://youtu.be/uwTAgwr3yCs

### Phase 2: "Scaling" Up
 - [x] Repeating steps under creating a level (4 times)
   - [x] Level 2
   - [x] Level 3
   - [x] Level 4
   - [x] Level 5
 - [x] Connecting levels together (want to use the timer)
 - Phase 2 demo video: https://youtu.be/875U5ALf2lc

### Phase 3: Tidying Up
 - [x] Creating win screen
 - [x] Fixing scales and locations of obstacles in game
 - [x] Tidying up look of game
 - Consider adding additional features (powerups, more characters, etc.)
   - Created:
     - [x] More playable characters (just skins)
     - [x] Endless mode (turn off saturn level)
     - [x] Shield Powerup (disappears after time, allows for one free collision)
 - Testing
   - [x] Character Selection
   - [x] Run Through Game
     - [x] Normal Mode
     - [x] Endless Mode
   - [x] Tweak Obstacle Speeds if Necessary
   - [x] Shield Powerup
   - [x] Proper Collision