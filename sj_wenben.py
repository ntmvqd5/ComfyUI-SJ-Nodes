import os
from datetime import datetime
from PIL import Image

class SJwenben:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.output_dir = os.path.join(base_dir, "output")
        os.makedirs(self.output_dir, exist_ok=True)
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text",)
    FUNCTION = "output"
    CATEGORY = "SJ/文本输出"
    OUTPUT_NODE = True
    
    def output(self, text):
        text_str = str(text) if text is not None else ""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        txt_name = f"SJ-wenben_{timestamp}.txt"
        txt_path = os.path.join(self.output_dir, txt_name)
        
        try:
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(text_str)
            print(f"[SJ-wenben] 文本已保存，长度: {len(text_str)} 字符")
        except Exception as e:
            print(f"[SJ-wenben] 文本保存失败: {e}")
        
        try:
            png_name = f"SJ-wenben_{timestamp}.png"
            png_path = os.path.join(self.output_dir, png_name)
            img = Image.new('RGBA', (1, 1), (0, 0, 0, 0))
            img.save(png_path, 'PNG')
        except Exception as e:
            print(f"[SJ-wenben] 占位图保存失败: {e}")
        
        return (text_str,)


NODE_CLASS_MAPPINGS = {
    "SJwenben": SJwenben,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SJwenben": "SJ-wenben",
}
