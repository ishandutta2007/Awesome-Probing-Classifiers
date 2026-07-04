import os

readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Probing-Classifiers/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

badge_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

content = content.replace(
    'alt="Discord" /></a>', 
    f'alt="Discord" /></a>{badge_right}'
)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added badge to right.")
