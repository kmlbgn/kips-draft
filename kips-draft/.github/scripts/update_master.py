import os

kip_directory = '../kips/'
readme_path = 'README.md'

# Fetch the list of KIP files
kip_files = [f for f in os.listdir(kip_directory) if os.path.isfile(os.path.join(kip_directory, f))]

# Read the current README content
with open(readme_path, 'r') as file:
    readme_content = file.readlines()

# Find the place in the README to insert the new KIPs
insertion_index = readme_content.index('## KIP List\n') + 1

# Add new KIP entries
for kip_file in kip_files:
    entry = f"- {kip_file.replace('.md', '')}\n"
    if entry not in readme_content:
        readme_content.insert(insertion_index, entry)
        insertion_index += 1

# Write the updated README content
with open(readme_path, 'w') as file:
    file.writelines(readme_content)