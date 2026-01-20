import os

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from typing import List



### PDF 読み込み
def load_pdf(file_path: str):
    
    if not os.path.exists(file_path):
        raise FileNotFoundError("ファイルパスが不正")

    try:
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        print(f"documents: {documents}")
        
        return documents
    
    except Exception as e:
        print(f"An error occurred while loading the PDF: {e}")
        raise e
    
# チャンク分割
def split_docs(
    documents: List[Document],
    chunk_size: int = 500,
    chunk_overlap: int = 50
) -> List[Document]:
    separators = [
        "\n\n", # 段落区切り
        "\n",   # 改行
        "。",   # 句点
        "、",   # 読点
        " ",    # スペース
        ""      # 最終手段：文字単位
    ]
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=separators
    )
    
    split_docs = text_splitter.split_documents(documents)
    return split_docs
    
# PDF オブジェクト取得    
documents = load_pdf("sample.pdf")

chunks = split_docs(documents, chunk_size=500, chunk_overlap=50)
for i, chunk in enumerate(chunks):
    print(f"Chunk {i + 1}:\n{chunk.page_content}\n")
    print(f"Metadata: {chunk.metadata}\n")

#for doc in documents:
#        print(f"Page content: {doc.page_content}")
#        print(f"Metadata: {doc.metadata}")
        
  


