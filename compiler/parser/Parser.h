#pragma once
#include "../lexer/Token.h"
#include "../ast/AST.h"
#include <vector>
#include <memory>

class Parser {
private:
    std::vector<Token> tokens;
    size_t current = 0;
    Token peek() { return current < tokens.size() ? tokens[current] : Token{TokenType::EndOfFile, "", 0}; }
    Token previous() { return tokens[current - 1]; }
    bool isAtEnd() { return peek().type == TokenType::EndOfFile; }
    Token advance() { if (!isAtEnd()) current++; return previous(); }
    bool match(TokenType type) { if (isAtEnd() || peek().type != type) return false; advance(); return true; }

public:
    Parser(const std::vector<Token>& tkns) : tokens(tkns) {}
    std::unique_ptr<Program> parse() {
        auto program = std::make_unique<Program>();
        while (!isAtEnd()) {
            if (peek().type == TokenType::Unknown || peek().value == "") { advance(); continue; }
            program->statements.push_back(parseStatement());
        }
        return program;
    }

private:
    std::unique_ptr<Stmt> parseStatement() {
        if (match(TokenType::Function)) {
            match(TokenType::Identifier); std::string name = previous().value;
            match(TokenType::LParen); std::vector<std::string> params;
            if (peek().type != TokenType::RParen) {
                do { match(TokenType::Identifier); params.push_back(previous().value); } while (match(TokenType::Comma));
            }
            match(TokenType::RParen); match(TokenType::LBrace);
            return std::make_unique<FunctionDeclStmt>(name, std::move(params), std::make_unique<BlockStmt>(parseBlock()));
        }
        if (match(TokenType::Return)) return std::make_unique<ReturnStmt>(parseExpression());
        
        if (peek().type == TokenType::Identifier && current + 1 < tokens.size() && tokens[current+1].type == TokenType::Equals) {
            std::string name = advance().value; advance(); // '='
            return std::make_unique<VarDeclStmt>(name, parseExpression());
        }
        return std::make_unique<ExprStmt>(parseExpression());
    }

    std::vector<std::unique_ptr<Stmt>> parseBlock() {
        std::vector<std::unique_ptr<Stmt>> stmts;
        while (!isAtEnd() && peek().type != TokenType::RBrace) stmts.push_back(parseStatement());
        match(TokenType::RBrace); return stmts;
    }

    std::unique_ptr<Expr> parseExpression() {
        auto left = parsePrimary();
        while (match(TokenType::Plus)) {
            std::string op = previous().value; left = std::make_unique<BinaryExpr>(std::move(left), op, parsePrimary());
        } return left;
    }

    std::unique_ptr<Expr> parsePrimary() {
        if (match(TokenType::String) || match(TokenType::Number)) return std::make_unique<LiteralExpr>(previous().value);
        
        // Parse Array: [ 1, 2, "Javed" ]
        if (match(TokenType::LBracket)) {
            std::vector<std::unique_ptr<Expr>> elements;
            if (peek().type != TokenType::RBracket) {
                do { elements.push_back(parseExpression()); } while (match(TokenType::Comma));
            }
            match(TokenType::RBracket);
            return std::make_unique<ArrayExpr>(std::move(elements));
        }

        // Parse Object: { name: "Javed", age: 20 }
        if (match(TokenType::LBrace)) {
            std::vector<std::pair<std::string, std::unique_ptr<Expr>>> props;
            if (peek().type != TokenType::RBrace) {
                do {
                    match(TokenType::Identifier); std::string key = previous().value;
                    match(TokenType::Colon);
                    props.push_back({key, parseExpression()});
                } while (match(TokenType::Comma));
            }
            match(TokenType::RBrace);
            return std::make_unique<ObjectExpr>(std::move(props));
        }

        if (match(TokenType::Identifier)) {
            std::string name = previous().value;
            while (match(TokenType::Dot)) { if (match(TokenType::Identifier)) name += "." + previous().value; }
            if (match(TokenType::LParen)) {
                std::vector<std::unique_ptr<Expr>> args;
                if (peek().type != TokenType::RParen) {
                    do { args.push_back(parseExpression()); } while (match(TokenType::Comma));
                }
                match(TokenType::RParen); return std::make_unique<CallExpr>(name, std::move(args));
            } return std::make_unique<IdentifierExpr>(name);
        }
        advance(); return std::make_unique<LiteralExpr>("ERROR");
    }
};
