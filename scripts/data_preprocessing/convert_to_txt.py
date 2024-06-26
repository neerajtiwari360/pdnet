import cv2
import numpy as np

def read_and_interleave_image(image_path):
    # Read the image using OpenCV
    image = cv2.imread(image_path)
    
    if image is None:
        raise FileNotFoundError(f"Image file '{image_path}' not found.")
    
    # Check if the image is RGB
    if len(image.shape) != 3 or image.shape[2] != 3:
        raise ValueError("The input image must be an RGB image.")
    
    # Get the height, width, and channels of the image
    height, width, channels = image.shape
    
    # Interleave the channels
    interleaved = image.flatten()
    
    return interleaved, height, width, channels

def save_to_txt_file(data, height, width, channels, output_file):
    with open(output_file, 'w') as f:
        # Write the array dimensions
        f.write(f"IMAGE_HEIGHT = {height}\n")
        f.write(f"IMAGE_WIDTH = {width}\n")
        f.write(f"IMAGE_CHANNELS = {channels}\n")
        
        # Write the array data
        f.write("image_data = [")
        
        for i, value in enumerate(data):
            if i % 12 == 0:
                f.write("\n    ")
            f.write(f"{value}, ")
        
        f.write("\n]\n")

def main():
    image_path = r'G:\My Drive\PIDNet\github\pdnet\data\raw_data\gtFine_trainvaltest\gtFine\train\ulm\ulm_000000_000019_gtFine_color.png'  # Change this to the path of your image
    output_file = r'G:\My Drive\PIDNet\github\pdnet\data\processed_data\image_data.txt'
    
    interleaved_data, height, width, channels = read_and_interleave_image(image_path)
    save_to_txt_file(interleaved_data, height, width, channels, output_file)
    print(f"Image data saved to '{output_file}'.")

if __name__ == "__main__":
    main()
