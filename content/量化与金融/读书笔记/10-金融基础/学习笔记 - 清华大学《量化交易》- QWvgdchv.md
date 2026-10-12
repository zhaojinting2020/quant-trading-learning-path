---
title: 清华大学《量化交易》学习笔记
url: https://my.feishu.cn/docx/QWvgdchvTopiqNx3vTvcCTg0nRh
quality: raw
fetch_source: feishu:cli
fetched_at: 2026-06-28 05:09:12+00:00
feishu_formatted_at: 2026-06-28 05:09:12+00:00
urls_repaired_at: 2026-06-28 05:09:12+00:00
wikilinks_unbulleted_at: 2026-06-28 05:48:29+00:00
custom-width: 85
code_blocks_repaired_at: '2026-07-02T05:27:29+00:00'
---

# 清华大学《量化交易》学习笔记

教学视频：

[https://www.bilibili.com/video/BV1D52CBREpX/?spm_id_from=333.337.sear...](https://www.bilibili.com/video/BV1D52CBREpX/?spm_id_from=333.337.search-card.all.click&vd_source=c8041efd376e7f34e73272f6ae86b7a5)

其他参考资料：

[https://github.com/jarry-creat/quantAnalysis](https://github.com/jarry-creat/quantAnalysis)

## 1.1 什么是量化交易

交易产品

- 股票
- CTA
- 期权
- FOF

盈利模式

- 单边多空策略
- 套利策略
- 对冲策略

策略信号

- 多因子策略
- 均值回归/动量效应/二八轮动/海龟策略
- 机器学习策略

## 1.2 量化交易的开发流程

数据获取 -> 数据清洗 -> 策略编写 -> 策略回测 -> 策略优化 -> 模拟盘交易 -> 实盘交易

数据获取

- 数据获取的内容包括：行情数据，宏观数据，财务数据，與情数据
- 数据获取的方法包括：网站下载，客户端，三方API，爬虫

数据清洗

垃圾数据清除，空值填充，格式转换，数据对齐

策略编写

信号捕捉 -> 交易 -> 建仓 -> 平仓

策略回测

回测参数设置 -> 策略实例化 -> 历史数据载入 -> 回测执行 -> 计算盈亏 -> 计算统计指标 -> 生成回测报告

策略优化

重视交易费 重视风险，重视退出 优化无止境，不要把过多的时间浪费在优化上

模拟盘交易

- 过去表现并不表示未来结果
- 模拟盘交易要保持至少半年以上
- 模拟盘稳定收益100%以上再考虑实盘交易

## 1.3 量化交易的策略分类

- 交易产品

  - 股票：通过股价的波动盈利
  - CTA：关注价格趋势利差
  - 期权：通过期权合约差价来盈利
  - FOF： fund of fund，在震荡的市场下，fof产品优势明显
- 盈利模式

  - 单边多空策略：根据股票的涨跌来进行盈利，低买高卖
  - 套利策略：利用金融产品价格与收益率暂时不一致的机会来获得收益。
  - 对冲策略：同时进行两笔行情相关，方向相反，数量相当，盈亏相抵的交易。在期货市场或者股票市场同时进行等量反向的交易，以锁定既得利润，通过抵消两个市场的损益来规避股票   市场的系统性风险。简单来说，就是做多的同时做空，市场向上赚钱，市场向下，少亏钱。
- 策略信号

  - 多因子策略：找到某些和收益最相关的指标，并根据该指标，建立一个股票组合，期望该组合在未来一段时间跑赢或者跑输指数。
  - 交易模型策略（均值回归/动量效应/二八轮动/海龟策略...)：市场趋势符合交易模型即可盈利。
  - 机器学习策略：从**大量数据**中找到某种规律，找到可盈利，可量化，可执行的策略信号。

## 1.4 股票的基本知识

### 1.4.1 股票的基本概念

股票带来的收益：分红，送股配股，交易收益

### 1.4.2 常见的金融标的的风险和收益

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_001.png]]

<p class="kb-image-caption">图例</p>

[https://www.swsresearch.com/institute_sw/allIndex/downloadCenter/indu...](https://www.swsresearch.com/institute_sw/allIndex/downloadCenter/industryType)

<p class="kb-image-caption">图例</p>
- KDJ：随机指标。通过价格波动的真实波幅来反映价格走势的强弱和超买超卖现象。适用于短期行情走势分析。一般交叉的时候都是买点或者卖点。转折点是超买点或者超卖点。

## 1.5 量化交易基本知识

### 1.5.1 量化交易平台

为量化交易人员提供量化数据，策略框架，回测框架，交易接口等功能的平台。常见的量化交易平台：聚宽，掘金，bigquant，ricequant等

### 1.5.2 利用numpy进行股价统计分析

#### 1.5.2.1 股价统计数据样本

股票代码; 交易日期; 收盘价; 开盘价; 最高价; 最低价; 成交量

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_004.png]]

<p class="kb-image-caption">图例</p>
- 成交量加权平均价格（VWAP）：**在某段时间内，按成交量加权计算的平均价格**。它能更准确地反映市场交易的真实平均成本。可以用来判断买入或者卖出是否在合理的价格。如果当天股价高于 VWAP → 表示买盘较强；低于 VWAP → 卖盘占优。
- 收益率：主要用对数收益率（log return），指所有价格取对数之后两两之间的差值。
- 波动率：越高说明波动越明显
- 年波动率/月波动率 ...

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_005.png]]

<p class="kb-image-caption">图例</p>

MACD有点类似于股价的加速度。当MACD=0, 说明股价在匀速上升或者匀速下降。当MACD出现与零轴的交点，说明股价出现了拐点，有可能是要大幅上涨/上涨减弱/大幅下跌/下跌减弱。关注这些点比单纯的关注股票的涨跌更重要。

#### 1.5.4.2 KDJ

随机指数。通过价格波动的真实波幅来反映价格走势的强弱和超买超卖现象。主要适用于短期行情的走势分析。

<p class="kb-image-caption">图例</p>

set_order_cost(OrderCost(close_tax=0.001, open_commission=0.0003, close_commission=0.0003, min_commission=5), type='stock')
```python

```
滑点

```python

set_slippage(PriceRelatedSlippage(0.002), type'stock')
```

成交量比例

```python

set_option('order_volume_ratio', 0.5)
```

动态复权模式

```python

set_option('use_real_price', True) #一般推荐打开，来模拟真实环境
```

#### 1.6.3.2 定时函数

设定回测和模拟交易中的运行时间和频率

```python

run_monthly(func, monthday, time='open', reference_security)
run_weekly(func, weekday, time='open', reference_security)
run_daily(func, time='open', reference_security)
```

交易函数

```python

order(security, amount, style, side='long', pindex=0)
order_value(security, value, style, side='long', pindex=0)
order_target(security, amount, style, side, pindex, close_todat=False)
```

#### 1.6.3.3 成交订单

```python

get_orders(order_id=None, security=None, status=None)
get_orders(order_id='123') #查询订单号为123的订单
get_orders(security='000001.XSHE') #查询所有标的为000001.XSHE的订单
```

撤单

```python
#在每天交易结束后对未完成的订单进行撤单

def after_market_clsoe(context):
    orders = get_open_orders()
    for _order in orders.values():
        cancel_order(_order)
```

账户出入金

```python

inout_cash(cash, pindex=0)
inout_cash(10000) #向账户充值10000元
```

#### 1.6.3.4 交易对象

order对象: 订单处理流程，包括：订单创建 -> 订单检查 -> 报单 -> 确认委托 -> 撮合

```python
def initialize(context):

    set_benchmark('000300.XSHG')
    run_weekly(market_open, 1, time='open')

def market_open(context):
    orders = order(g.security, 100)
    print(orders)

    if orders is None:
        print("创建订单失败")
    else:

        print("""交易费用： {}""".format(orders.commission))
        print("""是否买单： {}""".format(orders.is_buy))
        print("""订单状态： {}""".format(orders.status))
        print("""订单平均成交价格： {}""".format(orders.price))

    else:
        order(g.security, -800)
```

Trade对象: 订单成交相关信息

```python
def initialize(context):

    set_benchmark('000300.XSHG')
    g.security = "000001.XSHG"
    run_daily(market_open, 1, time='open')
    run_daily(after_market_clsoe, time='close')

def market_open(context):
    if g.security not in context.porfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)

def after_market_close(context):
    trades = get_trades()

    for _trade in trades.values():
        print("""成交记录： {}""".format(_trade))
        print("""成交时间： {}""".format(_trade.time))
        print("""对应的订单id： {}""".format(_trade.order_id))
```

#### 1.6.3.5 策略信息

context对象：策略信息的总览，包括账户，时间，持仓等信息

```python

subportfolios #当前单个操作仓位的资金，标的信息，是一个数组
portfolio # 账户信息，是subportfolio的汇总信息。当为单个操作仓位时，portfolio指向subportfolios[0]
def initialize(context):

    g.security = "000001.XSHG"

def handle_data(context, data):
    log.info(context.portfolio.total_value)
    log.info(context.portfolio.positions_value)
    log.info(context.current_dt.day)
    log.info(context.portfolio.returns)
    log.info(context.subportfolios[0].avaliable_cash)
```

position对象：输出持有的标的的信息

```python
def initialize(context):

    g.security = "000001.XSHG"

def handle_data(context, data):
    if g.security in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)

    long_positions_dict = context.portfolio.long_positions
    print(type(long_positions_dict))
    for position in list(long_positions_dict.values()):
        print(position.security, #标的
              position.total_amound, #总仓位
              position.value, #标的价值
              position.init_time #建仓时间
              )
```

#### 1.6.3.6 账户信息

portfolio： 总账户信息。

```python
def initialize(context):

    g.security = "000001.XSHG"

def handle_data(context, data):
    if g.security in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)

    print("""多单的仓位： {}""".format(context.portfolio.long_positions))
    print("""空单的仓位： {}""".format(context.portfolio.short_positions))
    print("""总权益： {}""".format(context.portfolio.total_value))
    print("""总权益的累计收益： {}""".format(context.portfolio.returns))
    print("""初始资金： {}""".format(context.portfolio.starting_cash))
    print("""持仓价值： {}""".format(context.portfolio.position_value))
```

subportfolio： 子账户信息

```python
def initialize(context):

    g.security = "000001.XSHG"

def handle_data(context, data):
    if g.security in context.portfolio.positions:
        order(g.security, 1000)
    else:
        order(g.security, -800)

    print("""累计出入金: {}""".format(context.subportfolios[0].inout_cash))
    print("""可用资金: {}""".format(context.subportfolios[0].avaliable_cash))
    print("""可取资金: {}""".format(context.subportfolios[0].transferable_cash))
    print("""挂单锁住资金: {}""".format(context.subportfolios[0].locked_cash))
    print("""账户所属类型: {}""".format(context.subportfolios[0].type))
```

## 1.7 量化交易数据获取

### 1.7.1 财务数据

get_fundamentals(): 查询财务数据

query():查询数据api，可以是整张表，也可以是表中的多个字段，或者计算出的结果

get_fundamentals_continuously()

```python
# 获取总市值
q = query(
    valuation
    ).filter(

        valuation.code = '000001.XSHE'
        )

df = get_fundamentals(q, '2022-09-01')
print(df['market_cap'][0])

# 获取财务数据
q = query(
    income.stateDate,
    income.code,

    income.basic_eps #基本每股收益 = 净利润/总股本
    ).filter(

        income.code = '000001.XSHE'
        )

rets = get_fundamentals(q, statDate='2022q2')
print(rets)

# 测试get_fundamentals_continuously
q = query(
    valuation.market_cap,
    valuation.pe_ratio,

    valuation.turnover_ratio,
    indicator.eps

    ).filter(valuation.code.in_(['000001.XSHE', '600000.XSHG']))

result = get_fundamentals_continuously(q, end_date='2022-01-01', count=5, panel=False)
print(result)
```

### 1.7.2 成分股

指数成分股 get_index_stocks(index_symbol, date)

行业成分股 get_industry_stocks(industry_code, date)

概念成分股 get_concept_stocks(concept_code, date)

```python
# 查询沪深300的所有股票（返回前100）

stocks = get_index_stocks('000300.XSHG')
print(stocks[:100])

#查询行业成分股，计算机互联网行业成分股
stocks = get_industry_stocks('I64'）
print(stocks)

#查询风电板块的成分股

stocks = get_concept_stocks('sc0084', date='2022-06-01')
print(stocks)
```

### 1.7.3 标的信息

获取所有标的信息 get_all_securities(types=[], date=None)

获取单个标的信息 get_security_info(code, date=None)

```python
#查询所有标的信息

print(get_all_securities()[:10])
#查询所有ETF的信息

print(get_all_securities(types=['etf'], date='2022-09-01')[:10])

#查询单个标的信息

start_date = get_security_info('000001.XSHE').start_date
print(start_date)

security_type = get_security_info('000001.XSHE').type
print(security_type)
```

### 1.7.4 交易数据

获取行情数据 get_price(security, start_date, end_date, frequency, fields, skip_paused, fq, count, panel, fill_paused)

获取龙湖榜数据 get_billboard_list(stock_list, start_date, end_date, count)

```python
#获取单只股票的一个时间段的行情数据

df = get_price('000001.XSHE', start_date='2015-01-01', end_date='2015-01-31', frequency='1m', fields = ['open', 'close'])
print(df)

#获取多只股票的一个时间段的行情数据

df = get_price(get_index_stocks('000903.XSHG'))
print(df.loc[df['code']=='000001.XSHE'])

#获取龙虎榜数据

df = get_billboard_list(stock_list=None, end_date='2022-09-01', count=1)
print(df[['code', 'abnormal_name', 'sales_depart_name', 'rank']][:10])
```

## 1.8 量化选股

### 1.8.1 一个基本面选股的例子

什么是量化选股？

利用数量化的方法选择股票组合，期望该股票组合能够获得超越基准收益率的投资行为。什么是技术面选股？

利用各种技术理论或者技术指标来分析和预测股票的未来价格趋势。什么是基本面选股？

通过对一家上市公司在发展过程中所面临的外部因素和内部因素进行分析，对其未来的发展前景进行预测，判断该上市公司的股票是否值得买进。量化选股注意事项

- 分配多股，减少单股重仓的情况（不要把鸡蛋放在一个笼子里）
- 全面研究个股基本面，增强个股判断逻辑和支撑
- 主动投资，而非被动投资

```python
import datetime
def initialize(context):

    set_benchmark('000300.XSHG')
    set_option('use_real_price', True)
    set_option('order_column_ratio', 1)
    set_order_cost(OrderCost(open_tax=0, close_tax=0.0001, open_commission=0.0003, close_commission=0.0003, close_today_commission=0, min_comission=5), type='stock')

    g.stocknum = 20
    g.days = 20
    g.refresh_rate = 100

    run_daily(trade, 'every_bar')

def check_stocks(context):
    q.query(
        indicator.code,

        valuation.capitalization,
        indicator.roe,

        indicator.gross_profit_margin
        ).filter(

            # 公司总市值大于 50 亿, 过滤掉市值太小, 风险较高的小公司，只保留中大盘股。
            valuation.capitailization>50,

            # 流通市值 > 总市值的 95%。挑选“几乎全部股份都能流通”的公司，
            # 避免那种大股东锁仓很多股份, 市场上能交易部分太小的情况。
            valuation.circulation_market_cap > valuation.market_cap * 0.95,

            # 选出盈利能力比较强的公司，说明其产品或服务的成本优势比较好。
            indicator.gross_profit_margin > 20,

            # 筛选出资金利用效率高, 回报率高的公司。一般 >15% 就算不错了，
            # >20% 说明公司盈利能力很强。
            indicator.roe > 20
            ).order_by(

                valuation.market_cap.desc()
                ).limit(
                    100
                    )

    # 根据当前年份，获取这一年的所有股票基本面数据（市值, 财报指标等），然后存到 df 里。
    df = get_fundamentals(q.statDate=str(context.current_dt)[:4])

    buylist = list(df['code'])
    buylist = detect_stock(buylist, context.current_dt, 750)
    buylist = filter_paused_stock(buy_list)[:20]
    return buylist

def filter_paused_stock(stock_list):
    current_date = get_current_date()
    return [stock for stock in stock_list if not current_date[stock].paused]

def detect_stock(stocks, beginData, n=180):
    stocklist=[]
    for stock in stocks:

        start_date = get_security_info(stock_.start_date
        if start_date < (beginDate - timedelta(days=n)).date():
            stocklist.append(stock)

    return stocklist

def trade(context):

    if g.days % g.refresh_rate ==0 :
        #基本面比较好的股票列表，top 20
        stocklist = check_stocks(context)
        #当前持仓的所有股票代码列表

        sell_list = list(context.portfolio.positions.keys())
        #当前持仓的所有股票代码列表 - stock_list = 不希望继续持有的股票列表
        sells = list(set(sell_list).difference(set(stock_list)))

        for stock in sells:

            order_target_value(stock, 0)

        if len(context.portfolio.positions) < g.stocknum:
            num = g.stocknum - len(context.portfolio.possitions)
            cash = context.portfolio.cash / num
        else:
            cash = 0

        for stock in stock_list:

            if (len(context.portfolio.positions) < g.stocknum) and (stock not in context.portfolio.positions):
                order_value(stock, cash)

        g.days = 1

    else:
        g.days += 1
```

### 1.8.2 量化选股营收因子

财务因子：评价企业基本面情况，通常包括

- 成长类因子：包括营收因子与利润因子

  - 营收因子：

    - 营业收入同比增长率(inc_revenue_year_on_year)：与上一年度同一期营业收入比较，上期指的是上一年度/季度/月度的同一期
    - 营业收入环比增长率(inc_revenue_annual)：与上一期营业收入相比较
    - 营业总收入(net_profit_total_revenue)：主营业务收入+其他业务收入

```python
    df = get_fundamentals(
        query(
            indicator.code,

            indicator.inc_revenue_year_on_year
            ).filter(

                indicator.inc_revenue_year_on_year > 300
                ).order_by(indicator.inc_revenue_year_on_year.desc()),
                date = '2022-09-01'
        )

    print(df)

    #获取df里每只股票过去 5 个交易日的涨停价

    df_new = history(5, unit='1d', field='high_limit', security_lsit=df['code'], df=True)
    print(df_new)
```
  - 利润因子：净利润同比增长率，净利润环比增长率，营业利润率，销售利润率，销售毛利率

    - 净利润同比增长率（inc_net_profit_year_on_year)：净利润就是企业的税后利润。同比表示与上一年度同期比较。
    - 净利润环比增长率(inc_net_profit_annual)：只针对上一期
    - 营业利润率:(operation_profit_to_total_revenue): 经营所得的营业利润占销售净收入的百分比，或者占投入资本额的百分比。
    - 销售净利润(net_profit_margin）：净利润与销售净收入的关系
    - 销售毛利润(gross_profit_margin): 毛利润与销售净收入的关系

```python
    df = get_fundamentals(
        query(
            indicator.code,

            indicator.inc_net_profit_year_on_year,
            ).filter(

                indicator.inc_net_profit_year_on_year > 300
                ).order_by(indicator.inc_net_profit_year_on_year.desc()),
                date = '2022-09-01'
        )
    print(df)
```
- 规模类因子：反映公司规模情况，主要用于体现市值大小对投资收益的影响。

  - 总市值（valuation.market_cap)：在特定时间股票的总价值=总股本数×股价。表示个股权重的大小或者大盘规模的大小。
  - 流通市值（valuation.circulating_market_cap): 在特定时间可交易的流通股票的总价值=可交易的流通股股数×股价。流通市值占总市值的比重越大，说明股票的市场价格越能反映出公司的真实价值。
  - 总股本(valuation.capitalization): 公司已经发行的普通股股份总数（包括a/b/h股），单位为万股
  - 流通股本(valuation.circulating_cap):公司已发行的境内上市流通股份总数（a股）

```python
  df = get_fundamentals(
      query(
          valuation.code,
          valuation.market_cap
          ).filter(

              valuation.market_cap > 10000
              ).order_by(valuation.market_cap.desc()),
      )
  print(df)
```
- 价值类因子：价值投资是挑选那些市场价格相对便宜，但从公司财务指标看仍然很有价值的股票。

  - 市净率(valuation.pb_ratio)：每股市价/每股净资产。越低越好，但也不绝对。一般超过50, 可能有泡沫现象。一般低于5, 说明公司也不太好。
  - 市销率（valuation.ps_ratio)：股价/每股销售额。用来剔除市盈率很低，主营业务没有核心竞争力，主要依靠非经营性损益而增加利润的上市公司。市销率低，可能表示公司被低估。
  - 动态市盈率（valuation.pcf_ratio)：股票现价/未来每股收益的预测值。指对下一年度的市盈率的预测。
  - 静态市盈率(valuation.pe_ratio)：股票现价/每股收益。基于公司的实际盈利表现，反映的是公司已经实现的盈利水平，可以用来评估一个公司当前的盈利能力与股价的关系。市盈率越小，说明投资回收期越短，风险越小。

```python
  df = get_fundamantals(
      query(
          valuation.code,
          valuation.pb_ratio,
          valuation.market_cap
          ).filter(

              valuation.market_cap > 8000,
              valluation.pb_ratio < 1.5
              ).order_by(valuation.pb_ratio.asc()),
              date = '2022-09-01'
      )
  print(df)

  df = get_fundamantals(
      query(
          valuation.code,
          valuation.pcf_ratio,
          valuation.pe_ratio,
          valuation.ps_ratio
          ).filter(

              valuation.ps_ratio < 0.5,
              valluation.pcf_ratio < 6,
              valuation.pe_ratio > 3,
              valuation.pe_ratio < 5,

              ).order_by(valuation.pe_ratio.asc()),
              date = '2022-09-01'
      )
  print(df)
```
- 质量类因子：指与财务质量，资本结构相关的因子。影响质量因子的因素大致包括：公司的盈利能力，盈利稳定性，资本结构，成长性，会计质量，派息/摊薄，投资能力等。

  - 净资产收益率(indicator.roe)：税后利润/所有者权益。该指标越高，说明投资带来的收益越高。
  - 总资产净利率(indicator.roa): 净利润/平均资产总额。反映的是公司运用全部资产所获得利润的水平。越高，说明公司的投入产出水平越高，资产运营越有效，成本费用控制水平比较高。

```python
  df = get_fundamentals(
      query(
          indicator.code,
          indicator.roe
          ).filter(
              indicator.roe > 50

              ).order_by(indicator.roe.asc()),
              date = '2019-03-01'
      )
  print(df）
```

## 1.9 量化择时

量化则是就是利用数量的方法，通过对各种宏观微观指标的量化分析，试图找到影响大盘走势的关键信息，并且对未来走势进行预测。通俗来讲就是采用量化的方式判断买点和卖点。趋势量化择时

基本思想来源于技术分析。技术分析认为**趋势存在延续性**，只要找到趋势方向，跟随操作即可。市场情绪量化择时

利用投资者的**热情程度来判断大势方向**。当情绪热烈时，大盘可能会继续涨，当投资者情绪低迷时，大盘可能会继续下跌。常用方法包括：调查问卷，开户人数，搜索指数，报告评级，融资融券数据，與情数据等。技术指标理论的三个假设

- 市场行为涵盖一切信息
- 价格沿趋势移动
- 历史会重演

什么是技术指标？

技术指标是技术分析中使用最多的一种方法，通过考虑市场行为的多个方面建立一个数学模型，并给出完整的数学公式。从而得到一个体现证券市场的某个方面的内在实质的数字，即所谓的技术指标值。

- 趋向指标：不试图捕顶和测底，如均线指标，MACD等。
- 反趋向指标（振荡指标）：具有强烈的捕顶和捉底的意图，对市场的转折点比较敏感。如KDJ，RSI.
- 压力支撑指标（通道指标）。通过顶部轨道线和底部轨道线来捕捉行情的顶部和底部。具有明显的压力线和支撑线。如布林带，BOLL指标，XS薛斯通道指标等。
- 量价指标：通过成交量变动来分析捕捉价格未来走势。重点关注成交量与价格涨跌的关系，如OBV能量潮指标，VOL成交量指标等。

### 1.9.1 趋向指标(DMI)

又称动向指标。基本原理是通过分析股价在上升下跌过程中的均衡，即供需关系受价格的变动由均衡到失衡的循环过程，从而提供对趋势判断的依据。大多数指标都是以每一日的收盘价的走势，升幅，跌幅的累计数来计算出不同的分析数据。但是这些指标往往忽略了每一日的高价低价的波动幅度。趋向指标就是把每日的高低波动的幅度因素计算在内，来分析预测未来的走势。

#### 1.9.1.1 MACD

<p class="kb-image-caption">图例</p>

```python
DIF, DEA, _MACD = MACD(security_list = security, check_date = '2022-09-01', SHORT = 12, LONG = 26, MID=9)

print(DIF)
print(DEA)
print(_MACD)

security_list = ['000001.XSHE', '000002.XSHE', '601211.XSHG']
_EMV, MAEMV = EMV(security_list = security_list, check_date='2022-09-01', N=14, M=9)
print(_EMV)
print(MAEMV)

security = '000001.XSHE'
_UOS, MAUOS = UOS(security_list = security, check_date = '2022-09-01', N1=7, N2=14, N3=28, M=6)
print(_UOS)
print(MAUOS)
```

#### 1.9.1.4 GDX

<p class="kb-image-caption">图例</p>

```python
_JS, MAJS1, MAJS2, MAJS3 = JS(security, check_date='2022-09-01', N=5, M1=5, M2=10, M3=20)
print(_JS, MAJS1, MAJS2, MAJS3)
```

#### 1.9.1.6 MA

<p class="kb-image-caption">图例</p>

相对强弱指标，是期货市场和股票市场中最为著名的摆动指标。显示的是股价向上波动的幅度占总的波动幅度的百分比。如果数值大，就说明市场处于强势状态，如果数值小，则表示市场处于弱势。

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_023.png]]

<p class="kb-image-caption">图例</p>

```python
DIF, DEA, _MACD = MACD(security_list=security, check_date = context.current_dt, SHORT=6, LONG=12, MID=9)
cash = context.portfolio.cash

if g.macd_yesterday<0 and _MACD[security]>0 and cash>0:
    order_value(security, cash)
elif g.macd_yesterday>0 and _MACD[security]<0 and context.portfolio.positions[security].closable_amount>0:
    order_target(security, 0)

g.macd_yesterday = _MACD[security]
```

### 1.10.3 风险指标

我们将股票投资收益率的不确定性称之为风险，具体是指股票市场的一些未知的，不可预测的因素对股价造成的不确定的影响，可能正面影响收益率，也可能是负面的背离。风险指标是对风险的量化评价。风险指标有利于投资者对策略进行一个客观的评价。无论是回测还是模拟，所有风险指标都只会根据每天收盘后的收益每天更新一次，并不考虑盘中的收益情况。

- Alpha：是投资者获得的与市场波动无关的回报。阿尔法系数，是基金/投资的绝对回报和按照beta系数计算的预期回报之间的差额。阿尔法收益与风险的相关性很低。

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_025.png]]

<p class="kb-image-caption">图例</p>
- Beta：表示投资的系统性风险，反映了策略对大盘变化的敏感性。例如一个策略的Beta为1.5, 则大盘涨1%的时候，策略可能涨1.5%，反之亦然。如果一个策略的Beta为-1.5, 则大盘涨1%的时候，策略跌1.5%， 反之亦然。

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_026.png]]

<p class="kb-image-caption">图例</p>
- 夏普比率：表示每承受一单位总风险，会产生多少的超额报酬，可以同时对策略的收益和风险进行综合考虑。表示投资人每多承担一份风险，可以拿到较无风险报酬率（定存利率）高出几分的报酬。若为正值，代表投资人承担报酬率波动风险有正的反馈，若为负值，代表投资人承受风险但报酬率反而不如银行利率，无参考意义。

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_027.png]]

<p class="kb-image-caption">图例</p>
- 索提诺比率：表示每承担一单位的下行风险将会i获得多少的超额回报。与夏普比率相比，索提诺运用下行波动率而不是总标准差，以区别不利和有利的波动。这一比率越高，表明承担相同单位下行风险时能获得更高的超额回报率。索提诺比率可以看作是夏普比率在衡量股票风险上的一种修正方式。

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_028.png]]

<p class="kb-image-caption">图例</p>

信息比率越大，说明该策略单位跟踪误差所获得的超额收益越高。因此，信息比率较大的策略的表现要优于信息比率较低的基准。合理的投资目标是在承担适度风险下，尽可能追求高信息比率。泡沫较少，信息比率较高; 泡沫较多，信息比率较低

![[attachments/清华大学量化交易学习笔记-QWvgdchvTopiqNx3vTvcCTg0nRh/img_029.png]]

<p class="kb-image-caption">图例</p>
- 最大回撤：指在选定周期内任一历史时点向后推，股价走到最低点时的收益率回撤幅度的最大值（即在某一段时期内股价从最高点开始回落到最低点的幅度）。最大回撤用来描述买入股票后可能出现的最糟糕的情况。最大回车是一个重要的风险指标。最大回撤为0, 说明是单边上涨。

![[img_032.png]]

<p class="kb-image-caption">图例</p>

因子分析将多个实测变量转换少数几个综合指标（潜变量），他反映一种降维的思想。通过降维将相关性高的变量聚集在一起，从而减少需要分析的变量的数量，减少为题分析的复杂性。用来确定维度数量，对表体系的维度由主观来做判断。

- 量化选股因子：多为财务指标，如营业利润率，销售净利率，营业收入环比增长率等。
- 量化择时因子：多为技术指标，如均线，换手率，波动率等。因子分析常见的流程为：

- 因子构造
- 因子选股
- 构建股票池
- 策略回测

常用的基础因子还有：

- 价量因子：指利用get_price()函数可以获取到的价量信息，如open, close, high, low, volume, money(成交金额）等。
- 财务数据因子：指当日可以看到的最新单季财务指标，如pe_ratio, turnover_ratio, pb_ratio, market_cap, circulating_market_cap等。
- 行业因子：包含证监会行业分类，聚宽一，二级行业分类以及申万一，二，三级行业分类。如A01（农业）， A02（林业）， B06（煤炭开采和洗选业），B07（石油和天然气开采业），C36（汽车制造业）等。
- 概念因子：概念板块代码。如GN028（智能电网），GN030（物联网），GN092（高端装备制造），GN181（一带一路）等。
- 指数因子：指数代码。如000001.XSHG（上证指数）， 000002.XSHG（A股指数），000003.XSHG（B股指数），000006.XSHG（地产指数）等。
- 资金流因子：get_money_flow()返回的因子。包括change_pct（涨跌幅），net_amount_main（主力净额），net_pct_main（主力净占比），net_amount_xl （超大单净额），net_pct_xl（超大单净占比），net_amount_1（大单净额），net_pct_1（大单净占比）等。

#### 1.10.4.1 因子测试

验证一个因子是否真的有“预测股票收益”的能力。因子测试的一般步骤如下：

- **因子构建**：根据研究目的设定具体的因子指标。例如，以过去 20 日的累计收益率作为动量因子。
- **分组回测**：依据因子值大小对样本股票进行分组（如分为高因子组与低因子组），并跟踪各组在未来一段时间内的收益表现。
- **收益比较**：对比高因子组与低因子组的平均收益差异，以评估因子的区分能力。
- **统计检验**：通过信息比率（IR）, 相关系数（IC）, t 检验等方法，对因子有效性进行显著性检验，以排除偶然性因素。

#### 1.10.4.2 自定义因子

三个基本属性，分别为

- name,
- max_window： 获取数据的最长时间窗口，返回日线数据
- dependencies：自定义因子依赖的基础因子的名称

一个核心函数,

calc(self, data)：data是字典对象。自定义因子的流程：

构造因子属性 -> 实现因子计算 -> 因子分析

单因子分析：调用analyze_factor函数实现

```python
from jqfactor import Factor, analyze_factor
import warnings

warnings.filterwarnings('ignore')

class MA10(Factor):
    name = 'ma10'
    max_window = 10
    dependencies = ['close']

    def calc(self, data):
        return data['close'][-10:].mean()

# 单因子分析
far = analyze_factor(
    factor=MA10,
    start_date='2022-09-01',
    end_date='2022-11-01',
    weight_method='mktcap',
    universe='000300.XSHG',
    industry='jq_l1',
    quantiles=9,
    periods=(1, 5, 10),
)

far.ic_monthly
```

#### 1.10.4.3 因子分析结果

`create_full_tear_sheet(demeaned, group_adjust, by_group, turnover_periods, avgretplot=(5, 15), std_bar=False)`

- demeaned: 是否使用超额收益计算
- group_adjust: 是否使用行业中性化收益计算
- by_group: 是否按行业显示
- turnover_periods: 调仓周期
- avgretplot：因子预测的天数
- std_bar：是否使用标准差

收益分析

包含7种常见的收益分析。通过比较不同因子值分组的平均收益, 累计收益，以及高低组之间的多空收益，来判断一个因子到底有没有“挑好股票”的本事。

**分组平均收益（Portfolio Return by Quantile）**

把股票按因子值分成若干组（如 5 组, 10 组），计算每组未来的平均收益，观察高低组的差异。

**分组累计收益（Cumulative Return by Quantile）**

对每个分组构建时间序列，计算累计收益曲线，判断因子在长期中的稳定性。

**分组多空组合收益（Long-Short Spread Return）**

构建多空组合（做多高分组，做空低分组），观察其平均收益和累计收益，检验因子的套利价值。

**收益差异的显著性检验（t-Test on Return Difference）**

检查高分组与低分组的收益差异是否显著，避免因子只是“运气好”。

**收益率与因子值的横截面回归（Cross-Sectional Regression）**

$$在每期做回归：未来收益 = α + β × 因子值，看 β 是否显著不为零，检验因子对收益的解释力。$$

**信息系数分析（IC/Rank IC Analysis）**

计算因子值与未来收益的相关系数（Pearson 或 Spearman），观察其大小, 显著性与稳定性。IC information coefficient. 代表预测值和实现值之间的相关性，通常用以评价预测能力。取值在-1和1之间，值越大，表示预测能力越好。

**信息比率与夏普比率（IR / Sharpe Analysis）**

用多空组合的收益计算信息比率或夏普比率，衡量因子带来的超额收益是否稳定, 是否值得实盘使用。

**换手率分析**

某因子第一分位持有的股票数量为30支，一天后一支发生变动，其换手率为1/30 = 3.33%

对于5日，10日的换手率，在每日都会对比当日1,5分位数的成分股与5,10日该分位数的成分股的变化进行计算。即：

每天把股票按换手率分成几组（最低的一组, 最高的一组）。然后看看：今天在这些组里的股票，跟前 5 天, 前 10 天在这些组里的股票是不是一样的？

 如果差不多一样 → 说明这个分组很稳定；如果老是换来换去 → 说明分组不稳定。一句话总结：
就是在检查“因子分组的股票会不会每天都大变动”，用来判断因子是不是靠谱。换手率还可以用来衡量交易成本：在实际的交易过程中，假设我们要维护投资组合的因子暴露恒定，对于高换手率因子，则需要进行更多的交易。交易中的税费和滑点，也会吞噬掉我们的部分利润。

```python

from jqfactor import analyze_factor
from jqfactor import Factor

warnings.filterwarnings('ignore')

class MA5(Factor):
    name = 'ma5'
    max_window = 5

    dependencies = ['close']

    def calc(self, data):

        return data['close'][-5:].mean()

far = analyze_factor(factor=MA5, start_date='2022-09-01', end_date='2022-11-01', weight_method='mktcap', universe='000300.XSHG', industry='jq_l1', quantilies=9, periods=(1,5,10))

far.create_full_tear_sheet(demeaned=False, group_adjust=False, by_group=False, turnover_periods=None, avgretplot(5, 15), std_bar=False)
```

- 10.4.4 Alpha因子

Alpha191

国泰君安数量化专题研究报告《基于短周期价量特征的多因子选股体系》给出了191个短周期交易型alpha因子。聚宽量化平台根据这份报告选取并实现了191个alpha因子，并开源给大家使用。

Alpha013

第13个alpha因子

$= ((HIGH\*LOW)^0.5 -VWAP).mean()$

```python

from jqfactor import Factor, analyze_factor
import numpy as np

warnings.filterwarnings('ignore')

class ALPHA013(Factor):
    name = 'alpha013'
    max_window = 1

    dependencies = ['high', 'low', 'volume', 'money']

    def calc(self, data):
        high = data['high']
        low = data['low']

        vwap = data['money']/data['volume']
        return (np.power(high*low, 0.5)-vwap).mean()

far = analyze_factor(factor=ALPHA013, start_date='2022-01-01', end_date='2022-03-01', weight_method='mktcap', universe='000300.XSHG', industry='jq_l1', quantiles=8, periods=(1,5,10))

far.create_full_tear_sheet(demeaned=False, group_ajust=False, by_group=False, turnover_periods=None, avgretplot=(5, 15), std_bar=False)

```

## 相关笔记

[[MOC-quant-finance|量化与金融（主题索引）]]
[[学习笔记 -《量化交易如何建立自己的算法交易事业》-FUANdgmF|《量化交易：如何建立自己的算法交易事业》学习笔记]]
[[学习笔记 -《Python-算法交易》-Cpv4djLF|《Python 算法交易》学习笔记]]
[[学习笔记 -《打开量化投资的黑箱》-NJEadk2a|《打开量化投资的黑箱》学习笔记]]
[[学习笔记 - 量化交易之路-Qod0dMaR|量化交易之路]]
[[学习笔记 - 量化工程师实战录-D8Y7ds8u|量化工程师实战录]]
[[LayerNorm-与-BatchNorm|LayerNorm 与 BatchNorm]] — _量化 / 概率 / 统计_
[[Nasdaq-Data-Link-Account-Profile|Nasdaq Data Link Account Profile]] — _量化 / 概率 / 统计_
[[Nasdaq-Data-Link-Account-Profile|Nasdaq Data Link Account Profile]] — _量化 / 概率 / 统计_