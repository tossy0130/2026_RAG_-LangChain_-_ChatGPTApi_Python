import os
from dotenv import load_dotenv # .env 読み込み

# .env ファイルから環境変数を読み込み
load_dotenv()

# 環境変数から、取得して 変数へ格納
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if not OPENAI_API_KEY:
    raise ValueError("OpenAi API Key is not set. " \
                     "Please set the OPENAI_API_KEY environment variable.")
print(f"open api key: {OPENAI_API_KEY}")