from text_chunking import TextChunker
import json


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
    chunk_five_mins()
    chunk_thirty_mins()
    chunk_one_hour()
    chunk_four_hours()
