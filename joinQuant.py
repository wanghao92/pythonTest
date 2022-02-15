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

    #查询简介
    # result = jq.get_security_info('600519.XSHG')
    # print(result.display_name)
    # print(result.name)
    # print(result.type)
    # print(result.parent)

    #获取指定日期范围内的所有交易日
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
