from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

def generate_image(prompt, output_path):
    pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cpu")
    image = pipe(prompt).images[0]
    image.save(output_path)

# Example usage
english_prompt = "A beautiful sunrise over a desert oasis"
generate_image(english_prompt)
