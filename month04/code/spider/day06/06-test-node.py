# # sudo pip3 install pyexecjs
import execjs

# with open('node.js', 'r') as f:
with open('node1.js', 'r') as f:
    js_data = f.read()

execjs_obj = execjs.compile(js_data)
sign = execjs_obj.eval('e("tiger")')
print(sign)
