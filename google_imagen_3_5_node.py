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

class GoogleImagen35Node:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api": ("STRING", {"default": "", "multiline": False}),
                "prompt_text": ("STRING", {"multiline": True, "default": "A futuristic city at sunset"}),
                "aspect_ratio": (["16:9", "9:16", "1:1"],),
                "candidates_count": ("INT", {"default": 4, "min": 1, "max": 4}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2147483647}),  # -1 = aleatorio
                "save_path": ("STRING", {"default": "C:\\Users\\$USERNAME\\Documents\\ComfyUI\\GeneratedImages\\"}),
                "prefix": ("STRING", {"default": "imagen_"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)  # Una sola salida que contiene un batch de imágenes
    FUNCTION = "generate_fx_35"
    CATEGORY = "AI Sandbox"

    def generate_fx_35(self, api, prompt_text, aspect_ratio, save_path, prefix, candidates_count, seed):
        # Delegamos toda la lógica al módulo externo

        return generate_and_save_images35(api, prompt_text, aspect_ratio, save_path, prefix, candidates_count, seed)
