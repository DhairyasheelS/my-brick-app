import qrcode
import os
from PIL import Image, ImageDraw, ImageFont

materials = ["brick", "cement", "wood", "glass", "pvc_pipe", "iron_rods"]
base_url = "https://my-brick-app.vercel.app/brick.html?type="

os.makedirs("qr_codes", exist_ok=True)

# Load font (use system default if Arial is unavailable)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except:
    font = ImageFont.load_default()

for material in materials:
    url = f"{base_url}{material}"
    
    # Generate QR code and convert to RGB
    qr_img = qrcode.make(url).convert("RGB")

    # Create label
    label_text = material.replace("_", " ").title()
    draw = ImageDraw.Draw(qr_img)
    bbox = draw.textbbox((0, 0), label_text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # Create new image with space for label
    new_img = Image.new("RGB", (qr_img.width, qr_img.height + text_height + 10), "white")
    new_img.paste(qr_img, (0, 0))

    # Draw label text centered
    draw = ImageDraw.Draw(new_img)
    text_position = ((qr_img.width - text_width) // 2, qr_img.height + 5)
    draw.text(text_position, label_text, fill="black", font=font)

    # Save the labeled QR image
    new_img.save(f"qr_codes/{material}.png")
    print(f"✅ QR generated for {material}: {url}")
