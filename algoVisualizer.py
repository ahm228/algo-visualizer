import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
ARRAY_SIZE = 200
RECT_WIDTH = WIDTH // ARRAY_SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
CLOCK = pygame.time.Clock()

array = [random.randint(10, HEIGHT - 10) for _ in range(ARRAY_SIZE)]

def drawArray(array, color=[]):
    WIN.fill((0, 0, 0))
    for i in range(len(array)):
        if i in color:
            rectColor = (255, 0, 0)  # Red for current items
        else:
            rectColor = (0, 128, 255)  # Blue by default
        pygame.draw.rect(WIN, rectColor, (i * RECT_WIDTH, HEIGHT - array[i], RECT_WIDTH, array[i]))
    pygame.display.update()

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                drawArray(array, [j, j+1])
                CLOCK.tick(350)

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            array[j + 1] = array[j]
            j -= 1
            drawArray(array, [j, j+1])
            CLOCK.tick(350)
        array[j + 1] = key
        drawArray(array, [j, i])
        CLOCK.tick(350)

def selectionSort(array):
    for i in range(len(array)):
        minIdx = i
        for j in range(i+1, len(array)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            if array[j] < array[minIdx]:
                minIdx = j
            drawArray(array, [j, minIdx])
            CLOCK.tick(350)
        array[i], array[minIdx] = array[minIdx], array[i]
        drawArray(array, [i, minIdx])
        CLOCK.tick(350)

def mergeSort(array, l=0, r=None):
    if r is None:
        r = len(array) - 1

    if l < r:
        m = l + (r - l) // 2

        mergeSort(array, l, m)
        mergeSort(array, m + 1, r)
        merge(array, l, m, r)

def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = array[l:l+n1]
    R = array[m+1:m+1+n2]

    i, j, k = 0, 0, l

    while i < n1 and j < n2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        drawArray(array, [k])
        CLOCK.tick(350)
        k += 1

    while i < n1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        array[k] = L[i]
        drawArray(array, [k])
        CLOCK.tick(350)
        i += 1
        k += 1

    while j < n2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        array[k] = R[j]
        drawArray(array, [k])
        CLOCK.tick(350)
        j += 1
        k += 1

def quickSort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pi = partition(array, low, high)
        
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            drawArray(array, [i, j])
            CLOCK.tick(350)

    array[i + 1], array[high] = array[high], array[i + 1]
    drawArray(array, [i + 1, high])
    CLOCK.tick(350)
    
    return i + 1

def heapSort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        drawArray(array, [i, 0])
        CLOCK.tick(350)
        heapify(array, i, 0)

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l

    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        drawArray(array, [i, largest])
        CLOCK.tick(350)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        heapify(array, n, largest)

def countingSortForRadix(array, position):
    n = len(array)
    output = [-1] * n
    count = [0] * 10

    for i in range(n):
        index = array[i] // position
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        index = array[i] // position
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
        drawArray(array, [i])
        CLOCK.tick(350)

    for i in range(len(array)):
        array[i] = output[i]
        drawArray(array, [i])
        CLOCK.tick(350)

def radixSort(array):
    maxNum = max(array)

    position = 1
    while maxNum // position > 0:
        countingSortForRadix(array, position)
        position *= 10

def shellSort(array):
    n = len(array)
    
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            
            temp = array[i]
            j = i
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                drawArray(array, [j, j-gap])
                CLOCK.tick(350)
                j -= gap
            
            array[j] = temp
            drawArray(array, [j])
            CLOCK.tick(350)

        gap //= 2

def isSorted(array):
    n = len(array)
    for i in range(1, n):
        if array[i] < array[i - 1]:
            return False
    return True

def bogoSort(array):
    while not isSorted(array):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        random.shuffle(array)
        drawArray(array, range(len(array)))
        CLOCK.tick(350)

def main():
    run = True
    while run:
        drawArray(array)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        bubbleSort(array)
        run = False

    pygame.quit()

if __name__ == "__main__":
    main()
