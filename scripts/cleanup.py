import os
from sys import argv
from pathlib import Path


def main():
    content = ""
    for note in Path(argv[1]).glob('*.md'):
        content += note.open().read()
    for img in Path(argv[1]+"/src").glob("*"):
        if img.name not in content:
            os.remove(img)


if __name__ == '__main__':
    main()
