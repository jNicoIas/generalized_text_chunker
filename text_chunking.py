from langchain.text_splitter import RecursiveCharacterTextSplitter
from utils import tiktoken_len, check_required_kwargs, check_chunk_size, check_chunk_vs_page_size
from helpers import get_pages
from getpass import getpass
import traceback
from semantic_router.encoders import OpenAIEncoder
from semantic_router.splitters import RollingWindowSplitter
from semantic_router.utils.logger import logger
from core import ChunkerConfig, RecursiveSplitterConfig, RollingWindowConfig
import sys

import json

class TextChunker:
    def __init__(self, 
                 payload:                   ChunkerConfig, 
                 payload_recursive:         RecursiveSplitterConfig = None,  # type: ignore
                 payload_rolling_window:    RollingWindowConfig = None): # type: ignore
        self.payload                = payload
        self.payload_recursive      = payload_recursive
        self.payload_rolling_window = payload_rolling_window
        self.__validate_input()   
    
    def __validate_input(self):
        if self.payload.mode == "recrusive":
            check_chunk_size(self.payload_recursive.chunk_size)
            check_chunk_vs_page_size(self.payload_recursive.chunk_size, self.payload.page_size)
               
    def __chunk_texts_per_page(self, page):
        try:
            # print(page, "\n")
            if self.payload.mode == "recursive":
                text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size      = self.payload_recursive.chunk_size,
                        chunk_overlap   = self.payload_recursive.chunk_overlap,
                        length_function = self.payload_recursive.length_function,
                        )
                chunks = text_splitter.split_text(page)
                return chunks
            if self.payload.mode == "rolling_window":
                text_splitter = RollingWindowSplitter(
                encoder             =self.payload_rolling_window.encoder,
                dynamic_threshold   =True,
                min_split_tokens    =self.payload_rolling_window.min_split_tokens,
                max_split_tokens    =self.payload_rolling_window.max_split_tokens,
                window_size         =self.payload_rolling_window.window_size,
                plot_splits         =self.payload_rolling_window.plot_splits, 
                enable_statistics   =self.payload_rolling_window.enable_statistics  
            )
                chunks = text_splitter([page])
                chunks = list(map(lambda v: v.content, chunks))
                
                
                return chunks
        except Exception as e:
            print("Exception @ __chunk_texts_per_page:", e)
        return []

    def chunk_text(self):
        try:
            pages = get_pages(
                    self.payload,
                    self.payload_recursive,
                    self.payload_rolling_window
                    )
            paragraph_chunks = []
            for page in pages:    
                             
                paragraph_chunks.extend(self.__chunk_texts_per_page(page))
            [print(paragraph_chunk, "\n\n") for paragraph_chunk in paragraph_chunks]
            return paragraph_chunks
        except Exception as e:
            print("Exception @ chunk_text:", e)

        
            
            
        
        
        
        