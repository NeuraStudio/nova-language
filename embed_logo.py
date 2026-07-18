import base64
import os
import glob

# 1. सबसे पहले neura-logo.png को ढूँढें
logo_path = 'neura-logo.png'

# अगर neura-logo.png नहीं है, तो 6639 वाली कोई भी फाइल ढूँढें
if not os.path.exists(logo_path):
    possible_files = glob.glob('6639*.png')
    if possible_files:
        logo_path = possible_files[0]
        print(f"Using found logo: {logo_path}")
    else:
        print("ERROR: Logo file not found. Please ensure 'neura-logo.png' is in the Nova folder.")
        exit(1)

# 2. इमेज को Base64 कोड में कन्वर्ट करें
with open(logo_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

base64_data_uri = f"data:image/png;base64,{encoded_string}"

# 3. HTML फाइलों में लिंक को Base64 कोड से बदलें
html_files = ['index.html', 'installer.html', 'hub.html']

for file_name in html_files:
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        
        # पुराने लिंक्स को नए Base64 कोड से बदल दें (Exact match के लिए)
        content = content.replace('https://raw.githubusercontent.com/Neurastudio/nova-language/main/neura-logo.png', base64_data_uri)
        content = content.replace('neura-logo.png', base64_data_uri)
        content = content.replace('neura-logo.svg', base64_data_uri) # just in case

        with open(file_name, 'w') as file:
            file.write(content)
        print(f"Successfully embedded exact logo into {file_name}")

print("\nDONE! Your exact logo is now permanently pasted INSIDE the code.")
