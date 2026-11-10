---
title: 《Python 算法交易》学习笔记
url: https://my.feishu.cn/docx/Cpv4djLFwoWd2CxiXgsc4laSn2f
quality: raw
attachments:
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/document/Yves Hilpisch - Python for Algorithmic Trading.pdf
    title: Yves Hilpisch - Python for Algorithmic Trading.pdf
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/document/The Kelly Criterion in Blackjack Sports Betting, and the Stock Market.pdf
    title: The Kelly Criterion in Blackjack Sports Betting, and the Stock Market.pdf
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/document/Betting_with_the_Kelly_Criterion.pdf
    title: Betting_with_the_Kelly_Criterion.pdf
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Capital_Management_Kelly.ipynb
    title: Capital_Management_Kelly.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Reading Financial Data From Different Sources.ipynb
    title: Reading Financial Data From Different Sources.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Working with Open Data Sources - Quandl.ipynb
    title: Working with Open Data Sources - Quandl.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Working with Open Data Sources - Eikon.ipynb
    title: Working with Open Data Sources - Eikon.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Mock Eikon Data API - Unstructured News Retrieval.ipynb
    title: Mock Eikon Data API - Unstructured News Retrieval.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Storing DataFrame Objects1.ipynb
    title: Storing DataFrame Objects1.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/UsingTsTables.ipynb
    title: UsingTsTables.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/UsingParquet.ipynb
    title: UsingParquet.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Storing_Data_with_SQLite3.ipynb
    title: Storing_Data_with_SQLite3.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Making Use of Vectorization.ipynb
    title: Making Use of Vectorization.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Strategies Based on Simple Moving Averages.ipynb
    title: Strategies Based on Simple Moving Averages.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/SMAVectorBacktester.py
    title: SMAVectorBacktester.py
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Strategies Based on Momentum.ipynb
    title: Strategies Based on Momentum.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/mean_reversion_backtest.ipynb
    title: mean_reversion_backtest.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Using Linear Regression for Market Movement Prediction.ipynb
    title: Using Linear Regression for Market Movement Prediction.ipynb
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/LRVectorBacktester.py
    title: LRVectorBacktester.py
  - file: attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Using Machine Learning for Market Movement Prediction.ipynb
    title: Using Machine Learning for Market Movement Prediction.ipynb
fetch_source: feishu:cli
fetched_at: 2026-08-08T03:38:14+00:00
custom-width: 85
---

原书 PDF：[[attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/document/Yves Hilpisch - Python for Algorithmic Trading.pdf|Yves Hilpisch - Python for Algorithmic Trading]]

Kelly 延伸阅读（第 10 章 Capital Management）：

- 前置：[[学习笔记 - Kelly准则及在仓位管理中的应用]]
- 笔记：[[attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/code/Capital_Management_Kelly.ipynb|Capital Management：Kelly 准则]]
- Thorp：[[attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/document/The Kelly Criterion in Blackjack Sports Betting, and the Stock Market.pdf|The Kelly Criterion in Blackjack, Sports Betting, and the Stock Market]]
- Hung：[[attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/document/Betting_with_the_Kelly_Criterion.pdf|Betting with the Kelly Criterion]]

# Introduction

## Python for Finance

Python 曾因作为解释型语言运行缓慢（尤其是处理金融循环算法时）而受到质疑。但随着 NumPy（通过向量化解决速度问题）和 pandas（提供强大的时间序列处理能力）的出现，Python 已转变为金融数据分析和算法交易的主流平台，其代码简洁性甚至取代了传统的伪代码。

- 从起步到主流： Python 诞生于 1991 年，但直到 2011 年左右才在金融界大规模普及。早期主要障碍是其 CPython 解释器在执行金融算法（如期权定价、风险管理）中常见的嵌套循环时，速度远不及 C 或 C++ 等编译型语言。
- 代码美学： Python 的语法极其接近数学公式和 LaTeX 标记。这使得开发者可以跳过编写“伪代码”的步骤，直接编写可执行的金融逻辑。
- NumPy： 2006 年发布的 NumPy 引入了 `ndarray` 对象。

  - 向量化（Vectorization） 是其核心性能利器：它将循环操作从 Python 层面移交给底层高效的 C 语言处理。
  - 在蒙特卡洛模拟测试中，向量化后的代码比纯 Python 循环快了约 8 倍。
- pandas： 由 Wes McKinney 在 AQR 对冲基金工作时开发，旨在将 R 语言的处理能力引入 Python。

  - 它的 `DataFrame` 类极大简化了金融时间序列（如比特币历史汇率、移动平均线计算）的获取、处理与可视化。
- 生态系统： 除了核心的 NumPy 和 pandas，Python 成功的关键还在于其丰富的扩展库，涵盖了从数据存储（PyTables、SQLite）到机器学习（scikit-learn、TensorFlow）的各个领域。

## Algorithmic Trading

算法交易是指基于数学或技术逻辑的正式程序进行的金融交易。本书的核心重点是利用算法实现Alpha策略（即超越市场基准的超额收益）。研究表明，虽然产生 Alpha 极其困难，但在宏观对冲等领域，系统化（算法）交易的表现往往优于人工决策。

**什么是算法交易？**

- 定义： 算法是为实现特定目标而按顺序执行的一系列操作。算法交易就是将这种逻辑应用于金融工具。
- 进化： 交易已从传统的交易所“公开喊价（Open Outcry）”全面转向电子化和全球联网的计算机自动下单。

**交易的六大动机**

无论是人工还是算法，交易主要出于以下目的：

- Beta 交易： 赚取市场风险溢价（如投资 S&P 500 ETF）。
- Alpha 生成： 赚取独立于市场的超额收益（本书重点）。
- 静态/动态套期保值： 对冲市场风险（如 Delta 中性对冲）。
- 资产负债管理： 确保资金足以覆盖债务（如保险公司）。
- 做市（Market Making）： 提供流动性，赚取买卖价差。

**算法 vs. 人工**

- 主动管理的困境： 统计显示，绝大多数主动型基金经理（约 80% 以上）在 5-10 年的长期维度内无法跑赢 S&P 500 基准。
- 系统化交易的优势： 根据 Harvey 等人（2016）的研究，在宏观策略（Macro）中，系统化算法交易在原始收益和风险调整收益上均优于人工交易。而在股票领域，算法交易在风险调整后的表现（Appraisal Ratio）也更具优势。

**Alpha 的定义**

本书将 Alpha 简化定义为：交易策略收益率 - 基准收益率。如果标普 500 涨了 10%，你的策略涨了 12%，那么 Alpha 就是 +2%。

## Python for Algorithmic Trading

本节总结了 Python 为何成为算法交易（Algorithmic Trading）领域的首选语言，并从数据处理、生态系统和行业趋势等多个维度给出了理由。

**核心技术优势**

- 卓越的数据分析能力： 算法交易的核心是高效管理和处理财务数据。Python 配合 NumPy 和 pandas 等库，在处理时序数据和数值计算方面比大多数编程语言更简单、更高效。
- 现代 API 的完美衔接： 现代交易平台（如 FXCM、Oanda）通常提供 RESTful API 或 Socket 流式接口。Python 天生具备处理这些网络协议的高效性，能够轻松获取历史数据和实时行情。

**丰富的生态系统**

- 专用交易库： 拥有大量针对算法交易开发的工具，例如用于回测的 PyAlgoTrade 和 Zipline，以及用于投资组合风险分析的 Pyfolio。
- 官方支持： 越来越多的金融数据服务商（如 Bloomberg、Refinitiv）和交易平台主动发布开源的 Python 软件包，方便用户对接其服务。
- 专业回测平台： 像 Quantopian（虽已于2020年停止服务，但对行业影响深远）这样的平台，曾利用 Python 构建了吸引数十万用户的标准化回测环境。

**行业影响力与职业前景**

- 机构广泛采用： 无论是买方（对冲基金）还是卖方（投行）都在利用 Python 简化交易部门的开发流程。这导致市场对掌握 Python 的金融人才需求急剧增加。
- 教育与资源： 随着相关书籍、培训课程和学术项目的爆发式增长，Python 在金融领域的学习门槛不断降低，形成了强大的正向循环。

## Focus and Prerequisites

本节简要概述了本书的学习重点（Focus）与先决条件（Prerequisites），明确了它作为一本“实践指南”的定位。

**Python 驱动的交易**

- 重点： 本书并非 Python 入门书，也不是金融理论教科书。它的核心焦点在于如何利用 Python 构建自动化算法交易系统的基础设施。
- 应用导向： 书中会展示如何进行策略回测、处理流式数据等具体代码实现，但不会深入探讨这些交易策略（如动量策略、均值回归）背后的统计验证或复杂细节。

**读者先决条件**

- Python 经验： 读者应具备 Python 编程基础，并熟悉数据分析常用的核心包（如 NumPy 和 pandas）。
- 工具熟练度： 期望读者熟悉交互式分析工具，如 IPython 或 Jupyter Notebook。
- 交易背景： 读者最好对算法交易有一定的了解。

**学习建议与资源支持**

- 补充阅读： 对于 Python 基础薄弱的读者，推荐 Hilpisch (2018)、McKinney (2017) 和 VanderPlas (2016) 等经典教材来夯实金融数据分析的基础。
- 技术跨度： 书中会涉及面向对象编程（OOP）和 scikit-learn（机器学习库）等高级应用，但不会详细解释其底层原理，重点在于应用。

## Trading Strategies

本节总结了书中作为示例的四种核心算法交易策略，它们都属于寻求超额收益（Alpha Seeking）的策略，即旨在产生独立于市场整体方向的正收益。

**基于结构化数据的 Alpha 策略**

- 数据来源： 策略信号完全源自结构化金融时间序列数据（如价格、收益率），不涉及新闻或社交媒体等非结构化数据。
- 标的范围： 主要针对单一金融工具（股指、单只股票或加密货币），不涉及复杂的配对交易或一篮子组合，以保持 Python 实现的简洁性。

**四种核心交易策略**

书中通过以下四种逻辑来演示自动化交易系统的构建：

简单移动平均线 (SMA)

- 原理： 基于技术分析。通过不同周期的均线交叉产生信号。
- 逻辑： 典型的“金叉/死叉”逻辑。当短期 SMA 高于长期 SMA 时看多（Long），反之看空（Short）或保持中性。

![[attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/img_001.png]]

动量策略 (Momentum)

- 原理： 假设金融资产在短期内会延续其近期的表现（即“惯性”）。
- 逻辑： 如果过去 5 天平均收益为负，则预测明天也为负。

均值回归 (Mean Reversion)

- 原理： 假设价格如果偏离其长期均值或趋势太远，最终会“回归”均值。
- 逻辑： 例如，股价远低于其 200 日均线时，预期其即将反弹并买入。

机器学习与深度学习 (ML/DL)

- 原理： 采用“黑盒”方法预测市场走势。
- 逻辑： 利用历史收益率作为特征（Features），训练模型预测未来的价格变动。

## Conclusion

算法交易世界是非常神秘且封闭的。 真正的成功者（产生 Alpha 的人）通常不愿分享其核心策略，以保护其盈利来源。

Python 已成为算法交易领域的标准工具。其优势在于拥有强大的数据分析生态系统（如各类库和 API），且深受顶级金融机构青睐。本书旨在通过将 Python 技术与交易实践（如回测和实盘对接）系统结合，帮助读者在竞争激烈的市场中获取超额收益。

# Python Infrastructure

Python 的部署与环境管理对初学者而言较为复杂。由于 Python 版本众多（如 CPython, PyPy）且第三方库依赖关系交错，开发者需要通过专业的工具链来确保环境的稳定性、一致性和可移植性。

Python 部署的挑战

- 版本碎片化：存在 CPython/Jython 等多种实现，以及 Python 2 与 3 的历史版本差异。
- 依赖地狱：标准库功能有限，第三方库（Packages）数量庞大且安装时常涉及系统级编译，版本冲突和维护成本高。

四大核心解决方案

文中提出了构建专业交易基础设施的四种技术手段：

- 包管理器 (Package Manager)：如 `pip` 或 `conda`。用于自动安装、更新和删除软件包，处理版本一致性。
- 虚拟环境 (Virtual Environment)：如 `virtualenv` 或 `conda`。允许在同一台机器上并存多个互不干扰的 Python 环境。
- 容器化 (Container)：如 `Docker`。将整个操作系统环境与代码打包，确保在本地与云端运行表现完全一致。
- 云实例 (Cloud Instance)：利用高性能、高可用的云服务器进行部署。按需计费且易于扩展，满足金融交易对安全和性能的要求。

![[attachments/Python-算法交易学习笔记-Cpv4djLFwoWd2CxiXgsc4laSn2f/img_002.png]]

## Anaconda as package and virtual env manager

[Python+Anaconda+PyCharm的安装和基本使用【适合完全零基础】](https://www.bilibili.com/video/BV1K7411c7EL?spm_id_from=333.788.videopod.episodes&vd_source=c8041efd376e7f34e73272f6ae86b7a5)

## Using Docker Containers

Docker 为软件提供了一种类似“航运集装箱”的标准化方式。它通过隔离的文件系统，确保程序在任何环境下（本地 Windows 或云端 Linux）都能以相同的方式运行。

**核心操作流程**

构建 (Build)：

需要两个文件：Dockerfile（定义构建步骤）和 Bash 脚本（执行具体的安装逻辑，如安装 Miniconda、Pandas 等）。

命令：`docker build -t pyalgo:basic .`

运行 (Run)：

使用 `docker run -ti` 启动交互式环境。

容器内可以独立运行特定的 Python 版本和库，不干扰宿主机。

管理 (Manage)：

- 分离 (Detach)： `Ctrl+p` -> `Ctrl+q` 可让容器在后台运行。
- 查看 (List)： 使用 `docker ps` 查看运行中的容器。
- 连接 (Attach)： 使用 `docker attach` 重新进入正在运行的容器。
- 清理 (Cleanup)： 停止后使用 `docker rm` 删除容器，`docker rmi` 删除镜像以节省磁盘空间（如文中镜像约为 2GB）。

**为什么使用 Docker？**

对于算法交易或通用的 Python 开发，Docker 提供了环境一致性。它解决了“在我的机器上能运行”的问题，让代码的部署和迁移变得极其高效且可靠。

如果你已经在用 Linux + Anaconda / Windows + Anaconda，那么当前阶段完全够用而且很高效，非常适合个人研究、学习量化、频繁调试和回测；

Docker 并不是马上必须的。Docker 的真正价值在部署和复现：当你需要上云、多机器运行、长期实盘、环境完全一致，或开始对外交付代码时，它几乎是标准配置。

## Using Cloud Instances

本节主要介绍了如何在 DigitalOcean 云端实例（Droplet）上搭建一套完整的 Python 及 Jupyter Lab 基础设施。

通过在云端部署 Jupyter Lab，开发者可以摆脱 SSH 终端的限制，直接通过浏览器进行代码编写、文件管理和系统操作。这种方式结合了云端的高可用性与本地操作的便捷性。

**基础设施构成**

云端环境包含以下关键组件：

- Jupyter Notebook/Lab: 提供交互式编程环境、终端、文本编辑器和文件管理器。
- 安全性: 使用 SSL 证书（RSA 公私钥） 进行加密传输，并配置密码哈希保护服务器。
- 环境管理: 通过 Miniconda 安装 Python 3.8 及其核心科学计算库（NumPy, pandas, Scikit-learn 等）。

**自动化部署流程**

部署过程由四个核心脚本/文件协同完成：

| 文件名称 | 主要功能 |
| --- | --- |
| setup.sh | 编排脚本：在本地执行，负责将所有必要文件通过 scp 拷贝到云端，并启动安装。 |
| install.sh | 安装脚本：在云端执行，更新系统、安装 Miniconda/Python 库并启动 Jupyter 服务。 |
| jupyter_notebook_config.py | 配置文件：定义服务器端口（如 8888）、绑定 IP、关联 SSL 证书及设置密码哈希。 |
| mykey.key / mycert.pem | 安全证书：通过 OpenSSL 生成，用于实现 https 加密连接。 |

**操作要点**

- 准备工作: 本地生成 RSA 密钥对，并获取 Jupyter 密码的 SHA1 哈希值。
- 创建实例: 在 DigitalOcean 选择 Ubuntu 镜像（如 20.04），建议配置为 2 核/2GB 内存。
- 一键部署: 运行 `bash setup.sh [服务器IP]`。
- 访问: 浏览器打开 `https://[服务器IP]:8888`，忽略自签名证书警告并输入密码即可开始工作。

使用云实例（如 Droplet）不仅成本低廉（按小时计费），且能提供专业的计算与存储环境。对于算法交易者而言，这是一种既安全又灵活的开发部署方案。

## 量化交易系统的工程化演进

| 阶段 | 阶段名称 | 典型环境与工具 | 核心工作内容 | 阶段目标 | 阶段演进动因 |
| --- | --- | --- | --- | --- | --- |
| Phase 1 | 单机研究实验室 | Windows / Linux Anaconda Jupyter Notebook | 数据获取与清洗（Pandas） 向量化回测与统计验证 | 验证交易策略在历史数据上的可行性与统计显著性 | 研究代码逐渐膨胀，Notebook 难以维护，复现成本上升 |
| Phase 2 | 开源框架进阶 | VS Code / PyCharm Backtrader / VN.py | 事件驱动回测 策略模块化 本地数据库（SQLite / MongoDB） | 构建可复用、可扩展的标准化回测系统 | 环境依赖复杂，跨机器部署困难，难以平滑过渡到实盘 |
| Phase 3 | 容器化转型 | Docker / Dockerfile Docker Compose | 运行环境封装 多服务解耦与编排 | 实现环境一致性与系统可复现性，显著降低部署与运维风险 | 实盘对稳定性与持续运行提出更高要求 |
| Phase 4 | 云端生产环境 | 云服务器（ECS / Droplet） Systemd / Tmux | 7×24 自动化运行 日志、监控与告警系统 | 支撑无人值守的实盘交易系统，满足长期稳定运行需求 | 系统架构成熟阶段 |

阶段升级是一种风险管理行为，而非炫技。在未解决当前阶段的核心问题之前，提前进入下一阶段只会放大系统性风险。

本书介绍的自动化量化交易系统在2026年并不是最流行最先进的，仅作为学习使用。

# Working with Financial Data

量化交易中的数据可以按两个维度划分：历史 vs 实时、结构化 vs 非结构化。本书主要关注结构化数据，尤其是用于回测的历史结构化数据。

典型量化交易流程从交易想法或假设出发，通过历史金融数据进行回测验证。本章围绕这一流程，重点解决三个基础问题：

- 数据获取（import）
- 数据处理（handling）
- 数据存储（storage）

量化数据主要可以分为以下四类： 

|  | 结构化数据 (Structured) | 非结构化数据 (Unstructured) |
| --- | --- | --- |
| 历史数据 (Historical) | 回测基础数据： * 收盘价 (Closing Price) * K线/分时数据 (OHLCV) * 财务报表 (收入、利润等) | 回溯分析素材： * 历史新闻存档 * 社交媒体历史记录 * 研报/白皮书 PDF 库 |
| 实时数据 (Real-time) | 交易执行数据： * 盘口五档/十档 (Bid/Ask) * 逐笔成交 (Tick Data) * 订单簿流 (L2 Order Book) | 舆情/事件监控： * 推特实时流 (Twitter Stream) * 突发新闻快讯 (Breaking News) * 财报会议实时转录 |

结构化数据通常存储在数据库中，可直接用于量化策略的数学运算和统计回归。非结构化数据需要通过 NLP 技术（如情感分析、实体识别）转化为数值信号后，才能被量化模型识别。

本书关注的数据类型范围为结构化数据; 关注的数据时间范围为历史 + 实时。本章重点关注历史结构化数据，如股票日收盘价、分钟级数据等。

本章也会介绍一些常用的python金融数据处理工具，包括：

- `pandas`：读取与处理数据 
- `Quandl`：开源数据源 
- `Eikon API`：机构级数据接口 
- `HDF5`：高效存储格式（适合大规模历史数据）

## Reading Financial Data From Different Sources

[[Reading Financial Data From Different Sources.ipynb]]

## Working with Open Data Sources

个人开发者或学生，建议按照以下梯度来选择数据工具

| 梯度 | 数据源 | 特点 |
| --- | --- | --- |
| 入门级 (完全免费) | yfinance, tushare (国内) | 简单、无门槛，适合练手。 |
| 专业学习级 (API 规范) | Nasdaq Data Link (Quandl), Alpha Vantage | 学习如何处理 API 密钥、JSON 解析和结构化时序数据。 |
| 机构模拟级 | QuantConnect (LEAN) | 这是真正的开源引擎。它提供回测框架，并自带了海量已清洗的机构级数据（免费供回测使用）。 |
| 顶级机构级 | Eikon, Bloomberg | 极度昂贵，数据极全，带 API 接口。 |

[[Working with Open Data Sources - Quandl.ipynb]]

[[Working with Open Data Sources - Eikon.ipynb]]

[[Mock Eikon Data API - Unstructured News Retrieval.ipynb]]

## Storing Financial Data Efficiently

[[Storing DataFrame Objects1.ipynb]]

[[UsingTsTables.ipynb]]

tstables 基于 HDF5 + 自定义封装，生态封闭且依赖老版本 pandas，维护已经停滞。现在主流使用 Parquet，因为它是标准化的列式存储格式，具备更好的压缩率和读取性能：

- 支持按列读取，减少无关数据扫描; 
- 分区裁剪，只读相关数据; 
- 跨生态兼容，如Spark / DuckDB / 云数据仓库。

[[UsingParquet.ipynb]]

[[Storing_Data_with_SQLite3.ipynb]]

## Conclusion

本章主要讲了金融时间序列数据的处理，包括：

-  从文件（如 CSV）读取数据 
-  从网络服务（如 Quandl）获取数据（如日线、期权数据） 
-  开放金融数据正在成为重要的数据来源 

此外，还介绍了数据存储方式：

-  使用 HDF5（高性能二进制存储） 
-  使用 SQLite（轻量关系型数据库） 

这些内容为后续章节打基础：

-  向量化回测 
-  机器学习 / 深度学习预测 
-  事件驱动回测 

# Mastering Vectorized Backtesting

本章主题是 “向量化回测（vectorized backtesting）”，一种利用 NumPy 和 pandas 实现的高效回测方法。

理解向量化回测，最直接的方式是和 “事件驱动回测（event-driven backtesting）” 对比着看。

**事件驱动回测**：

```Python
for bar in data:
    portfolio.update(bar)        # 盯市
    signals = strategy.on_bar(bar)
    orders = risk_manager.check(signals, portfolio)
    fills = broker.execute(orders, bar)  # 模拟撮合、滑点、手续费
    portfolio.apply(fills)
```

- 还原真实交易过程 -- 时间逐根 K 线向前推进，行情事件触发策略逻辑，策略产生信号，撮合引擎模拟下单，账户随之更新。
- 优势是真实 -- 滑点、手续费、部分成交、保证金、止损触发都能被精确建模，回测代码几乎可以原样搬到实盘; 
- 缺点是慢。

**向量化回测**：

```Python
# 简单的双均线策略
df['ma_fast'] = df['close'].rolling(5).mean()
df['ma_slow'] = df['close'].rolling(20).mean()
df['signal'] = (df['ma_fast'] > df['ma_slow']).astype(int)  # 1=持仓, 0=空仓
df['return'] = df['close'].pct_change()
df['strategy_return'] = df['signal'].shift(1) * df['return']  # shift防未来函数
df['cum_return'] = (1 + df['strategy_return']).cumprod()
```

- 把整段历史数据看作向量或矩阵，用一次性的数组运算代替逐根 K 线的循环。
- 一条策略的核心逻辑往往几行 pandas 代码就能写完 -- 算出指标列、生成持仓信号列、与收益率列相乘、累乘得到净值曲线。整个过程没有显式的时间循环，全部交给 NumPy 底层运算处理。
- 代价是放弃对交易细节的精细刻画 -- 订单簿、部分成交、复杂资金管理、路径依赖的风控规则都很难自然表达。换来的是数量级上的速度提升和代码上的极致简洁。

向量化回测特别适合以下场景：

- 策略逻辑简单时，向量化写法直观干净，没必要为几行信号逻辑搭起整套事件驱动框架。
- 交互式探索阶段，几行代码就能验证一个想法，换参数也方便，契合 Jupyter Notebook 这类研究环境。
- 做可视化时，方法天然贴合数据和信号的图形化呈现——指标、信号、收益本来就按列组织。
- 批量扫描参数时，速度优势明显，几百上千组参数组合可以在几秒内跑完。

实务中常见的是两阶段回测：先用向量化回测筛掉绝大多数没有 alpha 的想法，剩下的候选策略再用事件驱动框架做精细化回测，最后上实盘。

本章覆盖三类常见策略：

- SMA 策略通过短周期与长周期均线的交叉产生买卖信号。
- 动量策略假设近期趋势会延续，做空下跌资产、做多上涨资产。
- 均值回归策略的逻辑相反，认为价格在过度偏离均值后终究会回归，交易机会正出现在这些偏离时刻。

为了聚焦向量化方法本身，书中对策略做了若干简化。此外还会讨论数据窥探（data snooping）和过拟合（overfitting）的风险 -- 这是回测中最容易被忽视的坑。

## Making Use of Vectorization

[[Making Use of Vectorization.ipynb]]

## Strategies Based on Simple Moving Averages

[[Strategies Based on Simple Moving Averages.ipynb]]

[[SMAVectorBacktester.py]]

## Strategies Based on Momentum

动量策略可分为截面动量与时间序列动量两类。

**截面动量**

在一组可交易品种中，买入近期相对同业或基准表现较好的品种，卖出表现较差的品种。其前提是：相对强弱在一定时期内具有延续性。Jegadeesh & Titman（1993, 2001）与 Chan 等（1996）对这类策略及其收益来源作了系统研究。截面动量在历史上往往表现突出；Jegadeesh & Titman（1993）指出，按过去表现做多赢家、做空输家的组合，在 3 至 12 个月持有期内可获得显著正收益。

> *举例：在沪深 300 的成分股里，挑过去 6 个月涨幅最大的 30 只买入，涨幅最差的 30 只做空。*

**时间序列动量**

同样依据近期涨跌做多或做空，但参照的是品种自身的历史收益，而非横截面上的相对排名。Moskowitz 等（2012）在多种市场上对此作了详细检验：策略不依赖品种间的相对强弱，而只看单只证券过去是否上涨。他们在所考察的几乎所有品种上均观察到时间序列动量，这与随机游走假说的朴素含义相抵触——若价格服从随机游走，则过去的涨跌不应包含关于未来方向的信息。

> *举例：只看黄金。如果黄金过去 12 个月是涨的，就做多；是跌的，就做空。每个品种各自判断，互不影响。*

两类策略均利用收益的持续性，区别在于比较基准：

- 截面动量：在一群资产里，买强卖弱（和别人比）。
- 时间序列动量：对每个资产，自己涨就买、自己跌就卖（和自己的过去比）。

两者都是“追涨杀跌”，利用的都是趋势的延续性，只是参照对象不同。

[[Strategies Based on Momentum.ipynb]]

## 4.4 Strategies Based on Mean Reversion

[[mean_reversion_backtest.ipynb]]

## 4.5 Data Snooping and Overfitting

书中展示的"效果好"的策略例子,很多是靠数据窥探得来的——同一组数据被反复用来调参、试出满意的结果,这在真实的策略研究中其实是不诚实的,因为它给人一种策略有经济价值的假象。本书重点是讲 Python 编程,所以这种简化处理还算说得过去，就像数学教材爱举那种有唯一解的"完美例子"一样，但现实中这类情况是少数。

另一个相关问题是过拟合:模型描述的是噪声而不是信号,在测试数据上表现好,但对未来数据没什么预测力。哪怕是双均线这么简单的策略,也能跑出成千上万种参数组合,总有一些能跑出好看的数字。Bailey 等人(2015)指出,现在的算力让人几乎可以无限次试参数，但因为金融数据信噪比太弱，调出来的往往是过去的噪声而非未来的信号，结果就是一个过拟合的回测。Ioannidis(2005)在讨论医学论文时也指出类似问题:一项研究结论是否可信，取决于它成立的先验概率、研究的统计功效，以及显著性水平，越来越多所谓的"研究发现"其实站不住脚。

所以,书里某个策略在某组数据、某组参数下表现好,不代表推荐这套配置,也不能说明这类策略普遍有效。读者可以拿书里的代码去探索自己的想法,但要基于自己的回测、验证和结论去实践——金融市场奖励的是扎实的策略研究，不是靠暴力试参数堆出来的好看结果。

## 4.6 Conclusion

向量化是科学计算和金融分析中的强大工具，尤其是在算法交易策略回测这个场景下。本章用 NumPy 和 pandas 演示了向量化，并用它回测了三类策略：简单移动平均、动量、均值回归。

需要说明的是，本章做了不少简化处理——真正严谨的策略回测还得考虑数据问题、样本选择、避免过拟合、市场微观结构等更多因素。但本章的重点是从技术实现的角度讲清楚向量化这个概念本身，以及它在算法交易里能做什么。文中所有具体的例子和结果，都要放在数据窥探、过拟合、统计显著性这些问题的背景下去看待，不能直接当作可靠结论。

# Predicting Market Movements with Machine Learning

近年来，机器学习、深度学习和人工智能发展迅猛，全球算法交易员从中获益。

本章从专业量化交易员的视角出发，展示如何应用这些技术解决价格预测问题，主要涵盖以下策略：

- 基于线性回归的策略：利用线性回归外推趋势，推导资产未来的价格方向。
- 基于机器学习的策略：算法交易通常只需预测涨跌方向而非绝对幅度，因此预测本质上是分类问题。本章引入逻辑回归作为分类的基准模型。
- 基于深度学习的策略：利用脸书等巨头普及的神经网络算法，解决市场预测中的分类问题。

本章的核心目标是提供 “基于过往回报率来预测金融市场未来价格走势” 的实用方法。其基本假设是：有效市场假说（EMH）并不普遍成立，即历史可能提供某些启发，而这些启发可以通过统计技术进行挖掘。换句话说，我们假设金融市场中的某些模式会自我重复，从而可以利用过去的观察结果来预测未来的价格走势。

## 5.1 Using Linear Regression for Market Movement Prediction

[[Using Linear Regression for Market Movement Prediction.ipynb]]

[[LRVectorBacktester.py]]

## 5.2 Using Machine Learning for Market Movement Prediction

[[Using Machine Learning for Market Movement Prediction.ipynb]]

代码：https://github.com/yhilpisch/py4at
