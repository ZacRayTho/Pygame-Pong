import pygame
import math
from settings import *

class RayCasting:
    # RayCasting is , we need to cast a certain amount of rays in a given Field of View (FOV)
    # for each ray we need to discover the intersection point with the wall
    # check RayCastingDoom.png 
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.objects_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        self.objects_to_render = []
        for ray, values in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = values

            if proj_height < HEIGHT:
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
                )
                
                wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_HEIGHT - proj_height // 2)
            else: 
                texture_height = TEXTURE_SIZE * HEIGHT / proj_height
                wall_column = self.textures[texture].subsurface(
                    offset * (TEXTURE_SIZE - SCALE), HALF_TEXTURE_SIZE - texture_height // 2,
                    SCALE, texture_height
                )
                wall_column = pygame.transform.scale(wall_column, (SCALE, HEIGHT))
                wall_pos = (ray * SCALE, 0)

            self.objects_to_render.append((depth, wall_column, wall_pos))

    def ray_cast(self):
        # Ray casting is a technique used in 2D graphics to simulate the perception of depth and distance

        self.ray_casting_result = []
        # The code retrieves the player's position (ox, oy) and map position (x_map, y_map) from the game object
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        texture_vert, texture_hor = 1, 1

        # The variable ray_angle is initialized with the player's angle minus half of the field of view (HALF_FOV)
        # This value represents the starting angle of the first ray
        ray_angle = self.game.player.angle - HALF_FOV + 0.0001

        # enters a loop that iterates over each ray
        for ray in range(NUM_RAYS):
            # For each ray, the code calculates the sine (sin_a) and cosine (cos_a) of the current ray angle
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            # horizontals
            # The code calculates the intersection point of the ray with a horizontal wall
            # It determines whether the ray is going upwards or downwards based on the sign of sin_a
            y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

            # calculates the distance (depth_hor) from the player's position to the intersection point using trigonometry
            depth_hor = (y_hor - oy) / sin_a

            # x_hor variable represents the x-coordinate of the intersection point
            x_hor = ox + depth_hor * cos_a

            # It is incremented by dx for each step in the loop to simulate the ray's movement
            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                # checks if the current intersection point (tile_hor) is within the game map
                # If it is, it means the ray has intersected with a wall, and the loop is broken
                # Otherwise, the intersection point is updated by incrementing x_hor and y_hor and adjusting the depth
                tile_hor = int(x_hor), int(y_hor)
                if tile_hor in self.game.map.world_map:
                    texture_hor = self.game.map.world_map[tile_hor]
                    break
                x_hor += dx
                y_hor += dy
                depth_hor += delta_depth


            # verticals
            # the code now calculates the intersection point of the ray with a vertical wall
            # It determines whether the ray is going left or right based on the sign of cos_a
            # It calculates the distance (depth_vert) and the y-coordinate (y_vert) of the intersection point
            x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

            # calculates the distance (depth_vert) from the player's position to the intersection point using trigonometry
            depth_vert = (x_vert - ox) / cos_a

            # y_vert variable represents the y-coordinate of the intersection point
            y_vert = oy + depth_vert * sin_a

            # It is incremented by dy for each step in the loop to simulate the ray's movement
            delta_depth = dx / cos_a
            dy = delta_depth * sin_a

            for i in range(MAX_DEPTH):
                # checks if the current intersection point (tile_vert) is within the game map
                # If it is, it means the ray has intersected with a wall, and the loop is broken
                # Otherwise, the intersection point is updated by incrementing x_vert and y_vert and adjusting the depth
                tile_vert = int(x_vert), int(y_vert)
                if tile_vert in self.game.map.world_map:
                    texture_vert = self.game.map.world_map[tile_vert]
                    break
                x_vert += dx
                y_vert += dy
                depth_vert += delta_depth

            # depth
            # The code determines the final depth of the intersection by comparing the depth values of the horizontal and vertical intersections
            # The smaller depth value is chosen as the final depth
            if depth_vert < depth_hor:
                depth, texture = depth_vert, texture_vert
                y_vert %= 1
                offset = y_vert if cos_a > 0 else (1 - y_vert)
            else: 
                depth, texture = depth_hor, texture_hor
                x_hor %= 1
                offset = (1 - x_hor) if sin_a > 0 else x_hor

            # remove fishbowl effect
            # calculates the difference between the player's angle and the current ray angle
            # This cosine value represents the angular difference between the player's angle and the current ray angle
            # The calculated cosine value is multiplied by the depth of the intersection point (depth)
            # This adjustment modifies the depth based on the angle difference
            # The purpose of this adjustment may be to account for the perspective distortion caused by the player's viewing angle
            # By multiplying the depth by the cosine value, the depth is corrected to reflect the perspective of the player's viewpoint
            depth *= math.cos(self.game.player.angle - ray_angle)

            # draw for debug
            # draws a line on the game screen to represent the ray
            # start from the player's position (ox, oy) and extends to the intersection point (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a)
            # The line color is yellow, and the line width is set to 2.
            # pygame.draw.line(self.game.screen, 'yellow', (100 * ox, 100 * oy),
            #                  (100 * ox + 100 * depth * cos_a, 100 * oy + 100 * depth * sin_a), 2)

            # projection
            # proj_height represents the height of the wall segment to be drawn on the screen
            # It is calculated by dividing SCREEN_DIST (the distance between the player's viewpoint and the screen) by the depth of the intersection point (depth + 0.0001)
            # Adding 0.0001 is done to avoid potential division by zero errors
            proj_height = SCREEN_DIST / (depth + 0.0001)

            #DRAW WALLS
            # The depth value is raised to the power of 5 and multiplied by 0.00002 to adjust the intensity
            # The result is then used to calculate the color value by dividing 255 (the maximum color value) by the calculated intensity
            # The resulting color value is then replicated three times using the [...] * 3 notation
            # This ensures that the RGB values are identical, resulting in a grayscale color for the wall segment
            # color = [255 / (1 + depth ** 5 * 0.00002)] * 3

            # The parameters for pygame.draw.rect() are as follows:
            # self.game.screen: The surface on which the rectangle is drawn (the game screen).
            # 'white': The color of the rectangle (in this case, white).
            # (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height): The position and dimensions of the rectangle
            # The ray * SCALE determines the x-coordinate of the left edge of the rectangle
            # HALF_HEIGHT - proj_height // 2 determines the y-coordinate of the top edge of the rectangle, ensuring that the rectangle is vertically centered
            # SCALE determines the width of the rectangle, and proj_height determines the height
            # pygame.draw.rect(self.game.screen, color,
            #                  (ray * SCALE, HALF_HEIGHT - proj_height // 2, SCALE, proj_height))

            # ray casting result
            self.ray_casting_result.append((depth, proj_height, texture, offset))

            # After drawing the ray, the ray angle is incremented by DELTA_ANGLE, which represents the angle between each ray
            # This prepares the code for the next iteration of the ray casting loop.
            ray_angle += DELTA_ANGLE

    def update(self):
        self.ray_cast()
        self.get_objects_to_render()