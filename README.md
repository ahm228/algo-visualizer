The Sorting Algorithm Visualizer is a project built using the pygame library that visually showcases the working of various sorting algorithms on a randomly generated array. The array elements are represented as bars, and the height of each bar corresponds to the value of the array element.
Features

    Visual representation of sorting algorithms.
    Multiple sorting algorithms included:
        Bubble Sort
        Insertion Sort
        Selection Sort
        Merge Sort
        Quick Sort
        Heap Sort
        Radix Sort
        Shell Sort
        Bogo Sort
    Restart functionality to regenerate the array.
    Buttons for each sorting algorithm for easy interaction.

Getting Started
Prerequisites

    Ensure you have Python installed.
    Install pygame library using pip:
    pip install pygame

Running the Visualizer

    Clone/download the repository.
    Navigate to the directory containing the script.
    Run the script:
    python algovisualizer.py

Using the Visualizer

    Upon starting, the visualizer will display a randomly generated array as bars.
    Next to the visual representation, there are buttons corresponding to each sorting algorithm.
    Click on any sorting algorithm button to start the visualization of that sorting algorithm.
    Click the "Restart" button to regenerate the array.

Implementation Details

    pygame is used for the graphical representation and interactivity.
    Array bars are colored differently during swapping operations for better visualization.
    Delay is added between operations for visualization clarity.
    Functions for each sorting algorithm are defined, and their working is visualized using the drawArray function.
    A set of buttons is provided at the bottom for user interaction.