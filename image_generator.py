from diffusers import StableDiffusionPipeline
import torch

# Load the pretrained Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4").to("cpu")

def generate_image(prompt, output_path="generated_image.png"):
    # Generate the image
    image = pipe(prompt).images[0]
    # Save the image
    image.save(output_path)
    print(f"Image saved to {output_path}")

# Example usage
english_prompt = "A beautiful sunrise over a desert oasis"
generate_image(english_prompt)
