import math

RES = WIDTH, HEIGHT = 1600, 900
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

PLAYER_POS = 1.5, 5 # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002 # ROTATE SPEED

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

# SCREEN_DIST represents the distance between the player's viewpoint and the screen
# It is calculated by dividing HALF_WIDTH (half of the screen width) by the tangent of HALF_FOV (half of the field of view angle)
# This calculation determines how far the screen is positioned from the player
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)

# SCALE determines the scaling factor for the width of each ray
# It is calculated by dividing the screen width (WIDTH) by the number of rays (NUM_RAYS)
# This value determines the width of each column on the screen that represents a single ray
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2