import imageio
import numpy as np
import matplotlib.pyplot as plt
import os

chosen_directory = ""
os.chdir(chosen_directory)

chosen_image = 'avg_image_3_DyIG_60k_fusedSi.tiff'
img = imageio.imread(chosen_image)
img = np.squeeze(img)

dir_name = "New_Data"
parent_path = "C:\\Users\\chmer\\Desktop\\"
path = os.path.join(parent_path, dir_name)
os.mkdir(path)

def save_image(image, filename):
    plt.imshow(image, cmap='gray')  # Assuming default colormap is 'gray' for single-channel images
    plt.axis('off')
    plt.savefig(os.path.join(path, filename))
    plt.close()  # Close the current figure to free up resources

# Rotates image with 90-degree increments
def rotate(image):
    for num in range(0, 4):
        rotated_img = np.rot90(image, k=num)
        save_image(rotated_img, f'angle_{num*90}_image.tif')

# Rotates and recolors image
def rotate_and_recolor(image):
    colormaps = ['binary']
    for num in range(1, 4):
        rotated_img = np.rot90(image, k=num)
        for cmap_name in colormaps:
            save_image(rotated_img, f'rotated_{num*90}_{cmap_name}_image.tif')

# Recolors image
def recolor(image):
    colormaps = ['binary']
    for cmap_name in colormaps:
        save_image(image, f'{cmap_name}_image.tif')

# Function to break the image into quadrants
def break_into_quadrants(image):
    height, width = image.shape
    mid_height = height // 2
    mid_width = width // 2

    quadrants = [
        image[:mid_height, :mid_width],  # Top left
        image[:mid_height, mid_width:],  # Top right
        image[mid_height:, :mid_width],  # Bottom left
        image[mid_height:, mid_width:]   # Bottom right
    ]

    return quadrants

# Crops and recolors image quadrants
def crop_and_recolor(image):
    quadrants = break_into_quadrants(image)

    for i, quadrant in enumerate(quadrants):
        colormaps = ['Greys']
        for cmap_name in colormaps:
            save_image(quadrant, f'{cmap_name}_quadrant_{i+1}.tif')


'''['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone',
                      'pink', 'spring', 'summer', 'autumn', 'winter', 'cool',
                      'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper', 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu',
                      'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic','Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
                      'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
                      'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn','twilight', 'twilight_shifted', 'hsv', 'ocean', 'gist_earth', 'terrain',
                      'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
                      'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet',
                      'turbo', 'nipy_spectral', 'gist_ncar']'''