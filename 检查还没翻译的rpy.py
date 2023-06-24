import os
import re
import json

# 当前文件夹路径
folder_path = "."

# 定义正则表达式模式，用于匹配翻译文本行
pattern = r'old "(.*)"\n\s*new "(.*)"\n'

# 创建一个空字典来存储提取的文本
translations = {}

# 创建一个空列表来存储未翻译的文件名、文件夹路径和行号
untranslated_files = []

# 遍历当前文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".rpy"):
            # 打开Ren'Py脚本文件并逐行读取内容
            with open(os.path.join(root, filename), 'r', encoding='utf-8') as file:
                content = file.read()

                # 使用正则表达式找到匹配的文本行并提取文本
                matches = re.finditer(pattern, content)

                # 将提取的文本存储到字典中
                for match in matches:
                    old_text = match.group(1)
                    new_text = match.group(2)
                    line_number = content[:match.start()].count("\n") + 1

                    # 如果新文本为空字符串，则将未翻译的文本添加到字典中
                    if not new_text:
                        translations[old_text] = old_text
                        untranslated_files.append((os.path.join(root, filename), line_number))

# 将提取的文本保存为JSON文件
json_file_path = "untranslated.json"
formatted_translations = {k: v.strip() for k, v in translations.items()}
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(formatted_translations, json_file, ensure_ascii=False, indent=4)

# 生成文本日志文件
log_file_path = "untranslated_log.txt"
with open(log_file_path, 'w', encoding='utf-8') as log_file:
    log_file.write("Untranslated files:\n")
    for file, line_number in untranslated_files:
        log_file.write(f"- {file} - {line_number}\n")