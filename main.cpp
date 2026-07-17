#include <iostream>
#include <unordered_map>
#include <string>
#include "compiler/lexer/Lexer.h"
#include "compiler/parser/Parser.h"
#include "runtime/registry/Registry.h"

std::unordered_map<std::string, std::string> globalMemory;
std::unordered_map<std::string, FunctionDeclStmt*> userFunctions;
struct ReturnValueException { std::string value; };

void evaluateAST(const std::vector<std::unique_ptr<Stmt>>& statements, CommandRegistry& registry) {
    for (const auto& stmt : statements) {
        if (auto funcDecl = dynamic_cast<FunctionDeclStmt*>(stmt.get())) {
            userFunctions[funcDecl->name] = funcDecl; 
        }
        else if (auto varDecl = dynamic_cast<VarDeclStmt*>(stmt.get())) {
            if (auto lit = dynamic_cast<LiteralExpr*>(varDecl->initializer.get())) {
                globalMemory[varDecl->name] = lit->value;
            } else if (auto arr = dynamic_cast<ArrayExpr*>(varDecl->initializer.get())) {
                globalMemory[varDecl->name] = "[Array with " + std::to_string(arr->elements.size()) + " items]";
            } else if (auto obj = dynamic_cast<ObjectExpr*>(varDecl->initializer.get())) {
                globalMemory[varDecl->name] = "{Object with " + std::to_string(obj->properties.size()) + " keys}";
            }
        }
        else if (auto exprStmt = dynamic_cast<ExprStmt*>(stmt.get())) {
            if (auto callExpr = dynamic_cast<CallExpr*>(exprStmt->expr.get())) {
                std::vector<std::string> stringArgs;
                for (const auto& arg : callExpr->arguments) {
                    if (auto lit = dynamic_cast<LiteralExpr*>(arg.get())) stringArgs.push_back(lit->value);
                    else if (auto id = dynamic_cast<IdentifierExpr*>(arg.get())) stringArgs.push_back(globalMemory[id->name]);
                }
                
                if (userFunctions.count(callExpr->commandPath)) {
                    auto func = userFunctions[callExpr->commandPath];
                    for (size_t i = 0; i < func->params.size(); i++) globalMemory[func->params[i]] = stringArgs[i];
                    evaluateAST(func->body->statements, registry);
                } else {
                    registry.execute(callExpr->commandPath, stringArgs);
                }
            }
        }
    }
}

int main() {
    CommandRegistry registry;
    registry.registerCommand("Nova.show", [](const std::vector<std::string>& args) {
        for (const auto& arg : args) std::cout << arg << " ";
        std::cout << "\n";
    });

    // Final Phase 1 Code Test (Functions, Arrays, Objects, Memory)
    std::string sourceCode = 
        "function Welcome(person) {\n"
        "    Nova.show(\"Welcome to Nova OS,\", person)\n"
        "}\n"
        "name = \"Javed\"\n"
        "Welcome(name)\n"
        "players = [\"Javed\", \"Ali\", \"Khan\"]\n"
        "user = { role: \"CEO\", company: \"Neura Studio\" }\n"
        "Nova.show(\"Loaded Players:\", players)\n"
        "Nova.show(\"Loaded User Profile:\", user)\n";

    std::cout << "--- Nova: The Apex Language Engine (Phase 1 Complete) ---\n";
    
    Lexer lexer(sourceCode);
    Parser parser(lexer.tokenize());
    auto ast = parser.parse();

    evaluateAST(ast->statements, registry);
    return 0;
}
