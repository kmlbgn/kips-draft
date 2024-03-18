import os

kip_directory = 'kips/'
readme_header_path = 'includes/README_header.md'  # File containing the header content
readme_footer_path = 'includes/README_footer.md'  # File containing the footer content
readme_path = 'README.md'

# Fetch the list of KIP files
kip_files = [f for f in os.listdir(kip_directory) if os.path.isfile(os.path.join(kip_directory, f))]

# Read the header content
with open(readme_header_path, 'r') as header_file:
    header_content = header_file.readlines()

# Read the footer content
with open(readme_footer_path, 'r') as footer_file:
    footer_content = footer_file.readlines()

# Generate the list of new KIP entries
kip_entries = [f"- {kip_file.replace('.md', '')}\n" for kip_file in kip_files]

# Combine the header, KIP entries, and footer with a line of space between them
updated_content = header_content + ['\n'] + kip_entries + ['\n'] + footer_content

# Log the updated content
print("Updated content:")
print(updated_content)

# Write the updated README content
with open(readme_path, 'w') as readme_file:
    readme_file.writelines(updated_content)

print("README updated successfully.")
