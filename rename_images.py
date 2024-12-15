import os

# Directory where your images are located
directory = "img/projects/industrial-elegance/"

# List all files in the directory
files = os.listdir(directory)

# Filter out only image files (e.g., jpg, png)
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.JPG']
image_files = [f for f in files if any(f.endswith(ext) for ext in image_extensions)]

# Loop through each image and rename it
for index, image in enumerate(image_files, start=1):
    # Create the new filename with the desired format
    new_name = f"industrial-elegance-{index}{os.path.splitext(image)[1]}"

    # Get the full path for old and new filenames
    old_path = os.path.join(directory, image)
    new_path = os.path.join(directory, new_name)

    # Rename the file
    os.rename(old_path, new_path)
    print(f"Renamed '{image}' to '{new_name}'")
