from PIL import Image
import io

def process_image(file):
    try:
        image_bytes = file.read()
        image = Image.open(io.BytesIO(image_bytes))
        image.verify()  # validates image

        # DEMO-SAFE OUTPUT
        return "Detected sign gesture: HELLO (demo output)"

    except Exception as e:
        return f"Image processing failed: {str(e)}"
