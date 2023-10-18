import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
ARRAY_SIZE = 100
RECT_WIDTH = WIDTH // ARRAY_SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
CLOCK = pygame.time.Clock()

# Generate an array of random integers
array = [random.randint(10, HEIGHT - 10) for _ in range(ARRAY_SIZE)]

def draw_array(array, color=[]):
    WIN.fill((0, 0, 0))
    for i in range(len(array)):
        if i in color:
            rect_color = (255, 0, 0)  # Red for current items
        else:
            rect_color = (0, 128, 255)  # Blue by default
        pygame.draw.rect(WIN, rect_color, (i * RECT_WIDTH, HEIGHT - array[i], RECT_WIDTH, array[i]))
    pygame.display.update()

def bubble_sort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                draw_array(array, [j, j+1])
                CLOCK.tick(60)

def main():
    run = True
    while run:
        draw_array(array)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bubble_sort(array)
        run = False

    pygame.quit()

if __name__ == "__main__":
    main()
