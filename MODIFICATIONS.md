# 整合与修改说明

整理日期：2026-10-24。此文件说明无界新增的集成工作，不替代任何上游许可证，也不声明对上游成果的所有权。

- 基础环境：AutoDL 官方 ComfyUI 纯净版 v1。
- 在 `/root/wujie-image/ComfyUI` 安装固定提交的 ComfyUI 和插件，源码和 Git 版本记录保留。
- 已检查的 12 个 Git 仓库的受版本控制文件未被修改。是否清理基础镜像中的旧副本另见最终清理记录。
- 新增无界管理器、环境识别、公共模型只读映射与校验、启动脚本；本轮新增来源、许可、运行依赖清单和发布文档。
- Python 虚拟环境移动至固定目录时调整了启动脚本路径；包自身的许可保留。
- H3 Turbo 兼容文件：源自 t8star 分发、其 README 指向 larryvrh；由无界 `turbo_transform.py` 按固定规则转换张量键，生成 `minimax_h3_turbo_pruned_compatible_comfyui.safetensors`。这是格式适配，未重新训练。转换不授予额外模型权利；中转版本缺少许可文本需在公开发布前处理。
- IndexTTS 衍生适配声明：Any modifications made to the original model in this Derivative Work are not endorsed, warranted, or guaranteed by the original right-holder of the original model, and the original right-holder disclaims all liability related to this Derivative Work.
- 不将第三方模型、公共库文件、上游示例或第三方工作流宣传为无界自主训练或全部原创。
