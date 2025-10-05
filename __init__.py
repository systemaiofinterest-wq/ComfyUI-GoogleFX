# __init__.py
from .google_imagen_3_5_node import GoogleImagen35Node
from .google_image_R2I import GoogleImagenR2INode
from .google_nano_banana import GoogleNanoBananaNode
from .google_imagen_3_1_node import GoogleImagen31Node


NODE_CLASS_MAPPINGS = {
    "GoogleImagen35Node": GoogleImagen35Node,
    "GoogleImagenR2INode": GoogleImagenR2INode,
    "GoogleNanoBananaNode": GoogleNanoBananaNode,
    "GoogleImagen31Node": GoogleImagen31Node,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GoogleImagen35Node": "Google Imagen 3.5",
    "GoogleImagenR2INode": "Google Imagen R2I",
    "GoogleNanoBananaNode": "Google Imagen Nano Banana x4",
    "GoogleImagen31Node": "Google Imagen 3.1",
}


__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']