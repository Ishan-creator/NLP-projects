from langchain_community.llms import Ollama
from IPython.display import HTML, display
from PIL import Image, ImageGrab
from io import BytesIO
import base64
import cv2

llava = Ollama(model="llava-phi3")

def convert_to_base64(pil_image):
    buffered = BytesIO()
    pil_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def plt_img_base64(img_base64):
    image_html = f'<img src="data:image/jpeg;base64,{img_base64}" />'
    display(HTML(image_html))

def img_process(file_path):
    pil_image = Image.open(file_path)
    pil_image = pil_image.convert('RGB')
    image_b64 = convert_to_base64(pil_image)
    plt_img_base64(image_b64)
    return image_b64


class image():
    def chat_with_image(question, image_path):
        image_b64 = img_process(image_path)
        llm_with_image_context = llava.bind(images=[image_b64])
        return llm_with_image_context.invoke(question)[0]
    
check = image.chat_with_image("Explain the image" , "/home/ishan-pc/Desktop/Ishan-Github/NLP-projects/helper/modules/images.jpeg")

