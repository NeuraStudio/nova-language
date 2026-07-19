import os
import re
import time

def clear():
    os.system('clear')

def print_header():
    print("============================================================")
    print("  NOVA APEX ENGINE (v2.0.0-commercial) [linux-arm64]")
    print("  (c) 2026 Neura Studio. Chief Architect: JAVED.")
    print("  Architecture: NeuraVM | Execution: 0.01ms")
    print("  Type 'help' for commands. Type 'exit' to quit.")
    print("============================================================")

clear()
print_header()

variables = {}

while True:
    try:
        cmd = input("nova>>> ").strip()
        if not cmd:
            continue
            
        if cmd == "exit":
            break
        elif cmd == "clear":
            clear()
            print_header()
            continue
            
        # FIX 1: Nova.ask.user("Name :", name) without '->'
        if cmd.startswith("Nova.ask.user"):
            match = re.search(r'\("(.*?)",\s*(.*?)\)', cmd)
            if match:
                prompt_txt = match.group(1)
                var_name = match.group(2).strip()
                user_input = input(f"{prompt_txt} ")
                variables[var_name] = user_input
                continue
                
        # FIX 2: Dynamic Math and Print (Nova.show)
        elif cmd.startswith("Nova.show"):
            match = re.search(r'\((.*?)\)', cmd)
            if match:
                inner = match.group(1).replace('"', '').replace("'", "")
                # Check if it's a stored variable
                if inner in variables:
                    print(f"[0.01ms] {variables[inner]}")
                else:
                    try:
                        print(f"[0.01ms] {eval(inner)}")
                    except:
                        print(f"[0.01ms] {inner}")
            continue
            
        # FIX 3: Realistic Package Installer Simulation
        elif cmd.startswith("Nova.hub.install"):
            match = re.search(r'\(["\'](.*?)["\']\)', cmd)
            if match:
                pkg = match.group(1)
                print(f"[Nova Hub] Resolving '{pkg}' via Global Registry (12M+ packages)...")
                time.sleep(1)
                print(f"[NeuraVM] Compiling native bindings for {pkg}...")
                time.sleep(0.5)
                print(f"✅ SUCCESS: '{pkg}' installed natively into Nova environment.")
            else:
                print("SyntaxError: Use format Nova.hub.install(\"type:package\")")
            continue
            
        # Generic Execution
        elif cmd.startswith("Nova."):
            print("[0.01ms] Executed Native Instruction successfully.")
        else:
            print(f"SyntaxError: Invalid Nova syntax. Did you mean to use 'Nova.' namespace?")
            
    except KeyboardInterrupt:
        print("\nExiting Nova...")
        break
    except Exception as e:
        print(f"Engine Error: {e}")
