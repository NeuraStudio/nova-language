#pragma once
#include "Token.h"
#include <string>
#include <vector>
#include <cctype>

class Lexer {
private:
    std::string source;
    size_t pos = 0;
    int line = 1;

    char peek() { return pos < source.length() ? source[pos] : '\0'; }
    char peekNext() { return pos + 1 < source.length() ? source[pos+1] : '\0'; }
    char advance() { return pos < source.length() ? source[pos++] : '\0'; }

public:
    Lexer(const std::string& src) : source(src) {}

    std::vector<Token> tokenize() {
        std::vector<Token> tokens;
        while (pos < source.length()) {
            char c = peek();
            if (std::isspace(c)) { if (c == '\n') line++; advance(); }
            else if (c == '/' && peekNext() == '/') { while (peek() != '\n' && peek() != '\0') advance(); }
            else if (c == '/' && peekNext() == '*') { advance(); advance(); while (!(peek() == '*' && peekNext() == '/') && peek() != '\0') advance(); advance(); advance(); }
            else if (c == '#') { while (peek() != '\n' && peek() != '\0') advance(); }
            else if (std::isalpha(c) || c == '_') {
                std::string id;
                while (std::isalnum(peek()) || peek() == '_') id += advance();
                if (id == "if") tokens.push_back({TokenType::If, id, line});
                else if (id == "else") tokens.push_back({TokenType::Else, id, line});
                else if (id == "while") tokens.push_back({TokenType::While, id, line});
                else if (id == "for") tokens.push_back({TokenType::For, id, line});
                else if (id == "to") tokens.push_back({TokenType::To, id, line});
                else if (id == "try") tokens.push_back({TokenType::Try, id, line});
                else if (id == "catch") tokens.push_back({TokenType::Catch, id, line});
                else if (id == "finally") tokens.push_back({TokenType::Finally, id, line});
                else if (id == "function") tokens.push_back({TokenType::Function, id, line});
                else if (id == "return") tokens.push_back({TokenType::Return, id, line});
                else tokens.push_back({TokenType::Identifier, id, line});
            }
            else if (std::isdigit(c)) {
                std::string num; while (std::isdigit(peek())) num += advance();
                tokens.push_back({TokenType::Number, num, line});
            }
            else if (c == '"') {
                advance(); std::string str; while (peek() != '"' && peek() != '\0') str += advance(); advance();
                tokens.push_back({TokenType::String, str, line});
            }
            else if (c == '=' && peekNext() == '=') { advance(); advance(); tokens.push_back({TokenType::EqEq, "==", line}); }
            else if (c == '=') { advance(); tokens.push_back({TokenType::Equals, "=", line}); }
            else if (c == '<') { advance(); tokens.push_back({TokenType::Less, "<", line}); }
            else if (c == '>') { advance(); tokens.push_back({TokenType::Greater, ">", line}); }
            else if (c == '+') { advance(); tokens.push_back({TokenType::Plus, "+", line}); }
            else if (c == '-') { advance(); tokens.push_back({TokenType::Minus, "-", line}); }
            else if (c == '*') { advance(); tokens.push_back({TokenType::Star, "*", line}); }
            else if (c == '/') { advance(); tokens.push_back({TokenType::Slash, "/", line}); }
            else if (c == '{') { advance(); tokens.push_back({TokenType::LBrace, "{", line}); }
            else if (c == '}') { advance(); tokens.push_back({TokenType::RBrace, "}", line}); }
            else if (c == '[') { advance(); tokens.push_back({TokenType::LBracket, "[", line}); }
            else if (c == ']') { advance(); tokens.push_back({TokenType::RBracket, "]", line}); }
            else if (c == ':') { advance(); tokens.push_back({TokenType::Colon, ":", line}); }
            else if (c == '.') { advance(); tokens.push_back({TokenType::Dot, ".", line}); }
            else if (c == '(') { advance(); tokens.push_back({TokenType::LParen, "(", line}); }
            else if (c == ')') { advance(); tokens.push_back({TokenType::RParen, ")", line}); }
            else if (c == ',') { advance(); tokens.push_back({TokenType::Comma, ",", line}); }
            else { advance(); tokens.push_back({TokenType::Unknown, std::string(1, c), line}); }
        }
        tokens.push_back({TokenType::EndOfFile, "", line});
        return tokens;
    }
};
