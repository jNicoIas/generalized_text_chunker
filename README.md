# Text chunker

### 1. How to use the text Chunker?
- Copy the module in your repository. 
- Import the class "TextChunker()"
- Import the configuration classes for the input ChunkerConfig, RecursiveSplitterConfig, RollingWindowConfig
    - ChunkerConfig is for the general configuration for different chunkers
    - RecursiveSplitterConfig and RollingWindowConfig are chunker-specific configurations
**Sample Rolling Window Usage**
```
from text_chunker.text_chunking import 
from core import ChunkerConfig, RecursiveSplitterConfig, RollingWindowConfig


payload = ChunkerConfig(
    mode = "rolling_window",
    text = thesis,
    page_size       = 4000,
    page_overlap    = 100,
    is_pages_numbered  = True,
    is_pages_enabled  = True
)
payload_rolling_window = RollingWindowConfig(
    min_split_tokens = 50,
    max_split_tokens = 4000   
)
chunker = TextChunker(payload = payload, payload_rolling_window = payload_rolling_window)
paragraph_chunks = chunker.chunk_text()
```
**Sample Recursive Splitter Usage**
```
from text_chunker.text_chunking import 
from core import ChunkerConfig, RecursiveSplitterConfig, RollingWindowConfig, TextChunker
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
