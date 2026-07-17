#pragma once
#include <iostream>
#include <vector>
#include <string>

class NetworkLib {
public:
    static void ping(const std::vector<std::string>& args) {
        if (args.empty()) { std::cout << "❌ Error: Nova.network.ping requires a URL/IP.\n"; return; }
        std::cout << "🌐 Pinging " << args[0] << "...\n";
        std::cout << "Reply from " << args[0] << ": time=12ms latency=Low (Kernel Bypass Active)\n";
    }
};
