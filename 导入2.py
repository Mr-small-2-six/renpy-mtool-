import os
import re
import json

# 获取当前文件夹路径
folder_path = os.getcwd()

# 读取翻译文本的JSON文件
json_file_path = os.path.join(folder_path, 'TrsData.json')
with open(json_file_path, 'r', encoding='utf-8') as file:
    translations = json.load(file)

# 遍历文件夹中的所有RPY文件
rpy_files = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.rpy'):
            # 拼接子文件夹的路径和文件名
            file_path = os.path.join(root, file)
            rpy_files.append(file_path)

# 更新翻译文本
for rpy_file in rpy_files:
    with open(rpy_file, 'r', encoding='utf-8') as file:
        rpy_content = file.read()

    new_content = []
    lines = rpy_content.splitlines()

    for line in lines:
        # 匹配双引号内的文本
        match = re.search(r'"(.*?)"', line)
        if match:
            text = match.group(1)
            if text.strip() == "":
                # 如果文本是空白，就找到上一行的原始文本
                old_text_line = new_content[-1]
                old_text = old_text_line.split('"')[1]
                if old_text.strip() in translations:
                    # 如果原始文本有翻译，就替换掉空白文本
                    new_text = translations[old_text.strip()]
                    line = line.replace('""', '"{}"'.format(new_text))
                    if line.endswith('\\'):
                        line += ' '  # 添加一个空格来避免错误
                    print(old_text, new_text, line)
        new_content.append(line)

    # 保存更新后的RPY文件
    with open(rpy_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_content))

print("翻译文本导入成功！")
