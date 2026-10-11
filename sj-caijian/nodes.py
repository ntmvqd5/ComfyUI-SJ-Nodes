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

RATIOS = [
    (1.0, "1:1"),
    (4.0 / 3.0, "4:3"),
    (3.0 / 4.0, "3:4"),
    (16.0 / 9.0, "16:9"),
    (9.0 / 16.0, "9:16"),
    (3.0 / 2.0, "3:2"),
    (2.0 / 3.0, "2:3"),
    (21.0 / 9.0, "21:9"),
    (9.0 / 21.0, "9:21"),
]


class NineWanLiSJCrop:
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("图片",)
    FUNCTION = "crop"
    CATEGORY = CATEGORY
    DESCRIPTION = "测试节点 请勿使用"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {},
            "optional": {
                "image": ("IMAGE",),
            },
        }

    def crop(self, image=None):
        if image is None or torch is None or Image is None:
            return (None,)
        try:
            arr = image.detach().cpu().numpy()
            if arr.ndim == 3:
                arr = np.expand_dims(arr, 0)
            if arr.shape[0] == 0:
                return (None,)
            outs = []
            for i in range(arr.shape[0]):
                a = arr[i]
                h, w = a.shape[0], a.shape[1]
                orig_ratio = w / float(h)
                target = min(RATIOS, key=lambda t: abs(np.log(orig_ratio / t[0])))
                r = target[0]
                if r > orig_ratio + 1e-9:
                    new_h = int(round(w / r))
                    if new_h > h:
                        new_h = h
                    top = (h - new_h) // 2
                    outs.append(a[top:top + new_h, :, :])
                elif r < orig_ratio - 1e-9:
                    new_w = int(round(h * r))
                    if new_w > w:
                        new_w = w
                    left = (w - new_w) // 2
                    outs.append(a[:, left:left + new_w, :])
                else:
                    outs.append(a)
            out = np.stack(outs, 0)
            return (torch.from_numpy(out.astype(np.float32)),)
        except Exception:
            return (None,)


NODE_CLASS_MAPPINGS = {
    "NineWanLiSJCrop": NineWanLiSJCrop,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "NineWanLiSJCrop": "SJ-caijian",
}
