import os

readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Probing-Classifiers/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

seo_text = '\n<p align="center">\n  <strong>A curated list of awesome probing classifiers, diagnostic frameworks, and interpretability resources for deep neural networks. Explore monosemantic features, structural probing, causal interventions, and more!</strong>\n</p>\n'

banner_end = '</div>\n'
insertion = f'\n<div align="center">\n  {badges_left}\n</div>\n{seo_text}'

content = content.replace(banner_end, banner_end + insertion, 1)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added badges to left and SEO text.")
