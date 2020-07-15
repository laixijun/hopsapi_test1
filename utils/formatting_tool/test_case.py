# @Time ： 2020/7/16 00:43
# @Auth ： Yang Xiaobai
# @Email:  yangzhiyongtest@163.com


'''
实现思路
当小白来使用工具的时候，只是想实现传入参数获取结果，需要用到的元素有，URL、请求方式、传入参数、预期结果四个元素
当需求升级了，需要适应不同的URL、请求参数的参数化，
当需求再次升级，需要适应多接口联合测试，其中部分接口为测试数据的构造、权限的获取，解析预期结果的场景复杂化，传入参数的场景复杂化需要定制字段

1、能够只使用基础元素完成测试，自动识别需要测试的场景  比如：维护一个库，自动判断请求是APP还是web
2、用例字段的设计推荐使用单字符串，使用字典建议不超过3层
3、高频字段建议拆分，不出现在同一字典
4、接口测试必要元素放在字段前，无用字段支持为空

'''

