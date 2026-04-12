"""
Assignment 28: Image Filter Lab – OpenCV 
Date: 08/04/2026
"""


import cv2
import numpy as np
from PIL import Image, ImageDraw

# Create sample image
img = Image.new("RGB", (200, 200), color=(135, 206, 235))
draw = ImageDraw.Draw(img)

draw.ellipse([20, 20, 70, 70], fill=(255, 220, 0))      # sun
draw.rectangle([0, 150, 200, 200], fill=(34, 139, 34))  # ground
draw.rectangle([70, 100, 130, 150], fill=(180, 50, 50)) # house
draw.rectangle([90, 120, 110, 150], fill=(101, 67, 33)) # door
draw.polygon([(55, 100), (100, 60), (145, 100)], fill=(139, 90, 43)) # roof
draw.ellipse([140, 30, 180, 55], fill=(255, 255, 255))  # cloud

img.save("filter_input.png")

# Read image using OpenCV
original = cv2.imread("filter_input.png")

# -----------------------------
# Filter 1: Grayscale
# -----------------------------
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)

print(f"[GRAYSCALE]  Before: {original.shape} → After: {gray.shape}")
print(f"  Pixel[50,50] before: {tuple(original[50,50][::-1])} → after: {gray[50,50]}")
print(f"  Mean: {gray.mean():.2f}  Std: {gray.std():.2f}")

cv2.imwrite("filter_gray.png", gray)

# -----------------------------
# Filter 2: Gaussian Blur
# -----------------------------
blurred = cv2.GaussianBlur(gray, (15, 15), 0)

lap_before = cv2.Laplacian(gray, cv2.CV_64F).var()
lap_after  = cv2.Laplacian(blurred, cv2.CV_64F).var()

print(f"\n[GAUSSIAN BLUR]  Kernel: 15x15")
print(f"  Sharpness (Laplacian var): {lap_before:.1f} → {lap_after:.1f} (lower = blurrier)")
print(f"  Pixel[50,50]: {gray[50,50]} → {blurred[50,50]}")

cv2.imwrite("filter_blur.png", blurred)

# -----------------------------
# Filter 3: Canny Edge Detection
# -----------------------------
edges = cv2.Canny(blurred, 50, 150)

edge_count = np.count_nonzero(edges)
total_px = edges.shape[0] * edges.shape[1]

print(f"\n[CANNY EDGES]  Thresholds: 50 / 150")
print(f"  Image size  : {edges.shape[1]} x {edges.shape[0]} = {total_px:,} px")
print(f"  Edge pixels : {edge_count} ({edge_count/total_px*100:.1f}%)")
print(f"  Non-edge    : {total_px-edge_count} ({(total_px-edge_count)/total_px*100:.1f}%)")

cv2.imwrite("filter_edges.png", edges)

# -----------------------------
# Filter 4: Adaptive Threshold
# -----------------------------
thresh = cv2.adaptiveThreshold(
    gray,
    255,
    cv2.ADAPTIVE_THRESH_MEAN_C,
    cv2.THRESH_BINARY,
    11,
    2
)

white = np.count_nonzero(thresh == 255)

print(f"\n[ADAPTIVE THRESHOLD]")
print(f"  White px: {white:,} ({white/total_px*100:.1f}%)")
print(f"  Black px: {total_px-white:,} ({(total_px-white)/total_px*100:.1f}%)")

cv2.imwrite("filter_thresh.png", thresh)

# -----------------------------
# Pipeline Summary
# -----------------------------
print("\n[PIPELINE SUMMARY]")

for name, arr in [
    ("Original", original),
    ("Gray", gray),
    ("Blurred", blurred),
    ("Edges", edges),
    ("Thresh", thresh)
]:
    print(f"  {name:<12}: shape={arr.shape}  px[50,50]={arr[50,50]}")