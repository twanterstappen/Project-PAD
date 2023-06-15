from PIL import Image
from stegano import lsb


def encode_message(image_path, message, output_path):
    # Open the image using PIL library
    img = Image.open(image_path)

    # Encode the message into the image using LSB library
    encoded_img = lsb.hide(image_path, message)

    # Save the encoded image 
    encoded_img.save(output_path)

    print("Message successfully encoded into the image!")


image_path = 'static/uploads/image.jpg'
message = "Chameleons are experts in the art of hiding."
output_path = 'static/downloads/hidden_image.png'

encode_message(image_path, message, output_path)
