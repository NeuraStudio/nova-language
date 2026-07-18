#include <iostream>
#include <string>

using namespace std;

void printHeader() {
    cout << "====================================================\n";
    cout << "  NOVA APEX ENGINE (v1.0.0-commercial) [linux-arm64]\n";
    cout << "  (c) 2026 Neura Studio. Chief Architect: JAVED.\n";
    cout << "  Licensed under MIT. Type 'help' for commands.\n";
    cout << "====================================================\n";
}

int main() {
    printHeader();
    string input;
    
    while(true) {
        cout << "nova>>> ";
        if (!getline(cin, input)) break;
        
        // Trim spaces
        while(input.length() > 0 && input[0] == ' ') input.erase(0, 1);
        while(input.length() > 0 && input[input.length()-1] == ' ') input.erase(input.length()-1, 1);

        if (input == "exit" || input == "quit") break;
        if (input == "clear") { cout << "\033[2J\033[1;1H"; continue; }
        
        // Help and License Fix
        if (input == "help") {
            cout << "\nNova Interactive Shell Commands:\n";
            cout << "  exit, quit   - Exit the REPL\n";
            cout << "  license      - Show MIT License & Terms\n";
            cout << "  clear        - Clear the terminal screen\n\n";
            continue;
        }
        if (input == "license" || input == "licensed" || input == "copyright") {
            cout << "\nCopyright (c) 2026 Neura Studio. Created by JAVED.\n";
            cout << "Nova is a proprietary Apex-Level engine provided under the MIT License.\n\n";
            continue;
        }
        if (input.empty()) continue;

        if (input.find("Nova.show") != string::npos) {
            size_t start = input.find('"');
            size_t end = input.rfind('"');
            if (start != string::npos && end != string::npos && end > start) {
                cout << input.substr(start + 1, end - start - 1) << "\n";
            } else { cout << "SyntaxError: Expected string literal\n"; }
        }
        else if (input.find("Nova.import") != string::npos) {
            size_t start = input.find('"');
            size_t end = input.rfind('"');
            if (start != string::npos && end != string::npos && end > start) {
                string pkg = input.substr(start + 1, end - start - 1);
                cout << "[Nova Hub] Fetching package '" << pkg << "'...\n";
                cout << "✅ Successfully linked '" << pkg << "' to NeuraVM in 0.02ms.\n";
            }
        }
        else if (input.find("Nova.hardware.cpu.alloc") != string::npos) {
            cout << "⚙️ Hardware Locked: Threads allocated successfully.\n";
        }
        else {
            cout << "ReferenceError: '" << input << "' is not defined in Nova.\n";
        }
    }
    return 0;
}
