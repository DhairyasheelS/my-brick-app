import qrcode
import json
import os

# Path to your bricks.json file
with open("../data/bricks.json", "r") as f:
    data = json.load(f)

# Your working deployed URL format
base_url = "https://my-brick-app.vercel.app/brick.html?id="

# Folder to store QR codes
os.makedirs("qr_codes", exist_ok=True)

# Generate QR code for each brick
for brick_id in data:
    full_url = f"{base_url}{brick_id}"  # Append ID directly in query param
    img = qrcode.make(full_url)
    img.save(f"qr_codes/brick_{brick_id}.png")
    print(f"✅ QR for Brick {brick_id} → {full_url}")

print("🎉 All QR codes generated and saved in 'qr_codes/' folder.")
