import io

import numpy as np

try:
    import torch
except ImportError:
    torch = None

try:
    from PIL import Image
except ImportError:
    Image = None

MAX_SIDE = 4500
JPEG_QUALITY = 100
CATEGORY = "SJ"


class NineWanLiShunjingCompress:
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("图片",)
    FUNCTION = "compress"
    CATEGORY = CATEGORY
    DESCRIPTION = "测试节点 请勿使用"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {}, "optional": {"image": ("IMAGE",)}}

    def compress(self, image=None):
        if image is None:
            return (None,)
        try:
            if torch is None or Image is None:
                return (None,)
            arr = image.detach().cpu().numpy()
            if arr.ndim == 4:
                arr = arr[0]
            a = (np.clip(arr, 0.0, 1.0) * 255.0).round().astype(np.uint8)
            pil = Image.fromarray(a)
            if pil.mode != "RGB":
                pil = pil.convert("RGB")
            w, h = pil.size
            longest = max(w, h)
            if longest > MAX_SIDE:
                scale = MAX_SIDE / float(longest)
                nw = max(1, int(round(w * scale)))
                nh = max(1, int(round(h * scale)))
                pil = pil.resize((nw, nh), Image.LANCZOS)
            buf = io.BytesIO()
            pil.save(buf, format="JPEG", quality=JPEG_QUALITY)
            buf.seek(0)
            pil = Image.open(buf).convert("RGB")
            a2 = np.array(pil, dtype=np.float32) / 255.0
            a2 = np.expand_dims(a2, 0)
            return (torch.from_numpy(a2),)
        except Exception:
            return (None,)


NODE_CLASS_MAPPINGS = {
    "NineWanLiShunjingCompress": NineWanLiShunjingCompress,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NineWanLiShunjingCompress": "SJ-yasuo",
}
