from PIL import Image
import torch
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

def generate_caption_from_path(image_path):
    try:
        image = Image.open(image_path).convert("RGB")

        pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

        output_ids = model.generate(pixel_values, max_length=50)
        caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

        return caption

    except Exception as e:
        return f"Error: {str(e)}"

# add your image path here
img_path = "C:/Users/ADMIN/Downloads/WhatsApp Image 2025-07-11 at 14.12.31_9c160f84.jpg"  # Update if needed

caption = generate_caption_from_path(img_path)
print(f"\n🖼️ Caption: {caption}")