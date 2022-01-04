import requests
from lxml import etree
import pyttsx3

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'
}


def get_weather(city='beijing'):
    url = f'https://www.tianqi.com/{city}/'

    res = requests.get(url=url, headers=headers)
    # print(f'{res.text}')
    data = etree.HTML(res.text)

    '''
    <dl class="weather_info">
            <dt><img src="https://content.pic.tianqistatic.com/content/img/202112/01/ec35c6eddd287698.jpg" alt="" class="weaone_a"></dt>
            <dd class="name"><h1>北京天气</h1><i><a href="/chinacity.html" title="北京天气预报">[切换城市]</a></i></dd>
            <dd class="week">2022年01月02日　星期日　辛丑年冬月三十 </dd>
            <dd class="weather">
                <i><img src="//static.tianqistatic.com/static/wap2018/ico1/b0.png" ></i>
                <p class="now"><b>0</b><i>℃</i></p>
                <span><b>晴</b>-6 ~ 2℃</span>
            </dd>
            <dd class="shidu"><b>湿度：27%</b><b>风向：东北风 1级</b><b>紫外线：中等</b></dd>
            <dd class="kongqi" ><h5 style="background-color:#79b800;">空气质量：优</h5><h6>PM: 15</h6><span>日出: 07:35<br />日落: 17:00</span></dd>
    <dl>
    '''
    # 正则匹配
    weather_list = data.xpath('//dl[@class="weather_info"]//text()')
    # print(weather_list)

    # 循环提取文本，拼接为一句话
    weather_text = ''
    for text in weather_list:
        weather_text += text
    print(weather_text)
    return weather_text


if __name__ == '__main__':
    city = input('请输入城市拼音：')
    engine = pyttsx3.init()
    # 音量(默认：1)
    volume = engine.getProperty('volume')
    # 获取当前语速（默认值：200）
    rate = engine.getProperty('rate')
    print(f'语速：{rate}')
    engine.setProperty('rate', 175)

    # 标准的粤语发音
    voices = engine.setProperty(
        'voice', "com.apple.speech.synthesis.voice.sin-ji")
    # 普通话发音
    # voices = engine.setProperty(
    #     'voice', "com.apple.speech.synthesis.voice.ting-ting.premium")
    # 台湾甜美女生普通话发音
    # voices = engine.setProperty(
    #     'voice', "com.apple.speech.synthesis.voice.mei-jia")
    # engine.setProperty('volume', 0.7)

    '''
    voices = engine.getProperty('voices')       # 获取当前的音色信息
    engine.setProperty('voice', voices[0].id)  # 改变中括号中的值,0为男性,1为女性
    '''

    engine.say(get_weather(city))
    engine.runAndWait()
