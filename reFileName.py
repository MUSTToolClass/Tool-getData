import os

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.startswith("VCG"):
            new_filename = filename[len("VCG"):]
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            os.rename(old_file_path, new_file_path)
            print(f'Renamed: "{filename}" to "{new_filename}"')


directory_path = 'you own path'
rename_files_in_directory(directory_path)