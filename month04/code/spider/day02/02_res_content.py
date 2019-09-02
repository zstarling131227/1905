import requests
url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1566395335425&di=5fa8ed2950d2b618ba038015c2cb79d8&imgtype=0&src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201512%2F11%2F20151211013224_2QYBu.jpeg'
headers={
    'User-Agent':'Mpzilla/5.0'
}
html=requests.get(url,headers=headers).content

with open('华晨宇图片.jpg','wb') as f:
    f.write(html)
