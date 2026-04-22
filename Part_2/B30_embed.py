import cv2

from imwatermark import WatermarkEncoder



# Load your AI-generated image

bgr = cv2.imread('B30_Base.png')



# Create encoder and set our secret watermark (UWA2026 is 7 bytes)

encoder = WatermarkEncoder()

encoder.set_watermark('bytes', b'Richie_B30')



# Encode using DWT-DCT (this makes it survive editing)

bgr_encoded = encoder.encode(bgr, 'dwtDct')



# Save the watermarked image

cv2.imwrite('B30_Watermarked.png', bgr_encoded)

print("Invisible watermark 'Richie_B30' successfully embedded!")
