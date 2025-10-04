from PIL import Image
import io
import base64
import json
import requests
import os
import time
import torch
import random
import numpy as np
import datetime
from GoogleFX.google_gen import *

class GoogleImagenR2INode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "api": ("STRING", {"default": "", "multiline": False}),
                "prompt_text": ("STRING", {"multiline": True, "default": "A futuristic city at sunset"}),
                "aspect_ratio": (["16:9", "9:16", "1:1"], {"default": "16:9"}),
                "candidates_count": ("INT", {"default": 4, "min": 1, "max": 4}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2147483647}),
                "save_path": ("STRING", {"default": "C:\\Users\\$USERNAME\\Documents\\ComfyUI\\GeneratedImages\\"}),
                "prefix": ("STRING", {"default": "imagen_"}),
            },
            "optional": {
                "reference_image_1": ("IMAGE",),  # ← Ahora es IMAGE, no STRING
                "reference_image_2": ("IMAGE",),
                "reference_image_3": ("IMAGE",),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID"
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "generate_R2I"
    CATEGORY = "AI Sandbox"
    DESCRIPTION = "Genera imágenes con Google Imagen 3.5 (R2I) usando la API sandbox. Sube automáticamente imágenes de referencia desde ComfyUI."

    
    def generate_R2I(self, api, prompt_text, aspect_ratio, candidates_count, seed,
                                save_path, prefix,
                                reference_image_1=None, reference_image_2=None, reference_image_3=None,
                                unique_id=None):
        # Delegamos toda la lógica al módulo externo

        return generate_and_save_imagesR2I(api, prompt_text, aspect_ratio, candidates_count, seed, save_path, prefix, reference_image_1, reference_image_2, reference_image_3, unique_id)
