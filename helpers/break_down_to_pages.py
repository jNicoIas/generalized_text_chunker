from langchain.text_splitter import RecursiveCharacterTextSplitter

def get_pages(text, chunk_size, chunk_overlap, length_function, numbered_pages):
    try:
        text_splitter = RecursiveCharacterTextSplitter(
                        chunk_size      = chunk_size,
                        chunk_overlap   = chunk_overlap,
                        length_function = length_function,
                        add_start_index = True,  # Marker to add page start index
                        )
        if numbered_pages:
            pages = [f"###PAGE {str(index + 1)} START### {page} ###PAGE {str(index + 1)} END###" for index, page in enumerate(text_splitter.split_text(text))]
        else:
            pages = text_splitter.split_text(text)
    
        return pages
    except Exception as e:
        print("Exception @ get_pages:", e)