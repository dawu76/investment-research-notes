#!/bin/bash

BASE_DIR="$HOME/dev/sw-dev-notes/llms"

echo "Starting reorganization of $BASE_DIR..."

# 1. Create the new directory structure
mkdir -p "$BASE_DIR/logs/archive"
mkdir -p "$BASE_DIR/methodology"
mkdir -p "$BASE_DIR/architecture"
mkdir -p "$BASE_DIR/ecosystem"
mkdir -p "$BASE_DIR/playground"

# 2. Move methodology topics
mv "$BASE_DIR/prompt-engineering" "$BASE_DIR/methodology/" 2>/dev/null
mv "$BASE_DIR/fine-tuning" "$BASE_DIR/methodology/" 2>/dev/null
mv "$BASE_DIR/evaluation" "$BASE_DIR/methodology/" 2>/dev/null
mv "$BASE_DIR/tokenization" "$BASE_DIR/methodology/" 2>/dev/null
mv "$BASE_DIR/embeddings" "$BASE_DIR/methodology/" 2>/dev/null

# 3. Move architecture topics
mv "$BASE_DIR/agents" "$BASE_DIR/architecture/" 2>/dev/null
mv "$BASE_DIR/mcp" "$BASE_DIR/architecture/" 2>/dev/null
mv "$BASE_DIR/rag" "$BASE_DIR/architecture/" 2>/dev/null
mv "$BASE_DIR/transformers" "$BASE_DIR/architecture/" 2>/dev/null

# Create frameworks subdir and move the file
mkdir -p "$BASE_DIR/architecture/frameworks"
mv "$BASE_DIR/llm-frameworks.md" "$BASE_DIR/architecture/frameworks/index.md" 2>/dev/null

# 4. Move ecosystem topics
mv "$BASE_DIR/research" "$BASE_DIR/ecosystem/" 2>/dev/null
mv "$BASE_DIR/product-directions" "$BASE_DIR/ecosystem/" 2>/dev/null
mv "$BASE_DIR/product-integrations" "$BASE_DIR/ecosystem/" 2>/dev/null

# Create vendors and products subdirs
mkdir -p "$BASE_DIR/ecosystem/vendors"
mkdir -p "$BASE_DIR/ecosystem/products"
mv "$BASE_DIR/llm-vendor-products"/* "$BASE_DIR/ecosystem/vendors/" 2>/dev/null
rmdir "$BASE_DIR/llm-vendor-products" 2>/dev/null
mv "$BASE_DIR/llm-coding"/* "$BASE_DIR/ecosystem/products/" 2>/dev/null
rmdir "$BASE_DIR/llm-coding" 2>/dev/null

# Move remaining loose industry files
mv "$BASE_DIR/tech-industry" "$BASE_DIR/ecosystem/" 2>/dev/null

# 5. Move playground items
mv "$BASE_DIR/ollama" "$BASE_DIR/playground/" 2>/dev/null

# 6. Archive chronological notes from topic folders
# Find all YYYYMMDD.md files in the new subdirs and move them to logs/archive
find "$BASE_DIR/architecture" "$BASE_DIR/methodology" -name "202[0-9]*.md" -exec mv {} "$BASE_DIR/logs/archive/" \;
mv "$BASE_DIR/notes"/* "$BASE_DIR/logs/archive/" 2>/dev/null
rmdir "$BASE_DIR/notes" 2>/dev/null

# 7. Clean up other loose files into relevant categories
mv "$BASE_DIR/llm-inference.md" "$BASE_DIR/architecture/inference.md" 2>/dev/null
mv "$BASE_DIR/llm-aidata-notes.md" "$BASE_DIR/ecosystem/data-landscape.md" 2>/dev/null
mv "$BASE_DIR/nlp-spacy-notes.md" "$BASE_DIR/methodology/nlp-basics.md" 2>/dev/null

echo "Reorganization complete. Check $BASE_DIR for the new structure."
