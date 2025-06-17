Sulafa Yahya 
B2180.060101

General Overview
----------------
This Python program performs various image processing tasks using OpenCV, NumPy, Matplotlib, and SciPy libraries.
The tasks are divided into six problems, each addressing a different image manipulation or enhancement technique.
All required images must be placed inside a folder named 'images'.

Libraries Used
--------------
- OpenCV (cv2): For reading and processing images.
- NumPy: For numerical operations on arrays.
- Matplotlib: For displaying images and histograms.
- SciPy (fftpack): For frequency domain transformations.
- os: To handle file paths.
- random: To generate random pixel coordinates.

Utility Functions
-----------------
1. show_image(title, image, cmap=None, pause=3):
   - Displays an image with a title using Matplotlib.
   - Automatically closes after a few seconds.
   - Supports grayscale and color images.

2. get_image_path(filename):
   - Returns the full path to the image inside the 'images' folder.

Problem Breakdown
-----------------

Problem 1: Patch Manipulation
- Loads 'tf2_engineer.jpg'.
- Prints center coordinates and color values.
- Draws a yellow-colored patch at the center.
- Shows modified image with the patch.

Problem 2: Image Negatives
- Loads 'einstein.tif' in grayscale.
- Calculates negative by subtracting pixel values from 255.
- Shows original and negative images.
- Prints 5 random pixel comparisons between original and negative.

Problem 3: Log Transform & Inverse
- Loads 'pout .tif'.
- Applies log transformation to enhance darker regions.
- Applies inverse log and restoration to observe quality.
- Displays the results step by step.

Problem 4: Unsharp Masking
- Loads 'moon.tif'.
- Applies spatial unsharp masking using Gaussian blur.
- Applies frequency domain unsharp masking using FFT.
- Compares different sharpness levels (k=0.2, 0.5, 1.0).

Problem 5: Noise Reduction
- Loads 'pcb.tif'.
- Displays histogram to analyze noise.
- Applies a 3x3 median filter to remove salt-and-pepper noise.
- Compares number of noisy pixels before and after.

Problem 6: Histogram Equalization
- Loads 'pollen.tif'.
- Displays original histogram and image.
- Applies two contrast enhancement techniques:
  a) Histogram Equalization
  b) CLAHE (adaptive local contrast enhancement)
- Shows enhanced images and explains the difference.

Main Execution
--------------
- Checks if the 'images' folder exists.
- Runs all six problems in sequence.
- Waits for user input between each problem (when not using Jupyter).
- Displays outputs for user analysis.

Required Image Files
--------------------
Ensure these files are in a folder named 'images':
- tf2_engineer.jpg
- einstein.tif
- pout .tif (with space!)
- moon.tif
- pcb.tif
- pollen.tif
