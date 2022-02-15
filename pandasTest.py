import pandas as pd

def fun1():
    dic = {"name":['a', 'v', 'c', 'xz', 'zx', 'z'],"col1":[1,2,3,5,7,3], "col2":[5,5,6,1,2,3], "col3":[3,4,5,54,34,3]}
    df = pd.DataFrame(dic)
    print(df)

    print("head:")
    print(df.head(3))
    print("tail:")
    print(df.tail(2))

    print("shape:")
    print(df.shape)

    print("dtypes:")
    print(df.dtypes)

    print("index:")
    print(df.index)
    print("columns:")
    print(df.columns)

    print("info:")
    print(df.info())
    print("describe:")
    print(df.describe())

    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)

#数据的索引
def fun2():
    dic = {"name": ['a', 'v', 'c', 'xz', 'zx', 'z'],
           "col1": [1, 2, 3, 5, 7, 3],
           "col2": [5, 5, 6, 1, 2, 3],
           "col3": [3, 4, 5, 54, 34, 3]}
    df = pd.DataFrame(dic)

    print(df['name'])
    print(df[['name', 'col1']])

    #iloc[M,N] 获取m行n列的数据
    print("----iloc-----")
    print(df.iloc[2])   #根据索引获取一行
    print(df.iloc[:, 2]) #根据索引获取某一列,和df[col]类似
    print(df.iloc[2, 3]) #根据索引获取(2,2)的数据

    #loc[m,n] 获取行名m，列名n的数据
    print("----loc-----")
    print(df.loc[1])
    print(df.loc[:, 'name'])
    print(df.loc[1, 'col1'])

#数据的筛选
def fun3():
    dic = {"name": ['a', 'v', 'c', 'xz', 'zx', 'z'],
           "col1": [1, 2, 3, 5, 7, 3],
           "col2": [5, 5, 6, 1, 2, 3],
           "col3": [3, 4, 5, 54, 34, 3]}
    df = pd.DataFrame(dic)

    print(df['name'] == 'z')    #name == 'z'的行

    print("1------------")
    print(df[(df['name'] == 'z') | (df['col3'] == 3)])

    print("2------------")
    print(df[[True, True, True, True, True, True]])

    print("3------------")
    print(df[df == 3])  #矩阵中值等于3的所有方格

    print("4------------")
    print(df[df['col3'].isin([3, 4])])

    print("5------------")
    print(df.query('col2 == 3'))    #像sql规则筛选数据

#数据的处理
def fun4():
    dic = {"name": ['a', 'v', 'c', 'xz', 'zx', 'z'],
           "col1": [1, 2, 3, 5, 7, 3],
           "col2": [5, 5, 6, 1, 2, 3],
           "col3": [3, 4, 5, 54, 34, 3]}
    df = pd.DataFrame(dic)

    print(df.T) #转置
    df.columns = ['name1', 'col1', 'col3', 'col2']
    print(df.columns)

    print(pd.isnull(df))    #检查DataFrame对象中的空值，并返回一个Boolean数组
    pd.notnull(df)    #检查DataFrame对象中的非空值，并返回一个Boolean数组
    pd.dropna(df)    #删除所有包含空值的行
    df.dropna(axis=1)    #删除所有包含空值的列
    df.dropna(axis=1,thresh=1)    #删除所有小于n个非空值的行
    df.fillna(5)    #用5替换DataFrame对象中所有的空值
    df.rename(columns=lambda x: x + 1)    #批量更改列名
    df.rename(columns={'old_name': 'new_ name'})    #选择性更改列名
    df.set_index('column_one')    #更改索引列
    df.rename(index=lambda x: x + 1)    #批量重命名索引
    df.sort_values(['col1'])    #按值排序，默认为正序，可通过ascending=False指定倒序排序
    df.sort_index(ascending=False)    #按索引排序，默认为正序，可通过ascending=False指定倒序排序
    df.drop_duplicates(['col'])    #去重重复项，通过指定列设置去重的参照

#数据的合并和匹配
def fun5():
    dic = {"name": ['a', 'v', 'c', 'xz', 'zx', 'z'],
           "col1": [1, 2, 3, 5, 7, 3],
           "col2": [5, 5, 6, 1, 2, 3],
           "col3": [3, 4, 5, 54, 34, 3]}
    df = pd.DataFrame(dic)

    dic2 = {"name2": ['a2', 'v2', 'c2', 'xz2', 'zx2', 'z2'],
           "col21": [12, 22, 32, 52, 72, 32],
           "col22": [52, 2, 62, 12, 22, 32],
           "col23": [32, 42, 52, 542, 34, 32]}
    df2 = pd.DataFrame(dic2)

    print("-------0---------") #合并df1和df2，合并方式类似sql的多表联合查询
    print(df.merge(df2, how = 'inner', left_on= 'col1', right_on='col22'))

    print("-------1---------")
    print(df.append(df2))   #将df2行添加到df1后面，当不存在的列值为NaN

    print("-------2---------")
    print(pd.concat([df, df2], axis=1))   #将df2列添加到df1后面，当不存在的列值为NaN

    print("-------3---------")
    print(df.join(df2, on = "col1"))

#数据分类汇总
def fun6():
    dic = {"name": ['a', 'v', 'c', 'xz', 'zx', 'z'],
           "col1": [1, 2, 3, 5, 7, 3],
           "col2": [5, 5, 6, 1, 2, 3],
           "col3": [3, 4, 5, 54, 34, 3]}
    df = pd.DataFrame(dic)
    df.groupby(['col2'])['col1'].sum()#按指定的列做分类汇总;
    #groupby还可以配合agg，filter，transform，apply等高级函数使用
    df['col3'].map(lambda x: x * 2)# 将一个函数或匿名函数应用到Series或数据框的特定列
    df.apply(pd.np.cumsum)# 将一个函数或匿名函数应用到Series或数据框
    df.groupby(['col2']).agg({'col1': pd.np.sum, 'col3': pd.np.mean})# 一次性对多个列做聚合操作
    pd.pivot_table(df, index=['col2'])#以col2列为索引建立数据透视表，默认计算方式为求均值
    df.count()
    #非NaN的数量df.describe()
    #一次性产生多个汇总统计
    df.min()# 最小值
    df.max()# 最大值
    df.idxmax(axis=0, skipna=True)# 返回含有最大值的index的Series
    df.idxmin(axis=0, skipna=True)# 返回含有最小值的index的Series
    df.quantile(axis=0)
    #计算样本的分位数
    df.sum(axis=0, skipna=True)
    #返回一个含有求和小计的Series
    df.mean(axis=0, skipna=True)
    #返回一个含有平均值的Series
    df.median(axis=0, skipna=True)
    #返回一个含有算术中位数的Series
    df.var(axis=0, skipna=True)
    #返回一个方差的Series
    df.std(axis=0, skipna=True)
    #返回一个标准差的Series
    df.cumsum(axis=0, skipna=True)
    #返回样本的累计和
    df.cummin(axis=0, skipna=True)
    #返回样本的累计最大值
    df.cummax(axis=0, skipna=True)
    #返回样本的累计最小值

if __name__ == "__main__":

    fun5()