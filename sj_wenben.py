import os
from datetime import datetime

class SJwenben:
    """
    SJ-wenben 瞬境专用文本输出节点
    作用：把工作流中的文本输出保存为.txt文件，让RunningHub识别为文本结果。
    
    RunningHub识别原理：
    1. 扫描output目录下的文件，按扩展名判断outputType（.png→图片，.txt→文本）
    2. 如果是.txt文件，读取文件内容填充到API响应的text字段
    3. 网站后台配置该节点产出类型为"文本"后，自动展示text字段内容，不显示下载链接
    
    使用方法：
    1. 在工作流最后一级文本输出节点后面接上 SJ-wenben
    2. 网站后台"产出节点配置"里添加这个节点，产出类型选"文本"
    """
    
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
        
        # 保存为.txt文件到output目录
        # RunningHub会扫描这个目录，识别为文本输出
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"SJ-wenben_{timestamp}.txt"
        file_path = os.path.join(self.output_dir, filename)
        
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text_str)
            print(f"[SJ-wenben] 文本已保存，长度: {len(text_str)} 字符")
        except Exception as e:
            print(f"[SJ-wenben] 保存失败: {e}")
        
        # 返回文本内容，兼容仙宫云直接读取节点输出的方式
        return (text_str,)


NODE_CLASS_MAPPINGS = {
    "SJwenben": SJwenben,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SJwenben": "SJ-wenben",
}
