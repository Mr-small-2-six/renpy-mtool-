import os
import re
import json

# 当前文件夹路径
folder_path = "."

# 定义正则表达式模式，用于匹配对话文本行
# 使用非贪婪模式匹配任意字符，包括换行符
# 匹配say语句或translate语句中的第一个或第二个双引号内的文本
pattern = r'(?:say|translate)\s+[^"]*"(.*?)"'

# 创建一个空字典来存储提取的文本
translations = {}

# 遍历当前文件夹中的所有文件
for root, dirs, files in os.walk(folder_path):
    for filename in files:
        if filename.endswith(".rpy"):
            # 打开Ren'Py脚本文件并逐行读取内容
            with open(os.path.join(root, filename), 'r', encoding='utf-8') as file:
                content = file.read()

                # 使用正则表达式找到匹配的文本行并提取文本
                matches = re.findall(pattern, content)

                # 将提取的文本存储到字典中
                for match in matches:
                    text = match
                    # 将文本作为键和值，如果没有翻译，就用原始文本作为值
                    translations[text] = text

# 将提取的文本保存为JSON文件
json_file_path = "translations.json"
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    json.dump(translations, json_file, ensure_ascii=False, indent=4)
