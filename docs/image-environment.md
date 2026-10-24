# 无界工作台配套环境（基于 ComfyUI）

面向无界工作台的 ComfyUI 运行环境，集成连接、启动、环境检查和 AutoDL Art 公共模型库接入。基于 AutoDL 官方「ComfyUI 纯净版 v1」整理；本镜像是第三方项目的整合适配，不代表上游官方产品，也不声称模型由无界研发。

> 发布候选版本，尚未上架。Qwen-Image 2.1 仅获得上游研究许可范围内的使用权；商业用途需另行取得授权。其他模型仍受各自许可约束。环境可运行不代表已取得全部商业授权。

## 使用方法

1. 在支持对应公共模型库的 AutoDL Art 区域创建 NVIDIA x86_64 实例。本轮验证区域为西北 B 区，显卡为 3090 48GB。
2. 设置开机命令为 `python /root/wujie-image/start.py`。
3. 在无界工作台「云端管理」连接实例，检查环境与模型状态后再生成。WebUI 使用 6006 端口。
4. 已校验的公共模型通过只读挂载使用；公共模型缺失或版本不符时显示具体错误，不自动重新下载整套大模型。

第一次检查和模型加载仍需要时间。不同区域、显卡、模型参数和公共库供应状态可能影响可用性；本镜像不承诺任意实例即开即用或固定生成速度。

## 已验证的能力

| 能力 | 验证范围 |
| --- | --- |
| Qwen-Image 2.1 | 512×512、8 步出图，研究/评估用途；商业授权未取得 |
| MiniMax H3 | 原生文生视频、单参考图视频、4+4 步优化工作流 |
| IndexTTS 2.5 | 中文语音合成 |
| Real-ESRGAN / RIFE | 2 倍放大、24fps 到 48fps 补帧 |
| DWPose / SAM2.1 | 资源和依赖检查；尚未完成实际推理验收 |

运行测试日期为 2026-10-23。测试仅代表上述组合，不代表所有工作流或全部参数已验收。

## 来源与许可

| 组件 | 来源 / 作者 | 许可说明 |
| --- | --- | --- |
| ComfyUI | [Comfy-Org / comfyanonymous](https://github.com/Comfy-Org/ComfyUI) | GPL-3.0，保留源码、版权与许可证 |
| KJNodes | [kijai](https://github.com/kijai/ComfyUI-KJNodes) | GPL-3.0 |
| H3 潜空间放大节点 | [LBH-123-AI](https://github.com/LBH-123-AI/Comfyui_Minimax_h3_latent_Upscaler) | 节点 MIT；对应权重另按模型卡许可 |
| Qwen-Image 2.1 | [Qwen](https://huggingface.co/Qwen/Qwen-Image-2.1)，[Comfy-Org 打包版](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) | Qwen Research License，非商业研究/评估；商用需另行授权 |
| MiniMax H3 | [MiniMaxAI](https://huggingface.co/MiniMaxAI/MiniMax-H3)，Comfy-Org 格式适配 | MiniMax H3 Community License；含地域、使用、再分发及商业条件 |
| H3 混合权重 | [smhfacct](https://huggingface.co/smhfacct/Minimax-H3-fl2va-ref2va-hybrid-models) | 作者说明继承 MiniMax H3 原许可 |
| H3 加速与放大权重 | [larryvrh](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)、[t8star](https://huggingface.co/t8star/minimax-h3-4step-turbo-loras-comfyui-exp)、[lightx2v](https://huggingface.co/lightx2v/Minimax-h3-Turbo)、[LBH-123-AI](https://huggingface.co/LBH-123-AI/Minimax_h3_latent_Upscaler) | 按各版本模型卡及基础模型许可；t8star 中转版本未附独立许可，公开再分发范围待核对 |
| IndexTTS 2.5 | [index-tts / bilibili](https://github.com/index-tts/index-tts)，[IndexTeam](https://huggingface.co/IndexTeam/IndexTTS-2.5) | bilibili Model Use License；保留原声明并向后续使用者传递条款 |
| BigVGAN / w2v-BERT / CAMPPlus | NVIDIA / Meta / FunASR | 按各组件许可，见完整清单 |
| Real-ESRGAN | [xinntao](https://github.com/xinntao/Real-ESRGAN) | BSD-3-Clause |
| RIFE | [hzwer](https://github.com/hzwer/Practical-RIFE) | 代码 MIT；权重及使用条款以固定来源文件为准 |
| DWPose / SAM2 | [IDEA-Research](https://github.com/IDEA-Research/DWPose) / [Meta](https://github.com/facebookresearch/sam2) | Apache-2.0；保留原 NOTICE 等声明 |

完整版本、来源链接、许可证原文和校验值位于 `/root/wujie-image/release-notices/`。Python 依赖保留各自安装包许可证；系统组件保留 `/usr/share/doc/` 中版权文件。公开库挂载仅改变文件存储方式，不改变使用许可。

ComfyUI 和插件的原始代码仓库保留在镜像中。GPL 覆盖组件的源码及修改必须按其许可证提供；本说明不限制使用者依上游许可享有的权利。上游商标仅用于说明组件来源，不表示其为本镜像背书。

## 无界新增适配

固定环境目录、公共模型版本与 SHA-256 核验、云端管理连接、受控服务启动、安装和运行状态反馈。对应管理器源码位于 `/root/.local/share/wujie/`；这些整合工作不改变第三方软件和模型的原许可。

本候选环境中的 H3 Turbo 兼容权重由 t8star 所分发文件进行固定张量键映射转换，转换代码位于 `turbo_transform.py`。未声称重新训练或原创模型；其来源链与待核事项见 `RELEASE-REVIEW.md`。

## 数据与问题反馈

运行时生成的项目、输入、输出和账号信息应由使用者自行保管。发布镜像前必须完成实例隐私清理、复核镜像大小，并确认新实例首次启动；公开上架状态以 AutoDL 审核结果为准。问题请通过此镜像讨论区反馈，并附版本与脱敏后的错误信息。
