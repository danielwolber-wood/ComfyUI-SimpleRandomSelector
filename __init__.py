from .random_node import RandomFileSelector

NODE_CLASS_MAPPINGS = {
    "RandomFileSelector": RandomFileSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "RandomFileSelector": "Random Line form File"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]