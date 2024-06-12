# Text chunker

### 1. How to use the text Chunker?
- Copy the module in your repository. 
- Import the class "TextChunker()"
```
from text_chunker.text_chunking import TextChunker

chunker = TextChunker(
            text            = five_mins_transcript,
            chunk_size      = 451,
            chunk_overlap   = 50,
            page_size       = 1000,
            page_overlap    = 50,
        )
paragraph_chunks = chunker.chunk_text()
```
### 2. Input parameters
***text:***  The transcript or body of text that the TextChunker will process.

***chunk_size:*** The size of each text chunk in characters.

***chunk_overlap:*** The number of characters that will overlap between consecutive text chunks.

***length_function:*** *[opt]* The function used to calculate the length of text chunks; defaults to `tiktoken_len`.

***page_size:*** *[opt]* The size of each page in characters when pagination is enabled; defaults to infinity (no pagination).

***page_overlap:*** *[opt]* The number of characters that will overlap between consecutive pages; defaults to 0.

***is_pages_numbered:*** *[opt]* A boolean indicating whether pages should be numbered; defaults to False.

***is_pages_enabled:*** *[opt]* A boolean indicating whether pagination is enabled; defaults to False.

***mode:*** *[opt]* An optional mode parameter that can be used to specify additional processing behaviors.

### 3. Output

***paragraph_chunks:*** An array of text segments, each representing a coherent chunk of the original input text.

### 4. Other notes:
- The folders "dataset" and "output" are only for testing purposes.
