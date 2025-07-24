import os

def list_files_and_folders(root_dir, output_file, exclude_dirs=None):
    total_files = 0
    exclude_dirs = set(exclude_dirs or [])

    with open(output_file, 'w', encoding='utf-8') as f:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Modify dirnames in-place to skip excluded directories
            dirnames[:] = [d for d in dirnames if d not in exclude_dirs]

            # Indentation for nested folders
            level = dirpath.replace(root_dir, '').count(os.sep)
            indent = ' ' * 4 * level
            f.write(f'{indent}[Folder] {os.path.basename(dirpath)}\n')

            subindent = ' ' * 4 * (level + 1)
            for filename in filenames:
                f.write(f'{subindent}{filename}\n')
                total_files += 1
        f.write(f'Total number of files: {total_files}')

    print(f'Total number of files: {total_files}')

# Example usage
root_directory = r'D:\\Work\\TherapyPlatformSravya'  # Change this to your directory
output_text_file = 'folder_structure.txt'

list_files_and_folders(root_directory, output_text_file, exclude_dirs={'.git','node_modules'})
