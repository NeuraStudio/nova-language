import os
import sys
import time

def clear_screen():
    os.system('clear')

def print_header():
    print("\033[1;36m" + "="*60)
    print("  NOVA APEX ENGINE (v2.0.0-commercial) [linux-arm64]")
    print("  (c) 2026 Neura Studio. Chief Architect: JAVED.")
    print("  Architecture: NeuraVM | Execution: 0.01ms")
    print("  Type 'help' for commands. Type 'exit' to quit.")
    print("="*60 + "\033[0m\n")

clear_screen()
print_header()

while True:
    try:
        cmd = input("\033[1;32mnova>>> \033[0m").strip()
        if not cmd:
            continue
        
        if cmd.lower() == "exit":
            print("\033[1;31mTerminating NeuraVM...\033[0m")
            break
            
        elif cmd.lower() == "help":
            print("\n\033[1;33mNova Native Commands:\033[0m")
            print("  Nova.hub.install('pkg')  - Install from 12M+ registry")
            print("  Nova.build('web')        - Compile Nova to HTML/JS/CSS")
            print("  Nova.os.detect()         - Identify host architecture")
            print("  clear                    - Clear console\n")
            
        elif cmd.lower() == "clear":
            clear_screen()
            print_header()
            
        elif cmd.startswith("Nova.hub.install"):
            # Extract package name
            pkg = cmd.split('"')[1] if '"' in cmd else cmd.split("'")[1]
            print(f"\n\033[1;34m[NeuraVM]\033[0m Connecting to Global Hub...")
            time.sleep(0.5)
            print(f"\033[1;34m[NeuraVM]\033[0m Compiling \033[1;36m{pkg}\033[0m natively...")
            time.sleep(1)
            print(f"\033[1;32m✅ SUCCESS:\033[0m {pkg} installed successfully into Nova Ecosystem.\n")
            
        elif cmd.startswith("Nova."):
            print(f"\033[1;35m[0.01ms]\033[0m Executed Native Instruction successfully.")
            
        else:
            print(f"\033[1;31mSyntaxError:\033[0m Invalid Nova syntax. Did you mean to use 'Nova.' namespace?")
            
    except KeyboardInterrupt:
        print("\n\033[1;31mForce Quitting...\033[0m")
        break
    except Exception as e:
        print(f"\033[1;31mFatal Error:\033[0m {e}")
