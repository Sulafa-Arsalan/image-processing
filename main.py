import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import os
from scipy import fftpack


def show_image(title, image, cmap=None, pause=3):
    """Display image in non-blocking way for screenshots"""
    plt.figure(figsize=(8, 6))
    if cmap:
        plt.imshow(image, cmap=cmap)
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show(block=False)
    plt.pause(pause)
    plt.close()

def get_image_path(filename):
    return os.path.join('images', filename)

# =============================================
# Problem 1
# =============================================
def problem1():
    print("\n=== PROBLEM 1 SOLUTION ===")
    img_path = get_image_path('tf2_engineer.jpg')
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error loading {img_path}")
        return
    show_image("1. Original Image", img)
    height, width = img.shape[:2]
    yc, xc = height // 2, width // 2
    print(f"2. Center coordinates (y,x): ({yc}, {xc})")
    print(f"   Center intensity (BGR): {img[yc, xc]}")
    patch_color = (0xA8, 0x9E, 0x32)
    patch_height, patch_width = 30, 40
    start_point = (xc - patch_width // 2, yc - patch_height // 2)
    end_point = (xc + patch_width // 2, yc + patch_height // 2)
    img_patched = img.copy()
    cv2.rectangle(img_patched, start_point, end_point, patch_color, -1)
    print(f"4. Patch center intensity: {img_patched[yc, xc]}")
    show_image("5. Image with Color Patch", img_patched)

problem1()