# Danus 试用结果：边界局部化与次数导子

日期：2026-09-08。两个核心候选均已通过独立 LLM 审查并进入真实的 Danus 事实图。
这不是 Lean/Coq 形式化验证；中文整合稿也未另走整篇论文验证器。

## 数学结果

在 \(a+b\ge0\)、\(L=a+b+1\)、\(\lambda_L\ne0\) 下，得到

\[
T_{f_b}M_{a,b}(\chi)\cong M_{a+1,b-1}(\chi^+),
\qquad \chi^+(h_0)=\chi(h_0)+2,
\]

其余 Cartan 与中心特征值不变。中心参数任意，边界 \(b\) 可以为零或负整数，且可作任意有限次边界移动。

加入导子时，取真正的诱导函子

\[
\mathcal I(M)=U(\widetilde{\mathfrak g})\otimes_{U(\mathfrak g)}M
\cong\mathbb C[d]\otimes M,
\qquad x_r(P(d)\otimes u)=P(d-r)\otimes x_ru.
\]

对 \(F=f_n\) 在 \(M\) 上作用单射的情形，已证明自然同构

\[
T_F\mathcal I(M)\cong\mathcal I(T_FM).
\]

局部化的对应是 \(F^{-m}(P(d)\otimes u)\mapsto P(d+mn)\otimes F^{-m}u\)。
两项结果合成含导子的同构：

\[
T_{f_b}\widetilde M_{a,b}(\chi)\cong\widetilde M_{a+1,b-1}(\chi^+).
\]

限制：若固定原模 \(M_{-1,1}\)，\(n\ge2\) 时局部化为零；\(n\le0\) 时指定的生成向量像不是 \(h_1\)-特征向量，旧循环映射不能定义。这不构成非边界商的完整分类。诱导也不自动保持单性。

## 实际运行与审查

上游：[FrenzyMath/Danus](https://github.com/frenzymath/Danus)，release `v0.1.0-codex`，commit `7a51336e53cd1d558d0e766a61eb0fed46ebb05b`。上游源码未修改。

| 任务 | 审查过程 | 接受的 fact ID |
|---|---|---|
| 任意边界的 \(f_b\) 同构、固定原模的障碍、有限迭代 | 首次通过 | `d6bf6fef62dc8971` |
| 加入 \(d\) 与局部化的自然相容性 | 首次拒收：定理陈述缺少环境代数、函子和整数参数定义；补齐后二次通过 | `b388fabb701946d3` |

拒收轮并未发现平移符号或数学推导错误，但坚持陈述自包含。通过轮检查了正平移 \(+mn\)、逆平移 \(-mn\)、导子修正项、全部生成元的相容性、正合性和 smooth 性。

两个事实的内容哈希已重新计算，并与磁盘中的事实编号核对一致。候选和判定没有人工改写成“通过”。两个事实自身无依赖边；中文稿中的合并推论依赖这两个结果。

## 适配方式与边界

本机是 Windows，缺少可用 WSL。本次没有运行 Linux bootstrap 或常驻 swarm，而作了有限轮次的原生适配：

- 实际调用上游 `danus.verify.service.verify`、确定性预检查、`danus.gateway.server.fact_submit` 和 `danus.core.FactGraph`。
- 只替换进程与通信层：原生 Codex 子进程输出 JSON；进程内调用替代 HTTP/MCP；不改变数学接受规则和事实写入闸门。
- 两个 worker，三次候选生成、三次冷启动 verifier，共六次模型调用。每次均为只读 sandbox，沿用现有 ChatGPT 登录；未复制凭据。
- 启动时不加载全局 config.toml，使用 CLI 内置默认模型和 `high` 推理档；未启用额外付费策略 API，仍会正常消耗 Codex 额度。
- 未修改全局代理配置、未无沙箱运行、未向外发布、未留下常驻研究服务。

日志累计字段：输入 tokens 149700，缓存输入 tokens 19072，输出 tokens 27853；完整字段保存在审计 JSON。这里不据此推算美元费用。

适配层和上游相关模块的离线检查：67 通过，2 项依赖弃用警告。另有非阻断的启发式符号识别警告；LLM verifier 对正文定义作了独立审查。这些测试不证明数学结论。

Danus 官方也明确说明 verifier 是 LLM，而非形式化证明器：[安全与信任模型](https://github.com/frenzymath/Danus/blob/v0.1.0-codex/docs/security-and-trust.md)。用于论文前仍需作者及导师复核。

## 文件

- 中文证明稿：`boundary_derivation_extension_cn.tex` 及对应 PDF。
- 未改写的已接受英文候选：`danus_verified_proofs_en.md`。
- 机器可读审计：`danus_trial_audit.json`。
- 适配代码和复现方法：项目根目录的 `danus_trial/README.md`、`run_trial.py`。
- 原始运行目录：`work/danus-runs/20260908T070759Z/`，包含候选、拒收记录、最终判定和事实图。
