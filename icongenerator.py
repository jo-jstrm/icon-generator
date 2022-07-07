import argparse
from pathlib import Path
from PIL import Image

def _get_args():
    parser = argparse.ArgumentParser(description = '''Convert a .png to .icon and .icns''',epilog="")
    parser.add_argument('--source', type=str, default=".", help='Path to the background.png')
    parser.add_argument('--target', type=str, default="", help='Output directory. Icon iles will be created there.')
    return parser.parse_args()

def main():
    args = _get_args()
    filename = args.source
    icon_sizes = [(16,16), (32, 32), (48, 48), (64,64)]
    # For Windows
    icon = Image.open(Path(filename))
    icon.save(Path(f'{args.target}/icon.ico'), sizes=icon_sizes)
    # For Mac/Linux
    icon.save(Path(f'{args.target}/icon.icns'), sizes=icon_sizes)

if __name__ == '__main__':
    main()