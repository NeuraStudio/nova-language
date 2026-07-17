#pragma once
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

class MathLib {
public:
    static void power(const std::vector<std::string>& args) {
        if (args.size() < 2) { std::cout << "❌ Error: Nova.math.pow requires base and exponent.\n"; return; }
        try {
            double base = std::stod(args[0]);
            double exp = std::stod(args[1]);
            std::cout << std::pow(base, exp) << "\n";
        } catch (...) { std::cout << "❌ MathError: Invalid numbers provided.\n"; }
    }
};
