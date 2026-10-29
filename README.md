# wujie-autodl · 无界工作台镜像配套

## 2026-10-29 发布候选说明

当前准备的是 **v139-r7 测试候选**，镜像从普通 AutoDL 制作实例保存，再通过 AutoDL Art 发布。不是已完成客户端全流程验收的正式版。

- 自有仓库已安装到系统盘 `/root/wujie-autodl`，`python3 -B /root/wujie-autodl/wujie_autodl.py about` 已运行成功。
- 环境和辅助资源在 `/root/wujie-image`；其中 `data` 属于系统盘，不是私有数据盘 `/root/autodl-tmp`。
- 首启材料在 `/root/wujie-image/bootstrap/AutoDL镜像构建候选-v139-r7/`，101 项材料 SHA 已核对。
- 主 ComfyUI 固定提交 `73c9bad4d21e7addbe1d13bc92eee0f1431b017d`；主环境 Python 3.11.13、PyTorch 2.10.0+cu130，语音及媒体环境为 PyTorch 2.8.0+cu128。
- 此制作实例目前没有完成 GPU 封存，环境标记缺失；不会写入假标记或把无卡检查称为 GPU 验收。自动首启、新保存镜像的新实例检查及当前无界客户端全流程仍待验证。
- 私有候选的保存与公开审核状态应以 AutoDL / AutoDL Art 页面为准。本仓库的提交不代表已公开上架。

### v139-r7 候选使用边界

首次 GPU 环境检查入口：

```bash
/root/wujie-image/python311/python/bin/python3.11 -I -B /root/wujie-image/bootstrap/AutoDL镜像构建候选-v139-r7/first_boot.py
```

此入口重新校验材料、依赖和 GPU 能力，失败即受阻；不安装依赖、不下载模型、不建立公共模型链接、不提交推理。平台是否自动执行尚未验收，不能省略此事实。完成严格环境检查后，公共库校验、关联和服务启动仍由匹配版本的无界客户端负责。

该候选依赖 Art 只读公共模型挂载，普通 AutoDL 实例不能替代公共库。不得把旧数据盘中的模型或下载缓存当作候选交付内容。IndexTTS、Qwen、H3 的历史后台测试，不等于此新镜像或当前客户端已通过。

`wujie_autodl.py check/start` 是下方 **2026-10-24 旧镜像布局** 的入口，不适用于当前 r7 布局；当前候选不要调用它启动服务。`about` 只展示仓库说明，不证明模型可用。

## 历史记录：2026-10-24 旧布局

以下记录保留来源与使用历史；其中未完成事项、版本、启动路径不能当作当前候选状态。

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


