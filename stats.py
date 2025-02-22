def get_num_words(book):
    with open(book) as f:
        file_contents = f.read()
    total_count = len(file_contents.split())
    return(total_count)