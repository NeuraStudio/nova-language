#pragma once
#include <iostream>
#include <string>
#include "../../compiler/lexer/Lexer.h"
#include "../../compiler/parser/Parser.h"

class REPL {
public:
    template <typename RegistryType>
    static void start(RegistryType& registry) {
        std::cout << "=================================================\n";
        std::cout << "  NOVA INTERACTIVE SHELL v1.0.0\n";
        std::cout << "  (c) 2026 Neura Studio. All rights reserved.\n";
        std::cout << "  Type 'exit' to quit.\n";
        std::cout << "  AI Diagnostics: ACTIVE | Mode: Apex-Level\n";
        std::cout << "=================================================\n\n";

        std::string line;
        while (true) {
            std::cout << "nova>>> ";
            if (!std::getline(std::cin, line) || line == "exit") break;
            if (line.empty()) continue;

            try {
                Lexer lexer(line);
                Parser parser(lexer.tokenize());
                auto ast = parser.parse();
            } catch (const std::exception& e) {
                std::cout << "❌ " << e.what() << "\n";
            }
        }
    }
};
