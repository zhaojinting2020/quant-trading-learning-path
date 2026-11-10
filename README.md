<div align="center">

# 量化交易之路

### 从金融直觉到数学推导，从读书笔记到 Python 策略复现。

一份持续更新的量化学习记录，串起 **金融基础 · 数学方法 · 回测实践 · 风险管理**。

[学习路线](#1-量化-road-map) · [量化入门](#2-量化交易入门) · [书籍与实战](#6-量化实战) · [代码入口](#直接看代码)

</div>

---

量化学习中，我们需要搞清楚的，往往不只是“这个策略怎么写”，还有：**收益从哪里来？模型依赖什么假设？回测结果为什么不可信？**

这个仓库记录我沿着这些问题读书、推导和写代码的过程。内容包括中文读书笔记、公式推导、Jupyter Notebook，以及回测和交易接口的 Python 实现。既有书中方法的复现，也有围绕 Kelly 仓位、配对交易、前视偏差和国内期货接口的延伸实践。

## 1. 量化 road map

沿用我在飞书「量化交易之路」主页中的学习顺序：

| 阶段 | 要解决的问题 | 学习内容 |
| --- | --- | --- |
| 量化交易入门 | 量化系统由什么组成，应该从哪里学起？ | 交易框架、学习方向与基本认识 |
| 金融基础 | 策略交易的是什么，收益与风险从哪里来？ | 金融术语、财务报表、投资学、计量经济学、衍生品 |
| 数学基础 | 怎样描述不确定性，并理解模型的推导？ | 概率统计、线性代数、微积分 |
| 编程基础 | 怎样把金融问题变成可处理的数据与程序？ | Python 数据分析、金融数据、时间序列 |
| 量化实战 | 怎样实现、回测和审视一个交易策略？ | 书籍复现、信号构建、风险与仓位管理、交易接口 |
| 机器学习与深度学习 | 怎样把预测模型接到策略研究中？ | 回归、分类、神经网络与市场方向预测 |

路线图参考：[Quant Wiki 中文量化百科](https://quant-wiki.com/)。本仓库侧重记录我自己的读书、推导与代码实践。

## 2. 量化交易入门

先用[清华大学《量化交易》笔记](content/10-金融基础/学习笔记%20-%20清华大学《量化交易》-%20QWvgdchv.md)建立整体认识，再用[《打开量化投资的黑箱》](content/10-金融基础/学习笔记%20-《打开量化投资的黑箱》-NJEadk2a.md)理解阿尔法模型、风险模型与交易执行的关系。

也可以从一个具体问题切入：

| 你想了解什么 | 推荐入口 |
| --- | --- |
| 先建立量化交易的整体认识 | [清华大学《量化交易》笔记](content/10-金融基础/学习笔记%20-%20清华大学《量化交易》-%20QWvgdchv.md) · [《打开量化投资的黑箱》笔记](content/10-金融基础/学习笔记%20-《打开量化投资的黑箱》-NJEadk2a.md) |
| 补齐概率、统计和矩阵基础 | [概率论与统计学](content/20-数学基础/学习笔记%20-%20量化必备概率论与统计学基础-OYLZdqQE.md) · [线性代数](content/20-数学基础/学习笔记%20-%20量化必备线代基础-NQrUdhPP.md) |
| 跟着一本书动手做回测 | [《Python 算法交易》笔记](content/30-编程与实战/学习笔记%20-《Python-算法交易》-Cpv4djLF.md) · [配套代码目录](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/) |
| 研究策略与回测中的具体问题 | [《量化交易：如何建立自己的算法交易事业》笔记](content/30-编程与实战/学习笔记%20-《量化交易如何建立自己的算法交易事业》-FUANdgmF.md) · [配套代码目录](attachments/量化交易-如何建立自己的算法交易事业学习笔记-FUANdgmFMo3KBlx7W4acZiHyntc/code/) |
| 理解仓位为什么会改变长期结果 | [Kelly 准则推导与应用](content/30-编程与实战/学习笔记%20-%20Kelly准则及在仓位管理中的应用.md) · [Kelly 财富路径实验](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Kelly_Paths.ipynb) |

## 3. 金融基础

- [量化必备：100 个金融术语](content/10-金融基础/学习笔记%20-%20量化必备100个金融术语-VfHgd6ls.md)
- [《打开量化投资的黑箱》](content/10-金融基础/学习笔记%20-《打开量化投资的黑箱》-NJEadk2a.md)
- [《财务报表分析》](content/10-金融基础/学习笔记%20-《财务报表分析》-KLqJdUEm.md)

后续书目：[《投资学》](content/10-金融基础/学习笔记%20-《投资学》-KR6md9jE.md)、[《Econometrics: Methods and Applications》](content/10-金融基础/学习笔记%20-《Econometrics-Methods-and-Applications》-TA54devd.md)、[《期权期货和其他衍生品》](content/10-金融基础/学习笔记%20-《期权期货和其他衍生品》-SHrgd6vX.md)。这些本地笔记目前只有入口，正文待补充。

[浏览金融基础目录 →](content/10-金融基础/)

## 4. 数学基础

- [概率论与统计学基础](content/20-数学基础/学习笔记%20-%20量化必备概率论与统计学基础-OYLZdqQE.md)
- [线性代数基础](content/20-数学基础/学习笔记%20-%20量化必备线代基础-NQrUdhPP.md)
- [量化面试概率进阶题](content/20-数学基础/学习笔记%20-%20量化面试概率进阶题（基础笔记超纲题）.md)
- [线性代数代码练习](attachments/量化必备-线代基础-NQrUdhPPaoTB2fx52XucbNQ2n1L/code/)：样本协方差矩阵、单期市场模型与证券复制、非奇异矩阵与数值计算。

[微积分笔记](content/20-数学基础/学习笔记%20-%20量化必备微积分-MSBVdTCH.md)目前以提纲为主；概率统计已有较完整正文，线性代数持续补充。

[浏览数学基础目录 →](content/20-数学基础/)

## 5. 编程基础

这一阶段沿着飞书主页中的三个方向展开：**Python 数据分析基础 → Python 金融数据分析 → Python 时间序列处理**。

| 方向 | 当前入口 | 仓库中的进度 |
| --- | --- | --- |
| Python 数据分析基础 | NumPy / pandas 的使用见《Python 算法交易》数据与向量化示例 | 已有代码，独立基础教程待整理 |
| Python 金融数据分析 | [Python 金融数据分析](content/30-编程与实战/学习笔记%20-%20Python-金融数据分析.md) · [Python for Finance](content/30-编程与实战/学习笔记%20-%20Python-for-Finance-UPNPd8N7.md) | 目前为视频入口与书籍提纲 |
| Python 时间序列处理 | [《时间序列分析》](content/20-数学基础/学习笔记%20-《时间序列分析》-ZADvdBUL.md) | 已建笔记入口，正文待补充 |

## 6. 量化实战

| 书籍 / 专题 | 主要内容 | 当前材料 |
| --- | --- | --- |
| [《Python 算法交易》](content/30-编程与实战/学习笔记%20-《Python-算法交易》-Cpv4djLF.md) | 金融数据、向量化与事件驱动回测、机器学习、资金管理、交易接口 | 读书笔记，32 个主目录 Notebook，12 个 Python 模块 |
| [《量化交易：如何建立自己的算法交易事业》](content/30-编程与实战/学习笔记%20-《量化交易如何建立自己的算法交易事业》-FUANdgmF.md) | 配对交易、因子模型、市场状态、交易成本、回撤与风险 | 读书笔记，20 个 Notebook（含子目录） |
| [Kelly 准则与仓位管理](content/30-编程与实战/学习笔记%20-%20Kelly准则及在仓位管理中的应用.md) | 对数增长率、最优仓位、财富路径与杠杆 | 专题推导与代码实验 |
| [《因子投资：方法与实践》](content/30-编程与实战/学习笔记%20-%20《因子投资-方法与实践》.md) | 因子投资基础、因子溢价、定价框架 | 文字笔记与配图 |
| [《量化工程师实战录》](content/30-编程与实战/学习笔记%20-%20量化工程师实战录-D8Y7ds8u.md) | 阿尔法模型、风险模型与交易执行 | 学习提纲与阶段笔记 |

收录数量表示现有材料，不代表全书已经完成或所有示例都已验证。部分其他书目目前仅有提纲，后续随学习补充。

[浏览编程与实战目录 →](content/30-编程与实战/)

## 7. 机器学习与深度学习基础

从传统模型开始，再尝试神经网络，并把预测结果放回金融时间序列与策略评估中考察。

- [线性回归与市场走势预测](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Using%20Linear%20Regression%20for%20Market%20Movement%20Prediction.ipynb)
- [使用机器学习预测市场走势](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Using_Machine_Learning_for_Market_Movement_Prediction.ipynb)
- [深度学习与市场方向预测](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Using_deep_learning_market_prediction.ipynb)：将原书的 Keras 示例改写为 PyTorch Lightning 实践。

独立的机器学习基础笔记后续补充，目前先通过上述书籍实验进入。

## 8. 附录

### 阅读与资料

- [财经与经济学人阅读记录](content/50-杂志期刊/)
- [量化面试概率进阶题](content/20-数学基础/学习笔记%20-%20量化面试概率进阶题（基础笔记超纲题）.md)

## 直接看代码

代码目前与对应书籍的附件放在一起。下面提供直接入口，方便跳过附件目录查找。

| 问题 / 实验 | Notebook / 源码 |
| --- | --- |
| 均线策略如何向量化回测？ | [均线策略](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Strategies%20Based%20on%20Simple%20Moving%20Averages.ipynb) · [SMAVectorBacktester.py](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/SMAVectorBacktester.py) |
| 向量化回测与事件驱动回测有什么区别？ | [两种回测方式对照](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/vector_vs_eventBased_backtest.ipynb) |
| 怎么把 Kelly 仓位公式变成实验？ | [Kelly 资金管理](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Capital_Management_Kelly.ipynb) · [财富路径模拟](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Kelly_Paths.ipynb) |
| 回测里怎么识别前视偏差？ | [AkShare 前视偏差示例](attachments/量化交易-如何建立自己的算法交易事业学习笔记-FUANdgmFMo3KBlx7W4acZiHyntc/code/Lookahead-bias-akshare-demo.ipynb) |
| 配对交易如何落到数据和回测上？ | [GLD–GDX 配对交易](attachments/量化交易-如何建立自己的算法交易事业学习笔记-FUANdgmFMo3KBlx7W4acZiHyntc/code/GLD%E2%80%93GDX%20配对交易.ipynb) |
| 如何识别市场状态？ | [Market regime detection](attachments/量化交易-如何建立自己的算法交易事业学习笔记-FUANdgmFMo3KBlx7W4acZiHyntc/code/Market%20regime%20detection.ipynb) |
| 怎么把书中的交易接口思路迁移到国内期货？ | [天勤 TqSdk 期货算法交易](attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/天勤TqSdk期货算法交易.ipynb) |
| 股票收益率的协方差矩阵怎么构造？ | [五只股票的样本协方差矩阵](attachments/量化必备-线代基础-NQrUdhPPaoTB2fx52XucbNQ2n1L/code/1.1.2-五只股票的样本协方差矩阵.ipynb) |

## 本地阅读与运行

**只看笔记：** 在 GitHub 点击以上链接即可。部分正文使用 Obsidian 双链和嵌入语法，在 Obsidian 中阅读能获得更完整的跳转与配图体验。

**在 Obsidian 阅读：** 安装 [Git LFS](https://git-lfs.com/)，克隆仓库后，把仓库根目录作为 vault 打开。

```bash
git lfs install
git clone https://github.com/zhaojinting2020/quant-trading-learning-path.git
cd quant-trading-learning-path
git lfs pull
```

**运行代码：** 建议为所选书籍创建独立 Python 环境，从对应 `code/` 目录启动 Jupyter。各实验涉及的依赖、数据与接口不同；部分示例需要自行获取行情数据或配置账户。运行前先阅读 Notebook 的说明和代码，交易接口示例需核对账户与运行模式。

目录中的 `requirements.txt` 如有提供，可作为对应材料的环境参考；它不代表全仓库已经在统一环境中验证。

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
