import qrcode
import json
import os

materials = ["brick", "cement", "wood", "glass", "pvc_pipe", "steel_rods"]
base_url = "https://my-brick-app.vercel.app/brick.html?type="

os.makedirs("qr_codes", exist_ok=True)

for material in materials:
    url = f"{base_url}{material}"
    qr = qrcode.make(url)
    qr.save(f"qr_codes/{material}.png")
    print(f"✅ QR generated for {material}: {url}")
