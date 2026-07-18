import os

# HTML Content with the EXACT logo 5611_2.png
# and the comparison/hub features
files = {
    "website/public/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Neura Studio | Nova</title>
    <style>
        body { background: #fff; color: #111; font-family: sans-serif; margin: 0; }
        .nav { display: flex; justify-content: space-between; align-items: center; padding: 20px 50px; background: #fff; box-shadow: 0 1px 3px rgba(0,0,0,0.1); position: sticky; top: 0; }
        .nav-logo { display: flex; align-items: center; font-weight: 800; font-size: 20px; text-decoration: none; color: #000; }
        .logo { width: 45px; height: 45px; border-radius: 50%; margin-right: 12px; border: 2px solid #00CFFF; }
        .nav-links a { margin-left: 25px; text-decoration: none; color: #444; font-weight: 600; font-size: 14px; }
        .btn { background: #00CFFF; color: #fff; padding: 10px 20px; border-radius: 20px; font-weight: bold; }
        .hero { text-align: center; padding: 80px 20px; }
        h1 { font-size: 4em; font-weight: 800; }
        .comparison { max-width: 800px; margin: 50px auto; padding: 40px; background: #f9f9f9; border-radius: 16px; border: 1px solid #eee; }
        .bar { margin-bottom: 20px; }
        .bar-label { display: flex; justify-content: space-between; font-weight: 600; }
        .bar-track { background: #ddd; height: 12px; border-radius: 6px; overflow: hidden; }
        .bar-fill { height: 100%; border-radius: 6px; background: #007aff; }
    </style>
</head>
<body>
    <nav class="nav">
        <a href="index.html" class="nav-logo"><img src="5611_2.png" class="logo"> NEURA STUDIO</a>
        <div class="nav-links">
            <a href="index.html">Overview</a><a href="hub.html">Nova Hub</a>
            <a href="nova_console.html">Nova Console</a><a href="installer.html" class="btn">Get Nova</a>
        </div>
    </nav>
    <section class="hero">
        <h1>Code at the speed of thought.</h1>
    </section>
    <section class="comparison">
        <h2>Unrivaled Execution Speed (ms)</h2>
        <div class="bar"><div class="bar-label"><span>Nova (Native)</span><span>0.01ms</span></div><div class="bar-track"><div class="bar-fill" style="width:100%"></div></div></div>
        <div class="bar"><div class="bar-label"><span>Mojo</span><span>0.02ms</span></div><div class="bar-track"><div class="bar-fill" style="width:80%"></div></div></div>
        <div class="bar"><div class="bar-label"><span>C++</span><span>0.05ms</span></div><div class="bar-track"><div class="bar-fill" style="width:60%"></div></div></div>
    </section>
</body>
</html>""",
    "website/public/hub.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nova Hub</title>
    <style>
        body { background: #fff; font-family: sans-serif; padding: 40px; }
        .search { width: 100%; max-width: 600px; padding: 15px; font-size: 18px; border: 2px solid #00CFFF; border-radius: 8px; margin-bottom: 20px;}
        .grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 40px; }
        .card { padding: 20px; border: 1px solid #eee; border-radius: 12px; text-align: center; }
        .code { background: #000; color: #0f0; padding: 5px; border-radius: 4px; }
    </style>
</head>
<body>
    <a href="index.html"><img src="5611_2.png" style="width:50px;"></a>
    <h1>Nova Hub 📦</h1>
    <input type="text" id="s" class="search" placeholder="Search 12,000,000+ packages..." onkeyup="search()">
    <div class="grid" id="g"></div>
    <script>
        const pkgs = ["tensorflow", "react", "spring", "boost", "tokio", "django", "node", "pandas", "rails", "laravel", "gin", "dotnet", "swiftui", "flutter", "numpy", "vue", "kotlin", "pytorch"];
        function search() {
            const val = document.getElementById('s').value.toLowerCase();
            const g = document.getElementById('g');
            g.innerHTML = '';
            pkgs.filter(p => p.includes(val)).forEach(p => {
                g.innerHTML += `<div class="card"><h3>${p}</h3><code class="code">Nova.import("${p}")</code></div>`;
            });
        }
        search();
    </script>
</body>
</html>""",
    "website/public/installer.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Get Nova</title>
    <style>
        body { background: #fff; font-family: sans-serif; padding: 40px; text-align: center; }
        .grid { display: flex; justify-content: center; gap: 20px; margin-top: 20px;}
        .btn { padding: 20px; border: 2px solid #000; border-radius: 12px; cursor: pointer; }
    </style>
</head>
<body>
    <a href="index.html"><img src="5611_2.png" style="width:50px;"></a>
    <h1>Get Nova Engine</h1>
    <div class="grid">
        <div class="btn" onclick="show('terminal')"><h3>Nova Core Shell (Terminal)</h3></div>
        <div class="btn" onclick="show('ide')"><h3>Visual Installer (VS Code/PyCharm)</h3></div>
    </div>
    <div id="result"></div>
    <script>
        function show(type) {
            const r = document.getElementById('result');
            r.innerHTML = type === 'terminal' ? 
            '<h2>Run in Terminal:</h2><code style="background:#000; color:#0f0; padding:10px;">curl -sL https://ncs.neurastudio.com/install | bash</code>' :
            '<h2>Download Installer</h2><p>Select IDE: <select><option>VS Code</option><option>PyCharm</option></select></p><button>Download</button>';
        }
    </script>
</body>
</html>""",
    "website/public/nova_console.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nova Console</title>
    <style>
        body { background: #000; color: #0f0; font-family: monospace; padding: 20px; }
    </style>
</head>
<body>
    <a href="index.html" style="color:#fff;">⬅ Back</a>
    <h1>>_ NOVA NATIVE CONSOLE</h1>
    <div id="output">root@nova:~$ System Initialized...</div>
    <input type="text" style="background:transparent; border:none; color:#0f0; width:100%;" autofocus>
</body>
</html>"""
}

for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content)
    print(f"✅ Created/Updated: {path}")
