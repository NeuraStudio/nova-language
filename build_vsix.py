import os
import zipfile

print("🚀 Bypassing NPM... Building VS Code VSIX package natively via Python...")

# 1. Create necessary directories
os.makedirs("build_vsix/extension/syntaxes", exist_ok=True)

# 2. Package.json
pkg_json = """{
  "name": "nova-language",
  "displayName": "Nova Native Language",
  "description": "Official syntax highlighting for Nova Language by Neura Studio.",
  "version": "1.0.1",
  "publisher": "NeuraStudio",
  "engines": { "vscode": "^1.70.0" },
  "categories": ["Programming Languages"],
  "contributes": {
    "languages": [{ "id": "nova", "extensions": [".nova"], "aliases": ["Nova"] }],
    "grammars": [{ "language": "nova", "scopeName": "source.nova", "path": "./syntaxes/nova.tmLanguage.json" }]
  }
}"""
with open("build_vsix/extension/package.json", "w") as f: f.write(pkg_json)

# 3. Syntax Highlighting JSON
syntax_json = """{
  "scopeName": "source.nova",
  "patterns": [
    { "name": "keyword.control.nova", "match": "\\\\b(async|fn|if|else|import|export)\\\\b" },
    { "name": "support.class.nova", "match": "\\\\bNova\\\\b" },
    { "name": "string.quoted.double.nova", "begin": "\"", "end": "\"" }
  ]
}"""
with open("build_vsix/extension/syntaxes/nova.tmLanguage.json", "w") as f: f.write(syntax_json)

# 4. Content_Types.xml (Required for VSIX)
content_types = """<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="vsixmanifest" ContentType="text/xml" />
  <Default Extension="json" ContentType="application/json" />
</Types>"""
with open("build_vsix/[Content_Types].xml", "w") as f: f.write(content_types)

# 5. extension.vsixmanifest (Required for VSIX)
manifest = """<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011" xmlns:d="http://schemas.microsoft.com/developer/vsx-schema-design/2011">
  <Metadata>
    <Identity Language="en-US" Id="nova-language" Version="1.0.1" Publisher="NeuraStudio"/>
    <DisplayName>Nova Native</DisplayName>
    <Description xml:space="preserve">Official Nova Extension</Description>
  </Metadata>
  <Installation><InstallationTarget Id="Microsoft.VisualStudio.Code"/></Installation>
  <Dependencies/>
  <Assets><Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" /></Assets>
</PackageManifest>"""
with open("build_vsix/extension.vsixmanifest", "w") as f: f.write(manifest)

# 6. Zip it all up into a .vsix file
with zipfile.ZipFile('nova-language-1.0.1.vsix', 'w') as zf:
    for root, dirs, files in os.walk('build_vsix'):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, 'build_vsix')
            zf.write(file_path, arcname)

print("✅ SUCCESS: 'nova-language-1.0.1.vsix' has been generated successfully!")
print("🎯 You can now upload this file directly to the Microsoft VS Code Marketplace.")
