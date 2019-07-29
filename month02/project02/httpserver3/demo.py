"""
cookie
JSON ---》JavaScript
"""

import json
js=json.dumps({'a':1,'b':"hello"})
print(js)
dict=json.loads(js)