import os
from PIL import Image

print(" Welcome to Image Resizer Tool\n")

#  Default folders
default_input = "images"      
default_output = "resized"    

#  Step 1: Ask user for input folder (If you Want to use Default folder Just Press Enter)
input_folder = input(f"Enter the folder path where your images are stored (default: {default_input}): ").strip()
if not input_folder:
    input_folder = default_input

#  Step 2: Ask user for output folder (If you Want to use Default folder Just Press Enter)
output_folder = input(f"Enter the folder name for resized images (default: {default_output}): ").strip()
if not output_folder:
    output_folder = default_output

#  Step 3: Ask user for new width and height
try:
    width = int(input("Enter new width (default: 800): ").strip() or 800)
    height = int(input("Enter new height (default: 600): ").strip() or 600)
    new_size = (width, height)
except ValueError:
    print(" Invalid input! Using default size 800x600.")
    new_size = (800, 600)

#  Step 4: Create output folder if it doesn’t exist
os.makedirs(output_folder, exist_ok=True)

#  Step 5: Process images
count = 0
for file in os.listdir(input_folder):
    if file.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        image_path = os.path.join(input_folder, file)
        image = Image.open(image_path)

        resized_image = image.resize(new_size)

        save_path = os.path.join(output_folder, file)
        resized_image.save(save_path)
        print(f" Resized and saved: {save_path}")
        count += 1

#  Step 6: Final message
if count > 0:
    print(f"\n Done! {count} images resized and saved in '{output_folder}' folder.")
else:
    print("\n No images found in the folder.")
    
