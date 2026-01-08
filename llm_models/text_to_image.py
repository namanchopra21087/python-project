import torch
from diffusers import DiffusionPipeline

# switch to "mps" for apple devices
pipe = DiffusionPipeline.from_pretrained("Sygil/Sygil-Diffusion", dtype=torch.float16,device_map="balanced")

prompt = "environment art, realistic"
image = pipe(prompt).images[0]
image.save("result.png")