from sambanova import SambaNova
from config import API_KEY, BASE_URL

def get_client():
    return SambaNova(
        api_key=API_KEY,
        base_url=BASE_URL,
    )
