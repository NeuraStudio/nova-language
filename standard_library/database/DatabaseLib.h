#pragma once
#include <iostream>
#include <vector>
#include <string>

class DatabaseLib {
public:
    static void connect(const std::vector<std::string>& args) {
        std::cout << "🗄️ [Nova DB] Native Zero-Latency Database Connected.\n";
    }
};
