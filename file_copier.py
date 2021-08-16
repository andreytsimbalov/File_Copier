import os
import xml.etree.ElementTree as ElementTree
import shutil


def file_copier(file_xml):
    tree = ElementTree.parse(file_xml)
    root = tree.getroot()
    for child in root:
        file = child.attrib
        source_path = os.path.join(file['source_path'], file['file_name'])
        destination_path = os.path.join(file['destination_path'], file['file_name'])

        if not os.path.exists(source_path):
            print("File in source_path not found")
        elif not os.path.exists(file['destination_path']):
            print("destination_path not found")
        else:
            try:
                shutil.copy(source_path, destination_path)
                print("File copied successfully.")
            except shutil.SameFileError:
                print("Source and destination represents the same file.")
            except PermissionError:
                print("Permission denied.")


if __name__ == "__main__":
    file_copier("config.xml")
