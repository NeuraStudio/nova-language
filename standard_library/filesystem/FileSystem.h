#pragma once
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

class FileSystem {
public:
    static void read(const std::vector<std::string>& args) {
        if (args.empty()) { std::cout << "❌ Error: Nova.file.read requires a filename.\n"; return; }
        std::ifstream file(args[0]);
        if (!file.is_open()) { std::cout << "❌ Error: Could not find or open file '" << args[0] << "'\n"; return; }
        std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        std::cout << content << "\n";
    }

    static void write(const std::vector<std::string>& args) {
        if (args.size() < 2) { std::cout << "❌ Error: Nova.file.write requires filename and content.\n"; return; }
        std::ofstream file(args[0]);
        for (size_t i = 1; i < args.size(); ++i) file << args[i] << (i == args.size()-1 ? "" : " ");
        file.close();
        std::cout << "✅ Successfully wrote to " << args[0] << "\n";
    }
};
