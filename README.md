<div align="center">

# 量化交易之路

### 读懂量化经典，推清数学原理，亲手复现交易策略。

一份持续更新的量化学习记录，串起 **金融基础 · 数学方法 · 回测实践 · 风险管理**。

[学习路线](#1-量化-road-map) · [量化入门](#2-量化交易入门) · [书籍与实战](#6-量化实战)

</div>

---

从看懂收益率，到推导 Kelly 最优仓位；从计算协方差，到复现配对交易；从写出一段回测代码，到理解数据、执行与风控怎样配合——这是一条把量化基础知识融汇贯通的学习路线。

我把沿途的经典书籍、中文笔记、数学推导和 Python 实验整理在这里。你可以按路线系统学习，也可以选一本正在读的书，对照笔记推导公式、打开 Notebook 修改参数，亲手检验自己的理解。

**让读过的书，变成能够反复验证的知识。**

## 1. 量化 road map

[Quant Wiki 中文量化百科](https://quant-wiki.com/)提供量化领域的整体知识地图，适合查阅概念、了解研究方向和补充学习资源。
<img width="1280" height="981" alt="image" src="https://github.com/user-attachments/assets/3b164930-175a-4161-8856-454226ce50d0" />


下面按 “入门、金融、数学、编程、实战、机器学习” 组织我的学习材料。

**已完成、连载中**沿用个人学习进度；本仓库尚未收录的正文或资源会另行标注。

## 2. 量化交易入门

- [清华大学《量化交易》学习笔记](content/10-金融基础/学习笔记%20-%20清华大学《量化交易》-%20QWvgdchv.md) · 已完成

入门与职业方向参考：

- [2026 Quant Roadmap — Projects, Skills and Tips to Become a Developer, Trader or Researcher](https://www.youtube.com/watch?v=xPxmMFPbfFU)
- [How to Become a Quantitative Researcher](https://www.youtube.com/watch?v=6GrSRtqjN3Q)
- [How to Become a Quantitative Developer](https://www.youtube.com/watch?v=P6znLRvqkiA)

## 3. 金融基础

### 3.1 金融基本概念

[量化必备：100 个金融术语](content/10-金融基础/学习笔记%20-%20量化必备100个金融术语-VfHgd6ls.md) · 已完成

### 3.2 如何读懂财务报表

[《财务报表分析》学习笔记](content/10-金融基础/学习笔记%20-《财务报表分析》-KLqJdUEm.md) · 已完成

### 3.3 投资学

[《投资学》学习笔记](content/10-金融基础/学习笔记%20-《投资学》-KR6md9jE.md) · 本仓库正文待补充

### 3.4 计量经济学

[《Econometrics: Methods and Applications》学习笔记](content/10-金融基础/学习笔记%20-《Econometrics-Methods-and-Applications》-TA54devd.md) · 本仓库正文待补充

### 3.5 期权期货和其他衍生品

[《期权期货和其他衍生品》学习笔记](content/10-金融基础/学习笔记%20-《期权期货和其他衍生品》-SHrgd6vX.md) · 本仓库正文待补充

## 4. 数学基础

### 4.1 概率与统计基础

[量化必备：概率论与统计学基础](content/20-数学基础/学习笔记%20-%20量化必备概率论与统计学基础-OYLZdqQE.md) · 已完成


### 4.2 线性代数基础

[量化必备：线性代数基础](content/20-数学基础/学习笔记%20-%20量化必备线代基础-NQrUdhPP.md) · 连载中


### 4.3 微积分基础

[量化必备：微积分](content/20-数学基础/学习笔记%20-%20量化必备微积分-MSBVdTCH.md) · 当前为学习提纲

## 5. 编程基础

### 5.1 Python 数据分析基础

- [尚硅谷 Python 数据分析课程](https://www.atguigu.com/video/339/) · 网课学习
- [Pandas Cheat Sheet](attachments/Pandas_Cheat_Sheet.pdf) · 速查表

### 5.2 Python 金融数据分析

[Python for Finance 学习笔记](content/30-编程与实战/学习笔记%20-%20Python-for-Finance-UPNPd8N7.md) · 本仓库正文待补充

### 5.3 Python 时间序列处理

[《时间序列分析》学习笔记](content/20-数学基础/学习笔记%20-《时间序列分析》-ZADvdBUL.md) · 本仓库正文待补充

## 6. 量化实战

**主线：[《量化工程师实战录》](content/30-编程与实战/学习笔记%20-%20量化工程师实战录-D8Y7ds8u.md) · 连载中**

围绕这条主线，把读书与工程实践接起来：理解系统如何组成，研究因子与策略，建立回测，再逐步处理中国市场的交易约束和日常运维。

### 6.1 解构量化黑箱

[《打开量化投资的黑箱》学习笔记](content/10-金融基础/学习笔记%20-《打开量化投资的黑箱》-NJEadk2a.md) · 已完成

从阿尔法模型、风险模型和交易执行入手，建立对量化系统的整体认识。

### 6.2 因子挖掘

[《因子投资：方法与实践》学习笔记](content/30-编程与实战/学习笔记%20-%20《因子投资-方法与实践》.md) · 连载中

围绕因子投资框架，逐步学习因子处理、有效性检验、组合构建与风险管理。

### 6.3 工程化落地

[《Python 算法交易》学习笔记](content/30-编程与实战/学习笔记%20-《Python-算法交易》-Cpv4djLF.md) · 已完成

[配套代码目录](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/)收录 32 个主目录 Notebook 和 12 个 Python 模块，涉及数据处理、向量化与事件驱动回测、预测模型和交易接口。

### 6.4 防范陷阱与优化

《交易策略评估与优化》学习笔记 · 连载中，独立笔记尚未收录到本仓库

目前可先阅读[工程师实战录中的对应章节](content/30-编程与实战/学习笔记%20-%20量化工程师实战录-D8Y7ds8u.md#防范陷阱与优化)，并结合[前视偏差代码示例](attachments/量化交易-如何建立自己的算法交易事业学习笔记-FUANdgmFMo3KBlx7W4acZiHyntc/code/Lookahead-bias-akshare-demo.ipynb)理解回测中容易忽略的问题。

### 6.5 个人事业搭建

[《量化交易：如何建立自己的算法交易事业》学习笔记](content/30-编程与实战/学习笔记%20-《量化交易如何建立自己的算法交易事业》-FUANdgmF.md) · 已完成

[配套代码目录](attachments/量化交易-如何建立自己的算法交易事业学习笔记-FUANdgmFMo3KBlx7W4acZiHyntc/code/)收录 20 个 Notebook（含子目录），涵盖配对交易、因子模型、市场状态、交易成本与回撤分析。

延伸专题：[Kelly 准则与仓位管理](content/30-编程与实战/学习笔记%20-%20Kelly准则及在仓位管理中的应用.md) · [Kelly 财富路径实验](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Kelly_Paths.ipynb)

### 6.6 中国市场本土化

[章节提纲](content/30-编程与实战/学习笔记%20-%20量化工程师实战录-D8Y7ds8u.md#中国市场本土化) · 持续展开

- 标的池动态清洗
- A 股交易摩擦还原
- 执行仿真与时间序列陷阱
- 策略模板实战代码

### 6.7 量化工程的脏活

[章节提纲](content/30-编程与实战/学习笔记%20-%20量化工程师实战录-D8Y7ds8u.md#量化工程的脏活) · 持续展开

- 多源数据中台搭建
- 自动化运维与预警中心
- 开源框架实战选型
- 实盘接口与风控最后防线

代码收录数量表示现有材料，运行条件见下文[本地阅读与运行](#本地阅读与运行)。

## 7. 机器学习与深度学习基础

机器学习与深度学习的入门根基，前人之述备矣，好书好文不胜枚举，我便不在此班门弄斧了，仅附上几部自己心仪的经典链接，愿与诸君共同研读。

- [机器学习西瓜书（自己看）](https://github.com/lyhhhhhhhhhhh/awesome-machine-learning-1/blob/master/Machine-Learning%20%E3%80%8A%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0%EF%BC%88%E8%A5%BF%E7%93%9C%E4%B9%A6%EF%BC%89%E3%80%8B_%E5%91%A8%E5%BF%97%E5%8D%8E.pdf)

- [机器学习西瓜书 - 学习笔记（自己看）](https://github.com/Vay-keen/Machine-learning-learning-notes)

- [Pytorch 深度学习实战（自己看）](https://github.com/GISWLH/DataScience-master/blob/main/books/%E3%80%8Apytorch%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%E5%AE%9E%E6%88%98%E3%80%8B%E4%B8%AD%E6%96%87PDF+%E4%BC%8A%E8%8E%B1.pdf)

- [深度学习书集（自己看）](https://github.com/GISWLH/DataScience-master/tree/main/books)

## 8. 附录

### 更多财经书籍与杂志

- [财经与经济学人阅读记录](content/50-杂志期刊/)


## 本地阅读与运行

部分正文使用 Obsidian 双链和嵌入语法，在 Obsidian 中阅读能获得更完整的跳转与配图体验。

安装 [Git LFS](https://git-lfs.com/)，克隆仓库后，把仓库根目录作为 vault 打开。

```bash
git lfs install
git clone https://github.com/zhaojinting2020/quant-trading-learning-path.git
cd quant-trading-learning-path
git lfs pull
```

## 仓库结构

```text
content/
├── 10-金融基础/          # 术语、量化框架、财务分析
├── 20-数学基础/          # 概率统计、线代、面试概率题
├── 30-编程与实战/        # 书籍笔记、策略实践、Kelly 专题
├── 40-面试/              # 预留专题目录
└── 50-杂志期刊/          # 财经与经济学人阅读记录
attachments/
├── <书籍或专题>/code/    # Jupyter Notebook 与 Python 源码
└── ...                   # 配图及参考附件，由 Git LFS 管理
```

## 持续更新

这里记录的是一条仍在推进的学习路线。后续会继续补充读书笔记、代码实验，以及复现过程中遇到的问题和修正。

如果你也在读同一本书，欢迎通过 Issue 交流推导、指出代码问题，或分享不同的实现。希望这些记录能帮你更快找到下一步值得动手的问题。

学习笔记与策略示例仅用于研究，不构成投资建议。书籍、引用材料和第三方代码的权利归原权利人所有。
