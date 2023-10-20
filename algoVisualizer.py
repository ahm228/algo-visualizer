import pygame
import random

pygame.init()

while True:
    try:
        FPS = int(input("Please enter the desired frame rate (Note: 200 is recommended): "))
        if FPS <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive integer for the speed.")

while True:
    try:
        ARRAY_SIZE = int(input("Please enter the desired size of the array: "))
        if ARRAY_SIZE <= 0:
            raise ValueError
        break
    except ValueError:
        print("Please enter a valid positive integer for the array size.")

WIDTH = 800
HEIGHT = 600
RECT_WIDTH = WIDTH // ARRAY_SIZE
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
CLOCK = pygame.time.Clock()

array = [random.randint(10, HEIGHT - 10) for _ in range(ARRAY_SIZE)]

def drawArray(array, color=[]):
    WIN.fill((0, 0, 0))
    remainder = WIDTH % ARRAY_SIZE
    for i in range(len(array)):
        if i in color:
            rectColor = (255, 0, 0)
        else:
            rectColor = (0, 128, 255)
        
        extraWidth = 1 if i < remainder else 0
        pygame.draw.rect(WIN, rectColor, (i * RECT_WIDTH + min(i, remainder), HEIGHT - array[i], RECT_WIDTH + extraWidth, array[i]))

    pygame.display.update()


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                drawArray(array, [j, j+1])
                CLOCK.tick(FPS)

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            drawArray(array, [j, j+1])
            CLOCK.tick(FPS)

        array[j + 1] = key
        drawArray(array, [j, i])
        CLOCK.tick(FPS)

    return array

def selectionSort(array):
    for i in range(len(array)):
        minIdx = i

        for j in range(i+1, len(array)):
            if array[j] < array[minIdx]:
                minIdx = j
            drawArray(array, [j, minIdx])
            CLOCK.tick(FPS)

        array[i], array[minIdx] = array[minIdx], array[i]
        drawArray(array, [i, minIdx])
        CLOCK.tick(FPS)

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
        CLOCK.tick(FPS)
        k += 1

    while i < n1:
        array[k] = L[i]
        drawArray(array, [k])
        CLOCK.tick(FPS)
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        drawArray(array, [k])
        CLOCK.tick(FPS)
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
            CLOCK.tick(FPS)

    array[i + 1], array[high] = array[high], array[i + 1]
    drawArray(array, [i + 1, high])
    CLOCK.tick(FPS)
    
    return i + 1

def heapSort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        drawArray(array, [i, 0])
        CLOCK.tick(FPS)
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
        CLOCK.tick(FPS)
        
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
        CLOCK.tick(FPS)

    for i in range(len(array)):
        array[i] = output[i]
        drawArray(array, [i])
        CLOCK.tick(FPS)

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
                CLOCK.tick(FPS)
                j -= gap
            
            array[j] = temp
            drawArray(array, [j])
            CLOCK.tick(FPS)

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
        CLOCK.tick(FPS)

def bucketSort(array, drawArray=None, CLOCK=None):
    numBuckets = len(array)
    minValue, maxValue = min(array), max(array)
    if minValue == maxValue:
        return array

    buckets = [[] for _ in range(numBuckets)]

    for num in array:
        indexB = int((num - minValue) / (maxValue - minValue) * (numBuckets - 1))
        buckets[indexB].append(num)

    for i in range(numBuckets):
        buckets[i] = insertionSort(buckets[i])

    k = 0
    for b in buckets:
        for num in b:
            array[k] = num
            if drawArray and CLOCK:
                drawArray(array, [k])
                CLOCK.tick(FPS)
            k += 1

    return array

def countingSort(array):
    maxVal = max(array)
    countArray = [0] * (maxVal + 1)

    for num in array:
        countArray[num] += 1
        drawArray(array, [num])
        CLOCK.tick(FPS)
    
    for i in range(1, maxVal + 1):
        countArray[i] += countArray[i - 1]

    outputArray = [0] * len(array)

    for i in range(len(array) - 1, -1, -1):
        outputArray[countArray[array[i]] - 1] = array[i]
        countArray[array[i]] -= 1
        drawArray(outputArray, [i])
        CLOCK.tick(FPS)
    
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
                CLOCK.tick(FPS)
                swapped = True

        if (swapped == False):
            break
            
        swapped = False
        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                drawArray(array, [i, i + 1])
                CLOCK.tick(FPS)
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
                CLOCK.tick(FPS)
                swapped = True

def gnomeSort(array):
    index = 0
    while index < len(array):
        if index == 0 or array[index-1] <= array[index]:
            index += 1
        else:
            array[index], array[index-1] = array[index-1], array[index]
            drawArray(array, [index, index-1])
            CLOCK.tick(FPS)
            index -= 1

def pancakeFlip(array, k):
    start = 0
    while start < k:
        array[start], array[k] = array[k], array[start]
        drawArray(array, [start, k])
        CLOCK.tick(FPS)
        start += 1
        k -= 1

def pancakeSort(array):
    n = len(array)
    while n > 1:
        mi = array.index(max(array[0:n]))
        pancakeFlip(array, mi)
        pancakeFlip(array, n-1)
        n -= 1

def stoogeSort(array, l=0, h=None):
    if h is None:
        h = len(array) - 1
    if l >= h:
        return
    
    if array[l] > array[h]:
        array[l], array[h] = array[h], array[l]
        drawArray(array, [l, h])
        CLOCK.tick(FPS)
        
    if h-l+1 > 2:
        t = (h-l+1) // 3
        stoogeSort(array, l, h-t)
        stoogeSort(array, l+t, h)
        stoogeSort(array, l, h-t)

def cycleSort(array):
    writes = 0

    for cycleStart in range(0, len(array) - 1):
        item = array[cycleStart]

        position = cycleStart
        for i in range(cycleStart + 1, len(array)):
            if array[i] < item:
                position += 1

        if position == cycleStart:
            continue

        while item == array[position]:
            position += 1
        array[position], item = item, array[position]
        writes += 1
        drawArray(array, [cycleStart, position])
        CLOCK.tick(FPS)

        while position != cycleStart:
            position = cycleStart
            for i in range(cycleStart + 1, len(array)):
                if array[i] < item:
                    position += 1
            while item == array[position]:
                position += 1
            array[position], item = item, array[position]
            writes += 1
            drawArray(array, [cycleStart, position])
            CLOCK.tick(FPS)

    return writes

def spaghettiSort(array):
    maxVal = max(array)
    counters = [0] * (maxVal + 1)

    for num in array:
        counters[num] += 1

    i = 0
    for value, count in enumerate(counters):
        for _ in range(count):
            array[i] = value
            drawArray(array, [i])
            CLOCK.tick(FPS)
            i += 1

def bitonicSort(arr, up=True):
    n = len(arr)
    if n <= 1:
        return arr
    else:
        firstHalf = bitonicSort(arr[:n // 2], True)
        secondHalf = bitonicSort(arr[n // 2:], False)
        return bitonicMerge(firstHalf + secondHalf, up)

def bitonicMerge(arr, up):
    n = len(arr)
    if n == 1:
        return arr
    else:
        bitonicCompare(arr, up)
        firstHalf = bitonicMerge(arr[:n // 2], up)
        secondHalf = bitonicMerge(arr[n // 2:], up)
        return firstHalf + secondHalf

def bitonicCompare(arr, up):
    dist = len(arr) // 2
    for i in range(dist):
        if (arr[i] > arr[i + dist]) == up:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]
            drawArray(arr, [i, i + dist])  # Visualization
            CLOCK.tick(FPS)

def bitonicSortWrapper(arr):
    n = len(arr)
    nextPower = 1 << (n - 1).bit_length()
    
    paddingNeeded = nextPower - n
    if paddingNeeded:
        arr += [float('inf')] * paddingNeeded
    
    sortedArray = bitonicSort(arr)
    return sortedArray[:n]

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
    {"label": "Gnome Sort", "function": gnomeSort},
    {"label": "Pancake Sort", "function": pancakeSort},
    {"label": "Stooge Sort", "function": stoogeSort},
    {"label": "Cycle Sort", "function": cycleSort},
    {"label": "Spaghetti Sort", "function": spaghettiSort},
    {"label": "Bitonic Sort", "function": bitonicSortWrapper}
]

BUTTONS.append({"label": "Restart", "function": "RESTART"})

FONT = pygame.font.SysFont("Arial", 20)
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 20

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
                sortingAlgorithm = handleButtonClick(pygame.mouse.get_pos())
                if sortingAlgorithm:
                    sortingAlgorithm(array)

    pygame.quit()

if __name__ == "__main__":
    main()
