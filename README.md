# wujie-autodl · 无界工作台镜像配套

无界工作台在 AutoDL / AutoDL.Art 上使用的环境检查入口、启动入口与上游来源清单。

**状态：发布准备中。** 本仓库已建立；现有私有候选镜像尚未装入本仓库，也未完成清理后的新实例首次启动验收。仓库创建成功不代表镜像已经公开上架。

## 仓库内容

- `wujie_autodl.py`：Python 标准库命令行入口，提供项目介绍、只读文件检查和配套环境启动。
- `upstream-sources.json` / `licenses/`：固定来源版本、已收集的原始许可证、证据链接与 SHA-256。
- `model-sources.json`：预期模型路径及来源说明；是静态清单，不是实时就绪报告。
- `docs/image-environment.md`：已准备环境的使用说明及历史测试范围。
- `docs/release-status.md`：镜像发布前尚需完成的项目。

本仓库只包含镜像配套文本和脚本。模型权重由对应 AutoDL Art 公共库提供，需使用支持这些公共挂载的实例；仓库不会下载模型、收集账号信息或上传项目数据。

## 使用

要求 Python 3.9 或更新版本。查看说明可以在普通电脑上运行：

```bash
git clone https://github.com/z4568114-crypto/wujie-autodl.git
cd wujie-autodl
python3 wujie_autodl.py about
```

在已经准备好 `/root/wujie-image` 的配套 Linux 镜像内：

```bash
python3 wujie_autodl.py check
python3 wujie_autodl.py start
```

`check` 检查固定环境标记、启动文件、Python 入口和模型文件是否存在，缺失时退出码为 1。它不会读取整个模型或运行推理，结果仅代表文件可见性，不代表模型哈希、GPU 推理或使用许可已经验收。

`start` 先检查环境入口，再调用配套镜像已有的 `/root/wujie-image/start.py`。缺少配套环境时明确退出，不会自动安装或修改现有实例。本仓库目前不是从空白系统构建完整镜像的一键安装器。

## AutoDL 发布填写

- GitHub 仓库地址：`z4568114-crypto/wujie-autodl`（页面已带 `https://github.com/` 时只填这一段）。
- 建议镜像名称：`Wujie-AutoDL-PublicModels-v1`。
- 镜像内的目标仓库位置：`/root/wujie-autodl`；**此步骤尚待执行和验证**。
- 现有环境：PyTorch 2.8.0、CUDA 12.8；具体 Python 版本按图像与语音各自的虚拟环境确定。

## 来源与许可证

本项目为第三方整合适配。ComfyUI、插件与各模型的作者、来源、版本和原许可证仍保留；本仓库不将上游成果声明为无界原创，也不以统一许可证重新授权整套镜像。

主要上游包括 [ComfyUI](https://github.com/Comfy-Org/ComfyUI)、[KJNodes](https://github.com/kijai/ComfyUI-KJNodes)、[IndexTTS](https://github.com/index-tts/index-tts)、[MiniMax H3](https://huggingface.co/MiniMaxAI/MiniMax-H3) 和 [Qwen-Image 2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)。具体范围见 [NOTICE](NOTICE)、[整合记录](MODIFICATIONS.md) 及原始许可证。缺少许可文本的项目仍标注为待核对。

Qwen-Image 2.1 按已收集的研究许可证使用；商业用途不能由本仓库自行授权。公共模型挂载不会改变原模型许可。

## 本地检查

```bash
python3 -m unittest discover -s tests -v
```

这些检查验证命令行行为，不替代云端新实例首次启动与实际推理验收。
