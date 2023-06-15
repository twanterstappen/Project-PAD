from PIL import Image
from PIL.PngImagePlugin import PngInfo

def create_png_with_flag(flag, file_path):
    # Create a blank PNG image with a single pixel
    image = Image.new('RGB', (1, 1), (0, 0, 0))

    # Set the author metadata to the flag
    metadata = PngInfo()
    metadata.add_text("Author", flag)

    # Save the image with the metadata
    image.save(file_path, "PNG", pnginfo=metadata)

# Replace 'file_path' with the desired path and filename for the PNG file
file_path = 'flask/uploads/pixel.png'
flag = 'CyberCTF{Cry9t0_!s_n0t_alway$_fun!}'

create_png_with_flag(flag, file_path)
print(f"PNG file created with flag: {flag}")


#This is created using CHATGPT, we can remove this file later.
