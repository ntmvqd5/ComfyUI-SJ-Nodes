import numpy as np

try:
    import torch
except ImportError:
    torch = None

try:
    from PIL import Image
except ImportError:
    Image = None

CATEGORY = "SJ"


class NineWanLiSJFugai:
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("图片",)
    FUNCTION = "fugai"
    CATEGORY = CATEGORY
    DESCRIPTION = "测试节点 请勿使用"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "image_1": ("IMAGE",),
                "image_2": ("IMAGE",),
            },
        }

    def fugai(self, image_1=None, image_2=None):
        if image_1 is None or image_2 is None or torch is None or Image is None:
            return (None,)
        try:
            a = image_1.detach().cpu().numpy()
            b = image_2.detach().cpu().numpy()
            if a.ndim == 3:
                a = np.expand_dims(a, 0)
            if b.ndim == 3:
                b = np.expand_dims(b, 0)
            small = a[0]
            big = b[0]
            sh, sw = small.shape[0], small.shape[1]
            bh, bw = big.shape[0], big.shape[1]
            if sw > bw or sh > bh:
                scale = min(bw / sw, bh / sh)
                nw = max(int(round(sw * scale)), 1)
                nh = max(int(round(sh * scale)), 1)
                try:
                    pil = Image.fromarray(
                        (np.clip(small, 0.0, 1.0) * 255.0).round().astype(np.uint8)
                    ).convert("RGB")
                    pil = pil.resize((nw, nh), Image.LANCZOS)
                    small = np.array(pil).astype(np.float32) / 255.0
                    sh, sw = nh, nw
                except Exception:
                    return (None,)
            left = (bw - sw) // 2
            top = (bh - sh) // 2
            big = np.array(big, dtype=np.float32).copy()
            big[top:top + sh, left:left + sw, :] = small[:sh, :sw, :]
            big = np.expand_dims(big, 0)
            return (torch.from_numpy(big),)
        except Exception:
            return (None,)


NODE_CLASS_MAPPINGS = {
    "NineWanLiSJFugai": NineWanLiSJFugai,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NineWanLiSJFugai": "SJ-fugai",
}
