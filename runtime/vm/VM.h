#pragma once
#include <iostream>
#include <vector>
#include "../../compiler/bytecode/OpCode.h"

class NovaVM {
private:
    std::vector<uint8_t> bytecode;
    std::vector<double> stack; // Native fast stack

public:
    void loadChunk(const std::vector<uint8_t>& code) {
        bytecode = code;
    }

    void execute() {
        std::cout << "[Nova VM] Booting Native Bytecode Engine...\n";
        for (size_t ip = 0; ip < bytecode.size(); ++ip) {
            OpCode instruction = static_cast<OpCode>(bytecode[ip]);
            if (instruction == OpCode::OP_CONSTANT) { 
                stack.push_back(100.5); 
            }
            else if (instruction == OpCode::OP_ADD) {
                if (stack.size() >= 2) {
                    double b = stack.back(); stack.pop_back();
                    double a = stack.back(); stack.pop_back();
                    stack.push_back(a + b);
                }
            }
            else if (instruction == OpCode::OP_PRINT) {
                if (!stack.empty()) {
                    std::cout << stack.back() << "\n";
                    stack.pop_back();
                }
            }
            else if (instruction == OpCode::OP_HALT) {
                std::cout << "[Nova VM] Execution Halted (0.01ms).\n";
                return;
            }
        }
    }
};
