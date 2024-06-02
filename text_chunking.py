from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils import tiktoken_len, check_required_kwargs, check_chunk_size, check_chunk_vs_page_size
from helpers import get_pages
from concurrent.futures import ThreadPoolExecutor
import json


class TextChunker:
    def __init__(self, **kwargs):

        self.kwargs                 = kwargs
        self.text                   = kwargs.get("text")
        
        self.chunk_size             = kwargs.get("chunk_size")
        self.chunk_overlap          = kwargs.get("chunk_overlap")
        self.length_function        = kwargs.get("length_function", tiktoken_len)
        
        self.page_size              = kwargs.get("page_size", float("inf"))
        self.page_overlap           = kwargs.get("page_overlap", 0)
        self.is_pages_numbered      = kwargs.get("is_pages_numbered", False)
        self.is_pages_enabled       = kwargs.get("is_pages_enabled", False)
        
        self.mode                   = kwargs.get("mode", "")
        self.__validate_input()  
        
        
        
    def __validate_input(self):
        check_required_kwargs(self.kwargs)
        check_chunk_size(self.chunk_size)
        check_chunk_vs_page_size(self.chunk_size, self.page_size)
               
    def __chunk_texts_per_page(self, page):
        try:
            text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size      = self.chunk_size,
                    chunk_overlap   = self.chunk_overlap,
                    length_function = self.length_function,
                    )
            chunks = text_splitter.split_text(page)
            return chunks
        except Exception as e:
            print("Exception @ __chunk_texts_per_page:", e)

    def chunk_text(self):
        try:
            pages = get_pages(
                    text            = self.text,
                    chunk_size      = self.page_size if self.is_pages_enabled else float("inf"),
                    chunk_overlap   = self.page_overlap,
                    length_function = self.length_function,
                    numbered_pages  = self.is_pages_numbered
                    )
            
            paragraph_chunks = []
            for page in pages:
                paragraph_chunks.extend(self.__chunk_texts_per_page(page))
                
            return paragraph_chunks
        except Exception as e:
            print("Exception @ chunk_text:", e)

        
            
            
        
        
        
        