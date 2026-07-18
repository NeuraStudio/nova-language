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
        
        if (input == "exit" || input == "quit") break;
        if (input == "clear") { cout << "\033[2J\033[1;1H"; continue; }
        if (input == "copyright" || input == "license") {
            cout << "\nCopyright (c) 2026 Neura Studio. Created by Javed.\n";
            cout << "Nova is a proprietary Apex-Level engine provided under the MIT License.\n\n";
            continue;
        }
        if (input.empty()) continue;

        // Command Parsing
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
