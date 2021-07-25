import base64
import json
import os
import re
import sys
from svglib.svglib import svg2rlg

from bs4 import BeautifulSoup


def captcha_builder_auto(resp):
    
    with open('captcha.svg', 'w') as f:
        f.write(re.sub('(<path d=)(.*?)(fill=\"none\"/>)', '', resp['captcha']))
    print('******************************HHELLO WORLD*********************************************')
    drawing = svg2rlg('captcha.svg')
    path = os.getcwd()
    with open('captcha.svg','r') as svg_data:
        #model = open(os.path.join(os.path.dirname(sys.argv[0]), "model.txt")).read()
        model = open(path+'/src/model.txt').read()
        #svg_data = resp["captcha"]
        #svg_data = 
        soup = BeautifulSoup(svg_data, "html.parser")
        model = json.loads(base64.b64decode(model.encode("ascii")))
        CAPTCHA = {}

    for path in soup.find_all("path", {"fill": re.compile("#")}):
        ENCODED_STRING = path.get("d").upper()
        INDEX = re.findall("M(\d+)", ENCODED_STRING)[0]
        ENCODED_STRING = re.findall("([A-Z])", ENCODED_STRING)
        ENCODED_STRING = "".join(ENCODED_STRING)
        CAPTCHA[int(INDEX)] = model.get(ENCODED_STRING)

    CAPTCHA = sorted(CAPTCHA.items())
    CAPTCHA_STRING = ""

    for char in CAPTCHA:
        CAPTCHA_STRING += char[1]
    return CAPTCHA_STRING

