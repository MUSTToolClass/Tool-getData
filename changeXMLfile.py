import os
import xml.etree.ElementTree as ET

def update_xml_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".xml"):
            xml_file_path = os.path.join(directory, filename)

            tree = ET.parse(xml_file_path)
            root = tree.getroot()


            new_filename = f"{os.path.splitext(filename)[0]}.jpg"
            filename_element = root.find('filename')
            if filename_element is not None:
                filename_element.text = new_filename


            path_element = root.find('path')
            if path_element is not None:
                new_path = os.path.join(r"you own path", new_filename)
                path_element.text = new_path

            folder_element = root.find('folder')
            if folder_element is not None:
                folder_element.text = 'JPEGImages'

            tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
            print(f'Updated: "{filename}"')


directory_path = r'you own path'
update_xml_files_in_directory(directory_path)