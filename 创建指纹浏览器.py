
import requests
import time
import random
import fileinput
from tool import *


s = requests.session()
url = get_url()

def bit_create(name,proxy):
    if proxy == "":
        headers = {  
            # 'id': '2c9c29a2801851fe01801d5c64c600b2', # 有值时为修改，无值是添加
            # 'groupId': '2c996b378054663b01805a69f0344410', # 群组ID，绑定群组时传入，如果登录的是子账号，则必须赋值，否则会自动分配到主账户下面去
            'platform': '',  # 账号平台
            'platformIcon': 'other',  # 取账号平台的 hostname 或者设置为other
            'url': '',  # 打开的url，多个用,分开
            'name': name,  # 窗口名称
                    'remark': '',  # 备注
                    'userName': '',  # 用户账号
                    'password': '',  # 用户密码
                    'cookie': '',  # cookie
                    'proxyMethod': 2,  # 代理类型 1平台 2自定义
                    # 'agentId': '', # proxyMethod为1时，平台代理IP的id
                    # 自定义代理类型 ['noproxy', 'http', 'https', 'socks5', '911s5']
                    'proxyType': 'noproxy',
                    # 'host': '127.0.0.1',  # 代理主机
                    # 'port': '20045',  # 代理端口
                    # 'proxyUserName': '', # 代理账号
                    # 'proxyPassword': '', # 代理密码
                    # 'ip': '', # 911 s5 ip
                    # 'country': '', # 911 s5 国家地区
                    # 'province': '', # 911 s5 州/省
                    # 'city': '', # 911 s5城市
                    "syncTabs":False,
                    "credentialsEnableService":True,
                    "syncCookies":True,
                    "syncExtensions":True,
                    "browserFingerPrint": {
                        'coreVersion': '112',  # 内核版本，默认104，可选92
                        'ostype': 'PC',  # 操作系统平台 PC | Android | IOS
                        'os': 'Win32',  # 为navigator.platform值 Win32 | Linux i686 | Linux armv7l | MacIntel，当ostype设置为IOS时，设置os为iPhone，ostype为Android时，设置为 Linux i686 | | Linux armv7l
                        'version': '',  # 浏览器版本，建议92以上，不填则会从92以上版本随机
                        'userAgent': '',  # ua，不填则自动生成
                        'isIpCreateTimeZone': True,  # 基于IP生成对应的时区
                        'timeZone': '',  # 时区，isIpCreateTimeZone 为false时，参考附录中的时区列表
                        'timeZoneOffset': 0,  # isIpCreateTimeZone 为false时设置，时区偏移量
                        'webRTC': '0',  # webrtc 0替换 | 1允许 | 2禁止
                        'ignoreHttpsErrors': False,  # 忽略https证书错误，true | false
                        'position': '1',  # 地理位置 0询问 | 1允许 | 2禁止
                        'isIpCreatePosition': True,  # 是否基于IP生成对应的地理位置
                        'lat': '',  # 经度 isIpCreatePosition 为false时设置
                        'lng': '',  # 纬度 isIpCreatePosition 为false时设置
                        'precisionData': '',  # 精度米 isIpCreatePosition 为false时设置
                        'isIpCreateLanguage': True,  # 是否基于IP生成对应国家的浏览器语言
                        'languages': '',  # isIpCreateLanguage 为false时设置，值参考附录
                        'isIpCreateDisplayLanguage': False,  # 是否基于IP生成对应国家的浏览器界面语言
                        'displayLanguages': '',  # isIpCreateDisplayLanguage 为false时设置，默认为空，即跟随系统，值参考附录
                        'openWidth': 1280,  # 窗口宽度
                        'openHeight': 720,  # 窗口高度
                        'resolutionType': '0',  # 分辨率类型 0跟随电脑 | 1自定义
                        'resolution': '1920 x 1080',  # 自定义分辨率时，具体值
                        'windowSizeLimit': True,  # 分辨率类型为自定义，且ostype为PC时，此项有效，约束窗口最大尺寸不超过分辨率
                        'devicePixelRatio': 1,  # 显示缩放比例，默认1，填写时，建议 1｜1.5 | 2 | 2.5 | 3
                        'fontType': '2',  # 字体生成类型 0系统默认 | 1自定义 | 2随机匹配
                        'font': '',  # 自定义或随机匹配时，设置的字体值，值参考附录字体
                        'canvas': '0',  # canvas 0随机｜1关闭
                        'canvasValue': None,  # canvas为0随机时设置， 噪音值 10000 - 1000000
                        'webGL': '0',  # webGL图像，0随机｜1关闭
                        'webGLValue': None,  # webGL为0时，随机噪音值 10000 - 1000000
                        'webGLMeta': '0',  # webgl元数据 0自定义｜1关闭
                        'webGLManufacturer': '',  # webGLMeta 自定义时，webGL厂商值，参考附录
                        'webGLRender': '',  # webGLMeta自定义时，webGL渲染值，参考附录
                        'audioContext': '0',  # audioContext值，0随机｜1关闭
                        'audioContextValue': None,  # audioContext为随机时，噪音值， 1 - 100 ，关闭时默认10
                        'mediaDevice': '0',  # 媒体设备信息，0自定义｜1关闭
                        'mediaDeviceValue': None,  # mediaDevice 噪音值，不填则由系统生成，填值时，参考附录
                        'speechVoices': '0',  # Speech Voices，0随机｜1关闭
                        'speechVoicesValue': None,  # speechVoices为0时，随机时由系统自动生成，自定义时，参考附录
                        'hardwareConcurrency': '4',  # 硬件并发数
                        'deviceMemory': '8',  # 设备内存
                        'doNotTrack': '1',  # doNotTrack 0开启｜1关闭
                        # ClientRects true使用相匹配的值代替您真实的ClientRects | false每个浏览器使用当前电脑默认的ClientRects
                        'clientRectNoiseEnabled': True,
                        'clientRectNoiseValue': 0,  # clientRectNoiseEnabled开启时随机，值 1 - 999999
                        'portScanProtect': '0',  # 端口扫描保护 0开启｜1关闭
                        'portWhiteList': '',  # 端口扫描保护开启时的白名单，逗号分隔
                        'colorDepth': '24',  # 颜色深度
                        'deviceInfoEnabled': True,  # 自定义设备信息，默认开启
                        'computerName': '',  # deviceInfoEnabled 为true时，设置
                        'macAddr': '',  # deviceInfoEnabled 为true时，设置
                        # ssl是否禁用特性，默认不禁用，注意开启后自定义设置时，有可能会导致某些网站无法访问
                        'disableSslCipherSuitesFlag': False,
                        'disableSslCipherSuites': None,  # ssl 禁用特性，序列化的ssl特性值，参考附录
                        'enablePlugins': True,  # 是否启用插件指纹
                        'plugins': ''  # enablePlugins为true时，序列化的插件值，插件指纹值参考附录
                    }
        }
    else:
        proxy_temp = proxy.split(":")
        host = proxy_temp[0]
        port = proxy_temp[1]
        proxyUserName = proxy_temp[2]
        proxyPassword = proxy_temp[3]
        headers = {  # 'id': '2c9c29a2801851fe01801d5c64c600b2', # 有值时为修改，无值是添加
            # 'groupId': '2c996b378054663b01805a69f0344410', # 群组ID，绑定群组时传入，如果登录的是子账号，则必须赋值，否则会自动分配到主账户下面去
            'platform': '',  # 账号平台
            'platformIcon': 'other',  # 取账号平台的 hostname 或者设置为other
            'url': '',  # 打开的url，多个用,分开
            'name': name,  # 窗口名称
                    'remark': '',  # 备注
                    'userName': '',  # 用户账号
                    'password': '',  # 用户密码
                    'cookie': '',  # cookie
                    'proxyMethod': 2,  # 代理类型 1平台 2自定义
                    # 'agentId': '', # proxyMethod为1时，平台代理IP的id
                    # 自定义代理类型 ['noproxy', 'http', 'https', 'socks5', '911s5']
                    'proxyType': 'socks5',
                    'host': host,  # 代理主机
                    'port': port,  # 代理端口
                    'proxyUserName': proxyUserName, # 代理账号
                    'proxyPassword': proxyPassword, # 代理密码
                    # 'ip': '', # 911 s5 ip
                    # 'country': '', # 911 s5 国家地区
                    # 'province': '', # 911 s5 州/省
                    # 'city': '', # 911 s5城市
                    "syncTabs":False,
                    "credentialsEnableService":True,
                    "syncCookies":True,
                    "syncExtensions":True,                    
                    "browserFingerPrint": {
                        'coreVersion': '112',  # 内核版本，默认104，可选92
                        'ostype': 'PC',  # 操作系统平台 PC | Android | IOS
                        'os': 'Win32',  # 为navigator.platform值 Win32 | Linux i686 | Linux armv7l | MacIntel，当ostype设置为IOS时，设置os为iPhone，ostype为Android时，设置为 Linux i686 | | Linux armv7l
                        'version': '',  # 浏览器版本，建议92以上，不填则会从92以上版本随机
                        'userAgent': '',  # ua，不填则自动生成
                        'isIpCreateTimeZone': True,  # 基于IP生成对应的时区
                        'timeZone': '',  # 时区，isIpCreateTimeZone 为false时，参考附录中的时区列表
                        'timeZoneOffset': 0,  # isIpCreateTimeZone 为false时设置，时区偏移量
                        'webRTC': '0',  # webrtc 0替换 | 1允许 | 2禁止
                        'ignoreHttpsErrors': False,  # 忽略https证书错误，true | false
                        'position': '1',  # 地理位置 0询问 | 1允许 | 2禁止
                        'isIpCreatePosition': True,  # 是否基于IP生成对应的地理位置
                        'lat': '',  # 经度 isIpCreatePosition 为false时设置
                        'lng': '',  # 纬度 isIpCreatePosition 为false时设置
                        'precisionData': '',  # 精度米 isIpCreatePosition 为false时设置
                        'isIpCreateLanguage': True,  # 是否基于IP生成对应国家的浏览器语言
                        'languages': '',  # isIpCreateLanguage 为false时设置，值参考附录
                        'isIpCreateDisplayLanguage': False,  # 是否基于IP生成对应国家的浏览器界面语言
                        'displayLanguages': '',  # isIpCreateDisplayLanguage 为false时设置，默认为空，即跟随系统，值参考附录
                        'openWidth': 1280,  # 窗口宽度
                        'openHeight': 720,  # 窗口高度
                        'resolutionType': '0',  # 分辨率类型 0跟随电脑 | 1自定义
                        'resolution': '1920 x 1080',  # 自定义分辨率时，具体值
                        'windowSizeLimit': True,  # 分辨率类型为自定义，且ostype为PC时，此项有效，约束窗口最大尺寸不超过分辨率
                        'devicePixelRatio': 1,  # 显示缩放比例，默认1，填写时，建议 1｜1.5 | 2 | 2.5 | 3
                        'fontType': '2',  # 字体生成类型 0系统默认 | 1自定义 | 2随机匹配
                        'font': '',  # 自定义或随机匹配时，设置的字体值，值参考附录字体
                        'canvas': '0',  # canvas 0随机｜1关闭
                        'canvasValue': None,  # canvas为0随机时设置， 噪音值 10000 - 1000000
                        'webGL': '0',  # webGL图像，0随机｜1关闭
                        'webGLValue': None,  # webGL为0时，随机噪音值 10000 - 1000000
                        'webGLMeta': '0',  # webgl元数据 0自定义｜1关闭
                        'webGLManufacturer': '',  # webGLMeta 自定义时，webGL厂商值，参考附录
                        'webGLRender': '',  # webGLMeta自定义时，webGL渲染值，参考附录
                        'audioContext': '0',  # audioContext值，0随机｜1关闭
                        'audioContextValue': None,  # audioContext为随机时，噪音值， 1 - 100 ，关闭时默认10
                        'mediaDevice': '0',  # 媒体设备信息，0自定义｜1关闭
                        'mediaDeviceValue': None,  # mediaDevice 噪音值，不填则由系统生成，填值时，参考附录
                        'speechVoices': '0',  # Speech Voices，0随机｜1关闭
                        'speechVoicesValue': None,  # speechVoices为0时，随机时由系统自动生成，自定义时，参考附录
                        'hardwareConcurrency': '4',  # 硬件并发数
                        'deviceMemory': '8',  # 设备内存
                        'doNotTrack': '1',  # doNotTrack 0开启｜1关闭
                        # ClientRects true使用相匹配的值代替您真实的ClientRects | false每个浏览器使用当前电脑默认的ClientRects
                        'clientRectNoiseEnabled': True,
                        'clientRectNoiseValue': 0,  # clientRectNoiseEnabled开启时随机，值 1 - 999999
                        'portScanProtect': '0',  # 端口扫描保护 0开启｜1关闭
                        'portWhiteList': '',  # 端口扫描保护开启时的白名单，逗号分隔
                        'colorDepth': '24',  # 颜色深度
                        'deviceInfoEnabled': True,  # 自定义设备信息，默认开启
                        'computerName': '',  # deviceInfoEnabled 为true时，设置
                        'macAddr': '',  # deviceInfoEnabled 为true时，设置
                        # ssl是否禁用特性，默认不禁用，注意开启后自定义设置时，有可能会导致某些网站无法访问
                        'disableSslCipherSuitesFlag': False,
                        'disableSslCipherSuites': None,  # ssl 禁用特性，序列化的ssl特性值，参考附录
                        'enablePlugins': True,  # 是否启用插件指纹
                        'plugins': ''  # enablePlugins为true时，序列化的插件值，插件指纹值参考附录
                    }
        }

    a = s.post(f"{url}/browser/update", json=headers).json()
    b = a['data']['id']
    print(b)
    return b

if __name__ == "__main__":
    start = 1   # 开始序号
    num = int(input("输入需要创建指纹浏览器的数量："))
    proxy_list = open_txt(r'input/proxy.txt')
    is_proxy = input("是否需要使用sokct代理创建浏览器：(y/n)")
    for i in range(num):
        if is_proxy == "y":
            web_id = bit_create(str(start+i),proxy_list[i])
        else:
            web_id = bit_create(str(start+i),"")
        write_file(r"output/web_id.txt",[web_id+"\n"])
