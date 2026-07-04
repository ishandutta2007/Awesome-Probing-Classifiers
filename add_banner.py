import os
import re

assets_dir = "C:/Users/ishan/Documents/Projects/Awesome-Probing-Classifiers/assets"
os.makedirs(assets_dir, exist_ok=True)

svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200">
  <defs>
    <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#4a90e2;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#9013fe;stop-opacity:1" />
    </linearGradient>
  </defs>
  <rect width="100%" height="100%" fill="url(#grad)" rx="15" ry="15"/>
  <circle cx="100" cy="100" r="40" fill="#ffffff" opacity="0.2">
    <animate attributeName="r" values="40; 60; 40" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="700" cy="100" r="60" fill="#ffffff" opacity="0.1">
    <animate attributeName="r" values="60; 80; 60" dur="3s" repeatCount="indefinite" />
  </circle>
  <text x="50%" y="45%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="42" fill="white" font-weight="bold">Awesome Probing Classifiers</text>
  <text x="50%" y="70%" dominant-baseline="middle" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="white">Exploring the Depths of Neural Networks 🧠</text>
</svg>"""

with open(os.path.join(assets_dir, "banner.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Probing-Classifiers/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Decorate headers with emojis
emojis = {
    "## Probing Classifiers in AI: History, Progression, Variants, & Applications": "## 🚀 Probing Classifiers in AI: History, Progression, Variants, & Applications",
    "## 1. The Macro Chronological Evolution": "## 🕰️ 1. The Macro Chronological Evolution",
    "## 2. Core Functional & Complexity Variants": "## ⚙️ 2. Core Functional & Complexity Variants",
    "## 3. The Probing Classifier Execution Matrix": "## 🛠️ 3. The Probing Classifier Execution Matrix",
    "## 4. Production Engineering Challenges & Mitigations": "## 🚧 4. Production Engineering Challenges & Mitigations",
    "## 5. Frontier Real-World AI Interpretability Applications": "## 🌍 5. Frontier Real-World AI Interpretability Applications",
    "## References": "## 📚 References",
    "# Awesome-Probing-Classifiers": "# 🌟 Awesome-Probing-Classifiers"
}

for old, new in emojis.items():
    content = content.replace(old, new)

# Add banner at the top (after the main title)
banner_html = '\n<div align="center">\n  <img src="assets/banner.svg" alt="Banner" width="100%">\n</div>\n'
content = content.replace("# 🌟 Awesome-Probing-Classifiers\n", f"# 🌟 Awesome-Probing-Classifiers\n{banner_html}")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Generated banner and decorated README with emojis.")
