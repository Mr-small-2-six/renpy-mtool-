import json
import os

def fix_empty_strings(json_data):
    fixed_data = {}
    report = []

    for line_number, (key, value) in enumerate(json_data.items(), start=1):
        if value.strip() != "":
            fixed_data[key] = value
        else:
            report.append(f'Removed empty string for key "{key}" (Line {line_number})')

    return fixed_data, report

def save_report(report, filename):
    with open(filename, 'w') as file:
        for line in report:
            file.write(line + '\n')

def process_json_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    fixed_data, report = fix_empty_strings(json_data)

    output_filename = f"fixed_{os.path.basename(filename)}"
    with open(output_filename, 'w') as file:
        json.dump(fixed_data, file, indent=4)

    report_filename = f"report_{os.path.basename(filename)}.txt"
    save_report(report, report_filename)

def main():
    json_files = [f for f in os.listdir('.') if f.endswith('.json')]

    for filename in json_files:
        process_json_file(filename)

if __name__ == "__main__":
    main()
