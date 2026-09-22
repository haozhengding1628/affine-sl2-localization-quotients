# 非边界局部化商：可证性质与下一步问题

日期：2026-09-11。本文讨论不含次数导子的代数；含导子的诱导提升见第 8 节。

以下“命题”均附直接证明，不表示已经完成独立审稿或形式化验证。
未完成的单性与子模分类明确列为问题。本文不修改此前的边界同构笔记。

## 1. 假设与结论范围

沿用
\[
\mathfrak g=(\mathfrak{sl}_2\otimes\mathbb C[t,t^{-1}])\oplus\mathbb CK,
\qquad U=U(\mathfrak g),
\]
\[
[e_r,f_s]=h_{r+s}+r\delta_{r+s,0}K,\quad
[h_r,e_s]=2e_{r+s},\quad [h_r,f_s]=-2f_{r+s},\quad
[h_r,h_s]=2r\delta_{r+s,0}K.
\]
同族根向量交换，\(K\) 中心。
取整数 \(a,b\)，\(a+b\ge0\)，置 \(L=a+b+1\ge1\)，
\[
S_{a,b}=\operatorname{span}\{K,h_i\ (i\ge0),e_i\ (i>a),f_j\ (j>b)\}.
\]
特征 \(\chi\) 在根向量上为零，\(\chi(K)=\kappa\)，
\(\chi(h_i)=\lambda_i\)，其中 \(i>L\) 时 \(\lambda_i=0\)。
记
\[
M=M_{a,b}(\chi)=U\otimes_{U(S_{a,b})}\mathbb C_\chi,\qquad u=1\otimes1_\chi.
\]
中心参数使用 \(\kappa\)，以免与局部化指标 \(c\) 混淆。

固定整数 \(c<b\)，令
\[
F=f_c,\qquad Q_c=T_FM=D_FM/M,\qquad d_*=b-c\ge1,\qquad
w_m=F^{-m}u+M\quad(m\ge1).
\]
所有分式在局部化中解释；\(F^{-1}\) 不是商模 \(Q_c\) 上的算子。
\(\operatorname{ad}F\) 在 \(U\) 上局部幂零，所以 Ore 局部化存在。
以下一般结构结论不要求 \(\lambda_L\ne0\) 或 \(\kappa\ne-2\)；
使用这些假设时另行注明。

文献 FGXZ 的 Theorem 1.1 给出原模的单性判据
\[
M_{a,b}(\chi)\text{ 单}\iff \lambda_L\ne0,\ \kappa\ne-2.
\]
这个判据不能直接套到非边界商模。

## 2. PBW、根算子及权结构

### 命题 2.1：PBW 模型与分母过滤

取 PBW 序：先放 \(F\)，再放全部 \(f_j\)（\(j\le b,j\ne c\)），
再放 \(e_i\)（\(i\le a\)）、\(h_r\)（\(r<0\)），最后放 \(S_{a,b}\)。
记中间三族的有序单项式集合为 \(\mathcal X\)。则
\[
\{F^qXu:q\ge0,\ X\in\mathcal X\},\quad
\{F^qXu:q\in\mathbb Z,\ X\in\mathcal X\},\quad
\{F^{-m}Xu+M:m\ge1,\ X\in\mathcal X\}
\]
分别是 \(M,D_FM,Q_c\) 的基。
因此 \(F\) 在 \(M\) 上单射，\(Q_c\ne0\)，且 \(Q_c\) 可数无限维。

在 \(Q_c\) 上，\(F\) 满射且局部幂零；特别地不是单射。
\[
\ker F^r=\operatorname{span}\{F^{-m}Xu+M:1\le m\le r\}.
\]
这些核递增并穷尽 \(Q_c\)，但通常不是 \(\mathfrak g\)-子模。
每个非零 \(\mathfrak g\)-子模必与 \(\ker F\) 非零相交。
最后一句来自：对其中任意非零向量施加最高一个仍非零的 \(F\) 次幂。

作为交换代数
\(\mathbb C[f_j:j\le b]\) 的模，\(Q_c\) 是若干份
\[
\left(\mathbb C[F,F^{-1}]/\mathbb C[F]\right)
\otimes\mathbb C[f_j:j\le b,\ j\ne c]
\]
的直和，副本由剩余 \(e,h\) 的 PBW 单项式编号。
这是一个主理想的一阶局部上同调模型；不能把这一交换代数模型当成完整的
\(\mathfrak g\)-作用公式。

### 命题 2.2：负根模态出现一个“缺口”

在整个 \(Q_c\) 上，
\[
\begin{cases}
f_c\text{ 满射且局部幂零};\\
f_j\text{ 单射且不满射},&j\le b,\ j\ne c;\\
f_j\text{ 局部幂零},&j>b.
\end{cases}
\]
第二项由上述 PBW 模型中的多项式乘法得出。
第三项因为 \(f_ju=0\)、\(\operatorname{ad}f_j\) 局部幂零，
且 \(f_j\) 与 \(F\) 交换，故局部幂零性从 \(M\) 传到 \(D_FM\) 及商。
因此局部幂零的负根模态指标集合恰好为
\[
\{c\}\cup\{j:j>b\}.
\]

标准模 \(M_{a',b'}(\psi)\) 对应的集合是半直线 \(\{j:j>b'\}\)。
故 \(Q_c\) 不同构于任何标准模 \(M_{a',b'}(\psi)\)，不是仅仅指定循环向量不合适。
固定 \(a,b,\chi\)，不同 \(c\le b\) 的非零局部化商之间甚至满足
\[
\operatorname{Hom}_{\mathfrak g}(T_{f_c}M,T_{f_{c'}}M)=0\qquad(c\ne c').
\]
证明：源中的 \(f_c\) 局部幂零，而目标中的 \(f_c\) 单射。
此论证包括与边界商 \(c'=b\) 的比较。

### 命题 2.3：smooth 权模，但不是有限重数权模

\(Q_c\) 是 smooth 模，\(K\) 作用为 \(\kappa\)。
关于 \(\mathbb Ch_0\oplus\mathbb CK\)，它是权模，
\[
\operatorname{Supp}_{h_0}Q_c=\lambda_0+2\mathbb Z.
\]
若 \(X\) 含 \(r_e\) 个 \(e\)-因子、\(r_f\) 个 \(f\)-因子，则
\[
h_0(F^{-m}Xu+M)=(\lambda_0+2m+2r_e-2r_f)(F^{-m}Xu+M).
\]
每个非零权空间都可数无限维：在固定相应 \(m,r_e,r_f\) 后，
加入任意多个 \(h_{-1}\) 因子给出同权的不同 PBW 基向量。
所以它不是有限重数的 Harish--Chandra 模。
没有正模态 \(h_1\) 的特征向量并不意味着它不是上述 Cartan 的权模。

smooth 性由有限交换公式
\[
h_rF^{-m}=F^{-m}h_r+2mF^{-m-1}f_{r+c},
\]
\[
e_rF^{-m}=F^{-m}e_r
-mF^{-m-1}(h_{r+c}+r\delta_{r+c,0}K)
-m(m+1)F^{-m-2}f_{r+2c}
\]
直接得出：对固定分子，取 \(r,r+c,r+2c\) 充分大即可。
原诱导模的 smooth 性由将高模态移过有限 PBW 单词验证。

\(Q_c\) 没有非零有限维商：\(F\) 的满射性和局部幂零性传到商，
而有限维空间上的满射幂零算子只能作用在零空间上。
它也没有非零有限维子模：有限维 smooth \(\mathfrak g\)-模必为平凡模，
因为共同的高模态消去界生成的 Lie 理想是整个 \(\mathfrak g\)；
但 \(Q_c\) 上 \(f_{c+1}\) 单射。整个仿射代数意义下的可积性同样不成立。

## 3. 整个模都没有低阶正 Cartan 模态的特征向量

### 命题 3.1

对 \(1\le i\le d_*=b-c\)，任意 \(\zeta\in\mathbb C\) 和非零 \(v\in Q_c\)，
\[
\operatorname{pole}_F((h_i-\zeta)v)=\operatorname{pole}_F(v)+1.
\]
这里极点阶是 PBW 展开中最大分母阶数。
特别地，\(h_i\) 没有任何非零局部有限向量，且
\[
\ker p(h_i)=0\qquad(0\ne p\in\mathbb C[t]).
\]
这排除特征向量、广义特征向量以及任意非零有限维 \(h_i\)-稳定子空间。

证明：设 \(v\) 的最高极点项为 \(F^{-m}v_m+M\)，
其中 \(v_m\) 是不含 \(F\) 的非零 PBW 分子。
\(F^{-m}h_iv_m\) 的极点阶至多 \(m\)，而交换项的最高极点系数为
\[
2m f_{c+i}v_m\pmod {FM}.
\]
因为 \(c+i\le b\)、\(c+i\ne c\)，\(f_{c+i}\) 在 \(M/FM\) 上是单射的多项式乘法，
这个系数非零。减去 \(\zeta v\) 不影响最高极点项。
迭代后各次幂给出不同极点阶，故任何非零多项式都不消去 \(v\)。

特别地，任何包含 \(h_1\) 的 Lie 子代数上的一维特征，都不可能在 \(Q_c\)
中有非零特征向量。因此
\[
\operatorname{Hom}_{\mathfrak g}(M_{a',b'}(\psi),Q_c)=0
\]
对所有上述标准诱导模成立。不能称这些模完全“没有 Whittaker 向量”：
该结论只适用于含 \(h_1\) 的诱导子代数及其一维特征。

### 命题 3.2：高阶正 Cartan 模态的相反行为

若 \(i>d_*\)，则 \(h_iw_m=\lambda_iw_m\) 对所有 \(m\ge1\) 成立，
并且 \(h_i-\lambda_i\) 在整个 \(Q_c\) 上局部幂零。

证明后一句可用下述基本观察：在 smooth 模中，若 \(h_iw=\lambda w\)、\(i>0\)，
则 \((h_i-\lambda)^N Xw=(\operatorname{ad}h_i)^N(X)w\)。
对固定有限单词 \(X\)，右侧每项仅把根向量指标增加非负倍的 \(i\)，
或由 Cartan 括号产生中心项。次数 \(N\) 足够大时，必有一个根模态的指标
足够大，将其移至右侧后仍然足够大，于是消去 \(w\)。
由有限交换公式，\(Q_c\) 被所有 \(Uw_m\) 张成，因而结论成立。

所以低阶正 Cartan 模态的非局部有限区间恰好是 \(1,\ldots,b-c\)。
这给出了另一个可辨认局部化深度的模不变量。

## 4. 基本情形 \(Q_0=T_{f_0}M_{-1,1}\)

本节所有断言均允许任意 \(\lambda_0,\lambda_1,\kappa\)。
令 \(w_m=f_0^{-m}u+M\)。最关键的公式为
\[
f_0w_m=w_{m-1}\ (m>1),\qquad f_0w_1=0,\qquad
h_0w_m=(\lambda_0+2m)w_m,
\]
\[
e_0w_m=-m(\lambda_0+m+1)w_{m+1},
\]
\[
h_1w_m=\lambda_1w_m+2m f_1w_{m+1},\qquad
e_1w_m=-m\lambda_1w_{m+1}-m(m+1)f_1w_{m+2}.
\]
与边界 \(f_1\) 的情形不同，纯负幂递推的控制参数是 \(\lambda_0\)，不是 \(\lambda_1\)。

### 命题 4.1：循环性及指定循环向量的精确例外

\(Q_0\) 对所有参数都是循环模，且
\[
Q_0=Uw_1\iff\lambda_0\notin\{-2,-3,-4,\ldots\}.
\]
若 \(\lambda_0=-s\)、\(s\ge2\)，则 \(Q_0=Uw_s\)，但 \(Uw_1\ne Q_0\)。

证明充分性：若递推系数从 \(m=1\) 起均非零，\(w_1\) 生成所有 \(w_m\)。
若 \(\lambda_0=-s\)，从 \(w_s\) 出发向上使用 \(e_0\)，向下使用 \(f_0\)，
同样生成所有纯负幂。
给 PBW 因子赋权 \(\rho=2\#e+\#h\)，有限交换公式给出
\[
Xw_m=F^{-m}Xu+M+\text{严格较低 }\rho\text{ 的有限余项}.
\]
对 \(\rho\) 同时覆盖所有分母阶数归纳，即得所有 \(w_m\) 生成整个 \(Q_0\)。
必要性使用下一命题：若 \(\lambda_0=-s\)，\(e_0^{s-1}w_1=0\)，
故 \(Uw_1\) 位于一个真子模中，而 \(w_s\) 不在其中。

### 命题 4.2：整数参数下必可约

定义
\[
G=\{v\in Q_0:e_0^Nv=0\text{ 对某个 }N\ge1\}.
\]
由于 \(\operatorname{ad}e_0\) 在 \(U\) 上局部幂零，\(G\) 是 \(\mathfrak g\)-子模。
有
\[
\lambda_0\in\mathbb Z\ \Longrightarrow\ 0\ne G\ne Q_0,
\qquad
\lambda_0\notin\mathbb Z\ \Longrightarrow\ G=0.
\]
因此整数参数下 \(Q_0\) 总可约，即使原模满足 \(\lambda_1\ne0,\kappa\ne-2\) 因而是单模。
非整数时这里只证明 \(e_0\) 单射；尚不能由此断言 \(Q_0\) 单。

整数情形的完整构造如下。设 \(p=\lambda_0\in\mathbb Z\)，选
\(k\ge\max(1,p+2)\)，令 \(x=f_0,y=f_1,\eta=\lambda_1\)。
子空间 \(\mathbb C[x,y]u\) 在 \(e_0,f_0,h_0\) 下稳定，且
\[
e_0(x^j y^\ell u)
=j(p-j+1-2\ell)x^{j-1}y^\ell u
+\ell\eta x^j y^{\ell-1}u.
\]
取
\[
v_k=\sum_{j=0}^k a_j x^j y^{k-j}u,\qquad a_0=1,\qquad
a_j=-\frac{(k-j+1)\eta}{j(p-2k+j+1)}a_{j-1}.
\]
分母均非零，因为 \(p-2k+j+1\le p-k+1<0\)。
逐项抵消给出 \(e_0v_k=0\)，\(h_0v_k=(p-2k)v_k\)。
置 \(\mu=p-2k\le-2\)。商中
\[
f_0^{-1}v_k+M=f_1^k w_1\ne0,\qquad
e_0^{-\mu-1}(f_1^k w_1)=0.
\]
最后一个等式是普通 \(\mathfrak{sl}_2\) 负幂递推，因此 \(G\ne0\)。
另一方面取 \(m\ge\max(1,-p)\)，则从 \(w_m\) 开始的递推系数永不为零，
所以 \(w_m\notin G\)，证明 \(G\ne Q_0\)。

非整数情形：若 \(0\ne v\in G\)，取一个非零 \(h_0\)-权分量，再作用适当的
\(e_0\) 次幂得到 \(0\ne v'\in\ker e_0\)。因为 \(f_0\) 局部幂零，
选最小 \(N\ge1\) 使 \(f_0^Nv'=0\)。设 \(h_0v'=\nu v'\)，则
\[
0=e_0f_0^Nv'=N(\nu-N+1)f_0^{N-1}v',
\]
故 \(\nu=N-1\in\mathbb Z\)，与 \(\nu\in\lambda_0+2\mathbb Z\) 矛盾。

\(G\) 是最大的 \(e_0\)-局部幂零子模。作为
\(\langle e_0,h_0,f_0\rangle\cong\mathfrak{sl}_2\)-模，它局部有限。
商 \(Q_0/G\) 非零且 \(e_0\) 单射：
若 \(e_0v\in G\)，则 \(v\in G\)。
这里没有证明 \(G\)、\(Q_0/G\) 单，也没有证明整个模长度为二。

例如，\(\lambda_0=-2\) 时 \(e_0w_1=f_0w_1=h_0w_1=0\)，
但 \(Uw_1\) 一般远不止一维；它在整个仿射代数作用下是非零真子模。
\(\lambda_0=0\) 时，\(w_1\) 仍生成整个模，但
\(0\ne f_1^2w_1\in G\)、\(e_0^3f_1^2w_1=0\)。

### 可计算的 Takiff 子空间

\[
V=\operatorname{span}\{f_1^kw_m:m\ge1,k\ge0\}
\cong\mathbb C[x,x^{-1},y]/\mathbb C[x,y]
\]
是非负 current 子代数的子模，且次数至少二的模态作用为零。
它因而是 \(\mathfrak{sl}_2[t]/(t^2)\)-模，作用为
\[
\begin{aligned}
f_0&=x,& f_1&=y,\\
h_0&=\lambda_0-2x\partial_x-2y\partial_y,&
h_1&=\lambda_1-2y\partial_x,\\
e_0&=\lambda_0\partial_x+\lambda_1\partial_y
-x\partial_x^2-2y\partial_x\partial_y,&
e_1&=\lambda_1\partial_x-y\partial_x^2.
\end{aligned}
\]
这是精确公式，不是近似截断；但 \(V\) 不是整个仿射代数的子模，
因此不能把 \(V\) 的任意子模自动当成 \(Q_0\) 的子模。
上面使用 \(G\) 正是为了保证构造在整个仿射代数下稳定。

## 5. 一般 \(c<b\)：两种不同的参数区域

### 谱流归一化

定义自同构
\[
\sigma_k(e_i)=e_{i+k},\quad \sigma_k(f_i)=f_{i-k},\quad
\sigma_k(h_i)=h_i+k\delta_{i,0}K,\quad \sigma_k(K)=K.
\]
扭曲约定为 \(x\cdot_{\mathrm{new}}v=\sigma_k(x)v\)。
取 \(k=-c\)，得到
\[
(Q_c)^{\sigma_{-c}}
\cong T_{f_0}M_{a+c,b-c}(\chi'),
\qquad
\chi'(h_0)=\mu:=\lambda_0-c\kappa,\quad
\chi'(h_i)=\lambda_i\ (i>0).
\]
这是扭曲后的同构，不是忽略自同构的原模同构。
因此自然坐标为
\[
A=a+c,\qquad B=b-c=d_*,\qquad A+B=L-1,\qquad \mu=\lambda_0-c\kappa.
\]
FGXZ §3.1 已使用同类自同构；这里额外跟踪了局部化元素。

### 命题 5.1：深区 \(c\le-a-1\)，即 \(d_*\ge L\)

此时
\[
E=e_{-c},\qquad H=h_0-cK,\qquad F=f_c
\]
构成 \(\mathfrak{sl}_2\)，且 \(Eu=0,\ Hu=\mu u\)。
因此
\[
Ew_m=-m(\mu+m+1)w_{m+1}.
\]
命题 4.1 的循环性证明逐字推广：
\[
Q_c=Uw_1\iff\mu\notin\{-2,-3,\ldots\}.
\]
若 \(\mu=-s,\ s\ge2\)，则 \(Q_c=Uw_s\ne Uw_1\)。
这些断言不要求 \(\lambda_L\ne0\)。

定义
\[
G_c=\{v\in Q_c:E^Nv=0\text{ 对某个 }N\ge1\}.
\]
同样有
\[
\mu\in\mathbb Z\Longrightarrow 0\ne G_c\ne Q_c,\qquad
\mu\notin\mathbb Z\Longrightarrow G_c=0.
\]
所以在深区，\(\lambda_0-c\kappa\in\mathbb Z\) 是明确的可约性条件。

整数情形的构造取 \(G_1=f_b\)，在 \(\mathbb C[F,G_1]u\) 上有
\[
E(F^jG_1^\ell u)
=j(\mu-j+1-2\ell)F^{j-1}G_1^\ell u
+\ell\lambda_{d_*}F^jG_1^{\ell-1}u.
\]
因为 \(d_*\ge L\)，\(f_{b+d_*}u=0\)，而所有额外高模态均消去 \(u\)。
此公式与第 4 节完全相同，只需把
\((p,\eta,x,y)\) 换成 \((\mu,\lambda_{d_*},F,f_b)\)。
当 \(d_*>L\) 时 \(\lambda_{d_*}=0\)，构造反而简化为 \(v_k=f_b^ku\)。
于是存在非零
\[
f_b^kw_1\in G_c,\qquad k\ge\max(1,\mu+2),
\]
并且选择足够大的纯负幂即可证明 \(G_c\) 为真子模。
商 \(Q_c/G_c\) 中 \(E\) 单射。

### 命题 5.2：浅区 \(-a\le c<b\)，即 \(1\le d_*<L\)

此时 \(E=e_{-c}\) 属于原 PBW 补空间，不能使用 \(Eu=0\)。
改取 \(Y=e_{L-c}\)。有
\[
Yu=0,\quad [Y,F]=h_L,\quad f_{L+c}u=0,
\qquad Yw_m=-m\lambda_Lw_{m+1}.
\]
其中 \(L+c>b\) 正是浅区条件。
因此 \(\lambda_L\ne0\) 时，\(Q_c=Uw_1\)。

另一方面，\(E=e_{-c}\) 在整个 \(Q_c\) 上单射：
用 \(\rho=2\#e+\#h\) 比较最高层，左乘 \(E\) 的最高项是给 PBW 单项式
增加一个自由的 \(e_{-c}\) 因子，权增加二；其他交换项至多增加一。
最高项不会抵消。因此 \(G_c=0\)，不论 \(\mu\) 是否为整数。

这说明深区的整数可约性论证不能直接推广到所有 \(c<b\)。
浅区在 \(\lambda_L\ne0,\kappa\ne-2\) 下是否总单，是另一个待证问题。

## 6. 不分裂扩张、annihilator 与函子性质

### 命题 6.1：自然短正合列不分裂

\[
0\longrightarrow M\longrightarrow D_FM\longrightarrow Q_c\longrightarrow0
\]
永不分裂。因为 \(Q_c\) 是 \(F\)-torsion，而 \(F\) 在 \(D_FM\) 上单射，
故 \(\operatorname{Hom}_{\mathfrak g}(Q_c,D_FM)=0\)。
同时 \(\operatorname{Hom}_{\mathfrak g}(Q_c,M)=0\)，
而第 3 节给出 \(\operatorname{Hom}_{\mathfrak g}(M,Q_c)=0\)。

若 \(M\) 是单模，则它是 \(D_FM\) 的唯一简单子模，且是本质子模：
任意非零 \(v\in D_FM\) 乘以足够高的 \(F\) 次幂，得到 \(M\) 中的非零向量。
所以 \(D_FM\) 不可分解；这并不自动推出商 \(Q_c\) 不可分解。

### 命题 6.2：普通包络代数中的 annihilator 不变

\[
\operatorname{Ann}_U M
=\operatorname{Ann}_U D_FM
=\operatorname{Ann}_U Q_c.
\]
这里仅讨论普通 \(U\) 中的元素，不把结论未经证明地推广到临界层的完成中心。

证明：\(\operatorname{Ann}_UM\) 是双侧理想，故在
\(\Delta=\operatorname{ad}F\) 下稳定。负幂交换公式表明它也消去 \(D_FM\)，
再结合 \(M\hookrightarrow D_FM\)，得到前两个 annihilator 相等，
并包含于 \(\operatorname{Ann}_UQ_c\)。

反之，设 \(sQ_c=0\)，选择 \(t\ge0\) 使 \(\Delta^{t+1}(s)=0\)。
对 \(v\in M\) 和 \(m\ge1\)，\(sF^{-m}v\in M\)。左乘 \(F^{m+t}\)，得到
\[
P_v(m):=\sum_{j=0}^t
\binom{m+j-1}{j}F^{t-j}\Delta^j(s)v
\in F^{m+t}M.
\]
这是关于 \(m\) 的向量值多项式，其系数只有有限个 PBW 项，
所以它们的非负 \(F\) 次数有共同上界。
当 \(m\) 充分大时，它们张成的空间与 \(F^{m+t}M\) 相交为零。
于是 \(P_v(m)=0\) 对所有充分大的整数 \(m\) 成立，
故该多项式恒为零。代入 \(m=0\)，利用
\(\binom{j-1}{j}=0\)（\(j\ge1\)），得到 \(F^tsv=0\)。
\(F\) 在 \(M\) 上单射，故 \(sv=0\)，证明所需包含。

### 局部上同调与导出函子

对任意 \(U\)-模 \(V\)，将 \(T_FV\) 定义为局部化映射的余核，则
\[
T_FV=(U_F/U)\otimes_UV,\qquad
L_1T_F(V)=\{v:F^nv=0\text{ 对某个 }n\ge0\},\qquad
L_jT_F(V)=0\ (j\ge2).
\]
证明来自右 \(U\)-模的平坦分辨率 \(0\to U\to U_F\to U_F/U\to0\)。
因此它是右正合函子，并在三个项均 \(F\)-torsion-free 的短正合列上正合；
不能宣称它在所有模上正合。
特别地，
\[
D_FQ_c=0,\qquad T_FQ_c=0,\qquad L_1T_F(Q_c)\cong Q_c.
\]

## 7. 再局部化：与已知边界同构的联系

若 \(F=f_c,G=f_j\) 是两个不同的 PBW 自由负根模态（\(c,j\le b\)），则
\[
T_G(T_FM)\cong
\frac{D_{FG}M}{D_FM+D_GM}
\cong T_F(T_GM).
\]
这里 \(D_{FG}\) 表示同时反演 \(F,G\)。
证明：两元素交换，局部化交换；PBW 的两个独立多项式变量给出
\(D_FM\cap D_GM=M\)，并且任意一个先取商后另一个仍单射。
中间商由两个变量次数都严格为负的 PBW 项表示。

因此，在 \(\lambda_L\ne0\) 时，无论以什么次序对
\[
f_c,f_{c+1},\ldots,f_b
\]
依次作局部化商，最终得到
\[
M_{a+b-c+1,c-1}(\chi^{(b-c+1)}),
\qquad
\chi^{(b-c+1)}(h_0)=\lambda_0+2(b-c+1),
\]
其余特征值不变。
证明只需把次序交换为从 \(f_b\) 开始，逐次使用已有边界同构。
这是有限次、对不同模态的局部化商，不是同时反演后仅除以原模。

最基础的实例是
\[
T_{f_1}\bigl(T_{f_0}M_{-1,1}(\chi)\bigr)
\cong T_{f_0}\bigl(T_{f_1}M_{-1,1}(\chi)\bigr)
\cong M_{1,-1}(\chi^{(2)}),\qquad \lambda_1\ne0.
\]
这把新的非边界模与已经掌握的标准模联系起来，
但“再次取局部化商后是单模”不等于“第一次的商模是单模”。

## 8. 加入导子与顶点代数

之前证明的自然同构不要求 \(F\) 是边界元素，故仍有
\[
\mathcal I(Q_c)\cong T_{f_c}\mathcal I(M),\qquad
\mathcal I(M)=U(\widetilde{\mathfrak g})\otimes_{U(\mathfrak g)}M.
\]
在 \(\mathbb C[z]\otimes M\) 中，模态作用带平移 \(P(z-r)\)，
而分式识别带平移 \(P(z+mc)\)。
因 \(\mathcal I\) 正合且忠实，\(0\ne G_c\ne Q_c\) 会给出
\(0\ne\mathcal I(G_c)\ne\mathcal I(Q_c)\)。
反向的单性保持仍不能默认。

由 smooth 性及固定 level，这些模是普遍仿射顶点代数
\(V^\kappa(\mathfrak{sl}_2)\) 的弱模。
是否下降为其简单商的模，需要单独检查该顶点代数的定义理想；
不能仅凭 smooth 性宣布这一点。

## 9. 优先研究的问题：哪些还没有证明？

1. **基本模的非整数单性。** 在原模单的假设
   \(\lambda_1\ne0,\kappa\ne-2\) 下，最自然的候选判据是
   \(T_{f_0}M_{-1,1}\) 单当且仅当 \(\lambda_0\notin\mathbb Z\)。
   本文已证明必要方向，尚未证明充分方向。
   需要从任意非零子模中的向量出发，降到能够生成整个模的纯负幂；
   “\(w_1\) 生成整个模”以及“\(e_0\) 单射”都不能替代这一步。

2. **深区的对应判据。** 在 \(\lambda_L\ne0,\kappa\ne-2\) 下，
   研究非整数 \(\lambda_0-c\kappa\) 是否足以保证单性。
   可尝试秩一 twisting/completion 方法或直接 PBW 降阶；
   应证明相关函子适用于这里的 smooth 模范畴，而非直接套用 BGG \(\mathcal O\)。

3. **整数区的子模层。** 计算 \(G_c\)、\(Q_c/G_c\) 是否单、
   \(G_c\) 是否为 socle、扩张是否分裂，以及 Jordan--Hölder 长度。
   目前只得到一个规范非零真子模，不宣称长度为二或不可分解。

4. **浅区的单性。** 此时 \(e_{-c}\) 单射，深区的整数障碍消失。
   研究原模单是否已经足够，或是否有另一组共振条件。

5. **参数同构与退化。** 已知 \(\kappa\)、\(h_0\)-权支撑、
   负根局部幂零集合、低阶正 Cartan 非局部有限区间都是约束。
   高阶 \(h_i\) 的广义特征值也给出参数约束。
   尚未完成 \(\lambda_0,\ldots,\lambda_L\) 的完整同构分类，
   特别是 \(\lambda_L=0\) 或 \(\kappa=-2\) 的情形。

6. **临界层中心约化。** 在 \(\kappa=-2\) 时，结合完成中心作用，
   研究先中心约化再局部化与反序操作，以及所得简单商。
   普通包络代数 annihilator 相等的证明并不自动处理完成中心。

7. **多缺口与扭曲局部化。** 有限多根模态的局部化商有交换次序的性质，
   值得组织成多缺口族。另可对 \(D_FM\) 施加广义共轭
   \(\Theta_z(s)=\sum_{j\ge0}\binom zj(\operatorname{ad}F)^j(s)F^{-j}\)。
   这个公式定义在 \(F\) 已可逆的局部化上，不能直接拿来扭曲 \(Q_c\)。

## 10. 文献关系与核对记录

- **FGXZ (2024 v2; 2025 journal version):**
  V. Futorny, X. Guo, Y. Xue, K. Zhao,
  *Smooth representations of affine Kac--Moody algebras*.
  本文使用其原模定义、Theorem 1.1 单性判据、§3.1 自同构，
  以及 smooth 模与普遍仿射顶点代数的对应。
  [arXiv v2](https://arxiv.org/html/2404.03855v2)
- **FGM (2015):**
  V. Futorny, D. Grantcharov, R. A. Martins,
  *Localization of free field realizations of affine Lie algebras*.
  其 Theorem 4.3 在 imaginary Verma/free-field 模块中出现
  \(J-iK\in\mathbb Z\) 的可约性分界；§5 构造原始向量并证明相应非整数单性，
  引言也解释了局部化商与 Arkhipov 型函子的关系。
  这与本文深区的秩一共振吻合，但模块不同，其充分性结论不能直接引用为本文的结论。
  [arXiv v2](https://arxiv.org/html/1404.7148v2)

本次对 Takiff 子空间的作用公式做了 5866 项精确有理数检查，
包括全部六个生成元的括号关系、整数参数的最高向量递推、
非零局部幂零向量及纯负幂共振。参数检查包含 \(\lambda_1=0\)，
没有使用多项式次数截断；但仅检查有限组参数和向量，不代替上述一般证明。
脚本：work/check_nonboundary_takiff.py。
本次没有重新运行 Danus，也没有完成独立审稿或 Lean/Coq 形式化验证。
