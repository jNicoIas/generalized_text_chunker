from langchain.text_splitter import RecursiveCharacterTextSplitter
from semantic_router.splitters import RollingWindowSplitter
from core import ChunkerConfig, RecursiveSplitterConfig, RollingWindowConfig
from utils import tiktoken_len

def get_pages(payload:ChunkerConfig, payload_recursive:RecursiveSplitterConfig, payload_rolling_window:RollingWindowConfig):
    try:
       
        text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size      = payload.page_size if payload.is_pages_enabled else 1_000_000_000_000,
                        chunk_overlap   = payload.page_overlap,
                        length_function = tiktoken_len,
                        add_start_index = True,  # Marker to add page start index
                        )
        chunks = text_splitter.split_text(payload.text)
    
        if payload.is_pages_numbered:
            pages = [f"###PAGE {str(index + 1)} START### {page} ###PAGE {str(index + 1)} END###" for index, page in enumerate(chunks)]
        else:
            pages = chunks
    
        return pages
    except Exception as e:
        print("Exception @ get_pages:", e)
    return []