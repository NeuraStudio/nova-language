#pragma once
#include <string>
#include <vector>
#include <memory>

struct ASTNode { virtual ~ASTNode() = default; };

struct Expr : public ASTNode {};
struct LiteralExpr : public Expr { std::string value; LiteralExpr(std::string v) : value(v) {} };
struct IdentifierExpr : public Expr { std::string name; IdentifierExpr(std::string n) : name(n) {} };

struct BinaryExpr : public Expr {
    std::string op;
    std::unique_ptr<Expr> left, right;
    BinaryExpr(std::unique_ptr<Expr> l, std::string o, std::unique_ptr<Expr> r)
        : left(std::move(l)), op(o), right(std::move(r)) {}
};

struct CallExpr : public Expr {
    std::string commandPath;
    std::vector<std::unique_ptr<Expr>> arguments;
    CallExpr(std::string p, std::vector<std::unique_ptr<Expr>> a) : commandPath(p), arguments(std::move(a)) {}
};

struct Stmt : public ASTNode {};
struct ExprStmt : public Stmt { std::unique_ptr<Expr> expr; ExprStmt(std::unique_ptr<Expr> e) : expr(std::move(e)) {} };

struct VarDeclStmt : public Stmt {
    std::string name;
    std::unique_ptr<Expr> initializer;
    VarDeclStmt(std::string n, std::unique_ptr<Expr> i) : name(n), initializer(std::move(i)) {}
};

// --- NEW AST NODES FOR CONTROL FLOW ---
struct BlockStmt : public Stmt {
    std::vector<std::unique_ptr<Stmt>> statements;
    BlockStmt(std::vector<std::unique_ptr<Stmt>> stmts) : statements(std::move(stmts)) {}
};

struct IfStmt : public Stmt {
    std::unique_ptr<Expr> condition;
    std::unique_ptr<Stmt> thenBranch;
    std::unique_ptr<Stmt> elseBranch;
    IfStmt(std::unique_ptr<Expr> cond, std::unique_ptr<Stmt> thenB, std::unique_ptr<Stmt> elseB)
        : condition(std::move(cond)), thenBranch(std::move(thenB)), elseBranch(std::move(elseB)) {}
};

struct Program : public ASTNode { std::vector<std::unique_ptr<Stmt>> statements; };

// --- NEW AST NODES FOR LOOPS ---
struct WhileStmt : public Stmt {
    std::unique_ptr<Expr> condition;
    std::unique_ptr<Stmt> body;
    WhileStmt(std::unique_ptr<Expr> cond, std::unique_ptr<Stmt> b)
        : condition(std::move(cond)), body(std::move(b)) {}
};

struct ForStmt : public Stmt {
    std::string varName;
    std::unique_ptr<Expr> startExpr;
    std::unique_ptr<Expr> endExpr;
    std::unique_ptr<Stmt> body;
    ForStmt(std::string vName, std::unique_ptr<Expr> start, std::unique_ptr<Expr> end, std::unique_ptr<Stmt> b)
        : varName(vName), startExpr(std::move(start)), endExpr(std::move(end)), body(std::move(b)) {}
};

// --- NEW AST NODE FOR ERROR HANDLING ---
struct TryCatchStmt : public Stmt {
    std::unique_ptr<Stmt> tryBlock;
    std::string errorVarName;
    std::unique_ptr<Stmt> catchBlock;
    std::unique_ptr<Stmt> finallyBlock; // Optional
    
    TryCatchStmt(std::unique_ptr<Stmt> tBlock, std::string errName, std::unique_ptr<Stmt> cBlock, std::unique_ptr<Stmt> fBlock)
        : tryBlock(std::move(tBlock)), errorVarName(errName), catchBlock(std::move(cBlock)), finallyBlock(std::move(fBlock)) {}
};

// --- NEW AST NODES FOR FUNCTIONS ---
struct FunctionDeclStmt : public Stmt {
    std::string name;
    std::vector<std::string> params;
    std::unique_ptr<BlockStmt> body;
    
    FunctionDeclStmt(std::string n, std::vector<std::string> p, std::unique_ptr<BlockStmt> b)
        : name(n), params(std::move(p)), body(std::move(b)) {}
};

struct ReturnStmt : public Stmt {
    std::unique_ptr<Expr> value;
    ReturnStmt(std::unique_ptr<Expr> v) : value(std::move(v)) {}
};

// --- NEW AST NODES FOR COLLECTIONS ---
struct ArrayExpr : public Expr {
    std::vector<std::unique_ptr<Expr>> elements;
    ArrayExpr(std::vector<std::unique_ptr<Expr>> elms) : elements(std::move(elms)) {}
};

struct ObjectExpr : public Expr {
    std::vector<std::pair<std::string, std::unique_ptr<Expr>>> properties;
    ObjectExpr(std::vector<std::pair<std::string, std::unique_ptr<Expr>>> props) : properties(std::move(props)) {}
};
