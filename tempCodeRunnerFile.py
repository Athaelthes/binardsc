def text_clean():
    json_response = {
        'status_code': 200,
        'description': "Original Teks",
        'data': re.sub(r'[^a-zA-z0-9]',' ',"Halo, apa kabar semua?"),