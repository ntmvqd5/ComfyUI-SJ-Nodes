import os
import re

import numpy as np

try:
    import torch
except ImportError:
    torch = None

try:
    from PIL import Image
except ImportError:
    Image = None

try:
    import folder_paths
except ImportError:
    folder_paths = None

JPEG_QUALITY = 100
PREFIX = "SHUNJINGAI"
CATEGORY = "SJ"


class NineWanLiSJBaocun:
    RETURN_TYPES = ()
    FUNCTION = "save"
    CATEGORY = CATEGORY
    OUTPUT_NODE = True
    DESCRIPTION = "测试节点 请勿使用"

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"images": ("IMAGE",)}}

    def save(self, images):
        saved = []
        try:
            if images is None or torch is None or Image is None or folder_paths is None:
                return {"ui": {"images": saved}}
            arr = images.detach().cpu().numpy()
            if arr.ndim == 3:
                arr = np.expand_dims(arr, 0)
            if arr.shape[0] == 0:
                return {"ui": {"images": saved}}
            outdir = folder_paths.get_output_directory()
            start = self._next_index(outdir)
            for i in range(arr.shape[0]):
                a = (np.clip(arr[i], 0.0, 1.0) * 255.0).round().astype(np.uint8)
                pil = Image.fromarray(a)
                if pil.mode != "RGB":
                    pil = pil.convert("RGB")
                fn = os.path.join(outdir, "%s_%05d.jpg" % (PREFIX, start + i))
                pil.save(fn, format="JPEG", quality=JPEG_QUALITY)
                saved.append(
                    {
                        "filename": os.path.basename(fn),
                        "subfolder": "",
                        "type": "output",
                    }
                )
        except Exception:
            pass
        return {"ui": {"images": saved}}

    @staticmethod
    def _next_index(outdir):
        best = 0
        try:
            if os.path.isdir(outdir):
                for f in os.listdir(outdir):
                    mm = re.match(r"^%s_(\d+)\.jpg$" % PREFIX, f)
                    if mm:
                        best = max(best, int(mm.group(1)))
        except Exception:
            pass
        return best + 1


NODE_CLASS_MAPPINGS = {
    "NineWanLiSJBaocun": NineWanLiSJBaocun,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NineWanLiSJBaocun": "SJ-baocun",
}
