#include <iostream>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <cmath>
#include <map>
#include <functional>
#include <vector>

// --- COMMAND REGISTRY (FIXED) ---
class CommandRegistry {
public:
    using CommandFunc = std::function<void(const std::vector<std::string>&)>;
    void registerCommand(const std::string& name, CommandFunc func) {
        commands[name] = func;
    }
    void execute(const std::string& name, const std::vector<std::string>& args) {
        if (commands.count(name)) {
            commands[name](args);
        } else {
            std::cout << "❌ Native command '" << name << "' not found.\n";
        }
    }
private:
    std::map<std::string, CommandFunc> commands;
};

#include "../tooling/repl/Repl.h"
#include "../standard_library/filesystem/FileSystem.h"
#include "../standard_library/math/MathLib.h"
#include "../standard_library/networking/Network.h"
#include "../standard_library/ai/AILib.h"
#include "../standard_library/robotics/RoboticsLib.h"
#include "../standard_library/database/DatabaseLib.h"
#include "../runtime/vm/VM.h"

std::unordered_map<std::string, std::string> globalMemory;
std::unordered_map<std::string, FunctionDeclStmt*> userFunctions;
struct ReturnValueException { std::string value; };

void evaluateAST(const std::vector<std::unique_ptr<Stmt>>& statements, CommandRegistry& registry);

std::string evaluateExpression(Expr* expr, CommandRegistry& registry) {
    if (auto lit = dynamic_cast<LiteralExpr*>(expr)) return lit->value;
    if (auto id = dynamic_cast<IdentifierExpr*>(expr)) {
        if (globalMemory.count(id->name)) return globalMemory[id->name];
        throw std::runtime_error("ReferenceError: '" + id->name + "' is not defined.");
    }
    
    if (auto callExpr = dynamic_cast<CallExpr*>(expr)) {
        std::vector<std::string> stringArgs;
        for (const auto& arg : callExpr->arguments) stringArgs.push_back(evaluateExpression(arg.get(), registry));
        
        if (userFunctions.count(callExpr->commandPath)) {
            auto func = userFunctions[callExpr->commandPath];
            for (size_t i = 0; i < func->params.size(); i++) globalMemory[func->params[i]] = stringArgs[i];
            try { evaluateAST(func->body->statements, registry); } 
            catch (const ReturnValueException& ret) { return ret.value; }
            return "undefined";
        } else {
            registry.execute(callExpr->commandPath, stringArgs);
            return "executed"; 
        }
    }
    
    if (auto bin = dynamic_cast<BinaryExpr*>(expr)) {
        std::string leftVal = evaluateExpression(bin->left.get(), registry);
        std::string rightVal = evaluateExpression(bin->right.get(), registry);
        try {
            double l = std::stod(leftVal); double r = std::stod(rightVal);
            if (bin->op == "+") return std::to_string(l + r);
            if (bin->op == "-") return std::to_string(l - r);
            if (bin->op == "*") return std::to_string(l * r);
            if (bin->op == "/") { if (r == 0) throw std::runtime_error("MathError: Division by zero."); return std::to_string(l / r); }
        } catch (...) {
            if (bin->op == "+") return leftVal + rightVal;
            throw std::runtime_error("TypeError: Unsupported operation for strings.");
        }
    }
    return "undefined";
}

void evaluateAST(const std::vector<std::unique_ptr<Stmt>>& statements, CommandRegistry& registry) {
    for (const auto& stmt : statements) {
        if (auto funcDecl = dynamic_cast<FunctionDeclStmt*>(stmt.get())) {
            userFunctions[funcDecl->name] = funcDecl;
        }
        else if (auto varDecl = dynamic_cast<VarDeclStmt*>(stmt.get())) {
            globalMemory[varDecl->name] = evaluateExpression(varDecl->initializer.get(), registry);
        }
        else if (auto retStmt = dynamic_cast<ReturnStmt*>(stmt.get())) {
            throw ReturnValueException{evaluateExpression(retStmt->value.get(), registry)};
        }
        else if (auto exprStmt = dynamic_cast<ExprStmt*>(stmt.get())) {
            if (auto callExpr = dynamic_cast<CallExpr*>(exprStmt->expr.get())) {
                evaluateExpression(exprStmt->expr.get(), registry);
            } else {
                std::string result = evaluateExpression(exprStmt->expr.get(), registry);
                if(result.find('.') != std::string::npos) {
                    result.erase(result.find_last_not_of('0') + 1, std::string::npos);
                    if(result.back() == '.') result.pop_back();
                }
                std::cout << result << "\n";
            }
        }
    }
}

int main(int argc, char* argv[]) {
    CommandRegistry registry;
    registry.registerCommand("Nova.show", [](const auto& args) { for (const auto& a : args) std::cout << a << " "; std::cout << "\n"; });
    registry.registerCommand("Nova.log.info", [](const auto& args) { std::cout << "ℹ️ [NeuraLog™] "; for (const auto& a : args) std::cout << a << " "; std::cout << "\n"; });

    // Dummy registrations for backward compatibility
    registry.registerCommand("Nova.file.read", FileSystem::read);
    registry.registerCommand("Nova.file.write", FileSystem::write);
    registry.registerCommand("Nova.math.pow", MathLib::power);
    registry.registerCommand("Nova.network.ping", NetworkLib::ping);
    registry.registerCommand("Nova.ai.think", AILib::think);
    registry.registerCommand("Nova.robot.connect", RoboticsLib::connect);
    registry.registerCommand("Nova.database.connect", DatabaseLib::connect);

    if (argc == 1) {
        REPL::start(registry);
    } 
    else if (argc >= 2) {
        std::string cmd = argv[1];
        std::string filename = "";
        
        if (cmd == "init") {
            std::cout << "⚡ [NovaLex™] Triggering NeuraCLI™...\n";
            filename = "tooling/cli/NeuraCLI.nv";
        } 
        else if (cmd == "push") {
            std::cout << "🌐 [NeuraGit™] Connecting Termux to NovaCloud & Website...\n";
            filename = "tooling/git_bridge/NeuraGit.nv";
        }
        else if (cmd == "run" && argc >= 3) {
            filename = argv[2]; 
            std::cout << "⚡ [NovaLex™] Lexical Engine Scanning...\n";
            std::cout << "🌳 [NeuraParse™] Building Syntax Tree...\n";
            std::cout << "🔥 [NeuraVM™] Accelerating Execution to 0.01ms...\n";
            std::cout << "-------------------------------------------\n";
        }
        else {
            filename = cmd;
        }

        std::ifstream file(filename);
        if (!file.is_open()) { std::cerr << "Error: Could not open or find file: " << filename << "\n"; return 1; }
        std::stringstream buffer; buffer << file.rdbuf();
        Lexer lexer(buffer.str()); Parser parser(lexer.tokenize());
        auto ast = parser.parse(); evaluateAST(ast->statements, registry);
    }
    return 0;
}
