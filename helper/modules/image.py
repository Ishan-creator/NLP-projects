from langchain_community.llms import Ollama 
import cv2
import numpy as np

model= Ollama(model="llava-phi3")

# Replace with the actual path to your image on your system
image_path = "/home/ishan-pc/Desktop/Ishan-Github/NLP-projects/helper/modules/images.jpeg"  # Modify this path accordingly

# Load the image using cv2.imread
try:
  image = cv2.imread(image_path)
  if image is None:
    print(f"Error: Could not read image from path '{image_path}'")
    exit()
except Exception as e:
  print(f"Error loading image: {e}")
  exit()

# Generate text description
context = model.bind(image=image)
text = context.generate(prompts=["Describe the image"], temperature=1)

print(text)