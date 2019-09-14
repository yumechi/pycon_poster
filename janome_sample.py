from janome.tokenizer import Tokenizer

t = Tokenizer()
s = """
問題意識


初心者はAnacondaでの環境構築に触れる機会が多い

それに対して、Pythonista全員がAnacondaの知識があるわけではない（そのため初心者からのAnacondaの質問に答えられないこともある）

また、ネット上のPython環境構築情報には、Anacondaで環境構築した後、パッケージをpip installさせるという危険な手順が散見される


問題を解決する方法


本トークで初心者にはAnacondaの環境構築のTIPSを伝え、そもそもAnacondaの質問が発生しにくくする（危険な手順の問題にもアプローチ）

加えて、中級者・上級者にはAnacondaの質問に回答するためのよりどころとなる情報を提供する


Anacondaを排除するのではなく、一つの選択肢として残し、環境構築方法の多様性を保ちたいという意図です。
Anacondaという題材については、全Pythonistaが知るべきと考えています。


トークの流れ（案）

日本語を予定しています。
※現時点の考えのため、今後の調査・検証によって変更になる可能性があります



Anacondaとは

問題意識の共有（Anacondaの環境構築方法は広く知られていないために上記のような問題があります）

Anaconda環境の運用TIPS（検証結果次第ですが、condaでPythonのバージョンを分離し、venvで仮想環境構築、pipでパッケージ管理と伝える予定です）

時間の許す限り、裏付けの話（condaコマンドやvenvモジュールで何が行われているのか、conda installとpip installの仕組み、など）


Anacondaとpython.orgからインストールしたPythonを取り上げる理由

この記載は、homebrewやpyenvなどを取り上げない理由の説明でもあります



各種チュートリアルでよく案内される方法がpython.orgからのインストール（Django Girls TutorialやPyNyumonテキスト、pycampテキスト）

日本語の入門書はAnacondaで環境構築する本が増えている印象（入門者とAnacondaの接点が多いと考えている）

→この2つにより、Anacondaとpython.orgからインストールしたPythonが併用されてしまう

JetBrainsのPythonについてのsurvey (2018)では、python.orgが2位、Anacondaが3位

（1位はbrewやaptでのインストールですが、入門者はWindowsかMacを使うことが多い印象なので、それらに関わりが深い2位と3位を取り上げます）
"""

nouns = []
for token in t.tokenize(s):
    if token.part_of_speech.split(',')[0] == '名詞':
            nouns.append(token.base_form)
print('\n'.join(nouns))
