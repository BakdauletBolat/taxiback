def try_to_string_byte(bytes_data):

    try:
        raw_body = bytes_data.decode('utf8').replace("'", '"')
    except Exception:
        raw_body = bytes_data
    
    return raw_body
