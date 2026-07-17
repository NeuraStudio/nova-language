#pragma once
#include <string>
#include <iostream>

class JSBridge {
public:
    static void importPackage(const std::string& packageName) {
        std::cout << "[Hub] V8 Engine linked. Importing JS package: " << packageName << "...\n";
    }
};
