import os

parent_directory = os.path.dirname(__file__)
source_directory = os.path.join(parent_directory, 'walk_example')
output_file = "combined_files.txt"

with open(output_file, 'w') as combined_file:
    for dirpath, dirnames, filenames in os.walk(source_directory):
        for file in filenames:
            if file.endswith('.txt'):
                file_path = os.path.join(dirpath, file)
                if os.path.getsize(file_path) <= 120:
                    with open(file_path, 'r') as text_file:
                        content = text_file.read()
                        combined_file.write(f"Filename: {file}\n")
                        combined_file.write(f"Content:\n{content}\n")




