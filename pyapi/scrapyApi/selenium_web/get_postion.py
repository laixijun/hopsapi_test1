# @Time    : 8/13/2020 11:36 AM
# @Author  : Yang Xiaobai
# @Email   : yangzhiyongtest@163.com


class GetPostion:
    def __init__(self):
        pass
    
    # 获取位置的js
    # {'bottom': 533, 'height': 34, 'left': 800, 'right': 1120, 'toJSON': {}, 'top': 499, 'width': 320, 'x': 800, 'y': 499}
    def jsLocation(self):
        '''
        var div = document.getElementById('child');
        var reactObj = div.getBoundingClientRect();
        console.log(reactObj.left);
        console.log(reactObj.top);
        :return:
        '''
        # jsData="" \
        #        "var div = document.getElementById('nc_1__scale_text');" \
        #        "var reactObj = div.getBoundingClientRect();" \
        #        "return reactObj;"
        jsData = '''() => {
                    return {
                        reactObj: document.getElementById('login-wrap clearfix').getBoundingClientRect();
                    }
                }
        '''
        return jsData
        
        # return jsData

    
    # 登录login
    def jsLogin(self,url,obj):
        jsLogin="var httpRequest = new XMLHttpRequest();" \
                "httpRequest.open('POST', "+url+", true); " \
                "httpRequest.setRequestHeader(\"Content-type\",\"application/json\");" \
                                                "var obj = "+obj+";" \
                "httpRequest.send(JSON.stringify(obj));" \
                "return httpRequest.onreadystatechange = function () {" \
                                                                              "if (httpRequest.readyState == 4 && httpRequest.status == 200) {" \
                                                                              "var json = httpRequest.responseText;" \
                                                                              "console.log(json);" \
                                                                              "}};"
        return jsLogin
    
    
    