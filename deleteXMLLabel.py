import os


def remove_xml_declaration(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            xml_file_path = os.path.join(directory, filename)

            with open(xml_file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            if content and content[0].startswith('<?xml'):
                content.pop(0)

            with open(xml_file_path, 'w', encoding='utf-8') as file:
                file.writelines(content)

            print(f'Removed XML declaration from: "{filename}"')


directory_path = r'you own path'
remove_xml_declaration(directory_path)