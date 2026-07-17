#pragma once
#include <string>
#include <iostream>

class PythonBridge {
public:
    static void importPackage(const std::string& packageName) {
        std::cout << "[Hub] Allocating zero-cost FFI bridge for Python package: " << packageName << "...\n";
    }
};
