def get_url_string(author, start_index, max_results):
    url = "https://www.googleapis.com/books/v1/volumes"
    fields = "&fields=totalItems,items(id,volumeInfo(title,subtitle,authors,publishedDate,imageLinks/thumbnail))"
    query = f"?q={author}+inauthor&startIndex={start_index}&maxResults={max_results}&printType=books"
    return (url+query+fields).strip()
