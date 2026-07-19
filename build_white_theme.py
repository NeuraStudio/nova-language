import os

print("🚀 Building Ultra-Premium White Theme Website...")

# 1. INDEX.HTML (Matches 7271.jpg & 5919.jpg)
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Neura Studio | Nova</title>
    <style>
        /* Light Theme Core */
        body { background: #fafafa; color: #111; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; margin: 0; overflow-x: hidden; }
        
        /* Animations */
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(40px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes pulseShadow { 0% { box-shadow: 0 5px 15px rgba(0,207,255,0.2); } 50% { box-shadow: 0 10px 25px rgba(0,207,255,0.5); } 100% { box-shadow: 0 5px 15px rgba(0,207,255,0.2); } }
        @keyframes popIn { 0% { transform: scale(0.8); opacity: 0; } 100% { transform: scale(1); opacity: 1; } }
        
        .anim-up { animation: fadeInUp 0.8s cubic-bezier(0.16, 1, 0.3, 1) forwards; opacity: 0; }
        .delay-1 { animation-delay: 0.1s; } .delay-2 { animation-delay: 0.2s; } .delay-3 { animation-delay: 0.4s; }

        /* Navbar */
        .nav { display: flex; justify-content: space-between; align-items: center; padding: 15px 50px; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(15px); position: sticky; top: 0; z-index: 1000; box-shadow: 0 2px 20px rgba(0,0,0,0.05); }
        .nav-logo { display: flex; align-items: center; font-weight: 900; font-size: 22px; color: #111; text-decoration: none; }
        
        /* Circular Logo with Shadow & Click Animation */
        .premium-logo { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #00CFFF; object-fit: cover; margin-right: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.15); transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); animation: popIn 0.6s ease-out forwards; cursor: pointer; }
        .premium-logo:hover { transform: rotate(15deg) scale(1.15); box-shadow: 0 10px 25px rgba(0,207,255,0.4); }
        .premium-logo:active { transform: scale(0.9); } /* Click effect */

        .nav-links a { text-decoration: none; color: #555; font-weight: 600; margin: 0 15px; transition: 0.3s; }
        .nav-links a:hover { color: #00CFFF; }
        .btn { background: #00CFFF; color: #fff; padding: 10px 24px; border-radius: 30px; font-weight: bold; text-decoration: none; box-shadow: 0 5px 15px rgba(0,207,255,0.3); transition: 0.3s; }
        .btn:hover { background: #0099ff; transform: translateY(-3px); box-shadow: 0 10px 20px rgba(0,153,255,0.4); }

        /* Hero Section (7271.jpg Style) */
        .hero { text-align: center; padding: 100px 20px 40px; }
        h1 { font-size: 4.5em; font-weight: 900; letter-spacing: -2px; margin-bottom: 15px; color: #111; }
        p { color: #666; font-size: 1.3em; max-width: 600px; margin: 0 auto 30px; line-height: 1.5; }
        
        .action-btns { display: flex; justify-content: center; gap: 15px; margin-bottom: 60px; }
        .action-btn { background: #111; color: #fff; padding: 12px 25px; border-radius: 8px; font-weight: bold; text-decoration: none; display: flex; align-items: center; gap: 8px; transition: 0.3s; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .action-btn:hover { background: #333; transform: translateY(-3px); }

        /* Images Row */
        .image-row { display: flex; justify-content: center; gap: 20px; max-width: 1000px; margin: 0 auto 60px; align-items: center; }
        .image-row img { border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.1); object-fit: cover; transition: 0.5s; cursor: pointer; }
        .img-1 { width: 300px; height: 200px; } .img-2 { width: 400px; height: 250px; z-index: 10; transform: scale(1.05); box-shadow: 0 20px 40px rgba(0,0,0,0.15); } .img-3 { width: 300px; height: 200px; }
        .image-row img:hover { transform: scale(1.1) translateY(-10px); z-index: 20; box-shadow: 0 25px 50px rgba(0,0,0,0.2); }

        /* Code Editor */
        .code-wrapper { background: #0d1117; max-width: 900px; margin: 0 auto 60px; border-radius: 16px; overflow: hidden; box-shadow: 0 25px 50px rgba(0,0,0,0.2); text-align: left; }
        .code-header { background: #161b22; padding: 12px 20px; display: flex; align-items: center; color: #8b949e; font-family: monospace; font-size: 13px; }
        .dots { display: flex; gap: 8px; margin-right: 15px; } .dot { width: 12px; height: 12px; border-radius: 50%; } .red{background:#ff5f56;} .ylw{background:#ffbd2e;} .grn{background:#27c93f;}
        .code-body { padding: 30px; font-family: 'Courier New', monospace; font-size: 15px; color: #e2e8f0; line-height: 1.6; }
        .kw { color: #00CFFF; font-weight: bold; } .str { color: #a5d6ff; } .cmnt { color: #8b949e; }

        /* Comparison Chart (White Theme) */
        .speed-section { background: #fff; max-width: 900px; margin: 0 auto 100px; padding: 50px; border-radius: 20px; box-shadow: 0 10px 40px rgba(0,0,0,0.05); border: 1px solid #eaeaea; }
        .speed-section h2 { text-align: center; font-size: 2em; margin-bottom: 40px; color: #111; }
        .bar-container { margin-bottom: 25px; }
        .bar-label { display: flex; justify-content: space-between; font-weight: bold; margin-bottom: 10px; color: #333; font-size: 15px; }
        .bar-bg { background: #f0f0f0; border-radius: 10px; height: 12px; width: 100%; overflow: hidden; }
        .bar-fill { height: 100%; border-radius: 10px; transition: width 2s cubic-bezier(0.16, 1, 0.3, 1); width: 0; }
    </style>
</head>
<body>
    <nav class="nav">
        <a href="index.html" class="nav-logo"><img src="5611_2.png" class="premium-logo" alt="Logo"> NEURA STUDIO</a>
        <div class="nav-links"><a href="index.html" style="color:#00CFFF;">Overview</a><a href="hub.html">Nova Hub</a><a href="nova_console.html">Nova Console</a></div>
        <a href="installer.html" class="btn">Download Engine</a>
    </nav>

    <section class="hero anim-up">
        <h1>Make your code faster.</h1>
        <p>Nova is the ultimate God-Mode alternative to Python, Java, and C++. Built for AI, Robotics, and Quantum computing.</p>
        <div class="action-btns">
            <a href="nova_docs.html" class="action-btn">📄 Learn Nova</a>
            <a href="installer.html" class="action-btn">⚙️ Features & Arch</a>
            <a href="Nova_Syntax_Master_Guide.pdf" class="action-btn" download>📘 Syntax Master</a>
        </div>
    </section>

    <div class="image-row anim-up delay-1">
        <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=500&q=80" class="img-1">
        <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=600&q=80" class="img-2">
        <img src="https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=500&q=80" class="img-3">
    </div>

    <div class="code-wrapper anim-up delay-2">
        <div class="code-header"><div class="dots"><div class="dot red"></div><div class="dot ylw"></div><div class="dot grn"></div></div> CMD - Nova Interpreter</div>
        <div class="code-body">
            <span class="cmnt">// Enter your Nova code here</span><br>
            <span class="kw">Nova</span>.show(<span class="str">"Hello, Neura Studio!"</span>)<br>
            <span class="kw">Nova</span>.hardware.cpu.alloc(16, <span class="str">"exclusive"</span>)<br>
            <span class="kw">Nova</span>.show(<span class="str">"System Hacked. 0.01ms."</span>)<br>
        </div>
    </div>

    <section class="speed-section anim-up delay-3">
        <h2>Unrivaled Execution Speed</h2>
        <div class="bar-container"><div class="bar-label"><span>Nova (Native Bytecode)</span><span style="color:#00CFFF">0.01ms</span></div><div class="bar-bg"><div class="bar-fill" style="background:#00CFFF;" data-width="100%"></div></div></div>
        <div class="bar-container"><div class="bar-label"><span>C++ (GCC 03)</span><span style="color:#64748b">0.05ms</span></div><div class="bar-bg"><div class="bar-fill" style="background:#64748b;" data-width="60%"></div></div></div>
        <div class="bar-container"><div class="bar-label"><span>Python 3.11</span><span style="color:#ef4444">5.20ms</span></div><div class="bar-bg"><div class="bar-fill" style="background:#ef4444;" data-width="15%"></div></div></div>
    </section>

    <script>
        window.onload = () => { setTimeout(() => { document.querySelectorAll('.bar-fill').forEach(bar => { bar.style.width = bar.getAttribute('data-width'); }); }, 500); }
    </script>
</body>
</html>"""

# 2. HUB.HTML (Matches 5902.jpg - Light Theme Grid)
hub_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nova Hub</title>
    <style>
        body { background: #fafafa; color: #111; font-family: sans-serif; margin: 0; padding-bottom: 50px;}
        .nav { display: flex; justify-content: space-between; align-items: center; padding: 15px 50px; background: #fff; box-shadow: 0 2px 15px rgba(0,0,0,0.05); position: sticky; top:0; z-index:100; }
        .nav-logo { display: flex; align-items: center; font-weight: 900; font-size: 22px; color: #111; text-decoration: none; }
        .premium-logo { width: 45px; height: 45px; border-radius: 50%; border: 2px solid #00CFFF; object-fit: cover; margin-right: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); cursor: pointer; transition: 0.3s; }
        .premium-logo:hover { transform: scale(1.1); box-shadow: 0 8px 20px rgba(0,207,255,0.3); }
        .nav-links a { text-decoration: none; color: #555; font-weight: 600; margin: 0 15px; }

        .header { text-align: center; padding: 60px 20px 30px; animation: fadeIn 0.8s ease; }
        .header h1 { font-size: 3.5em; margin: 0 0 10px; color: #0d1b2a; }
        
        .search-box { display: flex; max-width: 600px; margin: 0 auto 50px; border-radius: 30px; overflow: hidden; box-shadow: 0 10px 25px rgba(0,0,0,0.05); border: 1px solid #eaeaea; background: #fff; animation: fadeIn 1s ease; }
        .search-box input { flex: 1; padding: 18px 25px; border: none; font-size: 16px; outline: none; }
        .search-box button { background: #0d1b2a; color: #fff; padding: 0 35px; font-weight: bold; border: none; cursor: pointer; }

        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 25px; max-width: 1100px; margin: 0 auto; padding: 0 20px; }
        .card { background: #fff; border: 1px solid #eaeaea; padding: 30px 20px; border-radius: 16px; text-align: center; transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1); box-shadow: 0 5px 15px rgba(0,0,0,0.02); cursor: pointer; animation: popUp 0.6s ease backwards; opacity: 0; }
        .card:hover { border-color: #00CFFF; transform: translateY(-8px); box-shadow: 0 15px 35px rgba(0,207,255,0.15); }
        .card img { height: 60px; margin-bottom: 20px; }
        .card h3 { margin: 0 0 15px; color: #111; font-size: 1.1em; }
        .cmd { background: #0d1b2a; color: #00CFFF; padding: 12px; border-radius: 8px; font-family: monospace; font-size: 12px; }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        @keyframes popUp { from { opacity: 0; transform: scale(0.9); } to { opacity: 1; transform: scale(1); } }
    </style>
</head>
<body>
    <nav class="nav">
        <a href="index.html" class="nav-logo"><img src="5611_2.png" class="premium-logo"> NEURA STUDIO</a>
        <div class="nav-links"><a href="index.html">Overview</a><a href="hub.html" style="color:#00CFFF;">Nova Hub</a><a href="nova_console.html">Nova Console</a></div>
    </nav>
    <div class="header">
        <h1>Nova Hub 📦</h1>
        <p style="color:#666; font-size:1.2em;">The Universal Package Manager. Search and install from 3,560,000+ packages.</p>
    </div>
    <div class="search-box">
        <input type="text" id="s" placeholder="Py..." onkeyup="search()">
        <button onclick="search()">🔍 Search</button>
    </div>
    <div class="grid" id="g"></div>
    <script>
        const pkgs = [
            {n:"python:tensorflow", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg"},
            {n:"js:react", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg"},
            {n:"java:spring", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg"},
            {n:"cpp:boost", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg"},
            {n:"rust:tokio", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rust/rust-plain.svg"},
            {n:"nova:quantum", i:"https://upload.wikimedia.org/wikipedia/commons/1/18/ISO_C%2B%2B_Logo.svg"},
            {n:"python:django", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"},
            {n:"js:node", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg"},
            {n:"python:pandas", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg"},
            {n:"ruby:rails", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg"},
            {n:"php:laravel", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg"},
            {n:"go:gin", i:"https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg"}
        ];
        function render() {
            let html = '';
            pkgs.forEach((p, i) => {
                html += `<div class="card" style="animation-delay:${i*0.05}s"><img src="${p.i}"><h3>${p.n}</h3><div class="cmd">Nova.import("${p.n}")</div></div>`;
            });
            document.getElementById('g').innerHTML = html;
        }
        function search() {
            let val = document.getElementById('s').value.toLowerCase();
            if(!val) return render();
            let html = '';
            pkgs.filter(p => p.n.includes(val)).forEach(p => {
                html += `<div class="card" style="opacity:1; animation:none;"><img src="${p.i}"><h3>${p.n}</h3><div class="cmd">Nova.import("${p.n}")</div></div>`;
            });
            document.getElementById('g').innerHTML = html;
        }
        render();
    </script>
</body>
</html>"""

# 3. NOVA CONSOLE (Matches 7691.jpg/7507_2.jpg - Interactive)
console_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Nova Console</title>
    <style>
        body { background: #fafafa; color: #111; font-family: sans-serif; margin: 0; padding: 20px;}
        .header { display: flex; justify-content: space-between; align-items: center; background: #fff; padding: 15px 30px; border-radius: 12px; box-shadow: 0 5px 15px rgba(0,0,0,0.05); margin-bottom: 20px; }
        .logo { width: 40px; height: 40px; border-radius: 50%; border: 2px solid #00CFFF; margin-right: 15px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); cursor: pointer; transition: 0.3s;}
        .logo:hover { transform: scale(1.1); }
        .run-btn { background: #00CFFF; color: #fff; padding: 10px 25px; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.3s;}
        .run-btn:hover { background: #0099ff; transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,207,255,0.4);}
        
        .split { display: flex; gap: 20px; height: 80vh; }
        .box { flex: 1; background: #0d1117; border-radius: 16px; padding: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.15); display: flex; flex-direction: column; }
        textarea { flex: 1; background: transparent; border: none; color: #a5d6ff; font-family: monospace; font-size: 15px; outline: none; resize: none; line-height: 1.6;}
        .output { flex: 1; color: #fff; font-family: monospace; font-size: 15px; overflow-y: auto; line-height: 1.6;}
    </style>
</head>
<body>
    <div class="header">
        <div style="display:flex; align-items:center;"><img src="5611_2.png" class="logo"> <h2>Nova Interactive Console</h2></div>
        <div>
            <a href="index.html" style="margin-right:20px; text-decoration:none; color:#555; font-weight:bold;">⬅ Back to Home</a>
            <button class="run-btn" onclick="runCode()">▶ Run Native</button>
        </div>
    </div>
    <div class="split">
        <div class="box">
            <span style="color:#8b949e; margin-bottom:10px;">// Enter Nova Syntax</span>
            <textarea id="code" spellcheck="false">Nova.hardware.cpu.alloc(16, "exclusive")\nNova.show("System ready.")</textarea>
        </div>
        <div class="box output" id="out">Awaiting execution...</div>
    </div>
    <script>
        function runCode() {
            let out = document.getElementById('out');
            let code = document.getElementById('code').value;
            out.innerHTML += "<br><br><span style='color:#00CFFF;'>[Compiling...]</span><br>";
            setTimeout(() => {
                let lines = code.split('\\n');
                lines.forEach(l => {
                    if(l.includes('Nova.show')) {
                        let m = l.match(/\\((.*?)\\)/);
                        if(m) out.innerHTML += `> <b>${m[1].replace(/['"]/g, '')}</b><br>`;
                    } else if(l.includes('Nova.')) {
                        out.innerHTML += `<span style="color:#8b949e;">> Executed [0.01ms]: ${l}</span><br>`;
                    }
                });
                out.scrollTop = out.scrollHeight;
            }, 600);
        }
    </script>
</body>
</html>"""

# Write files directly to the root directory
with open("index.html", "w") as f: f.write(index_html)
with open("hub.html", "w") as f: f.write(hub_html)
with open("nova_console.html", "w") as f: f.write(console_html)

print("✅ SUCCESS: White Theme HTML files created in root directory!")
