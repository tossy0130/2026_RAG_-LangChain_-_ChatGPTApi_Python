from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    length_function=len,
    separators=["\n\n", "\n", "。","、"," ",""]
)

# サンプルテキスト
long_text = """
以下は、テスト用に十分長い日本語テキストの例です。split_chunk.pyのtext変数に代入して使ってください。

例：
これはテスト用の長い文章です。LangChainのテキスト分割機能を試すために、いくつかの文を続けて書いています。AI技術は日々進化しており、さまざまな分野で活用されています。例えば、自然言語処理や画像認識、音声認識などがあります。LangChainは、ドキュメント検索やチャットボットの開発に役立つ強力なツールです。テキストを適切な長さに分割することで、効率的な情報検索や処理が可能になります。Pythonはそのようなタスクを簡単に実装できる人気のプログラミング言語です。今後もAIの発展に注目していきたいと思います。
このテキストをtext変数に代入して、分割結果を確認してみてください。必要に応じてさらに文章を追加することもできます。
"""

# チャンク取得
chunks = text_splitter.split_text(long_text)

# チャンク出力
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}: \n{chunk}\n")
    

