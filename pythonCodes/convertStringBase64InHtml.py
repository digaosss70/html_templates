import base64

def base64_to_html(base64_string):
    # Decodifica a string base64
    html_content = base64.b64decode(base64_string).decode('utf-8')
    print(html_content)

# Exemplo de uso
base64_string = inputs['base64_string']
base64_to_html(base64_string)