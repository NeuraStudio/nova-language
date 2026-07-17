#pragma once
#include <string>
#include <unordered_map>
#include <functional>
#include <vector>
#include <iostream>

// A generic function pointer type for Nova commands
using NovaCommand = std::function<void(const std::vector<std::string>& args)>;

class CommandRegistry {
private:
    std::unordered_map<std::string, NovaCommand> handlers;

public:
    // Registers a command path like "Nova.show" to a backend handler
    void registerCommand(const std::string& path, NovaCommand handler) {
        handlers[path] = handler;
    }

    // Executes the command if found in the registry
    void execute(const std::string& path, const std::vector<std::string>& args) {
        if (handlers.find(path) != handlers.end()) {
            handlers[path](args);
        } else {
            std::cerr << "[Runtime Error] Command not found: " << path << "\n";
        }
    }
};
