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
            rectColor = (255, 0, 0)

        else:
            rectColor = (0, 128, 255)

        pygame.draw.rect(WIN, rectColor, (i * RECT_WIDTH, HEIGHT - array[i], RECT_WIDTH, array[i]))

    pygame.display.update()

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                drawArray(array, [j, j+1])
                CLOCK.tick(200)

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            drawArray(array, [j, j+1])
            CLOCK.tick(200)

        array[j + 1] = key
        drawArray(array, [j, i])
        CLOCK.tick(200)

def selectionSort(array):
    for i in range(len(array)):
        minIdx = i

        for j in range(i+1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
            drawArray(array, [j, minIdx])
            CLOCK.tick(200)

        array[i], array[minIdx] = array[minIdx], array[i]
        drawArray(array, [i, minIdx])
        CLOCK.tick(200)

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
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1

        else:
            array[k] = R[j]
            j += 1

        drawArray(array, [k])
        CLOCK.tick(200)
        k += 1

    while i < n1:
        array[k] = L[i]
        drawArray(array, [k])
        CLOCK.tick(200)
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        drawArray(array, [k])
        CLOCK.tick(200)
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

        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            drawArray(array, [i, j])
            CLOCK.tick(200)

    array[i + 1], array[high] = array[high], array[i + 1]
    drawArray(array, [i + 1, high])
    CLOCK.tick(200)
    
    return i + 1

def heapSort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        drawArray(array, [i, 0])
        CLOCK.tick(200)
        heapify(array, i, 0)

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[l] > array[largest]:
        largest = l

    if r < n and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        drawArray(array, [i, largest])
        CLOCK.tick(200)
        
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
        index = array[i] // position
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
        drawArray(array, [i])
        CLOCK.tick(200)

    for i in range(len(array)):
        array[i] = output[i]
        drawArray(array, [i])
        CLOCK.tick(200)

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
            
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                drawArray(array, [j, j-gap])
                CLOCK.tick(200)
                j -= gap
            
            array[j] = temp
            drawArray(array, [j])
            CLOCK.tick(200)

        gap //= 2

def isSorted(array):
    n = len(array)
    for i in range(1, n):
        if array[i] < array[i - 1]:
            return False
        
    return True

def bogoSort(array):
    while not isSorted(array):
        random.shuffle(array)
        drawArray(array, range(len(array)))
        CLOCK.tick(200)

'''def bucketSort(array):
    arr = []
    slotNum = 10

    for i in range(slotNum):
        arr.append([])

    for j in array:
        indexB = int(slotNum * (j - min(array)) / (max(array) - min(array) + 1))
        arr[indexB].append(j)

    for i in range(slotNum):
        arr[i] = insertionSort(arr[i])

    k = 0
    for i in range(slotNum):
        for j in range (len(arr[i])):
            array[k] = arr[i][j]
            drawArray(array, [k])
            CLOCK.tick(200)
            k += 1

    return array'''

def countingSort(array):
    maxVal = max(array)
    countArray = [0] * (maxVal + 1)

    for num in array:
        countArray[num] += 1
        drawArray(array, [num])
        CLOCK.tick(200)
    
    for i in range(1, maxVal + 1):
        countArray[i] += countArray[i - 1]

    outputArray = [0] * len(array)

    for i in range(len(array) - 1, -1, -1):
        outputArray[countArray[array[i]] - 1] = array[i]
        countArray[array[i]] -= 1
        drawArray(outputArray, [i])
        CLOCK.tick(200)
    
    return outputArray

def cocktailShaker(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1

    while (swapped == True):
        swapped = False

        for i in range(start, end):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                drawArray(array, [i, i + 1])
                CLOCK.tick(200)
                swapped = True

        if (swapped == False):
            break
            
        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                drawArray(array, [i, i + 1])
                CLOCK.tick(200)
                swapped = True

        start = start + 1

def getNextGap(gap):
    gap = int((gap * 10) / 13)

    if gap < 1:
        return 1
    
    return gap

def combSort(array):
    n = len(array)
    gap = n
    swapped = True

    while gap != 1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        
        for i in range(0, n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]
                drawArray(array, [i, i + int(gap)])
                CLOCK.tick(200)
                swapped = True

'''
def cycleSort(array):

def pancakeSort(array):

def introSort(array):

def bitonicSort(array):

def spaghettiSort(array):

def timSort(array):

def treeSort(array):

def cubeSort(array):

def gnomeSort(array):

def stoogeSort(array):
'''

def regenerateArray():
    global array
    array = [random.randint(10, HEIGHT - 10) for _ in range(ARRAY_SIZE)]
    drawArray(array)
    drawButtons()
    pygame.display.update()

BUTTONS = [
    {"label": "Bubble Sort", "function": bubbleSort},
    {"label": "Insertion Sort", "function": insertionSort},
    {"label": "Selection Sort", "function": selectionSort},
    {"label": "Merge Sort", "function": mergeSort},
    {"label": "Quick Sort", "function": quickSort},
    {"label": "Heap Sort", "function": heapSort},
    {"label": "Radix Sort", "function": radixSort},
    {"label": "Shell Sort", "function": shellSort},
    {"label": "Bogo Sort", "function": bogoSort},
    {"label": "Bucket Sort", "function": bucketSort},
    {"label": "Counting Sort", "function": countingSort},
    {"label": "Cocktail Shaker Sort", "function": cocktailShaker},
    {"label": "Comb Sort", "function": combSort},
]

BUTTONS.append({"label": "Restart", "function": "RESTART"})

FONT = pygame.font.SysFont("Arial", 20)
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 30

TOTAL_BUTTONS_HEIGHT = len(BUTTONS) * (BUTTON_HEIGHT + 10)
START_X, START_Y = 10, HEIGHT - TOTAL_BUTTONS_HEIGHT

def drawButtons():
    for idx, button in enumerate(BUTTONS):
        pygame.draw.rect(WIN, (200, 200, 200), (START_X, START_Y + idx * (BUTTON_HEIGHT + 10), BUTTON_WIDTH, BUTTON_HEIGHT))
        text = FONT.render(button["label"], True, (0, 0, 0))
        WIN.blit(text, (START_X + (BUTTON_WIDTH - text.get_width()) // 2, START_Y + idx * (BUTTON_HEIGHT + 10) + (BUTTON_HEIGHT - text.get_height()) // 2))


def handleButtonClick(pos):
    for idx, button in enumerate(BUTTONS):
        if START_X <= pos[0] <= START_X + BUTTON_WIDTH and START_Y + idx * (BUTTON_HEIGHT + 10) <= pos[1] <= START_Y + idx * (BUTTON_HEIGHT + 10) + BUTTON_HEIGHT:
            if button["function"] == "RESTART":
                regenerateArray()
                return None
            return button["function"]
    return None

def main():
    run = True
    
    while run:
        drawButtons()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sorting_algorithm = handleButtonClick(pygame.mouse.get_pos())
                if sorting_algorithm:
                    sorting_algorithm(array)

    pygame.quit()

if __name__ == "__main__":
    main()
