def get_max_tries():
    """プレイヤーに最大挑戦回数を入力してもらい、その値を返す"""
    while True:
        max_tries_input = input("最大挑戦回数を設定してください (1以上の数字 / Enterでデフォルトの5回) > ").strip()
        if max_tries_input == "":
            return 5
        elif max_tries_input.isdigit() and int(max_tries_input) > 0:
            return int(max_tries_input)
        else:
            print("1以上の有効な数値を入力してください。")


def check_game_over(tries, max_tries, secret=None):
    """現在の挑戦回数（tries）が最大制限（max_tries）に達したか判定する"""
    return tries >= max_tries
