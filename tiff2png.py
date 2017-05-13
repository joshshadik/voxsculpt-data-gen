import argparse
import png
import os
from PIL import Image


def convertAll(source_dir, dest_dir):
    os.makedirs(dest_dir)

    for tiff_file in os.listdir(source_dir):
        tiff_path = os.path.join(source_dir, tiff_file)
        img = Image.open(tiff_path)
        file_name = os.path.join(dest_dir, '%s.png' % tiff_file)
        img.save(file_name)

    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tile pngs into 1 file")
    parser.add_argument("source_dir", help="Full path to dir with source pngs")
    parser.add_argument("dest_dir", help="Full path to the generated file")

    args = parser.parse_args()

    convertAll(args.source_dir, args.dest_dir)
