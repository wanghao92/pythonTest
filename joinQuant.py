import jqdatasdk as jq
import datetime
import pandas
#通用信息接口
def test():
    #登录
    jq.auth('18382205937', 'Wanghao123!')
    #查询当天剩余可调用条数
    count = jq.get_query_count()
    print(count)

    '''
    查询简介
    display_name: 中文名称
    name: 缩写简称
    start_date: 上市日期, [datetime.date] 类型
    end_date: 退市日期， [datetime.date] 类型, 如果没有退市则为2200-01-01
    type: 类型，stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B）
    parent: 分级基金的母基金代码
    '''
    # result = jq.get_security_info('600519.XSHG')
    # print(result.display_name)
    # print(result.name)
    # print(result.type)
    # print(result.parent)

    '''
    获取指定日期范围内的所有交易日
    display_name: 中文名称
    name: 缩写简称
    start_date: 上市日期
    end_date: 退市日期，如果没有退市则为2200-01-01
    type: 类型，stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B），
        fjm（分级母基金），mmf（场内交易的货币基金）open_fund（开放式基金）, bond_fund（债券基金）, 
        stock_fund（股票型基金）, QDII_fund（QDII 基金）, money_market_fund（场外交易的货币基金）, 
        mixture_fund（混合型基金）, options(期权)
    '''
    result = jq.get_trade_days(datetime.date(2022, 1, 1), "2022-02-10")
    print(result)

    #获取所有交易日
    jq.get_all_trade_days()

#行情接口
def test1():
    #登录
    jq.auth('18382205937', 'Wanghao123!')
    #查询当天剩余可调用条数
    count = jq.get_query_count()
    print(count)

    #
    result = jq.get_price('000001.XSHE',
                 start_date='2022-02-11 13:00:00', end_date='2022-02-11 14:00:00', count = None,
                 frequency='minute',
                 fields=['open','close','high','low','volume','money', 'high_limit', 'low_limit'])
    pd.set_option('display.max_columns', None)
    print(result)

def init():
    result = jq.auth('18382205937', 'Wanghao123!')
    print(result)
    print("connect joinQuant success...")


if __name__ == '__main__':
    test1()
