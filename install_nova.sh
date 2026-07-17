#!/bin/bash
echo "🚀 Installing Nova Engine (By Neura Studio)..."

# Compile the compiler we just built with maximum optimization
clang++ -std=c++17 -O3 main.cpp -o nova

# Install globally in Termux (or Linux)
if [ -d "$PREFIX/bin" ]; then
    mv nova $PREFIX/bin/nova
    chmod +x $PREFIX/bin/nova
else
    sudo mv nova /usr/local/bin/nova
    sudo chmod +x /usr/local/bin/nova
fi

echo "✅ Nova Engine Installed Successfully!"
echo "🔥 Type 'nova' in your terminal or VS Code to start!"
