import argparse
import png
import os




def createTiled(source_dir, dest_path, rows, columns):
    rows = int(rows)
    columns = int(columns)
    source_pngs = []
    for source_file in os.listdir(source_dir):
         source_path = os.path.join(source_dir, source_file)
         r=png.Reader( source_path)
         source_pngs.append( r.read() )
    
    img_w = (int)(source_pngs[0][0])
    img_h = (int)(source_pngs[0][1])

    print("using", len(source_pngs), "source images to tile")

    
    dest_data = [None] * rows * img_h

    for d in range(len(dest_data)):
        dest_data[d] = [None] * columns * img_w

    bitdepth = source_pngs[0][3]["bitdepth"]
    
    for r in range(rows):
        for c in range(columns):
            tile = r * columns + c
            pixData = list(source_pngs[tile][2])
            for y in range(img_h):
                for x in range(img_w):
                    iX = ( tile % columns ) * img_w
                    iY = ( tile // columns ) * img_h
                    pix = pixData[y][x]

                    dest_data[iY + y][iX + x] = pix


    f = open(dest_path, 'wb')
    w = png.Writer(img_w * columns, img_h * rows, greyscale=(bitdepth == 8))
    w.write(f, dest_data)
    f.close()
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Tile pngs into 1 file")
    parser.add_argument("png_folder", help="Full path to dir with source pngs")
    parser.add_argument("save_path", help="Full path to the generated file")
    parser.add_argument("columns", help = "columns in tiled png")
    parser.add_argument("rows", help="rows in tiled png")

    args = parser.parse_args()
    print(args)

    createTiled(args.png_folder, args.save_path, args.rows, args.columns )




