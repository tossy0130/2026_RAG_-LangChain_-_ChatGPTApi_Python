from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document

import config

# テキストをベクトル化する
embeddings = OpenAIEmbeddings()

def insert_document():
    
     documents = [
        # プログラミング関連
        Document(page_content="Pythonでデータ分析を行う方法", metadata={"category": "programming", "difficulty": "beginner"}),
        Document(page_content="JavaScriptでウェブアプリケーション開発", metadata={"category": "programming", "difficulty": "intermediate"}),
        Document(page_content="機械学習のアルゴリズム実装とPythonライブラリ", metadata={"category": "programming", "difficulty": "advanced"}),
        Document(page_content="SQLデータベース設計の基礎", metadata={"category": "programming", "difficulty": "beginner"}),
        
        # 料理関連
        Document(page_content="簡単な和食の作り方とレシピ", metadata={"category": "cooking", "difficulty": "beginner"}),
        Document(page_content="イタリアンパスタの本格的な調理法", metadata={"category": "cooking", "difficulty": "intermediate"}),
        Document(page_content="フランス料理のソース作りとテクニック", metadata={"category": "cooking", "difficulty": "advanced"}),
        Document(page_content="健康的な野菜サラダのレシピ集", metadata={"category": "cooking", "difficulty": "beginner"}),
        
        # スポーツ関連
        Document(page_content="サッカーの基本ルールと戦術", metadata={"category": "sports", "difficulty": "beginner"}),
        Document(page_content="テニスのサーブ技術向上方法", metadata={"category": "sports", "difficulty": "intermediate"}),
        Document(page_content="マラソンのトレーニング計画と栄養管理", metadata={"category": "sports", "difficulty": "advanced"}),
        Document(page_content="バスケットボールのシュート練習法", metadata={"category": "sports", "difficulty": "intermediate"}),
        
        # 旅行関連
        Document(page_content="東京の人気観光スポットガイド", metadata={"category": "travel", "difficulty": "beginner"}),
        Document(page_content="ヨーロッパ周遊旅行の計画方法", metadata={"category": "travel", "difficulty": "intermediate"}),
        Document(page_content="バックパッカーのための節約旅行術", metadata={"category": "travel", "difficulty": "advanced"}),
        Document(page_content="温泉地での癒し旅行プラン", metadata={"category": "travel", "difficulty": "beginner"}),
     ]

     # ベクトルストア　 データ保存処理
     vectorstore = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory="./chroma_db",
     )
     
### データ検索　###
def search_documents(query: str):
    vectorstore = Chroma(
        embedding_function=embeddings,
        persist_directory="./chroma_db",
    )

    # k = 検索結果数
    results = vectorstore.similarity_search_with_score(query, k=10)
    
    return results

# データ保存
insert_document()

# 検索
results = search_documents("Python")

# score　=> 類似性
for index, (doc, score) in enumerate(results):
    print(f"Result {index + 1}:")
    print(f"Content: {doc.page_content}")
    print(f"Metadata: {doc.metadata}")
    print(f"Score: {score}\n")
    
    
