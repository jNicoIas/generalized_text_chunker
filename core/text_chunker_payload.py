from typing import NamedTuple, Callable
from utils import tiktoken_len
from semantic_router.encoders import OpenAIEncoder
from .constants import OPENAI_API_KEY


class ChunkerConfig(NamedTuple):
    mode: str               = "recursive"
    text: str               = None # type: ignore
    page_size: int          = 1_000_000_000_000
    page_overlap: int       = 0
    is_pages_numbered: bool = False
    is_pages_enabled: bool  = False
        
class RecursiveSplitterConfig(NamedTuple):
    chunk_size: int             = None # type: ignore
    chunk_overlap: int          = None # type: ignore
    length_function: Callable   = tiktoken_len
        
class RollingWindowConfig(NamedTuple):
    encoder: OpenAIEncoder      = OpenAIEncoder(name="text-embedding-3-small", openai_api_key=OPENAI_API_KEY)
    min_split_tokens: int       = 50
    max_split_tokens: int       = 4000
    window_size: int            = 2
    plot_splits: bool           = False  # set this to true to visualize chunking
    enable_statistics: bool     = False  # to print chunking stats
    
    
class StatisticalConfig(NamedTuple):
    encoder: OpenAIEncoder      = OpenAIEncoder(name="text-embedding-3-small", openai_api_key=OPENAI_API_KEY)
    min_split_tokens: int       = 50
    max_split_tokens: int       = 4000
    split_tokens_tolerance: int = 10
    
