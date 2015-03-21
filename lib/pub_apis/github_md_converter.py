# coding: utf8
import requests
import json

API_HOST = 'https://api.github.com/markdown'
LOCAL_MARKDOWN_HOST = 'http://127.0.0.1:17900/md'

def get_md_doc_from_raw(text, mode='gfm'):

    try:
        params = {
            'text': text,
            'mode': mode,
            'context': 'github/gollum',
        }
        r = requests.post(API_HOST, data=json.dumps(params))
        if r:
            return r.text
        else:
            return ''
    except Exception, e:
        print e


def get_raw_from_md_doc(params):
    host = API_HOST + '/raw'
    try:
        r = requests.post(host, data=json.dumps(params))
        if r:
            return r.text
        else:
            return ''
    except Exception, e:
        print e


def get_md_doc_from_marked(text, mode='gfm'):
    try:
        params = {
            'text': text,
            # 'mode': mode,
            # 'context': 'github/gollum',
        }
        r = requests.post(LOCAL_MARKDOWN_HOST, data=json.dumps(params))
        if r:
            print r
            print r.text
            return r.text
        else:
            return ''
    except Exception, e:
        print e

if __name__ == '__main__':
    # x = get_md_doc_from_raw(**{
    #     # 'text': "Hello world github/linguist#1 **cool**, and #1!",
    #     'text': """```html
    #             <link rel="stylesheet" href="bower_components/highlightjs/styles/github.css">
    #             <link rel="stylesheet" href="css/github-style.css">
    #             ```""",
    #     "mode": "gfm",
    #     # "context": "github/gollum"
    # })
    # print x

    # a = get_md_doc_of_highlight(text='I am using __markdown__.')
    # b = get_md_doc_from_raw(text="""```html
    # <DOCTYPE html>
    # <html>
    # </html>
    # ```""")
    # print b
    a = get_md_doc_from_marked(text="""```html
    <DOCTYPE html>
    <html>
    </html>
    ```""")
