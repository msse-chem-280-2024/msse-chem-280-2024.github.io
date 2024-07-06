import os
import re


day = "day6"

def extract_lessons_section(text):
    split = text.split("\n")

    lesson_line = split.index("Lessons")

    list_start = split[lesson_line:].index("")

    lesson_list = split[lesson_line+list_start+1:]

    blank_line = lesson_list.index("")

    lesson_list = lesson_list[:blank_line]

    return [ "../" + x.strip() + ".md" for x in lesson_list ]

def extract_content_from_file(filepath):
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return None

def parse_overview(content):
    # Regex to capture title, objectives, and questions within the overview section
    title_pattern = r"^# (.+)$"
    overview_pattern = r"````\{admonition\} Overview.*?Questions:\n(.*?)\nObjectives:\n(.*?)```"
    
    title = re.search(title_pattern, content, re.MULTILINE)
    overview = re.search(overview_pattern, content, re.DOTALL)

    if title and overview:
        title = title.group(1).strip()
        # Transform each line into a Markdown list item with an asterisk
        questions = "\n".join(f"* {line.strip('- ')}" for line in overview.group(1).strip().splitlines() if line.strip())
        objectives = "\n".join(f"* {line.strip('- ')}" for line in overview.group(2).strip().splitlines() if line.strip())
        return title, objectives, questions
    return None, None, None



def process_files(paths):
    data = []
    for path in paths:
        content = extract_content_from_file(path)
        if content:
            title, objectives, questions = parse_overview(content)
            if title:
                path = path.replace('../', '')

                # Format the title with the path, changing .md to .html
                formatted_title = f"`{title} <{path.replace('.md', '.html')}>`_"
                data.append({'Lesson Title': formatted_title, 'Objectives': objectives, 'Questions': questions})
    return data


def save_to_csv(data, filename=f'{day}.csv'):
    import csv
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Main execution
file_content = ""
with open(f'../{day}.rst', 'r') as file:
    file_content = file.read()
file_paths = extract_lessons_section(file_content)
lesson_data = process_files(file_paths)
save_to_csv(lesson_data)
