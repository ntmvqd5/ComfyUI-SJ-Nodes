# ComfyUI-SJ-Nodes

ComfyUI 实用节点包：图片压缩与图片保存。

包含 3 个节点：

## SJ-yasuo ｜ 图片压缩（4500）

- 有图片输入时：若最长边超过 **4500px**，自动等比缩放至 4500px 以内，并转为 JPG（quality 100）
- 未超过 4500px：仅转为 JPG，尺寸不变
- **无图片输入时自动跳过，不报错**

## SJ-LM-yasuo ｜ 图片压缩（2048）

- 与 SJ-yasuo 相同逻辑，最长边上限为 **2048px**
- 适合对总像素有严格上限的模型接口

## SJ-baocun ｜ 图片保存

- 将输入图片**原尺寸**保存为 JPG（quality 100），不缩放、不改变分辨率
- 文件名固定前缀 `SHUNJINGAI_00001.jpg`（自动递增，不覆盖）
- 多张图片（batch）逐张保存
- 输出的 JPG **不含任何工作流元数据**（干净输出）
- 与 ComfyUI 原生保存节点一样，可在前端显示预览、可通过 API 取回图片

## 安装

将仓库克隆到 ComfyUI 的 `custom_nodes` 目录：

```
git clone https://github.com/ntmvqd5/ComfyUI-SJ-Nodes.git
```

重启 ComfyUI 后，节点位于「SJ」分类下。

## 依赖

- torch、numpy、Pillow（ComfyUI 自带）

## 许可

MIT
