from PIL import Image
import io
import json
import base64
import requests
import os
import time
import torch
import random
import numpy as np
from GoogleFX.google_gen import *

# Combinamos todas tus opciones en una sola lista, y agregamos "None" al inicio
ALL_STYLES = [
    "None",
    "35mm film",
    "8mm film",
    "lomography film",
    "digital photo",
    "minimal",
    "maximalist",
    "detailed",
    "abstract",
    "photorealistic",
    "intricate",
    "handmade",
    "sketchy",
    "painted",
    "sculpted",
    "chiaroscuro",
    "flat lighting",
    "high contrast",
    "diffuse lighting",
    "surreal",
    "impressionist",
    "cubist",
    "post-modern",
    "desaturated",
    "saturated",
    "vibrant",
    "subdued",
    "watercolor",
    "oil painting",
    "acrylic painting",
    "digital illustration",
    "blue and orange",
    "red and green",
    "yellow and purple",
    "pink and black",
    "dslr",
    "analog camera",
    "cinema camera",
    "mirrorless camera",
    "photography",
    "painting",
    "illustration",
    "sculpture",
    "dynamic",
    "static",
    "high octane",
    "chaotic",
    "macro photo",
    "wide angle",
    "telephoto",
    "bird's eye view",
    "scifi",
    "fantasy",
    "romance",
    "thriller"
]

class GoogleImagen31Node:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api": ("STRING", {"default": "", "multiline": False}),
                "prompt_text": ("STRING", {"multiline": True, "default": "A futuristic city at sunset"}),
                "aspect_ratio": (["16:9", "9:16", "1:1", "3:4", "4:3"],),
                "candidates_count": ("INT", {"default": 4, "min": 1, "max": 4}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2147483647}),
                "save_path": ("STRING", {"default": "C:\\Users\\$USERNAME\\Documents\\ComfyUI\\GeneratedImages\\"}),
                "prefix": ("STRING", {"default": "imagen_"}),
                "style_tag": (ALL_STYLES, {"default": "None"}),  # <-- Solo un selector
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_fx_31"
    CATEGORY = "AI Sandbox"

    def generate_fx_31(self, api, prompt_text, aspect_ratio, save_path, prefix, candidates_count, seed, style_tag):
        # Empezamos con el prompt base
        final_prompt = prompt_text.strip()

        # Solo agregamos el estilo si NO es "None"
        if style_tag != "None":
            final_prompt += " " + style_tag

        # Llamamos a la función externa con el prompt final
        return generate_and_save_images31(api, final_prompt, aspect_ratio, save_path, prefix, candidates_count, seed)