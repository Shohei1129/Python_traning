# 天気を受けとってどの傘を持つかを判別する関数
def whichUmbrella(weather):
    # 荷物
    baggage = ['wallet']

    # もし雨なら荷物に傘を追加
    if weather == 'rain':
        baggage.append('umbrella')
    # もし晴れなら荷物に日傘を追加
    elif weather == 'sunny':
        baggage.append('parasol')

    # 戻り値として荷物を返す
    return baggage

# 関数を実行する
baggage = whichUmbrella('sunny')

print(baggage)