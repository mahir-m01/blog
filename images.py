import os
import re
import shutil
import urllib.parse

# Paths
hugo_posts_dir = "/Users/mahir/Documents/blog/content/posts/"
images_dir = "/Users/mahir/Documents/Obsidian Vault/Images"
hugo_static_images_dir = "/Users/mahir/Documents/blog/static/images"

# Ensure Hugo static images folder exists
os.makedirs(hugo_static_images_dir, exist_ok=True)

# Process each markdown file in Hugo's content/posts folder
for filename in os.listdir(hugo_posts_dir):
    if not filename.endswith(".md"):
        continue

    hugo_filepath = os.path.join(hugo_posts_dir, filename)

    with open(hugo_filepath, "r", encoding="utf-8") as file:
        content = file.read()

    # Match ![[image.png]] or [[image.png]] (from copied Obsidian notes)
    pattern = r'(!?)\[\[([^\]]+\.(png|jpg|jpeg|gif|svg))\]\]'
    matches = re.findall(pattern, content)

    for prefix, image_name, ext in matches:
        full_match = f"{prefix}[[{image_name}]]"

        # URL-encode spaces for Hugo
        encoded_name = urllib.parse.quote(image_name)
        markdown_image = f"![{image_name}](/images/{encoded_name})"

        # Replace wiki-style link with standard Markdown
        content = content.replace(full_match, markdown_image)

        # Copy image from Obsidian Images folder to Hugo static/images
        image_source = os.path.join(images_dir, image_name)
        if os.path.exists(image_source):
            shutil.copy(image_source, hugo_static_images_dir)
        else:
            print(f"Warning: {image_source} not found!")

    # Write the updated content back to Hugo post file
    with open(hugo_filepath, "w", encoding="utf-8") as file:
        file.write(content)

print("Hugo markdown files processed and images copied successfully.")
