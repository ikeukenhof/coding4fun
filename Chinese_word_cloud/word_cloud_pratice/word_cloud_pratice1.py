import numpy as np
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator

# 生成'面具'
mask = np.array(Image.open('../pictures/owl.jpeg'))
# 提取颜色
mask_color = ImageColorGenerator(mask)
# 创建wordcloud对象
wcd = WordCloud(mask=mask, repeat=True, background_color='white', max_words=100, mode="RGBA")
# 根据文本生成wordcloud
wcd.generate("this is moon night out of window is clear and quiet")
# 需要generate，后设置颜色
wcd.recolor(color_func=mask_color)
img = wcd.to_image()
img.show()
