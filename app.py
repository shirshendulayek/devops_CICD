{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26\fsmilli13333 \cf2 \expnd0\expndtw0\kerning0
from flask import Flask\
import os\
\'a0\
app = Flask(__name__)\
\'a0\
@app.route('/')\
def hello():\
\'a0\'a0\'a0 build_id = os.getenv('BUILD_ID', 'Local')\
\'a0\'a0\'a0 return f"<h1>Hello from Flask!</h1><p>Deployed via Jenkins Webhook. Build ID: \{build_id\}</p>"\
\'a0\
if __name__ == "__main__":\
\'a0\'a0\'a0 app.run(host='0.0.0.0', port=5000)\
}