import os

from langchain.document_loaders import PyPDFLoader


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
    
    
# PDF オブジェクト取得    
documents = load_pdf("sample.pdf")

for doc in documents:
        print(f"Page content: {doc.page_content}")
        print(f"Metadata: {doc.metadata}")
        
  


