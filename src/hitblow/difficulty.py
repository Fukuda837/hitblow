"""難易度（桁数）を選択する機能"""

def ask_digits(default_digits):
    """ユーザーに桁数を変更するか確認し、変更する場合は入力させる関数"""
    
    # 1. まず、桁数を変更するかどうか（Yes/No）を聞く
    print(f"\n現在の設定は【 {default_digits} 桁】です。")
    change = input("桁数（難易度）を変更しますか？ (y / Enterでそのままスタート) > ").strip().lower()

    # 'y' 以外（Enterキーなど）が押された場合は、変更せずにそのまま返す
    if change != 'y':
        return default_digits

    # 2. 'y' が押された場合のみ、希望の桁数を聞く
    while True:
        ans = input("何桁で遊びますか？ (1〜10の数字を入力) > ").strip()
        
        # 1〜10の数字が入力されたかチェック
        if ans.isdigit() and 1 <= int(ans) <= 10:
            return int(ans)
            
        print("※ 1〜10の正しい数字で入力してください。")