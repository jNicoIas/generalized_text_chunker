from text_chunking import TextChunker
from core import ChunkerConfig, RecursiveSplitterConfig, RollingWindowConfig, StatisticalConfig
import json
from semantic_router.schema import DocumentSplit


def chunk_thesis_statistical():
    try:
        with open('dataset/thesis.txt', 'r') as file:
            thesis = file.read()
        payload = ChunkerConfig(
            mode                = "statistical",
            text                = thesis,
            page_size           = 4000,
            page_overlap        = 100,
            is_pages_numbered   = False,
            is_pages_enabled    = True,
        )
        payload_statistical = StatisticalConfig(
            min_split_tokens = 50,
            max_split_tokens = 100,
            is_output_chunks = False
        )
        chunker = TextChunker(payload = payload, payload_statistical = payload_statistical)
        paragraph_chunks = chunker.chunk_text()
        
        with open('output/chunk_thesis_450_statistical.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_thesis:",e)


def chunk_thesis_rolling_window():
    try:
        with open('dataset/thesis.txt', 'r') as file:
            thesis = file.read()
        payload = ChunkerConfig(
            mode = "rolling_window",
            text = thesis,
            page_size       = 4000,
            page_overlap    = 100,
            is_pages_numbered  = False,
            is_pages_enabled  = True
        )
        payload_rolling_window = RollingWindowConfig(
            min_split_tokens = 100,
            max_split_tokens = 4000   
        )
        chunker = TextChunker(payload = payload, payload_rolling_window = payload_rolling_window)
        paragraph_chunks = chunker.chunk_text()
        print(paragraph_chunks)
        paragraph_chunks_str = []
        
        with open('output/chunk_thesis_450_rolling.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_thesis:",e)

def chunk_thesis_md():
    try:
        with open('dataset/B1_mock_manuscript.md', 'r') as file:
            B1_mock_manuscript = file.read()
        payload = ChunkerConfig(
            mode = "recursive",
            text = B1_mock_manuscript,
            page_size       = 1000,
            page_overlap    = 50,
            is_pages_numbered  = False,
            is_pages_enabled  = False
        )
        payload_recursive = RecursiveSplitterConfig(
            chunk_size      = 451,
            chunk_overlap   = 50
        )
        chunker = TextChunker(payload = payload, payload_recursive = payload_recursive)
        paragraph_chunks = chunker.chunk_text()
        with open('output/chunk_thesis_md_450.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_md:",e)

def chunk_md():
    try:
        with open('dataset/md.txt', 'r') as file:
            five_mins_transcript = file.read()
        chunker = TextChunker(
            text            = five_mins_transcript,
            chunk_size      = 150,
            chunk_overlap   = 50,
            page_size       = 1000,
            page_overlap    = 50,
            is_pages_numbered  = False,
            is_pages_enabled  = False
        )
        paragraph_chunks = chunker.chunk_text()
        with open('output/chunk_md_150.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_md:",e)

def chunk_thesis():
    try:
        with open('dataset/thesis.txt', 'r') as file:
            thesis = file.read()
        payload = ChunkerConfig(
            mode = "recursive",
            text = thesis,
            page_size       = 1000,
            page_overlap    = 50,
            is_pages_numbered  = False,
            is_pages_enabled  = False
        )
        payload_recursive = RecursiveSplitterConfig(
            chunk_size      = 451,
            chunk_overlap   = 50
        )
        chunker = TextChunker(payload = payload, payload_recursive = payload_recursive)
        paragraph_chunks = chunker.chunk_text()
        with open('output/chunk_thesis_450.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_thesis:",e)

def chunk_five_mins():
    try:
        with open('dataset/5_mins.txt', 'r') as file:
            five_mins_transcript = file.read()
        chunker = TextChunker(
            text            = five_mins_transcript,
            chunk_size      = 451,
            chunk_overlap   = 50,
            page_size       = 1000,
            page_overlap    = 50,
            is_pages_numbered  = True,
            is_pages_enabled  = True
        )
        paragraph_chunks = chunker.chunk_text()
        with open('output/chunk_five_mins.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_five_mins:",e)
        
def chunk_thirty_mins():
    try:
        with open('dataset/30_mins.txt', 'r') as file:
            five_mins_transcript = file.read()
        chunker = TextChunker(
            text            = five_mins_transcript,
            chunk_size      = 451,
            chunk_overlap   = 50,
            page_size       = 1000,
            page_overlap    = 50,
            is_pages_numbered  = True,
            is_pages_enabled  = True
        )
        paragraph_chunks = chunker.chunk_text()
        with open('output/chunk_thirty_mins.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_five_mins:",e)
        
def chunk_one_hour():
    try:
        with open('dataset/1_hr.txt', 'r') as file:
            five_mins_transcript = file.read()
        chunker = TextChunker(
            text            = five_mins_transcript,
            chunk_size      = 451,
            chunk_overlap   = 50,
            page_size       = 1000,
            page_overlap    = 50,
            is_pages_numbered  = True,
            is_pages_enabled  = True
        )
        paragraph_chunks = chunker.chunk_text()
        with open('output/chunk_one_hour.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_one_hour:",e)
        
def chunk_four_hours():
    try:
        with open('dataset/4_hrs.txt', 'r') as file:
            five_mins_transcript = file.read()
        chunker = TextChunker(
            text            = five_mins_transcript,
            chunk_size      = 451,
            chunk_overlap   = 50,
            page_size       = 1000,
            page_overlap    = 50,
            is_pages_numbered  = True,
            is_pages_enabled  = True
        )
        paragraph_chunks = chunker.chunk_text()
        with open('output/chunk_four_hours.json', 'w') as file:
            json.dump(paragraph_chunks, file)
    except Exception as e:
        print("Exception @ chunk_four_hours:",e)
    
         
if __name__ == "__main__":    
    # chunk_five_mins()
    # chunk_thirty_mins()
    # chunk_one_hour()
    # chunk_four_hours()
    # chunk_thesis()
    # chunk_thesis_rolling_window()
    # chunk_md()
    # chunk_thesis_md()
    chunk_thesis_statistical()
    