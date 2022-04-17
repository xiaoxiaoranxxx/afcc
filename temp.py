from PIL import Image

im = Image.open('file.gif')

# 分离
for i in range(200):
    im.seek(i)
    im.save('num/'+str(i)+'.png')  # 保存在123的目录中

new_one = Image.new('RGB', (200, 600))

# 拼接
for j in range(200):
    ima = Image.open('num/'+str(j)+'.png')  # 打开123目录
    new_one.paste(ima, (j, 0, j+2, 600))

# 保存
new_one.save("flag.png")