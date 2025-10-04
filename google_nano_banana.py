import base64
import requests
import datetime
import os
import time
import torch
import random
import numpy as np
from PIL import Image
import io
from GoogleFX.google_gen import *

class GoogleNanoBananaNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "API_KEY": ("STRING", {"default": "", "multiline": False}),
                "prompt_text": ("STRING", {"multiline": True, "default": "A futuristic city at sunset"}),
                "candidates_count": ("INT", {"default": 4, "min": 1, "max": 4}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2147483647}),
                "save_path": ("STRING", {"default": "C:\\Users\\$USERNAME\\Documents\\ComfyUI\\GeneratedImages\\"}),
                "prefix": ("STRING", {"default": "imagen_"}),
            },
            "optional": {
                "reference_image_1": ("IMAGE",),
                "reference_image_2": ("IMAGE",),
                "reference_image_3": ("IMAGE",),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID"
            }
        }

    RETURN_TYPES = ("IMAGE",)  # ← Una sola salida (batch de imágenes)
    FUNCTION = "generate_N2I"
    CATEGORY = "Veo Nodes"
    DESCRIPTION = "Nodo unificado: acepta imágenes de ComfyUI, las sube y genera con referencias. Salida única en batch."

    def generate_N2I(self, API_KEY, prompt_text, candidates_count, seed,
                        save_path, prefix,
                        reference_image_1=None, reference_image_2=None, reference_image_3=None,
                        unique_id=None):
        # Delegamos toda la lógica al módulo externo

        return generate_images(API_KEY, prompt_text, candidates_count, seed, save_path, prefix, reference_image_1, reference_image_2, reference_image_3, unique_id)
