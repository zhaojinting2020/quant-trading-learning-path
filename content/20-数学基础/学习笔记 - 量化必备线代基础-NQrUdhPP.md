---
title: 量化必备：线代基础
url: 'https://www.feishu.cn/docx/NQrUdhPPaoTB2fx52XucbNQ2n1L'
quality: raw
attachments:
  - file: attachments/量化必备-线代基础-NQrUdhPPaoTB2fx52XucbNQ2n1L/量化必备-线代基础.pdf
    title: 量化必备-线代基础.pdf
feishu_formatted_at: '2026-06-28T09:37:59+00:00'
wikilinks_unbulleted_at: '2026-06-28T05:48:29+00:00'
custom-width: 85
---
## 前言：学习重点

本笔记围绕金融工程中的数值线性代数方法展开。交易、资产配置和风险管理中的许多问题，最终都需要求解线性方程组，或从时间序列数据估计协方差矩阵与相关矩阵。本笔记把数学方法与金融应用结合起来，并提供算法伪代码，帮助读者从理解公式走向实现计算。

**需要掌握的数学工具**

- 线性方程组与矩阵分解：LU 分解、Cholesky 分解，以及针对三对角对称正定矩阵的高效求解方法。
- 随机变量与矩阵的联系：线性变换性质、多元正态随机变量，为理解协方差结构和相关性建模打基础。
- 插值与拟合：高效三次样条插值、普通最小二乘法（OLS）与线性回归。
- 矩阵性质与判别方法：Gershgorin 定理、对角占优，以及判断矩阵正定性的 Sylvester 判据。

**数学方法对应哪些金融问题**

- Arrow-Debreu 单期市场模型，以及单期指数期权市场中的套利问题。
- 从时间序列数据估计协方差矩阵和相关矩阵。
- 用普通最小二乘法计算隐含波动率。
- 构建最小方差投资组合和最大收益投资组合。
- 计算风险价值（VaR）与投资组合 VaR。


## 1 向量与矩阵

### 1.1 列向量与行向量；矩阵的列形式与行形式

#### 1.1.1 基本概念

本笔记统一约定：向量符号默认表示列向量，行向量用相应列向量的转置表示。

$n$ 维向量 $v\in\mathbb R^n$ 记为 $v=(v_1,\ldots,v_n)^T$，具有 $n$ 个实数分量 $v_i\in\mathbb R$，$i=1,\ldots,n$。

若向量写成

$$
v=\begin{pmatrix}v_1\\v_2\\\vdots\\v_n\end{pmatrix},\tag{1.1}
$$

则称为长度为 $n$ 的列向量，也称 $n\times1$ 向量。若写成

$$
v^T=\begin{pmatrix}v_1&v_2&\cdots&v_n\end{pmatrix},\tag{1.2}
$$

则称为长度为 $n$ 的行向量，也称 $1\times n$ 向量。上标 $T$ 强调行向量是列向量的转置。

> 本书讨论的向量和矩阵，其元素均为实数。尽管复数会自然出现，例如实矩阵的特征值可能是复数，本书的叙述和记号仍以实向量和实矩阵为基础。

---

设 $A=(a_{ij})\in\mathbb R^{m\times n}$，即 $A$ 是一个 $m$ 行、$n$ 列的实矩阵，$a_{ij}$ 为其第 $i$ 行、第 $j$ 列的元素。

矩阵 $A$ 的列形式为

$$
A=\begin{bmatrix}a_1&\cdots&a_n\end{bmatrix},\tag{1.3}
$$

其中 $a_k$ 是 $A$ 的第 $k$ 列，即 $a_k=(a_{1k},\ldots,a_{mk})^T$。

矩阵 $A$ 的行形式为

$$
A=\begin{bmatrix}r_1^T\\r_2^T\\\vdots\\r_m^T\end{bmatrix}.\tag{1.4}
$$

令 $r_j=(a_{j1},\ldots,a_{jn})^T\in\mathbb R^n$，则 $A$ 的第 $j$ 行为 $r_j^T=(a_{j1},\ldots,a_{jn})$。

---

**行向量乘列向量**
设 $v=(v_1,\ldots,v_n)^T$ 为列向量，$w^T=(w_1,\ldots,w_n)$ 为行向量，则

$$
w^Tv=\sum_{i=1}^n w_iv_i.\tag{1.5}
$$

这一公式也是第 5 章中两向量的欧几里得内积公式。

**列向量乘行向量**
设 $v=(v_1,\ldots,v_m)^T$ 为长度 $m$ 的列向量，$w^T=(w_1,\ldots,w_n)$ 为长度 $n$ 的行向量，则 $vw^T$ 是 $m\times n$ 矩阵，元素为

$$
(vw^T)_{jk}=v_jw_k,\qquad j=1,\ldots,m,\ k=1,\ldots,n.\tag{1.6}
$$

**矩阵乘列向量** 
设 $A=\begin{bmatrix}a_1&\cdots&a_n\end{bmatrix}$ 是 $m\times n$ 矩阵，$v=(v_1,\ldots,v_n)^T$ 是列向量，则

$$
Av=\sum_{k=1}^n v_ka_k.\tag{1.7}
$$

换言之，结果 $Av$ 是一个列向量，它是矩阵 $A$ ==各列==的线性组合，系数就是 $v$ 的相应分量。向量 $w_1,\ldots,w_n$ 的线性组合指 $c_1w_1+\cdots+c_nw_n$，其中 $c_i\in\mathbb R$，也见定义 1.5。

若 $A=\begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}$，则 $m\times1$ 列向量 $Av$ 的第 $j$ 个分量为

$$
(Av)_j=r_j^Tv,\qquad 1\le j\le m.\tag{1.8}
$$

这里 $r_j^T$ 为 $1\times n$ 行向量，$v$ 为 $n\times1$ 列向量，因此可按式 (1.5) 相乘。

**行向量乘矩阵**
设 $A=\begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}$ 为 $m\times n$ 矩阵，$w^T=(w_1,\ldots,w_m)$ 为行向量，则

$$
w^TA=\sum_{j=1}^m w_jr_j^T.\tag{1.9}
$$

即行向量从左边乘矩阵，结果是矩阵==各行==的线性组合，系数是 $w^T$ 的相应分量。若 $A=\begin{bmatrix}a_1&\cdots&a_n\end{bmatrix}$，则结果的第 $k$ 个分量为

$$
(w^TA)_k=w^Ta_k,\qquad 1\le k\le n.\tag{1.10}
$$

**矩阵乘矩阵** 
设 $A$ 为 $m\times n$ 矩阵，$B$ 为 $n\times p$ 矩阵。

(i) 若 $B=\begin{bmatrix}b_1&\cdots&b_p\end{bmatrix}$，则

$$
AB=\begin{bmatrix}Ab_1&\cdots&Ab_p\end{bmatrix}.\tag{1.11}
$$

结果是 $m\times p$ 矩阵，其各列分别为 $A$ 乘以 $B$ 的相应列。

(ii) 若 $A=\begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}$，则

$$
AB=\begin{bmatrix}r_1^TB\\r_2^TB\\\vdots\\r_m^TB\end{bmatrix}.\tag{1.12}
$$

结果的各行分别为 $A$ 的相应行乘以 $B$。

(iii) 同时使用 $A$ 的行形式和 $B$ 的列形式，得到

$$
(AB)_{jk}=r_j^Tb_k,\qquad j=1,\ldots,m,\ k=1,\ldots,p.\tag{1.13}
$$

其中 $r_j^T$ 是 $1\times n$ 行向量，$b_k$ 是 $n\times1$ 列向量，因此乘法成立。

**三个矩阵相乘** 
设 $A=\begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}$ 为 $m\times n$ 矩阵，$B$ 为 $n\times p$ 矩阵，$C=\begin{bmatrix}c_1&\cdots&c_l\end{bmatrix}$ 为 $p\times l$ 矩阵，则

$$
(ABC)_{jk}=r_j^TBc_k,\qquad j=1,\ldots,m,\ k=1,\ldots,l.\tag{1.14}
$$

矩阵乘法满足结合律：$ABC=(AB)C=A(BC)$。

> 应主要把矩阵看成列向量或行向量的集合，而不只是单个元素的集合。对数值计算而言，这种观点便于高效实现；用列形式或行形式进行证明，通常也比逐元素证明更紧凑、更能揭示结构。本书多数证明都采用这种基于向量的方法。

---

**定义 1.1（向量转置）。** $n\times1$ 列向量 $v=(v_1,\ldots,v_n)^T$ 的转置为 $1\times n$ 行向量 $v^T=(v_1,\ldots,v_n)$；反过来，行向量 $v^T$ 的转置为列向量 $v$，即 $(v^T)^T=v$。注意：

$$
(cv)^T=cv^T,\qquad v\in\mathbb R^n,\ c\in\mathbb R.\tag{1.15}
$$

**定义 1.2（矩阵转置）。** $m\times n$ 矩阵 $A$ 的转置 $A^T$ 是 $n\times m$ 矩阵，其元素满足：

$$
(A^T)_{kj}=a_{jk},\qquad k=1,\ldots,n,\ j=1,\ldots,m.\tag{1.16}
$$

转置把列形式变为行形式，把行形式变为列形式：

$$
A=\begin{bmatrix}a_1&\cdots&a_n\end{bmatrix}
\Longleftrightarrow A^T=\begin{bmatrix}a_1^T\\\vdots\\a_n^T\end{bmatrix};\tag{1.17}
$$

$$
A=\begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}
\Longleftrightarrow A^T=\begin{bmatrix}r_1&\cdots&r_m\end{bmatrix}.\tag{1.18}
$$

由定义可得

$$
(A^T)^T=A,\tag{1.19}
$$

而对于同型矩阵 $A,B$，

$$
(A+B)^T=A^T+B^T.\tag{1.20}
$$

**引理 1.1。** 设 $A$ 是 $m\times n$ 矩阵，$v$ 是长度为 $n$ 的列向量，则

$$
(Av)^T=v^TA^T.\tag{1.21}
$$

**证明：见原书。**


**引理 1.2。** 设 $A$ 为 $m\times n$ 矩阵，$B$ 为 $n\times p$ 矩阵，则

$$
(AB)^T=B^TA^T.\tag{1.24}
$$

**证明：见原书。**

> 转置的结论可推广为 $(A_1\cdots A_p)^T=A_p^T\cdots A_1^T$，可用归纳法证明，见本章习题。

---

**定义 1.3（方阵）。** 行数和列数相同的矩阵称为方阵。$n\times n$ 方阵也称为 $n$ 阶方阵。

**定义 1.4（对称矩阵）。** ==方阵==与其转置相等时，称为对称矩阵。也就是说，$n$ 阶方阵 $A$ 对称，当且仅当 $A=A^T$，即

$$
a_{jk}=a_{kj},\qquad 1\le j<k\le n.
$$

两个对称矩阵的乘积不一定对称。例如

$$
A=\begin{pmatrix}1&2\\2&1\end{pmatrix},\qquad
B=\begin{pmatrix}2&1\\1&0\end{pmatrix}
$$

均为对称矩阵，但

$$
AB=\begin{pmatrix}4&1\\5&2\end{pmatrix}
\ne(AB)^T=\begin{pmatrix}4&5\\1&2\end{pmatrix}.
$$

**单位矩阵**记为 $I$，是主对角线元素全为 1、其余元素全为 0 的方阵：

$$
I=\begin{pmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&1\end{pmatrix}.
$$

有时 $n\times n$ 单位矩阵写成 $I_n$，但本书对各种阶数均用 $I$，其第 $k$ 列记为 $e_k$，满足

$$
(e_k)_i=
\begin{cases}
1,&i=k,\\
0,&i\ne k.
\end{cases}\tag{1.25}
$$

单位矩阵的列形式与行形式分别为

$$
I=\begin{bmatrix}e_1&\cdots&e_n\end{bmatrix},\qquad
I=\begin{bmatrix}e_1^T\\\vdots\\e_n^T\end{bmatrix},
$$

因为 $I=I^T$。

**引理 1.3。** (i) 设 $A=\begin{bmatrix}a_1&\cdots&a_n\end{bmatrix}$ 为 $m\times n$ 矩阵，$e_k$ 是 $n\times n$ 单位矩阵的第 $k$ 列，则

$$
Ae_k=a_k,\qquad k=1,\ldots,n,\tag{1.26}
$$

因此 $AI=A$。

(ii) 设 $A=\begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}$ 为 $m\times n$ 矩阵，$e_j$ 为 $m\times m$ 单位矩阵的第 $j$ 列，则

$$
e_j^TA=r_j^T,\qquad j=1,\ldots,m,\tag{1.27}
$$

因此 $IA=A$。

右乘基向量 $e_k$ 就取出矩阵的第 $k$ 列；左乘基向量的转置 $e_j^T$ 就取出第 $j$ 行。

---

#### 1.1.2 应用：从时间序列计算协方差矩阵

协方差的定义与性质，请回顾[[学习笔记 - 量化必备概率论与统计学基础-OYLZdqQE#协方差（Covariance）|量化必备：概率论与统计学基础 · 协方差]]。这里考虑如何从实际观测数据计算它。

假设我们记录了 $n$ 只股票在 $m$ 个交易日的收益率。将这些数据排列成一张表：每行对应一个交易日，每列对应一只股票，第 $i$ 行、第 $j$ 列记录 $X_j(t_i)$。

先选出第 $p$、第 $q$ 两列。这两列是在相同日期记录的一串收益率，因此可以逐日配对，计算它们相对于各自样本均值的偏离量。将每对偏离量相乘、求和，再除以 $m-1$，就得到这两只股票收益率的**样本协方差**。它根据有限的观测数据计算，用来估计总体协方差，因此记作 $\widehat{\operatorname{cov}}(X_p,X_q)$；上方的“帽子”表示这是样本估计值。

对所有股票两两进行这一计算，并把结果放在相应的行和列，就得到一个 $n\times n$ 的**样本协方差矩阵**。对角线是各只股票收益率的样本方差，非对角线是不同股票收益率的样本协方差。每一对变量的 $m$ 个观测经过求和后得到一个数，因此矩阵大小由变量数 $n$ 决定。

**计算公式**

设有 $n$ 个随机变量 $X_1,\ldots,X_n$，在 $m$ 个时点 $t_1,\ldots,t_m$ 观测它们。用 $X_j(t_i)$ 表示第 $j$ 个随机变量在第 $i$ 个时点的观测值，其中 $i=1,\ldots,m$，$j=1,\ldots,n$。$X_j$ 的样本均值记为

$$
\widehat\mu_{X_j}=\frac1m\sum_{i=1}^m X_j(t_i).
$$

计算两个变量的协方差时，用 $p,q$ 表示所选变量的编号，其中 $1\le p,q\le n$。

这些随机变量的样本协方差矩阵 $\widehat\Sigma_X$ 是 $n\times n$ 方阵，元素为

$$
(\widehat\Sigma_X)_{pq}=\widehat{\operatorname{cov}}(X_p,X_q),\qquad1\le p,q\le n,\tag{1.30}
$$

其中样本协方差为

$$
\widehat{\operatorname{cov}}(X_p,X_q)=\frac1{m-1}\sum_{i=1}^m
\bigl(X_p(t_i)-\widehat\mu_{X_p}\bigr)
\bigl(X_q(t_i)-\widehat\mu_{X_q}\bigr).\tag{1.31}
$$

因此

$$
(\widehat\Sigma_X)_{pq}=\frac1{m-1}\sum_{i=1}^m
\bigl(X_p(t_i)-\widehat\mu_{X_p}\bigr)
\bigl(X_q(t_i)-\widehat\mu_{X_q}\bigr).\tag{1.32}
$$

交换乘积中两项的顺序，便得到 $(\widehat\Sigma_X)_{pq}=(\widehat\Sigma_X)_{qp}$，所以样本协方差矩阵是对称矩阵。

用矩阵表达时间序列数据，可以高效计算协方差矩阵。令 $T_X$ 为 $m\times n$ 数据矩阵，满足

$$
(T_X)_{ij}=X_j(t_i),\qquad i=1,\ldots,m,\ j=1,\ldots,n.\tag{1.33}
$$

从每列中减去该随机变量的样本均值，得到 $m\times n$ 矩阵 $\overline T_X$：

$$
(\overline T_X)_{ij}=X_j(t_i)-\widehat\mu_{X_j}.\tag{1.34}
$$

样本协方差矩阵就可以写成

$$
\widehat\Sigma_X=\frac1{m-1}\overline T_X^T\overline T_X.\tag{1.35}
$$

**工程理解：** 
在资产收益率数据中，$T_X$ 的每一行是一条时点观测，每一列对应一项资产，且需要 $m>1$。因此 $\overline T_X^T\overline T_X$ 的维度为 $n\times n$。每列减去由同一批数据估计的样本均值后，该列元素之和为零，相当于损失一个自由度，因此通常使用 $m-1$ 作分母。如果不同时点的观测相互独立、来自同一个分布，且各变量的方差有限，那么上述样本协方差是总体协方差的无偏估计。“无偏”指重复抽样并计算时，估计结果的平均值等于真实的总体协方差。但时间序列在不同时点之间可能存在相关性，此时即使除以 $m-1$，也不一定无偏。

下面用五只股票的数据展示计算过程。

**例：五只股票的收益率数据:**

[[attachments/量化必备-线代基础-NQrUdhPPaoTB2fx52XucbNQ2n1L/code/1.1.2-五只股票的样本协方差矩阵.ipynb|Jupyter Notebook：五只股票的样本协方差矩阵]]。
关于由时间序列数据得到的协方差矩阵，更多性质见第 7.2 节。

### 1.2 矩阵的秩、零空间与值域

#### 1.2.1 基本概念

**定义 1.5（线性无关）。** 设 $w_1,\ldots,w_p$ 是同维向量。当且仅当使其线性组合等于零的系数只能全部为零时，称这些向量线性无关，即

$$
\sum_{i=1}^p c_iw_i=0,\quad c_i\in\mathbb R
\quad\Longrightarrow\quad c_i=0\ (i=1,\ldots,p).
$$

$m\times n$ 矩阵 $A$ 的列秩，是其中线性无关==列向量==的最大数目；行秩则是线性无关==行向量==的最大数目。不论是不是方阵，行秩总与列秩相等；第 10.5 节给出了这一事实的证明。因此下面的定义是一致的。

**定义 1.6（秩）。** 矩阵 $A$ 的秩记为 $\operatorname{rank}(A)$，等于 $A$ 中线性无关==列向量==的最大数目，也可等价地用行向量定义。

**定义 1.7（零空间）。** $m\times n$ 矩阵 $A$ 的零空间为

$$
\ker(A)=\{v\in\mathbb R^n:Av=0\}.
$$

零空间也称矩阵的核。

**定义 1.8（像空间）。** $m\times n$ 矩阵 $A$ 的像空间，由所有通过 $A$ 与向量相乘得到的向量组成：

$$
\operatorname{im}(A)=\{u\in\mathbb R^m:\exists v\in\mathbb R^n,\ u=Av\}.\tag{1.45}
$$

**定义 1.9（生成空间）。** 同维向量 $w_1,\ldots,w_p$ 生成的空间，是这些向量所有线性组合的集合：

$$
\operatorname{span}\{w_1,\ldots,w_p\}
=\left\{\sum_{i=1}^p c_iw_i:c_i\in\mathbb R,\ i=1,\ldots,p\right\}.\tag{1.46}
$$

**引理 1.4。** 设 $A=\begin{bmatrix}a_1&\cdots&a_n\end{bmatrix}$ 为 $m\times n$ 矩阵，则其像空间恰好是各列生成的空间：

$$
\operatorname{im}(A)=\operatorname{span}\{a_1,\ldots,a_n\}.\tag{1.47}
$$

**推导要点。** 由矩阵乘列向量的解释，

$$
Av=\sum_{i=1}^n v_i a_i.
$$

当系数向量 $v$ 遍历 $\mathbb R^n$ 时，$Av$ 恰好遍历各列的所有线性组合，因此像空间就是列向量的生成空间。

**定义 1.10（基）。** 设 $V$ 是 $\mathbb R^n$ 的一个子空间。如果 $v_1,\ldots,v_p\in V$ 线性无关，且它们生成整个 $V$，即 $V=\operatorname{span}\{v_1,\ldots,v_p\}$，则称它们构成 $V$ 的一组基。

**引理 1.5。** $\mathbb R^n$ 中一个向量空间的任意两组基，都包含相同数目的向量。本书后续不做这一结果的证明，可参见 Lax [26]。

**定义 1.11（维数）。** 向量空间 $V$ 的维数记为 $\dim(V)$，等于它的一组基所含向量的数目。

尽管一个向量空间有无穷多组不同的基，引理 1.5 保证了每组基中的向量数目相同，因此维数的定义没有歧义。

#### 1.2.2 应用：单期市场模型

在描述金融证券价格演化的单期市场模型中，可以用线性代数框架分析投资组合的收益。本节举例说明这一框架，它是 Arrow-Debreu 模型的基础；详细内容见第 3 章。

考虑包含 $m$ 种证券的市场。时刻 $t_0$ 的现价分别为 $S_{1t_0},\ldots,S_{mt_0}$，价格向量记为 $S_{t_0}=(S_{1t_0},\ldots,S_{mt_0})^T$，是 $m\times1$ 列向量。

假设在未来时刻 $\tau>t_0$，市场可能出现 $n$ 种状态 $\omega^1,\ldots,\omega^n$。若状态 $\omega^k$ 出现，第 $j$ 种资产的价格记为 $S_{j\tau}^{\omega^k}$。令

$$
S_\tau^{\omega^k}=\begin{pmatrix}S_{1\tau}^{\omega^k}\\S_{2\tau}^{\omega^k}\\\vdots\\S_{m\tau}^{\omega^k}\end{pmatrix},
\qquad
(S_{j\tau})^T=\begin{pmatrix}S_{j\tau}^{\omega^1}&S_{j\tau}^{\omega^2}&\cdots&S_{j\tau}^{\omega^n}\end{pmatrix}.
$$

其中 $S_\tau^{\omega^k}\in\mathbb R^m$ 是状态 $\omega^k$ 下所有资产价格构成的列向量；$S_{j\tau}\in\mathbb R^n$ 是第 $j$ 种资产在所有状态下的价格构成的列向量，其转置 $(S_{j\tau})^T$ 是上式中的 $1\times n$ 行向量。

**支付矩阵** $M_\tau$ 是一个 $m\times n$ 矩阵，记录未来时刻 $\tau$ 各种状态下的各种证券价格。其中，第 $j$ 行表示第 $j$ 种证券在共 $n$ 种状态下的价格；第 $k$ 列表示状态 $\omega^k$ 下共 $m$ 种证券的价格：

$$
M_\tau=\begin{bmatrix}S_\tau^{\omega^1}&\cdots&S_\tau^{\omega^n}\end{bmatrix},\tag{1.52}
$$

$$
M_\tau=\begin{bmatrix}S_{1\tau}^T\\S_{2\tau}^T\\\vdots\\S_{m\tau}^T\end{bmatrix}.\tag{1.53}
$$



**例：七种证券、六种状态的三个月市场。**

[[attachments/量化必备-线代基础-NQrUdhPPaoTB2fx52XucbNQ2n1L/code/1.2.1-单期市场模型与证券复制.ipynb|Jupyter Notebook：单期市场模型与证券复制]]

### 1.3 非奇异矩阵

#### 1.3.1 基本概念
从数值计算角度看，非奇异矩阵 $A$ 是使任意线性方程组 $Ax=b$ 都有唯一解 $x$ 的方阵。金融应用经常需要求解这类方程组，这是数值线性代数的基本问题。正式定义如下。

**定义 1.12。** 方阵 $A$ 非奇异，当且仅当存在一个称为 $A$ 的逆矩阵、记作 $A^{-1}$ 的矩阵，使

$$
AA^{-1}=A^{-1}A=I.\tag{1.73}
$$

**定义 1.13。** 不可逆的方阵称为奇异矩阵。

---

**以下设 $A$ 为非奇异矩阵。** 由式 (1.73) 的 $AA^{-1}=A^{-1}A=I$，可知 $A$ 也是 $A^{-1}$ 的逆矩阵，因此

$$
(A^{-1})^{-1}=A.\tag{1.74}
$$

逆矩阵只要存在，就必然唯一。

**证明：见原书。**

---

**定理 1.1。** 对 $n$ 阶方阵 $A$，下列条件等价，都可作为非奇异的定义：

$$
A\text{ 非奇异}\Longleftrightarrow\ker(A)=\{0\},\tag{1.75}
$$

$$
\Longleftrightarrow\operatorname{im}(A)=\mathbb R^n,\tag{1.76}
$$

$$
\Longleftrightarrow\operatorname{rank}(A)=n.\tag{1.77}
$$

同样，下列条件等价：

$$
A\text{ 奇异}\Longleftrightarrow\ker(A)\ne\{0\},\tag{1.78}
$$

$$
\Longleftrightarrow\exists v\in\mathbb R^n,\ v\ne0,\ Av=0.\tag{1.79}
$$

这一结果的证明可参见 Strang [41]。另外，$A$ 奇异也等价于 $\operatorname{im}(A)\ne\mathbb R^n$，或 $\operatorname{rank}(A)<n$。

还可以用行列式给出一个很有用的等价判别，详细内容见第 10.1.1 节。

**定理 1.2。** 对任意方阵 $A$，

$$
A\text{ 非奇异}\Longleftrightarrow\det(A)\ne0;\tag{1.80}
$$

$$
A\text{ 奇异}\Longleftrightarrow\det(A)=0.\tag{1.81}
$$
方阵非奇异，当且仅当其行列式不为零；方阵奇异，当且仅当其行列式为零。

**引理 1.6。** 设 $A,B$ 是同阶方阵。若 $AB=I$，则二者均非奇异，$B=A^{-1}$，$A=B^{-1}$，所以 $BA=I$。

**证明：见原书。**

**引理 1.7。** 设 $A,B$ 为同阶方阵。

(i) $AB$ 非奇异，当且仅当 $A,B$ 都非奇异。

(ii) 若二者非奇异，则

$$
(AB)^{-1}=B^{-1}A^{-1}.\tag{1.82}
$$

**证明：见原书。**

注意乘积的逆要反转顺序，一般而言 $(AB)^{-1}\ne A^{-1}B^{-1}$。它与转置关系 $(AB)^T=B^TA^T$ 有相同的逆序结构。该结论还可推广为 $(A_1\cdots A_p)^{-1}=A_p^{-1}\cdots A_1^{-1}$，可用归纳法证明，见本章习题。

**引理 1.8。** 若方阵 $A$ 非奇异，则 $A^T$ 也非奇异，且

$$
(A^T)^{-1}=(A^{-1})^T.\tag{1.83}
$$

**证明：见原书。**

**引理 1.9。** 对称非奇异矩阵的逆仍对称，即 $(A^{-1})^T=A^{-1}$。

**证明。** 因 $A^T=A$，由式 (1.83)，$(A^{-1})^T=(A^T)^{-1}=A^{-1}$。

#### 1.3.2 示例：非奇异矩阵与数值计算：
[[attachments/量化必备-线代基础-NQrUdhPPaoTB2fx52XucbNQ2n1L/code/1.3-非奇异矩阵与数值计算.ipynb|Jupyter Notebook：非奇异矩阵与数值计算]]

### 1.4 对角矩阵

#### 1.4.1 基本概念

**定义 1.14。** 方阵的所有非主对角线元素均为零时，称为对角矩阵。即 $n\times n$ 矩阵 $D$ 是对角矩阵，当且仅当

$$
d_{jk}=0,\qquad1\le j,k\le n,\quad j\ne k.\tag{1.84}
$$

记 $d_i=d_{ii}$，则

$$
D=\begin{pmatrix}d_1&0&\cdots&0\\0&d_2&\cdots&0\\\vdots&\vdots&\ddots&\vdots\\0&0&\cdots&d_n\end{pmatrix}.\tag{1.85}
$$

由此可知：(i) 对角矩阵均对称；(ii) 两个同阶对角矩阵的和与积仍为对角矩阵，另见引理 1.11；(iii) 对角矩阵既是上三角矩阵，又是下三角矩阵，反之也成立，见式 (1.103)、(1.104)。

简记为 $D=\operatorname{diag}\bigl(d_1,\ldots,d_n\bigr)$。其列形式和行形式分别为

$$
D=\begin{bmatrix}d_1e_1&\cdots&d_ne_n\end{bmatrix},\tag{1.86}
$$

$$
D=\begin{bmatrix}d_1e_1^T\\\vdots\\d_ne_n^T\end{bmatrix},\tag{1.87}
$$

其中 $e_k$ 为相应单位矩阵的第 $k$ 列。

**引理 1.10。** 设 $A$ 为 $m\times n$ 矩阵，列形式为 $A=\begin{bmatrix}a_1&\cdots&a_n\end{bmatrix}$，行形式为 $A=\begin{bmatrix}r_1^T\\\vdots\\r_m^T\end{bmatrix}$。

(i) 若 $D=\operatorname{diag}\bigl(d_1,\ldots,d_n\bigr)$，则

$$
AD=\begin{bmatrix}d_1a_1&\cdots&d_na_n\end{bmatrix}.\tag{1.88}
$$

(ii) 若 $D=\operatorname{diag}\bigl(d_1,\ldots,d_m\bigr)$，则

$$
DA=\begin{bmatrix}d_1r_1^T\\d_2r_2^T\\\vdots\\d_mr_m^T\end{bmatrix}.\tag{1.89}
$$

(iii) 若 $D_1=\operatorname{diag}\bigl(d_1^{(1)},\ldots,d_m^{(1)}\bigr)$，$D_2=\operatorname{diag}\bigl(d_1^{(2)},\ldots,d_n^{(2)}\bigr)$，则

$$
(D_1AD_2)_{jk}=d_j^{(1)}d_k^{(2)}a_{jk},\qquad j=1,\ldots,m,\ k=1,\ldots,n.\tag{1.90}
$$

**推导要点。** 右乘对角矩阵缩放各列，左乘对角矩阵缩放各行。从元素看，分别有

$$
(AD)_{ij}=a_{ij}d_j,\qquad (DA)_{ij}=d_i a_{ij},
$$

其中右乘时 $D$ 为 $n\times n$，左乘时 $D$ 为 $m\times m$。两侧都乘对角矩阵时，元素 $a_{ij}$ 同时乘以第 $i$ 行和第 $j$ 列的缩放因子，即式 (1.90)。

**引理 1.11。** 两个同阶对角矩阵的积仍为对角矩阵，而且对角矩阵的乘法满足交换律。具体地，若 $D_1=\operatorname{diag}\bigl(d_1^{(1)},\ldots,d_n^{(1)}\bigr)$、$D_2=\operatorname{diag}\bigl(d_1^{(2)},\ldots,d_n^{(2)}\bigr)$，则

$$
D_1D_2=\operatorname{diag}\bigl(d_1^{(1)}d_1^{(2)},\ldots,d_n^{(1)}d_n^{(2)}\bigr)=D_2D_1.\tag{1.93}
$$

**证明：见原书。**

**引理 1.12。** (i) 对角矩阵非奇异，当且仅当主对角线上所有元素均非零。即 $D=\operatorname{diag}\bigl(d_1,\ldots,d_n\bigr)$ 非奇异，当且仅当每个 $d_k\ne0$。

(ii) 对非奇异对角矩阵，

$$
D^{-1}=\operatorname{diag}\bigl(1/d_1,\ldots,1/d_n\bigr).\tag{1.94}
$$

**判别依据。** 因 $\det(D)=\prod_{k=1}^n d_k$，对角矩阵非奇异当且仅当每个 $d_k\ne0$。逆矩阵的完整验证见原书。

#### 1.4.2 协方差矩阵与相关矩阵之间的转换

设 $X_1,\ldots,X_n$ 均具有有限且严格为正的方差。协方差矩阵 $\Sigma_X$ 与相关矩阵 $\Omega_X$ 均为 $n\times n$ 矩阵，元素分别为

$$
(\Sigma_X)_{jk}=\operatorname{cov}(X_j,X_k),\qquad
(\Omega_X)_{jk}=\operatorname{corr}(X_j,X_k).
$$

回顾协方差与相关系数的关系：

$$
\operatorname{cov}(X_j,X_k)=\sigma_j\sigma_k\operatorname{corr}(X_j,X_k),
$$

其中 $\sigma_j,\sigma_k$ 为对应随机变量的标准差。令标准差对角矩阵为 $D_{\sigma_X}=\operatorname{diag}\bigl(\sigma_1,\ldots,\sigma_n\bigr)$，由式 (1.90)，

$$
\Sigma_X=D_{\sigma_X}\Omega_XD_{\sigma_X}.\tag{1.95}
$$

因此，已知相关矩阵和各变量的标准差，就能唯一确定协方差矩阵。

因为所有 $\sigma_i\ne0$，$D_{\sigma_X}$ 非奇异，逆矩阵为 $\operatorname{diag}\bigl(1/\sigma_1,\ldots,1/\sigma_n\bigr)$。所以

$$
\Omega_X=D_{\sigma_X}^{-1}\Sigma_XD_{\sigma_X}^{-1}.\tag{1.96}
$$

又因为 $\sigma_i^2=\operatorname{cov}(X_i,X_i)=(\Sigma_X)_{ii}$，

$$
D_{\sigma_X}=\operatorname{diag}\bigl(\sigma_1,\ldots,\sigma_n\bigr)
=\operatorname{diag}\bigl(\sqrt{(\Sigma_X)_{11}},\ldots,\sqrt{(\Sigma_X)_{nn}}\bigr).\tag{1.97}
$$

也就是说，标准差可以直接从协方差矩阵的对角线取得。协方差矩阵因而能唯一确定相关矩阵；但从相关矩阵还原协方差矩阵时，需要额外知道标准差。更多性质见第 7.1 节。

**工程理解。** 上述转换要求每个变量的方差有限且严格大于零，才能计算标准差并取其倒数。在样本中，若某列收益率恒定，其样本标准差为零，与该列相关的相关系数未定义，不能直接除以零；应先识别并处理这类列，再对方差为正的变量计算相关矩阵。

**例：由协方差得到相关矩阵。** 设三个随机变量的协方差矩阵为

$$
\Sigma_X=\begin{pmatrix}1&0.1&-0.6\\0.1&0.25&0.5\\-0.6&0.5&4\end{pmatrix}.
$$

则 $\sigma_1=1$、$\sigma_2=0.5$、$\sigma_3=2$，因此

$$
D_{\sigma_X}=\operatorname{diag}(1,1/2,2),\qquad
D_{\sigma_X}^{-1}=\operatorname{diag}(1,2,1/2),
$$

$$
\Omega_X=D_{\sigma_X}^{-1}\Sigma_XD_{\sigma_X}^{-1}
=\begin{pmatrix}1&0.2&-0.3\\0.2&1&0.5\\-0.3&0.5&1\end{pmatrix}.
$$

**例：由相关矩阵得到协方差。** 设三个随机变量的标准差为 $\sigma_1=2$、$\sigma_2=1$、$\sigma_3=0.9$，相关矩阵为

$$
\Omega_X=\begin{pmatrix}1&0.15&-0.2\\0.15&1&0.1\\-0.2&0.1&1\end{pmatrix}.
$$

此时 $D_{\sigma_X}=\operatorname{diag}(2,1,0.9)$，所以

$$
\Sigma_X=D_{\sigma_X}\Omega_XD_{\sigma_X}
=\begin{pmatrix}4&0.3&-0.36\\0.3&1&0.09\\-0.36&0.09&0.81\end{pmatrix}.
$$

样本协方差矩阵和样本相关矩阵之间也有类似关系。设 $\widehat\sigma_i=\sqrt{\widehat{\operatorname{var}}(X_i)}$ 为样本标准差，则样本相关系数为

$$
\widehat{\operatorname{corr}}(X_j,X_k)
=\frac{\widehat{\operatorname{cov}}(X_j,X_k)}{\widehat\sigma_j\widehat\sigma_k}.
$$

其中样本协方差由式 (1.31) 定义。两个样本矩阵的元素分别为 $(\widehat\Sigma_X)_{jk}=\widehat{\operatorname{cov}}(X_j,X_k)$、$(\widehat\Omega_X)_{jk}=\widehat{\operatorname{corr}}(X_j,X_k)$。令

$$
\widehat D_{\sigma_X}=\operatorname{diag}\bigl(\widehat\sigma_1,\ldots,\widehat\sigma_n\bigr)
=\operatorname{diag}\bigl(\sqrt{(\widehat\Sigma_X)_{11}},\ldots,\sqrt{(\widehat\Sigma_X)_{nn}}\bigr),\tag{1.98}
$$

则

$$
\widehat\Sigma_X=\widehat D_{\sigma_X}\widehat\Omega_X\widehat D_{\sigma_X},\tag{1.99}
$$

$$
\widehat\Omega_X=\widehat D_{\sigma_X}^{-1}\widehat\Sigma_X\widehat D_{\sigma_X}^{-1}.\tag{1.100}
$$

**五只股票的例子（续）。** 采用式 (1.44) 的样本协方差，日收益率的样本标准差对角矩阵为

$$
\widehat D_{\sigma_X}=\operatorname{diag}(0.0426,0.0254,0.0194,0.0072,0.0147).\tag{1.101}
$$

由式 (1.100)，样本相关矩阵为

$$
\widehat\Omega_X=\begin{pmatrix}
1&-0.0087&-0.0736&-0.0615&-0.2002\\
-0.0087&1&0.1075&-0.0506&0.2929\\
-0.0736&0.1075&1&0.5614&0.0591\\
-0.0615&-0.0506&0.5614&1&0.0250\\
-0.2002&0.2929&0.0591&0.0250&1
\end{pmatrix}.\tag{1.102}
$$

> 计算式 (1.101)、(1.102) 时，使用的是样本协方差矩阵未经舍入的数值，而不是式 (1.44) 中保留四位小数的显示值。

### 1.5 下三角矩阵、上三角矩阵与三对角矩阵

**定义 1.15。** 方阵主对角线上方的所有元素均为零时，称为下三角矩阵。即 $L=(\ell_{ij})\in\mathbb R^{n\times n}$ 下三角，当且仅当

$$
\ell_{jk}=0,\qquad1\le j<k\le n.\tag{1.103}
$$

**定义 1.16。** 方阵主对角线下方的所有元素均为零时，称为上三角矩阵。即 $U=(u_{ij})\in\mathbb R^{n\times n}$ 上三角，当且仅当

$$
u_{jk}=0,\qquad1\le k<j\le n.\tag{1.104}
$$

下三角矩阵的转置是上三角矩阵，上三角矩阵的转置是下三角矩阵；这两个陈述的逆命题也成立。

下面给出基于列形式、行形式的等价定义。

**引理 1.13。** $n$ 阶方阵下三角，当且仅当对每个 $k=2,\ldots,n$，第 $k$ 列前 $k-1$ 个元素均为零。即 $L=\begin{bmatrix}l_1&\cdots&l_n\end{bmatrix}$ 下三角，当且仅当

$$
\ell_{ik}=0,\qquad1\le i\le k-1,\quad k=2,\ldots,n.\tag{1.105}
$$

等价地，对于每个 $j=1,\ldots,n-1$，第 $j$ 行最后 $n-j$ 个元素均为零。即 $L=\begin{bmatrix}r_1^T\\\vdots\\r_n^T\end{bmatrix}$ 下三角，当且仅当

$$
\ell_{ji}=0,\qquad j+1\le i\le n,\quad j=1,\ldots,n-1.\tag{1.106}
$$

**引理 1.14。** $n$ 阶方阵上三角，当且仅当对每个 $k=1,\ldots,n-1$，第 $k$ 列最后 $n-k$ 个元素均为零。即 $U=\begin{bmatrix}u_1&\cdots&u_n\end{bmatrix}$ 上三角，当且仅当

$$
u_{ik}=0,\qquad k+1\le i\le n,\quad k=1,\ldots,n-1.\tag{1.107}
$$

等价地，对于每个 $j=2,\ldots,n$，第 $j$ 行前 $j-1$ 个元素均为零。即 $U=\begin{bmatrix}r_1^T\\\vdots\\r_n^T\end{bmatrix}$ 上三角，当且仅当

$$
u_{ji}=0,\qquad1\le i\le j-1,\quad j=2,\ldots,n.\tag{1.108}
$$

两个下三角矩阵相加仍下三角；两个上三角矩阵相加仍上三角；下三角或上三角矩阵乘常数，也分别保留相应结构。因此，同阶下三角矩阵的任意线性组合仍下三角，上三角矩阵同理。

**引理 1.15。** (i) 两个下三角矩阵之积仍下三角。(ii) 两个上三角矩阵之积仍上三角。

**证明：见原书。**

回顾第 10 章的行列式公式：三角矩阵的行列式为主对角线元素之积，

$$
\det(L)=\prod_{i=1}^n \ell_{ii},\tag{1.113}
$$

$$
\det(U)=\prod_{i=1}^n u_{ii}.\tag{1.114}
$$

**引理 1.16。** (i) 下三角矩阵 $L$ 非奇异，当且仅当所有 $\ell_{ii}\ne0$。(ii) 上三角矩阵 $U$ 非奇异，当且仅当所有 $u_{ii}\ne0$。

**证明。** 由式 (1.113)、(1.114) 及“非奇异当且仅当行列式非零”的定理 1.2，结论成立。$\square$

**引理 1.17。** (i) 非奇异上三角矩阵的逆仍上三角。(ii) 非奇异下三角矩阵的逆仍下三角。证明见第 10.7 节引理 10.18。

**定义 1.17（带状矩阵）。** $n\times n$ 矩阵 $A$ 是带宽参数为 $m$ 的带状矩阵，当且仅当

$$
a_{jk}=0,\qquad |j-k|>m.
$$

当 $m=0$ 时，这就是对角矩阵。例如，下面的 $6\times6$ 矩阵带宽参数为 2，符号 $\times$ 表示可能非零的位置：

$$
\begin{pmatrix}
\times&\times&\times&0&0&0\\
\times&\times&\times&\times&0&0\\
\times&\times&\times&\times&\times&0\\
0&\times&\times&\times&\times&\times\\
0&0&\times&\times&\times&\times\\
0&0&0&\times&\times&\times
\end{pmatrix}.
$$

带宽参数为 1 的矩阵称为**三对角矩阵**，在实际应用中经常出现。

**定义 1.18。** $n\times n$ 矩阵 $A$ 是三对角矩阵，当且仅当

$$
a_{jk}=0,\qquad1\le j,k\le n,\quad |j-k|>1.
$$

等价地，可能非零的元素仅限于主对角线上的 $a_{ii}$（$i=1,\ldots,n$）、上邻对角线上的 $a_{i,i+1}$（$i=1,\ldots,n-1$），以及下邻对角线上的 $a_{i,i-1}$（$i=2,\ldots,n$）。例如，$6\times6$ 三对角矩阵中可能非零的位置为

$$
\begin{pmatrix}
\times&\times&0&0&0&0\\
\times&\times&\times&0&0&0\\
0&\times&\times&\times&0&0\\
0&0&\times&\times&\times&0\\
0&0&0&\times&\times&\times\\
0&0&0&0&\times&\times
\end{pmatrix}.
$$

### 1.6 参考文献

有几部线性代数教材与本书强调数值实现和应用的思路相近。Gilbert Strang 的《线性代数导论》（Introduction to Linear Algebra）[41]、《线性代数及其应用》（Linear Algebra and Its Applications）[40]，以及 Peter Lax 的《线性代数及其应用》[26]，都是广受认可的著作。Strang 在 MIT OpenCourseWare 上的课程视频也是很好的学习资源。研究生层次的经典线性代数论述可参见 Horn 与 Johnson [22]。

线性代数的数值分析研究由 Golub 与 Van Loan 的经典专著 [18] 开创，之后由 Demmel [13] 进一步发展。Trefethen 与 Bau 的数值线性代数教材 [43] 富于洞见，介绍了各类数值方法背后的直觉。

本章及全书的一些习题，是要求定量技能的岗位面试中经常出现的问题。更多面试风格的题目可参见 Stefanica、Radoičić 与 Wang [39]。方括号中的编号沿用原书文献编号。

### 1.7 习题

**1.** 设

$$
A=\begin{pmatrix}
1&-1&2&5&4\\
3&-2&1&4&2\\
0&1&2&-1&3\\
-5&4&2&-4&3
\end{pmatrix}.
$$

证明 $A$ 的列秩和行秩均为 3。

**2.** 设 $x,y$ 是长度为 $n$ 的列向量，$I$ 是 $n$ 阶单位矩阵。

(i) 若 $y^Tx\ne-1$，证明

$$
(I+xy^T)^{-1}=I-\frac1{1+y^Tx}xy^T.
$$

换言之，证明

$$
\left(I-\frac1{1+y^Tx}xy^T\right)(I+xy^T)=I.
$$

(ii) 证明 $I+xy^T$ 非奇异，当且仅当 $y^Tx\ne-1$。

**3.** (i) 用数学归纳法证明

$$
\left(\prod_{i=1}^n A_i\right)^T=\prod_{i=1}^n A_{n+1-i}^T,
$$

其中 $A_i$ 是 $m_i\times n_i$ 矩阵，且 $n_i=m_{i+1}$，$i=1,\ldots,n-1$。

(ii) 对任意同阶非奇异方阵 $A_i$，证明

$$
\left(\prod_{i=1}^n A_i\right)^{-1}=\prod_{i=1}^n A_{n+1-i}^{-1}.
$$

**4.** 设 $D=\operatorname{diag}\bigl(d_1,\ldots,d_n\bigr)$ 是主对角线元素两两不同的对角矩阵，即 $j\ne k$ 时 $d_j\ne d_k$。对于 $n$ 阶方阵 $A$，证明 $AD=DA$ 当且仅当 $A$ 是对角矩阵。

**5.** 利用同阶对角矩阵满足 $D_1D_2=D_2D_1$，证明

$$
\prod_{i=1}^n D_i=\prod_{i=1}^n D_{p(i)},
$$

其中 $D_i$ 为同阶对角矩阵，$p:\{1,2,\ldots,n\}\to\{1,2,\ldots,n\}$ 是任意一一映射，即任意排列。

**6.** (i) 设 $A$ 为 $n\times n$ 矩阵，$L$ 为同阶非奇异下三角矩阵。证明：若 $LA$ 下三角，则 $A$ 下三角；若 $AL$ 下三角，则 $A$ 下三角。

(ii) 设 $A$ 为 $n\times n$ 矩阵，$U$ 为同阶非奇异上三角矩阵。证明：若 $UA$ 上三角，则 $A$ 上三角；若 $AU$ 上三角，则 $A$ 上三角。

**7.** 设 $A$ 非奇异，$k$ 为正整数。定义 $A^{-k}$ 为逆矩阵 $A^{-1}$ 的 $k$ 次幂，即 $A^{-k}=(A^{-1})^k$。证明这一定义是一致的，即

$$
A^kA^{-k}=A^{-k}A^k=I.
$$

**8.** (i) 设

$$
M=\begin{pmatrix}0&0&0&0\\3&0&0&0\\1&-1&0&0\\-1&2&1&0\end{pmatrix}.
$$

计算 $M^2$、$M^3$、$M^4$。

(ii) 设

$$
C=I+M=\begin{pmatrix}1&0&0&0\\3&1&0&0\\1&-1&1&0\\-1&2&1&1\end{pmatrix}.
$$

计算 $C^m$，其中 $m\ge2$ 为正整数。

提示：若同阶方阵 $A,B$ 满足 $AB=BA$，则可使用二项式公式

$$
(A+B)^m=\sum_{j=0}^m\binom mj A^jB^{m-j},\tag{1.115}
$$

其中 $m$ 为正整数，$\binom mj=m!/[j!(m-j)!]$，$k!=1\cdot2\cdots k$，且 $A^0=B^0=I$。

**9.** 设 $L$ 为 $n\times n$ 下三角矩阵，主对角线元素全为零，即 $\ell_{ii}=0$，$i=1,\ldots,n$。

(i) 证明 $L^n=0$。

(ii) 对正整数 $m\ge n$，用 $L,L^2,\ldots,L^{n-1}$ 表示 $(I+L)^m$。提示：使用式 (1.115) 的二项式公式。

**10.** 设同阶方阵 $A,B$ 的元素均非负，且每一行的元素和均为 1。证明 $AB$ 也具有相同性质，即其元素均非负、每一行的元素和也均为 1。

注：元素非负且每行元素和为 1 的矩阵，称为概率矩阵。

**11.** 五个随机变量的协方差矩阵为

$$
\Sigma=\begin{pmatrix}
1&-0.525&1.375&-0.075&-0.75\\
-0.525&2.25&0.1875&0.1875&-0.675\\
1.375&0.1875&6.25&0.4375&-1.875\\
-0.075&0.1875&0.4375&0.25&0.3\\
-0.75&-0.675&-1.875&0.3&9
\end{pmatrix}.
$$

求这些随机变量的相关矩阵。

**12.** 五个随机变量的相关矩阵为

$$
\Omega=\begin{pmatrix}
1&-0.25&0.15&-0.05&-0.30\\
-0.25&1&-0.10&-0.25&0.10\\
0.15&-0.10&1&0.20&0.05\\
-0.05&-0.25&0.20&1&0.10\\
-0.30&0.10&0.05&0.10&1
\end{pmatrix}.
$$

(i) 若标准差依次为 0.25、0.5、1、2、4，计算协方差矩阵。

(ii) 若标准差依次为 4、2、1、0.5、0.25，计算协方差矩阵。

**13.** 原书配套网站 `fepress.org/nla-primer` 的文件 `indeces-jul26-aug9-2012.xlsx`，包含 2012 年 7 月 26 日至 8 月 9 日道琼斯、纳斯达克及标普 500 指数的日末数值。

(i) 计算该期间三个指数的每日百分比收益率。

(ii) 计算三个指数每日百分比收益率的协方差矩阵。

(iii) 计算该期间三个指数的每日对数收益率。

(iv) 计算三个指数每日对数收益率的协方差矩阵。

注：资产在时刻 $t$ 的价格记为 $S(t)$，则 $t_1$ 到 $t_2$ 的百分比收益率与对数收益率分别为

$$
\frac{S(t_2)-S(t_1)}{S(t_1)},\qquad
\ln\left(\frac{S(t_2)}{S(t_1)}\right).
$$

**14.** 原书配套网站 `fepress.org/nla-primer` 的文件 `indices-july2011.xlsx`，包含 2011 年 1 月至 7 月九个美国主要指数的日末数值。

(i) 计算各指数每日百分比收益率的样本协方差矩阵及样本相关矩阵；再计算每日对数收益率的两个对应矩阵，并与百分比收益率的结果比较。

(ii) 计算各指数每周百分比收益率的样本协方差矩阵及样本相关矩阵；再计算每周对数收益率的两个对应矩阵，并与百分比收益率的结果比较。

(iii) 计算各指数每月百分比收益率的样本协方差矩阵及样本相关矩阵；再计算每月对数收益率的两个对应矩阵，并与百分比收益率的结果比较。

(iv) 评论每日、每周和每月收益率的样本协方差矩阵及样本相关矩阵之间的差异。

**15.** 某资产当前价格为 50 美元，三个月后可能为 60 或 45 美元。连续复利无风险年利率为 6%。考虑由现金和该资产两种证券组成的单期市场模型，三个月后有对应资产价格 60 和 45 美元的两种状态。

(i) 求该模型的支付矩阵。

(ii) 这个单期市场是否完备？即支付矩阵是否非奇异？

(iii) 如何用现金和标的资产复制该资产的三个月平值看跌期权？

**16.** 某资产当前价格为 40 美元，六个月后可能为 30、35、40、42、45 或 50 美元。考虑一个单期市场模型，其六种状态对应上述六个未来价格，包含四种证券：现金、标的资产、执行价为 40 美元的六个月平值看涨期权、执行价为 40 美元的六个月平值看跌期权。连续复利无风险年利率恒为 6%。

(i) 求该模型的支付矩阵。

(ii) 这个单期市场模型是否完备？

(iii) 这四种证券是否非冗余？

## 2 LU decomposition

### 2.1 The numerical solution of linear systems

### 2.2 Forward substitution

#### 2.2.1 Finding discount factors using forward substitution

### 2.3 Backward substitution

### 2.4 LU decomposition without pivoting

#### 2.4.1 Pseudocode and operation count for LU decomposition

### 2.5 Linear solvers using LU decomposition without pivoting

#### 2.5.1 LU linear solvers for tridiagonal matrices

### 2.6 LU decomposition with row pivoting

### 2.7 Linear solvers using LU decomposition with row pivoting

#### 2.7.1 Solving linear systems corresponding to the same matrix

#### 2.7.2 Finding discount factors using the LU decomposition

### 2.8 Cubic spline interpolation

#### 2.8.1 Cubic spline interpolation for zero rate curves

### 2.9 References

### 2.10 Exercises

## 3 The Arrow-Debreu one period market model

### 3.1 One period market models

### 3.2 Arbitrage-free markets

### 3.3 Complete markets

### 3.4 Risk-neutral pricing in arb-free complete markets

#### 3.4.1 State prices

### 3.5 A one period index options market model

### 3.6 References

### 3.7 Exercises

## 4 Eigenvalues and eigenvectors

### 4.1 Definitions and properties

### 4.2 Diagonal forms

### 4.3 Diagonally dominant matrices

### 4.4 Numerical computation of eigenvalues

### 4.5 Eigenvalues and eigenvectors of tridiagonal symmetric matrices

### 4.6 References

### 4.7 Exercises

## 5 Symmetric matrices and symmetric positive definite matrices

### 5.1 Symmetric matrices

### 5.2 Symmetric positive definite matrices

#### 5.2.1 Sylvester’s Criterion

#### 5.2.2 Positive definiteness criteria for symmetric matrices

### 5.3 The diagonal form of symmetric matrices

### 5.4 References

### 5.5 Exercises

## 6 Cholesky decomposition. Efficient cubic spline interpolation.

### 6.1 Cholesky decomposition

#### 6.1.1 Pseudocode and operation count for Cholesky decomposition

### 6.2 Linear solvers for symmetric positive definite matrices

#### 6.2.1 Solving linear systems corresponding to the same spd matrix

### 6.3 Optimal linear solvers for tridiagonal spd matrices

### 6.4 Efficient implementation of the cubic spline interpolation

#### 6.4.1 Efficient cubic spline interpolation for zero rate curves

### 6.5 References

### 6.6 Exercises

## 7 Covariance matrices. Multivariate normals.

### 7.1 Covariance and correlation matrices

### 7.2 Covariance and correlation matrix estimation from time series data

### 7.3 Linear Transformation Property

### 7.4 Necessary and sufficient conditions for covariance and correlation matrices

### 7.5 Finding normal variables with a given covariance or correlation matrix

#### 7.5.1 Monte Carlo simulation for basket options pricing

### 7.6 Multivariate normal random variables

### 7.7 Multivariate random variables formulation for covariance and correlation matrices

### 7.8 References

### 7.9 Exercises

## 8 Ordinary least squares (OLS). Linear regression.

### 8.1 Ordinary least squares

#### 8.1.1 Least squares for implied volatility computation

### 8.2 Linear regression: ordinary least squares for time series data

### 8.3 Ordinary least squares for random variables

### 8.4 The intuition behind ordinary least squares for time series data

### 8.5 References

### 8.6 Exercises

## 9 Efficient portfolios. Value at Risk.

### 9.1 Efficient portfolios. Markowitz portfolio theory

### 9.2 Blueprints for finding efficient portfolios

### 9.3 Minimum variance portfolios

#### 9.3.1 Minimum variance portfolios and the tangency portfolio

### 9.4 Maximum return portfolios

#### 9.4.1 Maximum return portfolios and the tangency portfolio

### 9.5 Minimum variance portfolio with no cash position

### 9.6 Value at Risk (VaR). Portfolio VaR.

#### 9.6.1 VaR of combined portfolios and subadditivity

### 9.7 References

### 9.8 Exercises

## 10 Mathematical appendix and technical results

### 10.1 Numerical linear algebra tools

#### 10.1.1 Determinants

#### 10.1.2 Permutation matrices

#### 10.1.3 Orthogonality

#### 10.1.4 Quadratic forms

### 10.2 Mathematical tools

#### 10.2.1 Multivariable functions

#### 10.2.2 Lagrange multipliers

#### 10.2.3 The “Big O” notation

### 10.3 European options overview

### 10.4 Eigenvalues of symmetric matrices

### 10.5 Row rank equal to column rank

### 10.6 Technical results for the Cholesky and LU decompositions

### 10.7 More technical results

### 10.8 Exercises

## Bibliography

## Index
