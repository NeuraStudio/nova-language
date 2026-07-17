#pragma once
#include <cstdint>

// The Native Bytecode Instructions for Nova (Blazing Fast execution)
enum class OpCode : uint8_t {
    OP_CONSTANT,
    OP_ADD,
    OP_SUBTRACT,
    OP_MULTIPLY,
    OP_DIVIDE,
    OP_PRINT,
    OP_STORE_GLOBAL,
    OP_LOAD_GLOBAL,
    OP_CALL,
    OP_HALT
};
