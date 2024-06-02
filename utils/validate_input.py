def check_required_kwargs(kwargs):
    required_kwargs = ['text', 'chunk_size', 'chunk_overlap']
    for kwarg in required_kwargs:
        if kwarg not in kwargs:
            raise ValueError(f"Missing required argument: {kwarg}")
        
def check_chunk_size(chunk_size):
    if chunk_size < 450:
        raise ValueError(f"Chunk size should be greater than 450 to maintain high quality semantic meaning")

def check_chunk_vs_page_size(chunk_size, page_size):
    if chunk_size > page_size:
        raise ValueError(f"Page size should be greater than Chunk size")
