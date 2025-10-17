import os, shutil
from copystatic import copy_content
from textnode import TextNode, TextType


def main():
    print("Deleting public directory...")
    if os.path.exists("./public"):
        shutil.rmtree("./public")

    print("Copying static files to public directory...")
    copy_content("./static", "./public")



main()
