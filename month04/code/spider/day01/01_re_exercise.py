import re
html='''
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
'''

r_list=re.compile(r'<div class="animal">.*?title="(.*?)".*?content">(.*?)</p>',re.S)
r=r_list.findall(html)
print(r)
for i in r:
    print("动物名称：",i[0].strip())
    print("动物类型：",i[1].strip())
    print("*"*50)
