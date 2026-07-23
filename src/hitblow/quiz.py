"""突発4択クイズ機能"""

import random
from .core import make_secret  # ★ 新しい答えを作るために追加

# ★ クイズの問題データ。後からここを編集するだけで簡単に問題を増やせます！
QUIZZES = [
    {
        "question": "プログラミング言語「Python」の名前の由来は？",
        "choices": ["1. 蛇の種類", "2. コメディ番組", "3. 車の名前", "4. 開発者のペット"],
        "answer": "2"
    },
    {
        "question": "日本の初代内閣総理大臣は誰？",
        "choices": ["1. 伊藤博文", "2. 大隈重信", "3. 板垣退助", "4. 西郷隆盛"],
        "answer": "1"
    },
    {
        "question": "次のうち、一番大きい動物は？",
        "choices": ["1. アフリカゾウ", "2. シロナガスクジラ", "3. キリン", "4. カバ"],
        "answer": "2"
    },
    {
        "question": "遣唐使を廃止したのは誰？",
        "choices": ["1. 藤原道長", "2. 平清盛", "3. 源頼朝", "4. 菅原道真"],
        "answer": "4"
    },
    {
        "question": "安土桃山時代に天下統一を成し遂げたのは誰？",
        "choices": ["1. 徳川家康", "2. 武田信玄", "3. 豊臣秀吉", "4. 織田信長"],
        "answer": "3"
    },
    {
        "question": "日本で最も人口の多い市区町村は？",
        "choices": ["1. 横浜市", "2. 名古屋市", "3. 大阪市", "4. 広島市"],
        "answer": "1"
    },
    {
        "question": "次のうち、EU(欧州連合)に加盟していない国は？",
        "choices": ["1. フランス", "2. イタリア", "3. スペイン", "4. ノルウェー"],
        "answer": "4"
    },
    {
        "question": "平城京に遷都したのはいつ？",
        "choices": ["1. 710", "2. 794", "3. 645", "4. 749"],
        "answer": "1"
    }
]

def check_quiz(secret, digits):  # ★ 引数に secret と digits を追加
    """
    3分の1の確率でクイズを出題する。
    発動した場合は、正解するまで別々のクイズを出題し続ける。
    1回でも間違えると、Hit & Blowの答えが変更されるペナルティが発生する。
    """
    # 1〜3のランダムな数字を作り、1以外なら何もしない（約33%の確率で発動）
    if random.randint(1, 3) != 1:
        return secret  # ★ 何も起きなかった場合は元の答えをそのまま返す

    print("\n🚨 【突発イベント】Hit & Blowの判定に進むには、クイズに正解する必要があります！")
    
    last_quiz = None  # 直前に出題した問題を記憶する変数
    mistake_made = False  # ★ 既に間違えてペナルティを受けたかを記録
    
    while True:
        # 問題を選ぶ（前回と同じ問題が連続で出ないようにする工夫）
        if last_quiz is not None and len(QUIZZES) > 1:
            # 前回出た問題「以外」のリストを作って、そこから選ぶ
            candidates = [q for q in QUIZZES if q != last_quiz]
            q = random.choice(candidates)
        else:
            q = random.choice(QUIZZES)
            
        print(f"\n問題: {q['question']}")
        for choice in q['choices']:
            print(f"  {choice}")
            
        ans = input("答えを番号(1〜4)で入力 > ").strip()
        
        if ans == q['answer']:
            print("⭕ 正解！ 予想した数字の Hit & Blow 判定に進みます。\n")
            break  # 正解したらループを抜けて、ゲームに戻る
        else:
            print("❌ 不正解！ 正解するまで戻れません。次の問題いきます！")
            
            # ★ 1回目の不正解時に答えをランダムに変更する処理
            if not mistake_made:
                print("⚠️ 【ペナルティ】Hit & Blowの正解の数字がランダムに変更されました！")
                secret = make_secret(digits)
                mistake_made = True  # ペナルティ実行済みにする
                
            last_quiz = q  # 今出題した問題を記録して、次は違う問題が出るようにする

    return secret  # ★ 最終的な答え（変更されたか、元のままか）をゲームに返す