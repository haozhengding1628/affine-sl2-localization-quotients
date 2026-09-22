# Danus-accepted mathematical candidates

Date: 2026-09-08. These are LLM-reviewed proofs, NOT formal proof certificates.

The two facts are independent. Applying the derivation functorial theorem to the boundary theorem yields the combined isomorphism in the Chinese note.


## Boundary

Fact ID: `d6bf6fef62dc8971`. Accepted attempt: 1.

### Statement

Let \(\mathfrak g\) be the complex Lie algebra with generators \(e_i,f_i,h_i\) for \(i\in\mathbb Z\), and central \(K\), satisfying
\[
[e_i,f_j]=h_{i+j}+i\delta_{i+j,0}K,\quad [h_i,h_j]=2i\delta_{i+j,0}K,
\]
\[
[h_i,e_j]=2e_{i+j},\quad [h_i,f_j]=-2f_{i+j},\quad [e_i,e_j]=[f_i,f_j]=0.
\]
Put \(U=U(\mathfrak g)\). For integers \(a,b\) with \(a+b\ge0\), set \(L=a+b+1\) and
\[
S_{ab}=\operatorname{span}\{K,h_i\ (i\ge0),e_i\ (i>a),f_j\ (j>b)\}.
\]
Let \(\chi(K)=c\), \(\chi(h_i)=\lambda_i\) for \(0\le i\le L\), \(\chi(h_i)=0\) for \(i>L\), and let \(\chi\) vanish on the root vectors in \(S_{ab}\). Write \(M_{ab}(\chi)=U\otimes_{U(S_{ab})}\mathbb C_\chi\), with inducing vector \(u\).

**Boundary move.** If \(\lambda_L\ne0\), then, for \(F=f_b\), multiplication by \(F\) is injective on \(M_{ab}(\chi)\), and there is an isomorphism
\[
\Phi:M_{a+1,b-1}(\chi^+)\xrightarrow{\sim}T_FM_{ab}(\chi),\qquad v\longmapsto F^{-1}u+M_{ab}(\chi),
\]
where \(\chi^+(h_0)=\lambda_0+2\) and all other Cartan and central values remain unchanged. This holds for arbitrary integers \(a,b\) as above and arbitrary \(c\).

Writing \(Y=e_{a+1}\), an explicit preimage of every pure negative power is
\[
\Phi^{-1}(F^{-m}u+M_{ab}(\chi))
=\frac{(-1)^{m-1}}{(m-1)!\lambda_L^{m-1}}Y^{m-1}v\qquad(m\ge1).
\]
In particular, for \(a=-1,b=n\ge1\) and \(\lambda_n\ne0\), this is
\[
\frac{(-1)^{m-1}}{(m-1)!\lambda_n^{m-1}}e_0^{m-1}v.
\]
If \(\lambda_L=0\), the same cyclic assignment is well-defined but is not injective.

**Keeping the original module fixed.** Let \(M=M_{-1,1}(\chi)\), with \(\lambda_1\ne0\). For every \(n\ge2\), \(f_n\) acts locally nilpotently, so \(D_{f_n}M=0\) and its localization cokernel is zero. For \(n\le0\), \(f_n\) acts injectively and \(T_{f_n}M\ne0\), but \(f_n^{-1}u+M\) is not an \(h_1\)-eigenvector. Consequently, no homomorphism from any standard module \(M_{a',b'}(\psi)\) can send its inducing vector to this vector. For \(n=1\), the boundary move gives \(T_{f_1}M\cong M_{0,0}(\chi^+)\).

**Finite iteration.** Under \(\lambda_L\ne0\), define \(N_0=M_{ab}(\chi)\) and \(N_{r+1}=T_{f_{b-r}}N_r\). For every finite \(r\ge0\),
\[
N_r\cong M_{a+r,b-r}(\chi^{(r)}),
\]
where \(\chi^{(r)}(h_0)=\lambda_0+2r\), with all other Cartan and central values unchanged.

### Proof

**Localization and PBW preliminaries.** First, \(S_{ab}\) is a Lie subalgebra and the displayed values define a character. Indeed, the only potentially relevant root-pair bracket has indices \(i>a,j>b\), hence \(i+j\ge a+b+2=L+1>0\). Its Cartan value under \(\chi\) is zero and its central term is absent. The remaining brackets also have zero character value. The same argument applies after any boundary move.

For any integer \(n\), let \(F=f_n\) and \(\delta=\operatorname{ad}F\). Directly from the relations,
\[
\delta(e_i)=-h_{i+n}-i\delta_{i+n,0}K,\qquad
\delta^2(e_i)=-2f_{i+2n},\qquad \delta^3(e_i)=0,
\]
while \(\delta(h_i)=2f_{i+n}\), \(\delta^2(h_i)=0\), and \(\delta(f_i)=\delta(K)=0\). The Leibniz rule therefore makes \(\delta\) locally nilpotent on \(U\).

PBW implies that \(U\) is a domain: its associated graded algebra for the usual degree filtration is the symmetric algebra of \(\mathfrak g\). The identities
\[
F^NA=\sum_k\binom Nk\delta^k(A)F^{N-k},\qquad
AF^N=\sum_k(-1)^k\binom NkF^{N-k}\delta^k(A)
\]
show that powers of \(F\) satisfy both Ore conditions. For example, if \(\delta^k(A)=0\) for \(k>d\), choosing \(N\ge m+d\) makes the first expression belong to \(UF^m\) and the second to \(F^mU\). Thus \(U[F^{-1}]\) exists.

We recall explicitly the fraction properties used below. Every element of \(D_FM\) can be represented as \(F^{-r}z\), with \(r\ge0,z\in M\). The fraction construction identifies \((r,z)\) and \((s,y)\) precisely when, for some \(t\ge r,s\),
\[
F^{t-r}z=F^{t-s}y.
\]
These are the equivalence relations of the vector-space direct limit under multiplication by \(F\); the Ore identities supply its localized module structure. In particular, \(z\) maps to zero exactly when some power of \(F\) kills \(z\). Consequently, injectivity of \(F\) implies injectivity of \(M\to D_FM\).

For later use, finite commutation with an inverse gives, for \(m\ge1\),
\[
AF^{-m}=\sum_{k\ge0}\binom{m+k-1}{k}F^{-(m+k)}\delta^k(A).\tag{1}
\]
For \(m=1\), this follows by iterating \(AF^{-1}=F^{-1}A+F^{-1}\delta(A)F^{-1}\); the iteration terminates by local nilpotence. Induction on \(m\) proves the displayed coefficients.

Now take \(F=f_b\) and \(M=M_{ab}(\chi)\). Let \(\mathcal X\) consist of all monomials
\[
X=e(\alpha)h(\beta)f(\gamma),\qquad
\alpha_i\le a,\quad\beta_i\le-1,\quad\gamma_i\le b-1,
\]
with factors ordered within each family, including the empty monomial. Choose a total ordering of a basis of \(\mathfrak g\) in which the exterior generators occur as
\[
F;\quad e_i\ (i\le a);\quad h_i\ (i<0);\quad f_i\ (i\le b-1),
\]
followed by a basis of \(S_{ab}\). PBW, followed by tensoring over \(U(S_{ab})\), says that
\[
\{F^qXu:q\ge0,\ X\in\mathcal X\}\tag{2}
\]
is a basis of \(M\). In particular, left multiplication by \(F\) simply increases \(q\), so it is injective.

Clearing a common denominator in a finite linear relation now shows that
\[
\{F^kXu:k\in\mathbb Z,\ X\in\mathcal X\}
\]
is a basis of \(D_FM\). Indeed, multiplication by a sufficiently large power of \(F\) converts any proposed relation into a relation among (2). Therefore
\[
\{F^{-m}Xu+M:m\ge1,\ X\in\mathcal X\}\tag{3}
\]
is a basis of \(T_FM\).

For the source \(M^+=M_{a+1,b-1}(\chi^+)\), put \(Y=e_{a+1}\). Order its exterior generators as the generators occurring in \(X\), followed by \(Y\), and then place a basis of \(S_{a+1,b-1}\) last. PBW gives the source basis
\[
\{XY^pv:p\ge0,\ X\in\mathcal X\}.\tag{4}
\]
The exterior span need not be a subalgebra: these assertions follow from PBW freeness as a right module over the enveloping algebra of the inducing subalgebra.

**Well-definedness of the cyclic map.** Write \(w=F^{-1}u+M\), and extend the convention \(\lambda_i=0\) to \(i>L\). For \(i\ge0\),
\[
h_iF^{-1}u=\lambda_iF^{-1}u+2F^{-2}f_{b+i}u.
\]
For \(i>0\), the second term is zero because \(f_{b+i}u=0\); for \(i=0\), it equals \(2F^{-1}u\). Thus \(h_0w=(\lambda_0+2)w\), \(h_iw=\lambda_iw\) for \(i>0\), and \(Kw=cw\).

All \(f_j\) commute with \(F\). Hence \(f_jw=0\) for \(j>b\), while \(f_bw=u+M=0\).

Finally, let \(j>a+1\). Then \(j+b\ge L+1>0\), so there is no central term in \([e_j,F]\). Formula (1) gives
\[
e_jF^{-1}u
=F^{-1}e_ju-F^{-2}h_{j+b}u-2F^{-3}f_{j+2b}u=0.
\]
Here \(e_ju=0\), \(h_{j+b}u=0\), and \(j+2b>b\). These are all the defining relations for the inducing vector of \(M^+\). The induced-module universal property therefore gives the homomorphism \(\Phi(v)=w\).

**The pure negative-power tower.** Since
\[
[Y,F]=h_L,\qquad [F,h_L]=2f_{b+L},
\]
formula (1) yields
\[
YF^{-m}u
=F^{-m}Yu-mF^{-(m+1)}h_Lu
-m(m+1)F^{-(m+2)}f_{b+L}u
=-m\lambda_LF^{-(m+1)}u.\tag{5}
\]
We used \(Yu=0\), \(L\ge1\), and \(f_{b+L}u=0\). In particular, no central-charge restriction appears. Iteration gives
\[
\Phi(Y^pv)=c_pF^{-(p+1)}u+M,
\qquad c_p=(-1)^pp!\lambda_L^p.\tag{6}
\]
This proves the asserted explicit preimages when \(\lambda_L\ne0\).

**Triangularity for every PBW monomial and denominator.** Assign weights
\[
\operatorname{wt}(e_i)=2,\quad \operatorname{wt}(h_i)=1,\quad
\operatorname{wt}(f_i)=\operatorname{wt}(K)=0,
\]
and give a word its total weight. This defines a nonnegative filtration on \(U\). Every nonzero generator bracket has weight at most the sum of the input weights minus one: the four possibilities are \([e,f]\), \([h,h]\), \([h,e]\), and \([h,f]\). Thus every PBW reordering preserves or lowers total weight, including brackets with central terms.

Also, \(\delta=\operatorname{ad}F\) lowers weight by at least one and kills the weight-zero subalgebra. Consequently,
\[
\delta^k(X)\text{ has weight at most }\operatorname{wt}(X)-k,
\qquad \delta^k(X)=0\text{ if }k>\operatorname{wt}(X).
\]
Reorder \(\delta^k(X)u\) in the target PBW basis (2). Moving inducing-subalgebra factors to the right does not increase weight. Evaluating them on \(u\) does not increase weight either: Cartan generators become scalars, \(K\) becomes \(c\), and root generators act by zero. Hence the result is a finite linear combination of
\[
F^qX'u,\qquad q\ge0,\quad
\operatorname{wt}(X')\le\operatorname{wt}(X)-k.\tag{7}
\]
Apply (1) with \(A=X\). Its \(k=0\) term is \(F^{-m}Xu\). Each term with \(k\ge1\), after (7), has the form
\[
F^{-(m+k-q)}X'u.
\]
If \(m+k-q\le0\), it lies in \(M\) and vanishes in the quotient. Otherwise it is a basis vector of (3) of strictly smaller exterior weight. Thus, for every \(m\ge1\),
\[
XF^{-m}u+M
=F^{-m}Xu+M+
\text{a finite sum of terms of exterior weight }<\operatorname{wt}(X).\tag{8}
\]
This accounts for all reorderings and all resulting denominators, without any bound on the denominator being needed.

Combining (6) and (8),
\[
\Phi(XY^pv)=c_pF^{-(p+1)}Xu+M+
\text{terms of exterior weight }<\operatorname{wt}(X).\tag{9}
\]
Here exterior weight means the weight of \(X\) in the indicated vector-space bases; the exponent \(p\) is not counted.

Suppose \(\lambda_L\ne0\), so every \(c_p\ne0\). Surjectivity follows by induction on exterior weight, simultaneously for all denominators. At weight zero, \(X\) contains only commuting \(f\)-factors, and (9) has no correction terms. At a larger weight, \(c_{m-1}^{-1}XY^{m-1}v\) maps to the desired basis vector \(F^{-m}Xu+M\) plus finitely many smaller-weight vectors, all already in the image.

For injectivity, take a nonzero finite linear combination of source basis vectors (4) and choose the largest exterior weight occurring in it. By (9), its terms of that weight map to distinct target basis vectors, with nonzero coefficients multiplied by the nonzero numbers \(c_p\). All correction terms have smaller weight. The image therefore cannot vanish. This proves the isomorphism without any simplicity assumption.

If \(\lambda_L=0\), well-definedness still holds, but (5) gives \(\Phi(Yv)=0\). The source PBW basis shows \(Yv\ne0\), proving failure of injectivity of this particular map.

**Changing \(n\) while fixing \(M_{-1,1}\).** Let \(M=M_{-1,1}(\chi)\).

If \(n\ge2\), then \(F=f_n\) kills \(u\). Given \(A\in U\), choose \(N\) such that \((\operatorname{ad}F)^N(A)=0\). Expanding \(F^NAu\) by the earlier binomial identity, every term with \(k<N\) contains a positive power of \(F\) acting on \(u\), while the \(k=N\) term is zero. Thus \(F^NAu=0\). Every vector of \(M\) is therefore killed by a power of \(F\), and the fraction criterion gives \(D_FM=0\). Its cokernel is zero as well.

If \(n\le0\), then \(F=f_n\) is an exterior generator of the original module. Place it first in a PBW ordering, followed by \(e_i\) for \(i\le-1\), \(h_i\) for \(i<0\), and all remaining \(f_j\) with \(j\le1\). Exactly the argument for (2)–(3) proves injectivity of \(F\) and the corresponding negative-power quotient basis. In that quotient,
\[
h_1(F^{-1}u+M)
=\lambda_1(F^{-1}u+M)+2F^{-2}f_{n+1}u+M.\tag{10}
\]
Because \(n+1\le1\) and \(n+1\ne n\), the second summand is a nonzero PBW basis vector distinct from \(F^{-1}u+M\). Equation (10) cannot equal any scalar multiple of \(F^{-1}u+M\). Thus this vector is not an \(h_1\)-eigenvector. Every standard inducing vector is an \(h_1\)-eigenvector, so a homomorphism sending it to this vector is impossible. The case \(n=1\) is the boundary theorem with \(a=-1,b=1\).

**Iteration.** After \(r\) boundary moves the parameters are \((a+r,b-r)\), whose sum is still \(a+b\). Hence \(L\ge1\) and the nonzero value \(\lambda_L\) are unchanged. The next boundary generator is \(f_{b-r}\), and the proved theorem applies again, increasing only the \(h_0\)-value by two. Induction proves the finite iterated formula, even when the boundary index passes through zero or becomes negative.

### Scope

The specialization M_{-1,n} changes the inducing module and requires λ_n≠0. It must be distinguished from localizing the fixed M_{-1,1}, whose Cartan values above index 1 vanish. For n≤0 on the fixed module, the proof excludes the specified cyclic map; it does not classify T_{f_n}M or exclude isomorphisms using another cyclic vector. Likewise, when λ_L=0, only the stated map is proved noninjective. The iteration concerns successive localization quotients of changing modules; no infinite iteration or simultaneous-localization identification is asserted.


## Derivation

Fact ID: `b388fabb701946d3`. Accepted attempt: 2.

### Statement

Work over \(\mathbb C\). Let \(\mathfrak g\) be the affine \(\mathfrak{sl}_2\) Lie algebra without degree derivation, with basis \(e_r,h_r,f_r\) for \(r\in\mathbb Z\), and \(K\), subject to
\[
[e_r,f_s]=h_{r+s}+r\delta_{r+s,0}K,\qquad [h_r,h_s]=2r\delta_{r+s,0}K,
\]
\[
[h_r,e_s]=2e_{r+s},\qquad [h_r,f_s]=-2f_{r+s},\qquad [e_r,e_s]=[f_r,f_s]=0,
\]
with \(K\) central; here \(\delta_{i,j}\) is the Kronecker delta. Let
\[
\widetilde{\mathfrak g}=\mathfrak g\rtimes\mathbb C d,\qquad [d,x_r]=r x_r\quad(x=e,h,f),\qquad [d,K]=0.
\]
Write \(U=U(\mathfrak g)\), \(\widetilde U=U(\widetilde{\mathfrak g})\), and define induction of a left \(\mathfrak g\)-module \(N\) by
\[
I(N)=\widetilde U\otimes_U N.
\]
Fix \(n\in\mathbb Z\) and \(F=f_n\). For \(R=U\) or \(\widetilde U\), the powers of \(F\) admit Ore localization \(R_F\). For a left \(R\)-module \(N\), put \(D_FN=R_F\otimes_RN\). If \(F\) acts injectively on \(N\), identify \(N\) with its image in \(D_FN\) and put \(T_FN=D_FN/N\).

For every \(F\)-injective \(\mathfrak g\)-module \(M\), there are natural \(\widetilde{\mathfrak g}\)-module isomorphisms
\[
\alpha_M:D_FI(M)\xrightarrow{\sim}I(D_FM),\qquad
\overline\alpha_M:T_FI(M)\xrightarrow{\sim}I(T_FM).
\]
Under the PBW realization \(I(N)=\mathbb C[d]\otimes N\), the action is
\[
d(P(d)\otimes u)=dP(d)\otimes u,\qquad
x_r(P(d)\otimes u)=P(d-r)\otimes x_ru,\qquad
K(P(d)\otimes u)=P(d)\otimes Ku.
\]
For \(m\ge0\), the localization isomorphism is
\[
\alpha_M\bigl(F^{-m}(P(d)\otimes u)\bigr)
=P(d+mn)\otimes F^{-m}u.
\]
Consequently, any given \(\mathfrak g\)-isomorphism \(\Phi:A\to T_FM\) induces a \(\widetilde{\mathfrak g}\)-isomorphism
\[
\mathcal L=\overline\alpha_M^{-1}\circ I(\Phi):I(A)\xrightarrow{\sim}T_FI(M).
\]
If \(\Phi(a)=F^{-m}u+M\), its formula is
\[
\mathcal L(P(d)\otimes a)=F^{-m}(P(d-mn)\otimes u)+I(M).
\]
A module is called smooth here if each vector is annihilated by \(e_r,h_r,f_r\) for all sufficiently large integers \(r\); for a \(\widetilde{\mathfrak g}\)-module this means smoothness of its restriction to \(\mathfrak g\). If \(M\) is smooth, all the induced modules, localizations, and localization quotients above are smooth, as are \(A\) and \(I(A)\) when \(\Phi\) is given. The assertion concerning \(\Phi\) is conditional and establishes no particular boundary isomorphism. No simplicity conclusion is asserted.

### Proof

All tensor products without a subscript are over \(\mathbb C\). A homogeneous mode \(x_r\) denotes one of \(e_r,h_r,f_r\), of degree \(r\), while \(K\) has degree zero.

1. Choose a PBW ordering with \(d\) before an ordered basis of \(\mathfrak g\). PBW gives the right \(U\)-module decomposition
\[
\widetilde U=\bigoplus_{k\ge0}d^kU.
\]
Indeed, the ordered PBW monomials consist precisely of a power of \(d\) followed by a PBW monomial in \(U\). Therefore multiplication gives a right \(U\)-module isomorphism \(\mathbb C[d]\otimes U\cong\widetilde U\), and hence
\[
I(N)\cong\mathbb C[d]\otimes N.
\]
The relation \([d,x_r]=rx_r\) gives \(x_rd=(d-r)x_r\); induction on polynomial degree yields
\[
x_rP(d)=P(d-r)x_r.
\]
This proves the action stated above, including the formulas for \(d\) and \(K\).

For completeness, these formulas directly satisfy the Lie relations. For two modes,
\[
(x_ry_s-y_sx_r)(P(d)\otimes u)
=P(d-r-s)\otimes[x_r,y_s]u.
\]
Each noncentral term in the bracket has degree \(r+s\), so the expression agrees with its prescribed action. A central term occurs only when \(r+s=0\), when the polynomial shift vanishes. Thus all affine brackets, with their stated central coefficients, hold. Moreover,
\[
[d,x_r](P(d)\otimes u)
=\bigl(dP(d-r)-(d-r)P(d-r)\bigr)\otimes x_ru
=rx_r(P(d)\otimes u).
\]
The centrality of \(K\), including \([d,K]=0\), follows directly. In contrast, the untwisted tensor action \(x_r(P\otimes u)=P\otimes x_ru\), with \(d\) acting by multiplication, gives \([d,x_r]=0\). It fails whenever a mode of nonzero degree acts nontrivially.

The same PBW decomposition proves that \(I\) is exact: as a vector-space functor, it is \(N\mapsto\bigoplus_{k\ge0}d^k\otimes N\), with every induced map acting coefficient by coefficient. Thus it preserves kernels, images, and surjections.

2. Set \(\delta=\operatorname{ad}F\). The defining brackets give
\[
\begin{aligned}
\delta(f_r)&=0,&\delta(K)&=0,\\
\delta(h_r)&=2f_{r+n},&\delta(d)&=-nF,\\
\delta(e_r)&=-h_{r+n}-r\delta_{r+n,0}K,&
\delta^2(e_r)&=-2f_{r+2n}.
\end{aligned}
\]
Consequently \(\delta^2(h_r)=\delta^2(d)=0\) and \(\delta^3(e_r)=0\). Since \(\delta\) is a derivation, its iterated Leibniz formula on a finite product is a multinomial sum. For a sufficiently large iteration, every summand differentiates some factor beyond its nilpotence bound. Every element of an enveloping algebra is a finite linear combination of finite products, so \(\delta\) is locally nilpotent on both \(U\) and \(\widetilde U\).

We give the localization details explicitly. Let \(R\) denote either enveloping algebra. PBW identifies its associated graded algebra with the symmetric algebra of the corresponding Lie algebra. This is a polynomial algebra, possibly on infinitely many variables, and is a domain: any particular pair of polynomials lies in a polynomial algebra on finitely many variables. Leading symbols therefore show that \(R\) is a domain. In particular, all powers of \(F\) are regular on both sides.

If \(\delta^{t+1}(a)=0\), the identities
\[
F^Na=\sum_{j=0}^{t}\binom Nj\delta^j(a)F^{N-j},\qquad
aF^N=\sum_{j=0}^{t}(-1)^j\binom NjF^{N-j}\delta^j(a)
\tag{1}
\]
hold for \(N\ge t\). They follow by induction from \(Fa=aF+\delta(a)\) and \(aF=Fa-\delta(a)\), using Pascal's identity. For \(N\ge m+t\), the first expression is right-divisible by \(F^m\), and the second is left-divisible by \(F^m\). These are the left and right Ore common-multiple conditions; regularity supplies the denominator cancellation condition.

One can construct the module localization directly. For any left \(R\)-module \(N\), form symbols \([m,u]\), where \(m\ge0\) and \(u\in N\), with equality defined by
\[
[m,u]=[\ell,v]\quad\Longleftrightarrow\quad
F^{k-m}u=F^{k-\ell}v\text{ for some }k\ge m,\ell.
\tag{2}
\]
This is an equivalence relation: any two witnessing indices can be increased to a common index. Addition is performed at a common index, and scalar multiplication acts on the numerator. Thus the symbols form a vector space, with \([m,u]=[m+1,Fu]\).

For \(a\in R\), choose \(L\ge0\) and \(b\in R\) satisfying
\[
F^La=bF^m,
\tag{3}
\]
which is possible by (1), and set \(a[m,u]=[L,bu]\). This action is independent of the choice: if another pair is \((L',b')\), increase both indices to \(Q\ge L,L'\). Then
\[
(F^{Q-L}b-F^{Q-L'}b')F^m=0,
\]
so regularity implies equality of the coefficients. It also respects the transition \([m,u]=[m+1,Fu]\). At a common sufficiently large \(L\), write \(F^La=b_mF^m=b_{m+1}F^{m+1}\); cancellation gives \(b_m=b_{m+1}F\). These facts imply compatibility with every equality in (2).

The action is multiplicative. If \(F^La=bF^m\) and \(F^Qc=c'F^L\), then \(F^Qca=c'bF^m\), giving
\[
c(a[m,u])=[Q,c'bu]=(ca)[m,u].
\]
Additivity follows by increasing indices until the coefficients for the summands have a common denominator, and the identity acts as the identity. The map \(N\to D_FN\), \(u\mapsto[0,u]\), is \(R\)-linear. On this symbol space, \(F\) acts invertibly, with inverse \([m,u]\mapsto[m+1,u]\).

If \(j:N\to V\) is an \(R\)-module map and \(F\) is invertible on \(V\), its unique extension is
\[
[m,u]\longmapsto F^{-m}j(u).
\]
Equation (2) proves well-definedness. Equation (3), after multiplying by the inverses of the powers of \(F\) in \(V\), proves \(R\)-linearity. Uniqueness follows because \([m,u]=F^{-m}[0,u]\).

To identify this construction with algebra localization without invoking a localization theorem, let \(R_F\) be the algebra obtained by adjoining a two-sided inverse of \(F\) to \(R\). Modules on which \(F\) acts invertibly are exactly the modules extending to \(R_F\), and such extension is unique. The symbol space and \(R_F\otimes_RN\) have the same universal property just proved, so the natural maps between them are inverse. Taking \(N=R\) also shows that \(R\to R_F\) is injective and every element of \(R_F\) has the form \(F^{-m}a\). Together with the Ore identities above, this realizes the asserted Ore localization. We henceforth write \(F^{-m}u\) for \([m,u]\).

The construction establishes the following facts. Every finite sum has a common denominator, because for \(q\ge m\),
\[
F^{-m}u=F^{-q}F^{q-m}u.
\tag{4}
\]
The kernel of \(N\to D_FN\) consists exactly of vectors killed by a power of \(F\), by (2). In particular, this map is injective for \(F\)-injective \(N\).

Localization is exact as well. For an exact sequence \(0\to N'\xrightarrow{i}N\xrightarrow{p}N''\to0\), a fraction \(F^{-m}u'\) mapping to zero has \(i(F^ku')=0\) for some \(k\), so it was zero already. Every fraction over \(N''\) lifts by lifting its numerator. Finally, if \(F^{-m}u\) maps to zero, then \(F^kp(u)=0\) for some \(k\), so \(F^ku=i(u')\) for some \(u'\in N'\), and
\[
F^{-m}u=F^{-m-k}i(u')
\]
lies in the localized image. This proves exactness at every term.

The useful localization action formula is, for \(m\ge1\),
\[
aF^{-m}u=\sum_{j\ge0}\binom{m+j-1}{j}F^{-m-j}\delta^j(a)u.
\tag{5}
\]
Each sum is finite. For \(m=1\), repeatedly substitute the identity
\[
aF^{-1}=F^{-1}a+F^{-1}\delta(a)F^{-1};
\]
the remaining term eventually vanishes by local nilpotence. Induction on \(m\) gives (5): grouping terms of total differentiation order \(j\) uses
\[
\sum_{i=0}^j\binom{m+i-1}{i}=\binom{m+j}{j},
\]
which follows by telescoping Pascal's identity. For \(m=0\), the action has just the term \(a u\).

In particular, the explicit mode actions on \(D_FM\) are
\[
\begin{aligned}
f_r(F^{-m}u)&=F^{-m}f_ru,\\
h_r(F^{-m}u)&=F^{-m}h_ru+2mF^{-m-1}f_{r+n}u,\\
e_r(F^{-m}u)&=F^{-m}e_ru-mF^{-m-1}(h_{r+n}+r\delta_{r+n,0}K)u\\
&\qquad-m(m+1)F^{-m-2}f_{r+2n}u,\\
K(F^{-m}u)&=F^{-m}Ku.
\end{aligned}
\tag{6}
\]
These formulas also apply when \(m=0\), with the correction terms zero. For a \(\widetilde{\mathfrak g}\)-module, (5) additionally gives
\[
d(F^{-m}w)=F^{-m}dw-mnF^{-m}w.
\tag{7}
\]
The construction above already proves these actions obey the algebra relations.

On \(I(M)\), the action of \(F\) is
\[
F(P(d)\otimes u)=P(d-n)\otimes Fu.
\tag{8}
\]
Translation of polynomials is invertible. The map \(\mathrm{id}\otimes F\) is injective when \(F\) is injective on \(M\), since its kernel is computed coefficient by coefficient. Their composite (8) is therefore injective, justifying the quotient \(T_FI(M)\).

3. The \(\mathfrak g\)-module \(D_FM\) has invertible \(F\), so (8) on \(I(D_FM)\) has inverse
\[
F^{-1}(P(d)\otimes z)=P(d+n)\otimes F^{-1}z.
\]
Iterating gives the positive shift
\[
F^{-m}(P(d)\otimes z)=P(d+mn)\otimes F^{-m}z.
\tag{9}
\]
Define the linear map on fractions by
\[
\alpha_M\bigl(F^{-m}(P(d)\otimes u)\bigr)
=P(d+mn)\otimes F^{-m}u.
\tag{10}
\]
For a fixed denominator this prescription is linear on the numerator. The transition to denominator \(F^{m+1}\) changes that numerator to \(P(d-n)\otimes Fu\); its image is
\[
P(d-n+(m+1)n)\otimes F^{-m-1}Fu
=P(d+mn)\otimes F^{-m}u.
\]
Thus (10) respects the fraction relations. Common denominators then prove well-definedness for arbitrary sums.

We check every type of generator. Whenever nonzero, \(\delta^j(x_r)\) is homogeneous of degree \(r+jn\); if it contains a central term, that term has the same degree zero. For \(m\ge1\), (5) and (10) give
\[
\begin{aligned}
\alpha_M\bigl(x_rF^{-m}(P(d)\otimes u)\bigr)
&=\sum_{j\ge0}\binom{m+j-1}{j}
P(d-(r+jn)+(m+j)n)\otimes F^{-m-j}\delta^j(x_r)u\\
&=P(d+mn-r)\otimes x_r(F^{-m}u)\\
&=x_r\alpha_M\bigl(F^{-m}(P(d)\otimes u)\bigr).
\end{aligned}
\]
For \(m=0\), the same equality follows directly from the induced action, with only the term \(j=0\). Centrality of \(K\) gives its intertwining immediately. For \(d\), (7) yields
\[
\begin{aligned}
\alpha_M\bigl(dF^{-m}(P(d)\otimes u)\bigr)
&=\alpha_M\bigl(F^{-m}((d-mn)P(d)\otimes u)\bigr)\\
&=dP(d+mn)\otimes F^{-m}u\\
&=d\alpha_M\bigl(F^{-m}(P(d)\otimes u)\bigr).
\end{aligned}
\]
Thus \(\alpha_M\) is a \(\widetilde{\mathfrak g}\)-module map, including the degree derivation.

It is surjective because the elementary tensors spanning its target have preimages
\[
\beta_M(P(d)\otimes F^{-m}u)
=F^{-m}(P(d-mn)\otimes u).
\tag{11}
\]
For injectivity, write any element of the source as \(F^{-m}w\), with \(w\in I(M)\). If its image is zero, applying \(F^m\) shows that the image of \(w\) in \(I(D_FM)\) is zero. The map \(M\to D_FM\) is injective, and PBW exactness makes \(I(M)\to I(D_FM)\) injective. Hence \(w=0\). This proves injectivity and also proves that (11) is a well-defined inverse.

At denominator zero, \(\alpha_M\) is the induced inclusion \(I(M)\to I(D_FM)\). Applying the exact functor \(I\) to
\[
0\longrightarrow M\longrightarrow D_FM\longrightarrow T_FM\longrightarrow0
\]
therefore identifies the corresponding quotients and gives
\[
\overline\alpha_M:T_FI(M)\xrightarrow{\sim}I(T_FM).
\]
Its inverse is
\[
\overline\beta_M\bigl(P(d)\otimes(F^{-m}u+M)\bigr)
=F^{-m}(P(d-mn)\otimes u)+I(M).
\tag{12}
\]
This descent uses PBW exactness, so it is independent both of the chosen fraction and of the representative modulo \(M\).

For a \(\mathfrak g\)-module map \(f:M\to N\), localization acts by \(F^{-m}u\mapsto F^{-m}f(u)\), and induction acts by \(P\otimes u\mapsto P\otimes f(u)\). Substitution in (10) and (12) shows that the respective squares commute. Thus the isomorphisms are natural on \(F\)-injective modules.

4. Now assume, explicitly, that \(\Phi:A\to T_FM\) is a given \(\mathfrak g\)-isomorphism. The composite
\[
\mathcal L=\overline\beta_M\circ I(\Phi)
\]
is a \(\widetilde{\mathfrak g}\)-isomorphism. If \(\Phi(a)=F^{-m}u+M\), formula (12) gives
\[
\mathcal L(P(d)\otimes a)
=F^{-m}(P(d-mn)\otimes u)+I(M).
\tag{13}
\]
Every value of \(\Phi\) admits a single-fraction representative by common denominators, and the established quotient map guarantees independence of that choice.

If \(A=Uv\) is cyclic, \(I(A)\) is generated by \(1\otimes v\), since its vectors are sums of \(d^k b(1\otimes v)\), with \(b\in U\). If
\[
\Phi(v)=F^{-\ell}u_v+M,
\]
then
\[
\mathcal L(1\otimes v)=F^{-\ell}(1\otimes u_v)+I(M).
\tag{14}
\]
In particular, a given formula \(\Phi(v)=F^{-1}u+M\) lifts to \(F^{-1}(1\otimes u)+I(M)\).

Whenever \(\Phi(q_m)=F^{-m}u+M\), (10) gives the exact preimage
\[
\boxed{\mathcal L^{-1}\bigl(F^{-m}(P(d)\otimes u)+I(M)\bigr)
=P(d+mn)\otimes q_m.}
\tag{15}
\]
Indeed, substituting the polynomial \(P(d+mn)\) into (13) cancels its shift.

The map \(I(\Phi):I(A)\to I(T_FM)\) is literally \(\mathrm{id}_{\mathbb C[d]}\otimes\Phi\). After swapping vector-space factors, it is \(\Phi\otimes\mathrm{id}_{\mathbb C[d]}\). To use that shorthand for the map into \(T_FI(M)\), one must incorporate the shifted identification (12). The coefficient-preserving prescription
\[
P(d)\otimes(F^{-m}u+M)\longmapsto F^{-m}(P(d)\otimes u)+I(M)
\]
is generally incorrect. Besides its incompatibility with fraction transitions, (7) exhibits the missing \(-mn\) term in its interaction with \(d\). When \(n=0\), all polynomial shifts vanish.

5. Suppose \(M\) is smooth in the sense defined in the statement. For any vector \(\sum_iP_i(d)\otimes u_i\in I(M)\), choose a common cutoff annihilating all of the finitely many \(u_i\). The induced action formula then shows that every mode above this cutoff annihilates the tensor. Thus induction preserves smoothness.

For a fraction \(F^{-m}u\in D_FM\), let \(N\) be a smoothness cutoff for \(u\). Choose an integer \(B\) large enough that, for every \(r\ge B\),
\[
r\ge N,\qquad r+n\ge N,\qquad r+2n\ge N,\qquad r+n\ne0.
\]
Such a \(B\) exists for every fixed integer \(n\), including negative \(n\). All terms in (6) vanish for \(r\ge B\); the last condition removes the possible central correction. Hence \(D_FM\) is smooth. Common denominators cover every vector in it. A quotient of a smooth module is smooth, because a cutoff for a representative also annihilates its class. Consequently \(T_FM\), \(I(D_FM)\), and \(I(T_FM)\) are smooth. The isomorphisms already proved give smoothness of \(D_FI(M)\) and \(T_FI(M)\). If \(\Phi\) is given, it also transfers smoothness to \(A\), and then to \(I(A)\).

There is an obstruction to simply adding \(d\) to a one-dimensional inducing character. Let an inducing subalgebra contain \(h_L\), where \(L>0\), and let its character satisfy \(\chi(h_L)=\lambda_L\ne0\). If it extended to a one-dimensional character on a Lie subalgebra also containing \(d\), scalar operators would commute, whereas
\[
0=[\chi(d),\chi(h_L)]=\chi([d,h_L])=L\lambda_L\ne0.
\]
This contradiction is independent of the chosen scalar \(\chi(d)\). Polynomial induction instead supplies a non-scalar derivation action obeying the required brackets.

6. Finally, an induced isomorphism does not imply simplicity. Induction need not preserve simplicity: take the one-dimensional trivial \(\mathfrak g\)-module \(N=\mathbb C\), on which every mode and \(K\) act by zero. It is simple, since its only vector subspaces are zero and itself. Its induced module is \(I(N)=\mathbb C[d]\), with all modes and \(K\) acting by zero and \(d\) acting by multiplication. The subspace \(d\mathbb C[d]\) is nonzero, proper, and stable under every generator. Therefore \(I(N)\) is not simple.

Here \(F\) acts by zero on \(N\), so this example concerns induction generally and is outside the \(F\)-injective hypothesis. It proves the stated failure of simplicity preservation without making any claim about simplicity under additional hypotheses.

### Scope

This is a self-contained candidate for independent verification, with no claim of acceptance. The affine presentation, central normalization, integer parameter n, degree extension, and induction functor are explicit in the statement. The boundary isomorphism Φ is assumed, not proved. Smoothness means eventual annihilation by all sufficiently high loop modes. The simplicity example concerns induction generally; it does not settle simplicity for F-injective or particular boundary modules.
