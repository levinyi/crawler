import requests
url = 'http://exercise.kingname.info/ajax_1_backend'

html = requests.get(url).content.decode()
print(html)
url_post = 'http://exercise.kingname.info/ajax_1_postbackend'

html_kingname = requests.post(url_post, json={'name': 'qingnan', 'age': 24}).content.decode()
html_other = requests.post(url_post, json={'name': 'alsdfj', 'age': 4}).content.decode()

print(html_kingname)
print(html_other)


################################################# exercise 2:  ##############################
import json
import re
url = 'http://exercise.kingname.info/exercise_ajax_2.html'
html = requests.get(url).content.decode()
code_json = re.search("secret = '(.*?)'", html, re.S).group(1)
code_dict = json.loads(code_json)
print(code_dict['code'])
