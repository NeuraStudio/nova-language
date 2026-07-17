#pragma once
#include <iostream>
#include <vector>
#include <string>

class RoboticsLib {
public:
    static void connect(const std::vector<std::string>& args) {
        std::cout << "🤖 [Nova Robotics] Scanning for hardware on COM/Serial ports...\n";
        std::cout << "⚡ Connection Established. Actuators and Sensors are online.\n";
    }
    static void move(const std::vector<std::string>& args) {
        if (args.empty()) return;
        std::cout << "🦾 [Nova Robotics] Executing hardware instruction: MOVE " << args[0] << "\n";
    }
};
