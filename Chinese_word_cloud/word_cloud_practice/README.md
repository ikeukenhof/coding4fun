constructor_color_contour.png 为**WordCloud**对象设置**contour_width=1,contour_color='red'**的结果
> 注: 若设置mode ='RGBA',且contour_width不为0, 则会抛出异常 ValueError: operands could not be broadcast together with shapes (310,309,4) (310,309,3)

constructor_color.png 为正常效果（scale属性为默认值1）
constructor_color_scale.png 为设置scale=20的效果
scale值越大，图片分辨率越大，越清晰，占用内存越大