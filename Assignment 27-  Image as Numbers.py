"""
Assignment 27: Image as Numbers
Date: 06/04/2026
"""

# -----------------------------
# 📦 Imports (safe check)
# -----------------------------
try:
    import numpy as np
    from PIL import Image, ImageDraw
except ImportError:
    print("❌ Required libraries not installed.")
    print("👉 Run: python -m pip install numpy pillow")
    exit()

# -----------------------------
# 🎨 Create Synthetic Image
# -----------------------------
img = Image.new("RGB", (100, 100), color=(135, 206, 235))  # sky blue
draw = ImageDraw.Draw(img)

draw.ellipse([10, 10, 40, 40], fill=(255, 220, 0))   # sun
draw.rectangle([0, 75, 100, 100], fill=(34, 139, 34)) # ground
draw.rectangle([35, 50, 65, 75], fill=(180, 50, 50))  # house
draw.rectangle([45, 60, 55, 75], fill=(101, 67, 33))  # door
draw.ellipse([60, 15, 85, 30], fill=(255, 255, 255))  # cloud

img.save("sample_image.png")

# -----------------------------
# 🔢 Convert to NumPy Array
# -----------------------------
arr = np.array(img)

# -----------------------------
# 📊 Image Info
# -----------------------------
print("\n=== IMAGE SHAPE ===")
h, w, c = arr.shape
print(f"Shape: {arr.shape}")
print(f"Height: {h}px | Width: {w}px | Channels: {c}")
print(f"dtype: {arr.dtype} | Total pixels: {h*w:,}")

# -----------------------------
# 🔍 Pixel Values (5x5)
# -----------------------------
print("\n=== PIXEL VALUES (Top-left 5x5) ===")
for row in range(5):
    row_data = " ".join(f"[{r:3},{g:3},{b:3}]" for r, g, b in arr[row, :5])
    print(row_data)

# -----------------------------
# 🎯 Single Pixel
# -----------------------------
print("\n=== SINGLE PIXEL (20,20) ===")
r, g, b = arr[20, 20]
print(f"R={r}  G={g}  B={b}  HEX=#{r:02X}{g:02X}{b:02X}")

# -----------------------------
# 📊 Channel Statistics
# -----------------------------
print("\n=== CHANNEL STATISTICS ===")
channels = {
    "Red": arr[:, :, 0],
    "Green": arr[:, :, 1],
    "Blue": arr[:, :, 2]
}

for name, ch in channels.items():
    print(f"{name:<6}: min={ch.min()} max={ch.max()} "
          f"mean={ch.mean():.2f} std={ch.std():.2f}")

# -----------------------------
# 🌗 Grayscale Brightness
# -----------------------------
print("\n=== GRAYSCALE BRIGHTNESS ===")
gray = 0.299*arr[:,:,0] + 0.587*arr[:,:,1] + 0.114*arr[:,:,2]
avg = gray.mean()
pct = avg / 255 * 100

print("Formula: Y = 0.299R + 0.587G + 0.114B")
print(f"Avg brightness: {avg:.2f}/255 = {pct:.1f}%")

# Better bar visualization
bars = int(pct // 5)
print("Bar: [" + "█"*bars + " "*(20-bars) + "]")

# -----------------------------
# 🔎 Array Slice
# -----------------------------
print("\n=== RAW ARRAY SLICE arr[0:3, 0:3] ===")
print(arr[0:3, 0:3])