import base64
import os
import glob

print("🚀 Starting Bulletproof Nova Website Build...")

# 1. AUTO-DETECT LOGO (Crash-proof & Name-proof)
logo_b64 = "https://cdn-icons-png.flaticon.com/512/3233/3233508.png" # Fallback

# यह आपके फोल्डर में मौजूद किसी भी .png फाइल को ढूंढ लेगा (चाहे उसका नाम कुछ भी हो)
png_files = glob.glob('website/public/*.png') + glob.glob('*.png')

if png_files:
    target_logo = png_files[0] # पहली PNG फाइल को उठा लेगा
    with open(target_logo, "rb") as img:
        b64_str = base64.b64encode(img.read()).decode('utf-8')
        logo_b64 = "data:image/png;base64," + b64_str
        print(f"✅ SUCCESS: Automatically found and converted your logo -> {target_logo}")
else:
    print("❌ ERROR: No .png files found at all in website/public/. Please upload the logo.")

# ==========================================
# 2. INDEX.HTML (White Theme + Speed Comparison)
# ==========================================
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Neura Studio | Nova</title>
    <style>
        body { background-color: #ffffff; color: #111; font-family: -apple-system, sans-serif; margin: 0; overflow-x: hidden; }
        .nav { display: flex; justify-content: space-between; align-items: center; padding: 15px 50px; background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.05); position: sticky; top: 0; z-index: 100;}
        .nav-logo { display: flex; align-items: center; font-weight: 900; font-size: 22px; color: #111; text-decoration: none;}
        .premium-logo { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #00CFFF; object-fit: cover; margin-right: 12px; }
        .nav-links { display: flex; gap: 20px; align-items: center;}
        .nav-links a { text-decoration: none; color: #555; font-weight: 600; font-size: 15px;}
        .nav-links a:hover { color: #00CFFF; }
        .btn { background: #00CFFF; color: #fff; padding: 10px 24px; border-radius: 30px; text-decoration: none; font-weight: bold;}
        
        .hero { text-align: center; padding: 60px 20px 20px; }
        .hero h1 { font-size: 4.5em; font-weight: 900; letter-spacing: -2px; margin-bottom: 20px; color: #111;}
        .image-row { display: flex; justify-content: center; gap: 20px; max-width: 1000px; margin: 40px auto; align-items: center;}
        .image-row img { border-radius: 12px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); object-fit: cover;}
        
        .speed-section { background: #fff; max-width: 900px; margin: 50px auto; padding: 40px 50px; border-radius: 16px; box-shadow: 0 5px 20px rgba(0,0,0,0.05); border: 1px solid #eaeaea;}
        .speed-section h2 { text-align: center; font-size: 1.8em; margin-bottom: 40px; font-weight: 900;}
        .bar-container { margin-bottom: 25px; }
        .bar-label { display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 8px; font-size: 14px;}
        .bar-bg { background: #eaebed; border-radius: 10px; height: 10px; width: 100%; overflow: hidden;}
        .bar-fill { height: 100%; border-radius: 10px; }
    </style>
</head>
<body>
    <div class="nav">
        <a href="index.html" class="nav-logo"><img src="LOGO_PLACEHOLDER" class="premium-logo"> NEURA STUDIO</a>
        <div class="nav-links">
            <a href="index.html" style="color:#00CFFF;">Overview</a>
            <a href="hub.html">Nova Hub</a>
            <a href="nova_console.html">Nova Console</a> 
        </div>
        <a href="installer.html" class="btn">Get Nova</a>
    </div>
    
    <div class="hero">
        <h1>Code at the speed of thought.</h1>
        <div class="image-row">
            <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=300&q=80" style="width:300px; height:200px;">
            <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=400&q=80" style="width:400px; height:250px; transform:scale(1.05); z-index:10;">
            <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=300&q=80" style="width:300px; height:200px;">
        </div>
    </div>

    <!-- COMPARISON AS IN YOUR IMAGE -->
    <div class="speed-section">
        <h2>Unrivaled Execution Speed</h2>
        <div class="bar-container"><div class="bar-label"><span>Nova (Native Bytecode)</span><span style="color:#00CFFF">0.01ms</span></div><div class="bar-bg"><div class="bar-fill" style="width: 100%; background: #00CFFF;"></div></div></div>
        <div class="bar-container"><div class="bar-label"><span>Mojo</span><span style="color:#ff8a00">0.02ms</span></div><div class="bar-bg"><div class="bar-fill" style="width: 80%; background: #ff8a00;"></div></div></div>
        <div class="bar-container"><div class="bar-label"><span>C++ (GCC 03)</span><span style="color:#64748b">0.05ms</span></div><div class="bar-bg"><div class="bar-fill" style="width: 50%; background: #64748b;"></div></div></div>
        <div class="bar-container"><div class="bar-label"><span>Python 3.11</span><span style="color:#ef4444">5.20ms</span></div><div class="bar-bg"><div class="bar-fill" style="width: 10%; background: #ef4444;"></div></div></div>
    </div>
</body>
</html>"""
index_html = index_html.replace("LOGO_PLACEHOLDER", logo_b64)

# ==========================================
# 3. HUB.HTML (LIVE INTERNET SEARCH ENGINE)
# ==========================================
hub_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nova Hub</title>
    <style>
        body { background-color: #ffffff; color: #111; font-family: -apple-system, sans-serif; margin: 0; }
        .nav { display: flex; justify-content: space-between; align-items: center; padding: 15px 50px; background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .nav-logo { display: flex; align-items: center; font-weight: 900; font-size: 22px; color: #111; text-decoration: none;}
        .premium-logo { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #00CFFF; object-fit: cover; margin-right: 12px; }
        .nav-links a { margin: 0 15px; text-decoration: none; color: #555; font-weight: 600;}
        
        .hub-header { text-align: center; padding: 50px 20px 20px; }
        .search-bar { max-width: 600px; margin: 0 auto 50px; display: flex; border: 2px solid #00CFFF; border-radius: 30px; overflow: hidden;}
        .search-bar input { flex: 1; padding: 15px 20px; border: none; outline: none; font-size: 16px; }
        .search-bar button { background: #00CFFF; color: white; border: none; padding: 15px 30px; font-weight: bold; cursor: pointer;}
        
        .grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; max-width: 1000px; margin: 0 auto 50px; padding: 0 20px;}
        .card { background: #fff; border-radius: 12px; padding: 25px 20px; text-align: center; border: 1px solid #eaeaea; transition: 0.3s;}
        .card:hover { border-color:#00CFFF; box-shadow: 0 10px 25px rgba(0,207,255,0.1);}
        .card img { height: 50px; margin-bottom: 15px;}
        .code-box { background: #0f172a; color: #38bdf8; padding: 10px; border-radius: 6px; font-family: monospace; font-size: 13px;}
    </style>
</head>
<body>
    <div class="nav">
        <a href="index.html" class="nav-logo"><img src="LOGO_PLACEHOLDER" class="premium-logo"> NEURA STUDIO</a>
        <div class="nav-links"><a href="index.html">Overview</a><a href="hub.html" style="color:#00CFFF;">Nova Hub</a><a href="nova_console.html">Nova Console</a></div>
    </div>

    <div class="hub-header">
        <h1 style="font-size:3em; margin-bottom:5px;">Nova Hub 🌍</h1>
        <p style="color:#666;">Connected to Global Registry. Searching 12M+ Packages Live.</p>
    </div>
    
    <div class="search-bar">
        <input type="text" id="searchInput" placeholder="Search internet for any package...">
        <button onclick="searchLiveInternet()">Search Global</button>
    </div>

    <div class="grid" id="packageGrid">
        <div class="card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"><h3>python:tensorflow</h3><div class="code-box">Nova.import("python:tensorflow")</div></div>
        <div class="card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"><h3>js:react</h3><div class="code-box">Nova.import("js:react")</div></div>
        <div class="card"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg"><h3>java:spring</h3><div class="code-box">Nova.import("java:spring")</div></div>
    </div>
    
    <div class="grid" id="dynamicGrid"></div>

    <script>
        async function searchLiveInternet() {
            let query = document.getElementById('searchInput').value.trim();
            let defaultGrid = document.getElementById('packageGrid');
            let dynamicGrid = document.getElementById('dynamicGrid');
            
            if(query.length < 2) {
                defaultGrid.style.display = 'grid';
                dynamicGrid.innerHTML = '';
                return;
            }
            
            defaultGrid.style.display = 'none';
            dynamicGrid.innerHTML = '<h3 style="grid-column: 1/-1; text-align:center;">Fetching live data from internet... ⏳</h3>';
            
            try {
                let response = await fetch('https://registry.npmjs.org/-/v1/search?text=' + query + '&size=15');
                let data = await response.json();
                
                dynamicGrid.innerHTML = '';
                data.objects.forEach(item => {
                    let name = item.package.name;
                    let desc = item.package.description || "Official Nova Package";
                    dynamicGrid.innerHTML += `
                    <div class="card">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg">
                        <h3>nova:${name}</h3>
                        <p style="font-size:11px; color:#888; height:30px; overflow:hidden;">${desc}</p>
                        <div class="code-box">Nova.import("nova:${name}")</div>
                    </div>`;
                });
                if(data.objects.length === 0) dynamicGrid.innerHTML = '<h3 style="grid-column: 1/-1; text-align:center;">No package found on internet.</h3>';
            } catch(e) {
                dynamicGrid.innerHTML = '<h3 style="grid-column: 1/-1; text-align:center; color:red;">Network Error. Check internet connection.</h3>';
            }
        }
    </script>
</body>
</html>"""
hub_html = hub_html.replace("LOGO_PLACEHOLDER", logo_b64)

# ==========================================
# 4. INSTALLER.HTML (Mojo Style with VS Code support)
# ==========================================
installer_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Get Nova</title>
    <style>
        body { background: #f8f9fa; font-family: -apple-system, sans-serif; margin: 0; color: #111;}
        .nav { display: flex; align-items: center; padding: 15px 50px; background: #fff; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .nav-logo { display: flex; align-items: center; font-weight: 900; font-size: 22px; color: #111; text-decoration: none;}
        .premium-logo { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #00CFFF; object-fit: cover; margin-right: 12px; }

        .container { max-width: 900px; margin: 60px auto; background: #fff; padding: 50px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); text-align: center; border: 1px solid #eee;}
        .grid { display: flex; justify-content: center; gap: 30px; margin-top: 30px;}
        .method-card { border: 2px solid #eaebed; padding: 40px 30px; border-radius: 20px; cursor: pointer; width: 250px; transition: 0.3s; background: #fff;}
        .method-card:hover { border-color: #00CFFF; transform: translateY(-5px); box-shadow: 0 15px 30px rgba(0,207,255,0.15); }
        .method-card img { height: 70px; margin-bottom: 20px; }
        
        .os-card { border: 2px solid #eaebed; padding: 25px 20px; border-radius: 16px; cursor: pointer; width: 140px; transition: 0.3s; background: #fff; color: #111;}
        .os-card:hover { border-color: #00CFFF; transform: translateY(-5px); box-shadow: 0 10px 20px rgba(0,0,0,0.05); }
        .os-card img { height: 55px; margin-bottom: 15px; object-fit: contain; }

        .step { display: none; }
        .step.active { display: block; }
        .cmd-box { background: #000; color: #0f0; padding: 25px; border-radius: 12px; font-family: monospace; font-size: 18px; margin-top: 30px; text-align: left;}
        .back-btn { background: none; border: none; color: #888; font-weight: bold; cursor: pointer; text-align: left; width: 100%; margin-bottom: 20px;}
    </style>
</head>
<body>
    <div class="nav"><a href="index.html" class="nav-logo"><img src="LOGO_PLACEHOLDER" class="premium-logo"> NEURA STUDIO</a></div>

    <div class="container">
        <div id="step-method" class="step active">
            <h1>Install Nova</h1>
            <div class="grid">
                <div class="method-card" onclick="startFlow('gui')">
                    <img src="https://cdn-icons-png.flaticon.com/512/3233/3233508.png">
                    <h3>Visual Installer</h3><p style="color:#888;">Standard GUI download.</p>
                </div>
                <div class="method-card" onclick="startFlow('cli')" style="background:#0d1117; color:#fff; border-color:#333;">
                    <h1 style="color:#27c93f;">>_</h1>
                    <h3>Mojo-Style Terminal</h3><p style="color:#8b949e;">Command Line Setup.</p>
                </div>
            </div>
        </div>

        <div id="step-os" class="step">
            <button class="back-btn" onclick="goBack('step-method')">⬅ Back</button>
            <h1>Select OS</h1>
            <div class="grid">
                <div class="os-card" onclick="selectOS('mac')"><img src="https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg"><h3>macOS</h3></div>
                <div class="os-card" onclick="selectOS('win')"><img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Windows_logo_-_2012.svg"><h3>Windows</h3></div>
                <div class="os-card" onclick="selectOS('linux')"><img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg"><h3>Linux</h3></div>
            </div>
        </div>

        <div id="step-ide" class="step">
            <button class="back-btn" onclick="goBack('step-os')">⬅ Back</button>
            <h1>Select IDE Integration</h1>
            <div class="grid">
                <div class="os-card" onclick="selectIDE('vscode')"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg"><h3>VS Code</h3></div>
                <div class="os-card" onclick="selectIDE('pycharm')"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pycharm/pycharm-original.svg"><h3>PyCharm</h3></div>
                <div class="os-card" onclick="selectIDE('terminal')"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg"><h3>Terminal Only</h3></div>
            </div>
        </div>

        <div id="step-result" class="step">
            <button class="back-btn" onclick="goBack('step-ide')">⬅ Back</button>
            <h1>Run this command</h1>
            <div class="cmd-box" id="cli-command"></div>
        </div>
    </div>

    <script>
        let curMethod = ''; let curOS = ''; 
        function hideAll() { document.querySelectorAll('.step').forEach(e => e.classList.remove('active')); }
        function goBack(id) { hideAll(); document.getElementById(id).classList.add('active'); }
        
        function startFlow(method) { curMethod = method; hideAll(); document.getElementById('step-os').classList.add('active'); }
        function selectOS(os) { curOS = os; hideAll(); document.getElementById('step-ide').classList.add('active'); }
        
        function selectIDE(ide) {
            hideAll();
            if(curMethod === 'gui') {
                let ext = (curOS === 'win') ? '.exe' : (curOS === 'mac' ? '.dmg' : '.sh');
                let a = document.createElement('a');
                a.href = "data:text/plain;charset=utf-8,Downloading...";
                a.download = "nova-" + ide + "-installer" + ext;
                a.click();
                setTimeout(() => window.location.href = 'index.html', 1000);
            } else {
                document.getElementById('step-result').classList.add('active');
                let cmd = "";
                if(curOS === 'mac') cmd = "curl -sL https://ncs.neurastudio.com/mac/" + ide + " | bash";
                if(curOS === 'linux') cmd = "curl -sL https://ncs.neurastudio.com/linux/" + ide + " | bash";
                if(curOS === 'win') cmd = "irm https://ncs.neurastudio.com/win/" + ide + " | iex";
                document.getElementById('cli-command').innerText = cmd;
            }
        }
    </script>
</body>
</html>"""
installer_html = installer_html.replace("LOGO_PLACEHOLDER", logo_b64)

# ==========================================
# 5. CONSOLE.HTML (Hacker Style Premium CMD)
# ==========================================
console_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nova Console</title>
    <style>
        body { background-color: #050505; color: #fff; font-family: 'Courier New', monospace; margin: 0; padding: 0;}
        .header { display: flex; justify-content: space-between; align-items: center; padding: 20px 40px; background: #111; border-bottom: 2px solid #333;}
        .premium-logo { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #0f0; object-fit: cover; margin-right: 15px;}
        .header h1 { margin: 0; color: #0f0; font-size: 24px; text-shadow: 0 0 10px #0f0;}
        
        .main-area { padding: 40px; display: flex; flex-direction: column; height: calc(100vh - 150px); }
        .terminal { background: #000; border: 1px solid #333; border-radius: 8px; flex: 1; padding: 20px; box-shadow: 0 0 30px rgba(0,255,0,0.1); display: flex; flex-direction: column;}
        .output { flex: 1; overflow-y: auto; color: #bbb; line-height: 1.6;}
        .input-line { display: flex; align-items: center; color: #0f0; margin-top: 10px;}
        .input-line span { margin-right: 10px; font-weight: bold; }
        .input-line input { background: transparent; border: none; color: #0f0; font-family: inherit; font-size: 16px; flex: 1; outline: none;}
        
        .sys-text { color: #00CFFF; }
        .err-text { color: #ff5f56; }
    </style>
</head>
<body>
    <div class="header">
        <div style="display: flex; align-items: center;">
            <img src="LOGO_PLACEHOLDER" class="premium-logo">
            <h1>NOVA NATIVE CONSOLE</h1>
        </div>
        <a href="index.html" style="color:#888; text-decoration:none;">[ EXIT TERMINAL ]</a>
    </div>
    
    <div class="main-area">
        <div class="terminal">
            <div class="output" id="out">
                <span class="sys-text">Nova Core Engine v2.0 - Initialized</span><br>
                Type "help" for commands or execute standard syntax.<br><br>
            </div>
            <div class="input-line">
                <span>root@nova:~#</span>
                <input type="text" id="cmdInput" autocomplete="off" autofocus onkeypress="handleEnter(event)">
            </div>
        </div>
    </div>

    <script>
        function handleEnter(e) {
            if(e.key === 'Enter') {
                let input = document.getElementById('cmdInput');
                let out = document.getElementById('out');
                let val = input.value.trim();
                
                out.innerHTML += `<div><span style="color:#0f0;">root@nova:~#</span> ${val}</div>`;
                
                if(val === 'help') {
                    out.innerHTML += `<div class="sys-text">Available: Nova.show(), Nova.os.kernel_bypass(), clear</div>`;
                } else if(val === 'clear') {
                    out.innerHTML = '';
                } else if(val.includes('Nova.')) {
                    out.innerHTML += `<div style="color:#aaa;">[0.01ms] Native Execution: OK</div>`;
                } else if(val !== '') {
                    out.innerHTML += `<div class="err-text">SyntaxError: Unrecognized command</div>`;
                }
                
                input.value = '';
                out.scrollTop = out.scrollHeight;
            }
        }
    </script>
</body>
</html>"""
console_html = console_html.replace("LOGO_PLACEHOLDER", logo_b64)

# Writing all files
os.makedirs("website/public", exist_ok=True)
with open("website/public/index.html", "w") as f: f.write(index_html)
with open("website/public/installer.html", "w") as f: f.write(installer_html)
with open("website/public/hub.html", "w") as f: f.write(hub_html)
with open("website/public/nova_console.html", "w") as f: f.write(console_html)

print("✅ SUCCESS: All files securely built inside website/public/!")
