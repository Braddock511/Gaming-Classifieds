from imagekitio import ImageKit
from database import get_credentials

def upload_file_imageKit(image: str):
    credentials = get_credentials()

    imageKit_config = {
        "public_key": credentials["api_imagekit_id"],
        "private_key": credentials["api_imagekit_secret"],
        "url_endpoint": credentials["api_imagekit_endpoint"]
    }

    imagekit = ImageKit(**imageKit_config)

    result = imagekit.upload_file(file=image, file_name=f'{image[:10]}.png')

    return result.response_metadata.raw