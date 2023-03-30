import os
from osgeo import gdal
from PIL import Image

def process_geotiff(input_path, output_folder):
    tile_size = 1024

    # Open the input GEOTIFF file using GDAL
    dataset = gdal.Open(input_path)
    width = dataset.RasterXSize
    height = dataset.RasterYSize

    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for x_offset in range(0, width, tile_size):
        for y_offset in range(0, height, tile_size):
            tile_width = min(tile_size, width - x_offset)
            tile_height = min(tile_size, height - y_offset)

            # Read the data from the GEOTIFF file for the current tile
            data = dataset.ReadAsArray(x_offset, y_offset, tile_width, tile_height)

            # Create a new PIL Image with the same number of bands as the input image
            image = Image.fromarray(data[0], mode='L')
            for band_index in range(1, dataset.RasterCount):
                band_data = Image.fromarray(data[band_index], mode='L')
                image = Image.merge('RGBA' if dataset.RasterCount == 4 else 'RGB', (image, band_data))

            # Save the tile as a PNG file
            tile_filename = f'tile_{x_offset}_{y_offset}.png'
            tile_output_path = os.path.join(output_folder, tile_filename)
            image.save(tile_output_path)