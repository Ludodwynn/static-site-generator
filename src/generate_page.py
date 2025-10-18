import os
from markdown_blocks import extract_title, markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        template_content = f.read()

    markdown_html_node = markdown_to_html_node(markdown_content)
    markdown_html = markdown_html_node.to_html()
    markdown_title = extract_title(markdown_content)

    html = template_content.replace("{{ Title }}", markdown_title)
    html = html.replace("{{ Content }}", markdown_html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(html)
