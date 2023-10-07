import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
ARRAY_SIZE = 100
RECT_WIDTH = WIDTH // ARRAY_SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Generate an array of random integers
array = [random.randint(10, HEIGHT - 10) for _ in range(ARRAY_SIZE)]

# Function to draw the array
def draw_array(array, color=[]):
    for i in range(len(array)):
        rect_color = (0, 128, 255)  # Blue color by default
        if i in color:
            rect_color = (255, 0, 0)  # Red color for selected elements
        pygame.draw.rect(WIN, rect_color, (i * RECT_WIDTH, HEIGHT - array[i], RECT_WIDTH, array[i]))

# Main loop
run = True
while run:
    WIN.fill((0, 0, 0))  # Fill the window with black

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Bubble sort
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                # Swap
                array[j], array[j + 1] = array[j + 1], array[j]

                # Draw the updated array
                draw_array(array, [j, j+1])
                pygame.display.update()
                time.sleep(0.02)  # Slow down for visualization

pygame.quit()
