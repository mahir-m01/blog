import os
import re
import shutil
import urllib.parse

# Paths
posts_dir = "/Users/mahir/Documents/Obsidian Vault/8 - Website/posts/"
images_dir = "/Users/mahir/Documents/Obsidian Vault/Images"
static_images_dir = "/Users/mahir/Documents/blog/static/images"

# Ensure Hugo static images folder exists
os.makedirs(static_images_dir, exist_ok=True)

# Process each markdown file
for filename in os.listdir(posts_dir):
    if not filename.endswith(".md"):
        continue

    filepath = os.path.join(posts_dir, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

    # Match ![[image.png]] or [[image.png]]
    pattern = r'(!?)\[\[([^\]]+\.(png|jpg|jpeg|gif|svg))\]\]'
    matches = re.findall(pattern, content)

    for prefix, image_name, ext in matches:
        full_match = f"{prefix}[[{image_name}]]"

        # URL-encode spaces for Hugo
        encoded_name = urllib.parse.quote(image_name)
        markdown_image = f"![{image_name}](/images/{encoded_name})"

        # Replace wiki link with standard Markdown
        content = content.replace(full_match, markdown_image)

        # Copy image to Hugo static folder if it exists
        image_source = os.path.join(images_dir, image_name)
        if os.path.exists(image_source):
            shutil.copy(image_source, static_images_dir)
        else:
            print(f"Warning: {image_source} not found!")

    # Write updated content back to file
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

print("Markdown files processed and images copied successfully.")
