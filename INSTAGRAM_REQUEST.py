import requests
import json


headers = {"origin": "https://www.instagram.com",
"referer": "https://www.instagram.com/",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63"}


def get_hash(link):
    USERNAME = link.split('/')[-2]
    s.get(link)
    var = s.get('https://www.instagram.com/static/bundles/metro/Consumer.js/5d2c1365b382.js')
    HASH = [x for x in var.text.split(',') if "queryId:" in x][5].split('"')[1]
    s.close()
    return HASH, USERNAME


def scrap(rota):
    global alll
    
    quantidade = 100
    url = f"""https://www.instagram.com/graphql/query/?query_hash={HASH}&variables=%7B%22shortcode%22%3A%22{USERNAME}%22%2C%22first%22%3A{quantidade}%2C%22after%22%3A%22{rota}%22%7D"""
    parse = json.loads(requests.get(url, headers=headers).text)
    textos = [x['node']['text'] for x in parse['data']['shortcode_media']['edge_media_to_parent_comment']['edges']]

    for x in textos:
        print('--->', x)
        alll.append(x)
        
    nextpage = parse['data']['shortcode_media']['edge_media_to_parent_comment']['page_info']['end_cursor']
    scrap(nextpage)


s = requests.Session()
HASH, USERNAME = get_hash('https://www.instagram.com/p/CJARH6JnTsu/')
alll = []

try:
    scrap('QVFCWWxBSk5wVjJXLS1YbC1Fb1pGclJaU0VBTUlydm1pdHRkWE9UQUtyaThvZU5ZLU9sUlo3TnRXVFhENE9SNy0tUUVkYzhIcGU2Ynl2Sm53TEtvUkFVMg==')
except:
    print(len(alll))
