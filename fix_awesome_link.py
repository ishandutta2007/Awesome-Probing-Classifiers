import os

readme_path = "C:/Users/ishan/Documents/Projects/Awesome-Probing-Classifiers/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("https://github.com/sindresorhus/awesome", "https://github.com/ishandutta2007/Awesome-Awesome-Awesome")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced awesome link")
