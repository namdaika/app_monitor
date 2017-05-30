# -*- coding: utf-8 -*-
# Author: Nam Nguyen Hoai
import requests

IP_SEND = 'http://113.190.232.90:3333'
IP_LOCAL = 'http://113.190.232.90:3333'


def get_content_from_server():
    raw_response = requests.get(IP_LOCAL).content
    list_response = raw_response.split(b'\n')[1]
    final_response = list_response.split(b'<br>')[0]
    return str(final_response, encoding='utf-8')

