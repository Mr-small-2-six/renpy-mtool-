import os
import json

def check_and_fix_chinese_strings(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        translations = json.load(file)

    updated_translations = {}
    for key, value in translations.items():
        if isinstance(value, str):
            fixed_value = value.replace('\\', '\\\\')  # 修复反斜杠转义
            updated_translations[key] = fixed_value

    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(updated_translations, file, ensure_ascii=False, indent=4)

# 获取当前文件夹路径
folder_path = os.getcwd()

# 遍历文件夹中的所有JSON文件
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.json'):
            # 拼接子文件夹的路径和文件名
            file_path = os.path.join(root, file)
            check_and_fix_chinese_strings(file_path)

print("翻译文本检查和修复完成！")