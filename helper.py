def is_key_or_isbn(word):
    '''q:ISBN,关键字
        page:控制翻页的参数
    '''
    isisbn = 'key'
    if len(word) == 13 and word.isdigit():
        isisbn = 'isbn'
    pass