import os

def rename_files(directory, pattern="photo"):
    # Change the current working directory to the target directory
    os.chdir(directory)
    
    # List all files in the directory
    files = os.listdir()

    # Filter out non-image files
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    images = [file for file in files if file.endswith(image_extensions)]

    # Rename each file
    for index, image in enumerate(images, start=1):
        new_name = f"{pattern}{index}.jpg"
        os.rename(image, new_name)
        print(f"Renamed '{image}' to '{new_name}'")

# Example usage
directory_path = '/path/to/your/photos'
rename_files(directory_path)
