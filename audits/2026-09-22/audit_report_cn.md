# affine-sl2-localization-quotients：数学审查与可复现反例

审查日期：2026-09-22。仓库：`haozhengding1628/affine-sl2-localization-quotients`。
快照：`main@5f766461cb0a01d171b136b55a64cd1f214886de`。

## 0. 范围与结论

本次重点逐段审查以下源文件，而不是仅依据 README 或编译 PDF：

- `outputs/localization_quotients_unified_en.tex`
- `outputs/localization_quotients_additional_progress_en.tex`
- `outputs/gc_structure_advisor_en.tex`
- `outputs/gc_structure_research_cn.tex`
- `work/check_gc_sanity.py`
- `work/check_gc_filter.py`

并对照 Futorny–Guo–Xue–Zhao, *Smooth representations of affine Kac–Moody algebras*, arXiv:2404.03855v2，特别是 Theorem 1.1 与关于含 derivation 模的部分。

**结论：9 月 22 日 G_c 结构稿存在明确数学错误。错误不推翻边界同构，也不推翻 9 月 15 日附录的深区单性判据与唯一极大子模论证。**

必须区分：

1. 已被显式反例否定的断言：E 作用公式、用 T 的幂描述全部原初空间、特定参数下 P_0 一维、按横向 sl2 最高权构造的尾部是仿射子模。
2. 因依赖错误证明而应撤回为未确定的断言：G_c 永不单、零 socle、无限合成长度、所列滤过商为单模。这次审查没有证明这些结论的否命题。
3. 可以保留的结构：G_c 作为横向 sl2 模的局部有限性与完全可约分解。

本次另外实现了不预设模态指标截断的 PBW 检查器，完成 154 项有限精确检查。它不是 Lean/Coq 形式验证，也不等于执行了原仓库的全部测试。未修改远端仓库。

## 1. 可保留的主要进展

采用仓库记号，L=a+b+1≥1，中心水平为 κ。

### 1.1 边界同构

在 λ_L≠0 下，任意水平都有

\[
\mathcal T_{f_b}M_{a,b}(\chi)\cong M_{a+1,b-1}(\chi^+),
\qquad \lambda_0^+=\lambda_0+2,
\]

其余 character 参数不变。右正规 PBW 比较给出

\[
XE^pu'\longmapsto (-1)^p p!\lambda_L^p XF^{-p-1}u+M,
\qquad E=e_{a+1},\quad F=f_b.
\]

在本次检查中，这一基比较及迭代边界移动的证明没有发现错误。README 应明确写出 λ_L≠0。

### 1.2 非边界的基础结构

PBW 局部化模型、负根模态的 gap invariant、权支撑、Cartan 模态的 pole-growth 论证、深区 cyclicity、普通包络代数中的 annihilator 保持、商局部化的导出函子描述，以及互相交换的自由 f 模态的多重商局部化，具有独立于最新 G_c 稿的直接证明。

### 1.3 深区的准确单性判据和 simple head

假设

\[
c<b,\quad c\le-a-1,\quad \lambda_L\ne0,\quad\kappa\ne-2,
\]

令 E=e_{-c}, F=f_c, H=h_0-cK, μ=λ_0-cκ。9 月 15 日附录证明

\[
Q_c\text{ simple}\iff \mu\notin\mathbb Z.
\]

若 μ∈Z，则

\[
0\ne G_c=\{v\in Q_c:E^nv=0\text{ for some }n\}\subsetneq Q_c
\]

是唯一极大子模，Q_c/G_c 单，扩张不分裂，Q_c 不可分解。

关键一般性论证值得保留：对 Q 的子模逆像 P⊂D，构造

\[
W(P)=\bigcap_{n\ge0}F^nP.
\]

利用 ad F 的局部幂零性证明 W(P) 为 A-子模且对 F^{-1} 稳定。非零 W(P) 与原 simple 模 M 相交后给出 W(P)=D。再用横向 Casimir

\[
C=H^2+2H+4FE,
\qquad
F^nE^nz=4^{-n}\prod_{j=0}^{n-1}\bigl(C-(\nu+2j)(\nu+2j+2)\bigr)z
\]

及 Bézout 恒等式，从任意非 E-torsion 子模向量构造非零 W(P)。此处没有把 C 当成整个仿射包络代数的中心元。

这个证明不依赖最新稿的 T=π_0 E 递推。因此最新错误不传递到该判据。

### 1.4 中心约化与 derivation

对于通过 U-模自同态作用的交换代数 R 及其代数理想 I，有

\[
\mathcal T_F(V/IV)\cong (\mathcal T_F V)/I(\mathcal T_F V).
\]

cokernel 证明不要求 F 在 V/IV 上单射。临界水平实际 Sugawara 作用与其局部化延拓的一致性，附录另有 smoothness 论证。这一交换性本身不保证约化后非零或单。

加入 derivation 时应保留半直积作用

\[
x_r(P(d)\otimes v)=P(d-r)\otimes x_rv.
\]

诱导与商局部化交换，但诱导不一般保持单性。仓库附录对这一点的限定是正确的。

## 2. 错误一：丢失正次 F 分子项

以下反例全部位于最基本的

\[
Q=\mathcal T_{f_0}M_{-1,1}(\mu,\lambda_1,\kappa),
\qquad E=e_0,\quad F=f_0,\quad H=h_0.
\]

分式均表示商模中的类；F^{-1} 不是 Q 上的作用算子。

`lem:Eaction` 声称，定义 T=π_0 E 后，

\[
E(F^{-m}Xu)=F^{-m}T(Xu)
-m(\mu+\deg X+m+1)F^{-m-1}Xu.
\]

问题是：EXu∈M 的正次 F 分量在左乘 F^{-m} 后，并不都落回 M。F^r 项在 0≤r<m 时仍然贡献商模。

取 X=f_{-1}f_1。由真正的仿射括号关系，

\[
EXu=(f_1h_{-1}+\lambda_1f_{-1}-2F)u.
\]

所以

\[
\begin{aligned}
E(F^{-2}f_{-1}f_1u)
={}&F^{-2}(f_1h_{-1}+\lambda_1f_{-1})u\\
&-2F^{-1}u
-2(\mu-1)F^{-3}f_{-1}f_1u.
\end{aligned}
\]

最新稿公式漏掉了非零的 −2w_1。此错误对 μ、λ_1、κ 没有特殊限制。

## 3. 修正后的原初空间递推

令 V_0 是 F-free PBW 基向量的线性张成，使用向量空间直和

\[
M=\bigoplus_{r\ge0}F^rV_0.
\]

对 x∈V_0 定义线性算子 A_r:V_0→V_0：

\[
Ex=\sum_{r\ge0}F^r A_rx,
\qquad A_0=T.
\]

每个给定 x 的和有限。若 Hx=(μ+δ)x，则 Q 中正确公式为

\[
E(F^{-m}x)
=\sum_{r=0}^{m-1}F^{-(m-r)}A_rx
-m(\mu+\delta+m+1)F^{-m-1}x.
\]

设 v=Σ_{m=1}^N F^{-m}x_m 为权 ν 的非零原初向量，x_N≠0。最高 pole 仍迫使

\[
N=\nu+1,\qquad \nu\in\mathbb Z_{\ge0}.
\]

这一部分原结论可以保留。但其余各层必须满足

\[
\boxed{
\sum_{m=k}^{N}A_{m-k}x_m
=(k-1)(\nu-k+2)x_{k-1},
\quad 1\le k\le N,\quad x_0=0.
}
\]

从最高层向下解三角系统，最后 k=1 给出 compatibility condition。例如 ν=1 时：

\[
x_1=A_0x_2,\qquad (A_0^2+A_1)x_2=0,
\]

而不是原稿的 A_0^2x_2=0。

### 一个真正否定 T^{ν+1} 条件的原初向量

定义

\[
Z=h_{-1}^2+4f_{-1}e_{-1}+2h_{-2}
=h_{-1}^2+2(e_{-1}f_{-1}+f_{-1}e_{-1}).
\]

由括号直接可知 [E,Z]=[F,Z]=[H,Z]=0；这不意味着 Z 在整个仿射代数中中心。

在 μ=−1 时，

\[
p=\lambda_1F^{-1}u+F^{-2}f_1u\in P_1.
\]

于是 Zp 也属于 P_1，其两个 pole 层为

\[
Zp=F^{-1}x_1+F^{-2}x_2,
\]

\[
x_1=(\lambda_1Z-4h_{-1})u,
\qquad
x_2=(f_1Z-4(\kappa+1)f_{-1})u.
\]

完整 PBW 重排给出

\[
T^2x_2=8e_{-1}u\ne0.
\]

而 A_1x_2=−8e_{-1}u，恰由修正系统抵消。这说明 `thm:P` 的结论本身错误，不只是证明书写不完整。

## 4. 错误二：μ=−2 时 P_0 并非一维

最新英文和中文稿都断言 μ=−2 时 P_0=Cw_1。这与显式构造冲突。

在 μ=−2 时，Ew_1=Fw_1=Hw_1=0。利用上一节的 Z，可得

\[
Z^n w_1=F^{-1}Z^nu+M\in P_0,
\qquad n=0,1,2,\ldots.
\]

这些向量线性无关。理由：Z 只含负指标模态；Z^n u 的最高 PBW 次数为 2n，其主符号是

\[
(h_{-1}^2+4f_{-1}e_{-1})^n\ne0.
\]

不同 n 的最高次数不同，且没有分子 F 因子造成商模消失。

因此

\[
\dim P_0=\infty
\]

在这个基本模型、μ=−2 的整个参数族中成立，特别也包括 λ_1≠0、κ≠−2。

第一项新的原初向量已经是

\[
F^{-1}(h_{-1}^2+4f_{-1}e_{-1}+2h_{-2})u+M.
\]

另一方面，原稿“通过乘 h_{-1} 的幂证明原初空间无穷维”的理由也不成立，因为 [E,h_{-1}]=−2e_{-1}，乘 h_{-1} 不保持 ker E。这里使用的是确实与横向 sl2 对易的 Z。

## 5. 错误三：按横向最高权的尾部不是仿射子模

正确分解是作为横向 sl2 模的分解：

\[
G\cong\bigoplus_{\nu\ge0}P_\nu\otimes L(\nu).
\]

原稿据此定义

\[
G^{\ge\nu}=\bigoplus_{\nu'\ge\nu}P_{\nu'}\otimes L(\nu')
\]

并在 `lem:stable` 声称这些是整个仿射代数的子模。这一声称错误。

### 5.1 中心项给出的极短反证

取基本模型 μ=−2，并取 κ≠0（例如 λ_1=κ=1，原模是 simple）。p=w_1 属于横向 L(0) 块。

由 Ep=Fp=0，

\[
h_{\pm1}p=-Fe_{\pm1}p.
\]

而 e_{±1}p∈P_2，因此 h_{±1}p 属于 G^{≥2}。若 G^{≥2} 是仿射子模，则

\[
[h_1,h_{-1}]p=2\kappa p\in G^{\ge2}.
\]

这与 p 位于 L(0) 块且 κ≠0 矛盾。

同理，非零水平的非零平凡仿射商模不可能存在：K 在商模上仍为 κ，但所有 h 模态作用零会迫使 [h_1,h_{-1}]=2K 作用零。

### 5.2 被遗漏的降权原初投影

对 ν≥2 及 p∈P_ν，正确的一个降权投影是

\[
\boxed{
\ell_j(p)=f_jp-\frac1\nu Fh_jp
-\frac1{\nu(\nu+1)}F^2e_jp\in P_{\nu-2}.
}
\]

直接对右侧施加 E 即可验证。其原理是 current 模态在横向 sl2 的伴随作用下形成 L(2)，而

\[
L(2)\otimes L(\nu)
\cong L(\nu+2)\oplus L(\nu)\oplus L(\nu-2)
\qquad(\nu\ge2).
\]

最后一个分量不能省掉。

这个投影确实非零，并非仅是形式上的可能性。在 μ=−2 时取 p_2=e_{-1}w_1∈P_2。则

\[
\begin{aligned}
\ell_1(p_2)
&=f_1p_2-\tfrac12 Fh_1p_2-\tfrac16F^2e_1p_2\\
&=F^{-1}\left(
\tfrac13 f_1e_{-1}+\tfrac{\lambda_1}{6}h_{-1}
+\tfrac{2\kappa-2}{3}
\right)u+M\in P_0\setminus\{0\}.
\end{aligned}
\]

非零由 f_1e_{-1} 的 PBW 系数 1/3 保证。这还在 κ=0 时直接否定尾部稳定性。

### 5.3 影响范围

因此必须撤回当前证明中的：

- 作为仿射子模的“标准权滤过”；
- 其商的单性与据此识别的 head；
- 由该滤过推出的 G_c 永不单、soc(G_c)=0、soc(Q_c)=0、合成长度无限。

这里撤回的是作为已证结论的地位，并没有由此证明实际 G_c 是单的或具有有限长度。应回到 9 月 15 日附录已正确区分的状态：unique maximal submodule/simple head 已证，G_c 的内部结构尚待正确论证。

## 6. 其他局部错误与验证问题

### 6.1 原初升权算子的最高 pole 系数

原稿 `prop:proj` 把 e_i p 的最高层写成 e_iX。基本反例是 μ=−2：

\[
e_{-1}w_1
=F^{-1}e_{-1}u-F^{-2}h_{-1}u-2F^{-3}f_{-1}u+M.
\]

最高 pole 为 3，系数是 −2f_{-1}u，而非 e_{-1}u。中文稿的例子实际上写出了正确最高项，但其一般命题又写错。

### 6.2 原脚本的三模态空间不封闭

两个 G_c 脚本都把分子主要表示为 f_1^p e_{-1}^q h_{-1}^s。一般仿射重排会产生其他模态，不能未经证明删掉。

最短例子：

\[
T(h_{-1}^2u)
=-4e_{-1}h_{-1}u-4e_{-2}u.
\]

原脚本只保留第一项。类似地，f_2u=0 不意味着 f_2 在所有后继 PBW 向量上作用零。

`check_gc_sanity.py` 还包含五处 `check(True, ...)`：四处仅记录 f_{-1} 链，另一处记录一个 two-variable 断言。这些调用只增加计数，没有验证相关命题。

`check_gc_filter.py` 的“权记账”只检查若干向量是纯 H-weight，不能证明横向不可约块最高权不下降，更不能证明尾部是仿射子模。其 E 实现还预设了正在被审查的错误作用公式。

### 6.3 源文档一致性

英文 G_c 稿重复使用 c 表示中心水平和局部化下标，宜统一为 κ 和 c。标题附近还存在重复的 `\large ...}` 源码片段，需要编译时检查；本审查没有把该源文件完整编译一遍。

统一稿的 Open problems 与 9 月 15 日附录不同步：深区非整数单性及 simple head 已在附录推进，不应仍列为完全未证；相反 README 把最新 G_c 内部结构过早升级为定理。

## 7. 建议修改顺序

第一步，修正 README 的 theorem-status：边界、深区判据、unique maximal/simple head、代数中心约化交换性保留；G_c 的完整内部分类标记为被反例阻断。

第二步，以 A_r 全分量替换 π_0 单算子递推，保留正确的最高 pole=N=ν+1 结论；原初空间必须是 PBW 向量的线性空间，不能写成单个 monomial 的集合。

第三步，对所有仿射生成元同时计算到 L(ν+2)、L(ν)、L(ν−2) 的投影。新的结构研究必须包含上述非零降权通道，不能沿用旧尾部滤过。

第四步，将本报告的四类反例加入独立回归测试，增加跨模态重排与完整 Lie relation 检查，移除计作通过的 `check(True, ...)`。

研究陈述目前可稳妥推进到：在非临界非退化深区，商局部化的精确单性判据、整数参数的唯一极大子模和简单头部；内部 G_c 分类不能视为已完成。

## 8. 附件与运行

同目录文件：

- `independent_pbw_audit.py`：独立精确 PBW 检查程序；无预设模态指标截断。
- `independent_pbw_audit_results.json`：154 项检查名称与具体反例输出。
- `independent_pbw_audit.log`：本次执行结果。

运行：

```sh
python -m pip install sympy
python independent_pbw_audit.py
```

程序对有限输入进行精确符号计算，不依赖网络，也不修改被审查仓库。无预设指标截断不等于检查了无限多个向量：完整性的数学论证仍由正文的括号、PBW 与表示论证明承担。

原始材料定位：

- 仓库快照：https://github.com/haozhengding1628/affine-sl2-localization-quotients/tree/5f766461cb0a01d171b136b55a64cd1f214886de
- 外部输入：https://arxiv.org/html/2404.03855v2
