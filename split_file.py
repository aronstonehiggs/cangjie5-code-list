def split_file(input_file, start_line=44, lines_per_file=100):
    split_files = []
    
    with open(input_file, 'r') as file:
        # Skip to the starting line
        for _ in range(start_line - 1):
            next(file)
        
        line_count = 0
        file_count = 1
        output_file = None
        
        for line in file:
            if line_count % lines_per_file == 0:
                if output_file:  # Close the previous file if it's open
                    output_file.close()
                output_filename = f'cangjie5_dict_{file_count}.txt'
                output_file = open(output_filename, 'w')
                split_files.append(output_filename)  # Add to the list of split files
                file_count += 1
            
            output_file.write(line)
            line_count += 1
        
        if output_file:  # Close the last file if it was opened
            output_file.close()
    
    return split_files

def append_to_readme(split_files):
    with open('README.md', 'a') as readme:
        readme.write("\n## Split Files\n")
        readme.write("\n- List of split files:\n")
        for filename in split_files:
            readme.write(f"  - [{filename}](./{filename})\n")

# Example usage
split_files = split_file('cangjie5.dict.yaml', start_line=44, lines_per_file=100)
append_to_readme(split_files)

