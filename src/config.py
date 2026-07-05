from dataclasses import dataclass 
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Config:
    """项目配置"""
    api_key: str
    base_url: str
    model: str

def _load_config() -> Config:
    """从.env文件加载配置"""

    api_key = os.getenv("API_KEY")
    base_url = os.getenv("BASE_URL")
    model = os.getenv("MODEL")

    if not api_key:
        raise ValueError("API_KEY is missing.")
    if not base_url:
        raise ValueError("BASE_URL is missing.")
    if not model:
        raise  ValueError("MODEL is missing.")
    
    return Config(api_key=api_key, base_url=base_url, model=model)

config =_load_config()