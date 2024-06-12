from decouple import config

OPENAI_API_KEY: str=config("OPENAI_API_KEY", cast=str) # type: ignore