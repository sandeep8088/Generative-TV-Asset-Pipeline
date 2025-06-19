import os
from PIL import Image
import openai
import matplotlib.pyplot as plt

# Set your OpenAI API key
openai.api_key = "your-api-key"

# Image loader
img_path = 'data/images'
images = [Image.open(os.path.join(img_path, file)) for file in os.listdir(img_path) if file.endswith('.jpg')]

# Caption generator
def generate_caption(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write an exciting short-form ad caption for this product:
{prompt}"}]
    )
    return response['choices'][0]['message']['content']

# Process and display
for idx, img in enumerate(images):
    caption = generate_caption(f"Brand new product image {idx+1}")
    plt.imshow(img)
    plt.title(caption)
    plt.axis('off')
    plt.savefig(f"data/output/ad_{idx+1}.png")
    print(f"Generated caption: {caption}")
