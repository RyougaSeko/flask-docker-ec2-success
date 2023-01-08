import requests

API_KEY = 'a771d007-d6b5-2e6d-6142-b723dee6d399:fx' # 自身の API キーを指定

def translation(path):

    f = open(path, 'r', encoding="UTF-8")
    text = f.read()
    f.close()

    source_lang = 'EN'
    target_lang = 'JA'

    # パラメータの指定
    params = {
                'auth_key' : API_KEY,
                'text' : text,
                'source_lang' : source_lang, # 翻訳対象の言語
                "target_lang": target_lang  # 翻訳後の言語
            }

    # リクエストを投げる
    request = requests.post("https://api-free.deepl.com/v2/translate", data=params) # URIは有償版, 無償版で異なるため要注意
    result = request.json()['translations'][0]['text']

    return result