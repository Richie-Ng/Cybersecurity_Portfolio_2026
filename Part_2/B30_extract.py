import cv2
from imwatermark import WatermarkDecoder

# Load the EDITED image
bgr = cv2.imread('B30_Edited.png')

# We expect a 7-byte payload ('UWA2026' = 7 characters * 8 bits = 56)
decoder = WatermarkDecoder('bytes', 80)

# Extract the watermark
watermark = decoder.decode(bgr, 'dwtDct')

print("Extracted Watermark from Edited Image:", watermark.decode('utf-8'))
