from weasyprint import HTML

html_content = """
<!DOCTYPE html>
<html>
<head>
<style>
    @page { size: A4; margin: 25mm 20mm; @bottom-right { content: "Page " counter(page); font-family: sans-serif; color: #888; font-size: 10pt;} @top-left { content: "Neura Studio Documentation"; font-family: sans-serif; color: #00CFFF; font-weight: bold; font-size: 10pt; } }
    body { font-family: 'Segoe UI', Roboto, Helvetica, sans-serif; color: #333; line-height: 1.7; background-color: #fff; }
    
    /* Branding & Website Look */
    .header { text-align: center; border-bottom: 2px solid #eaebed; padding-bottom: 30px; margin-bottom: 40px; margin-top: 100px;}
    .header h1 { color: #111; font-size: 42pt; font-weight: 900; margin: 0; letter-spacing: -1.5px;}
    .header .subtitle { color: #00CFFF; font-size: 24pt; font-weight: bold; margin-top: 5px; }
    .header .author { color: #666; font-size: 16pt; margin-top: 20px; }

    h2 { color: #111; font-size: 20pt; margin-top: 40px; border-bottom: 1px solid #ddd; padding-bottom: 8px; }
    h3 { color: #3B82F6; font-size: 16pt; margin-top: 25px; }
    
    p { font-size: 12pt; text-align: justify; color: #444; }
    
    /* Python-Style Syntax Documentation Blocks */
    .doc-block { background: #f8f9fa; border-left: 4px solid #00CFFF; padding: 15px 20px; margin: 20px 0; border-radius: 0 8px 8px 0; }
    .syntax-def { font-family: 'Courier New', monospace; font-size: 13pt; font-weight: bold; color: #111; margin-bottom: 10px; display: block;}
    .param-list { margin-left: 20px; font-size: 11.5pt; color: #555; }
    .param-list strong { color: #111; }
    
    /* Terminal/CMD Block */
    .terminal-box { background: #121826; color: #e2e8f0; padding: 20px; border-radius: 8px; font-family: 'Courier New', monospace; font-size: 12pt; margin: 20px 0; box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    .terminal-box .comment { color: #64748b; }
    .terminal-box .keyword { color: #38bdf8; font-weight: bold;}
    .terminal-box .string { color: #a3e635; }
    
    .img-container { text-align: center; margin: 35px 0; }
    .img-container img { max-width: 100%; border-radius: 12px; box-shadow: 0 15px 35px rgba(0,0,0,0.15); }
    .chapter { page-break-before: always; }
</style>
</head>
<body>
    <div class="header">
        <h1>NEURA STUDIO</h1>
        <div class="subtitle">Nova Engine Official Documentation</div>
        <div class="author">By Javed (Chief Architect)</div>
    </div>

    <div class="img-container">
        <img src="https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=800&q=80">
    </div>
    <p>Welcome to the official documentation for Nova. Nova is a high-performance, statically typed, natively compiled language designed for AI, Robotics, and OS-level manipulation. This document outlines the syntax, internal mechanisms, and standard library functions in a structured format.</p>

    <div class="chapter">
        <h2>1. Hardware Allocation Module</h2>
        <p>The `hardware` module provides direct, low-level access to the CPU and GPU. Unlike Python which relies on the OS scheduler, Nova can bind itself directly to specific hardware cores.</p>
        
        <div class="doc-block">
            <span class="syntax-def">Nova.hardware.cpu.alloc(threads: int, mode: str) -> bool</span>
            <p>Allocates a specific number of logical CPU threads exclusively to the NeuraVM instance.</p>
            <div class="param-list">
                <strong>Parameters:</strong><br>
                • <strong>threads</strong> <em>(int)</em> – The number of cores to lock (e.g., 16).<br>
                • <strong>mode</strong> <em>(str)</em> – The allocation strategy ("exclusive" or "shared").
            </div>
            <div class="param-list" style="margin-top:10px;">
                <strong>Returns:</strong> <em>True</em> if allocation was successful, <em>False</em> otherwise.
            </div>
        </div>

        <div class="terminal-box">
            <span class="comment">// Example Usage</span><br>
            <span class="keyword">Nova</span>.hardware.cpu.alloc(16, <span class="string">"exclusive"</span>);
        </div>
        
        <div class="img-container">
            <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&q=80">
        </div>
    </div>

    <div class="chapter">
        <h2>2. AI & Neural Engine</h2>
        <p>Nova does not require massive external dependencies like TensorFlow. The mathematical backend required for tensor operations and matrix multiplication is built directly into the C++ core of NeuraVM.</p>

        <div class="doc-block">
            <span class="syntax-def">Nova.ai.think(task_name: str, tensor_cores: bool = true) -> ModelObject</span>
            <p>Initializes a native neural network training loop optimized for the specific task.</p>
            <div class="param-list">
                <strong>Parameters:</strong><br>
                • <strong>task_name</strong> <em>(str)</em> – The description of the compilation task.<br>
                • <strong>tensor_cores</strong> <em>(bool)</em> – Whether to strictly utilize GPU Tensor cores.
            </div>
        </div>

        <div class="terminal-box">
            <span class="comment">// Example Usage</span><br>
            <span class="keyword">let</span> model = <span class="keyword">Nova</span>.ai.think(<span class="string">"Optimize NLP Model"</span>);<br>
            model.train();
        </div>
    </div>

    <div class="chapter">
        <h2>3. Nova Hub (Package Management)</h2>
        <p>Nova Hub allows cross-language execution. You can import Python modules or JavaScript libraries, and the NeuraVM will automatically compile them into fast native bytecode.</p>
        
        <div class="img-container">
            <img src="https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80">
        </div>

        <div class="doc-block">
            <span class="syntax-def">Nova.import(package_uri: str) -> Module</span>
            <p>Fetches and links an external library from the Nova Global Hub.</p>
            <div class="param-list">
                <strong>Parameters:</strong><br>
                • <strong>package_uri</strong> <em>(str)</em> – The language and package name separated by a colon (e.g., "python:pandas").
            </div>
        </div>

        <div class="terminal-box">
            <span class="keyword">Nova</span>.import(<span class="string">"python:django"</span>);<br>
            <span class="keyword">Nova</span>.import(<span class="string">"rust:tokio"</span>);
        </div>
    </div>
</body>
</html>
"""

HTML(string=html_content).write_pdf('Nova_Official_Documentation.pdf')
print("✅ Python-Style PDF Generated: Nova_Official_Documentation.pdf")
