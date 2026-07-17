#pragma once
#include <string>

enum class TokenType {
    Identifier, String, Number,
    Dot, LParen, RParen, Comma,
    LBrace, RBrace, LBracket, RBracket, Colon, // Added [, ], :
    Equals, EqEq, Less, Greater,
    Plus, Minus, Star, Slash,
    If, Else, While, For, To,
    Try, Catch, Finally, Function, Return,
    EndOfFile, Unknown
};

struct Token {
    TokenType type;
    std::string value;
    int line;
};
