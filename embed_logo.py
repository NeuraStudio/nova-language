import base64
import os
import glob

# public फोल्डर या मुख्य फोल्डर में png ढूँढें
files = glob.glob('public/*.png') + glob.glob('*.png')
logo_path = None

for f in files:
    # कोई भी png फाइल जिसे आपने डाला है
    logo_path = f
    break

if logo_path:
    print(f"✅ Logo found at: {logo_path}")
    with open(logo_path, "rb") as img:
        b64 = base64.b64encode(img.read()).decode('utf-8')
        data_uri = f"data:image/png;base64,{b64}"
    
    with open("index.html", "r") as html_file:
        content = html_file.read()
        
    # कोड के अंदर लोगो को परमानेंट पेस्ट कर दें
    content = content.replace("LOGO_BASE64_PLACEHOLDER", data_uri)
    
    with open("index.html", "w") as html_file:
        html_file.write(content)
    print("✅ Success! Logo has been permanently embedded inside index.html")
else:
    print("❌ Error: No PNG image found in public/ or current folder.")
