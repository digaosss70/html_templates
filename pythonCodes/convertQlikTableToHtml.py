import json

def json_to_html_table(json_data):
    # Carregar dados JSON
    data = json_data
    
    if not data:
        return "<p>Sem dados para exibir.</p>"

    # Começo da tabela HTML
    html = '<table border="1" style="border-collapse: collapse; width: 100%;">'
    
    # Cabeçalho da tabela
    html += '<thead><tr>'
    for key in data[0].keys():
        html += f'<th scope="col" style="-moz-box-sizing: border-box; -webkit-box-sizing: border-box; box-sizing: border-box; text-align: left; padding: 10px; font-weight: 600; background: #009845; color: #FFF;">{key}</th>'
    html += '</tr></thead>'
    
    # Corpo da tabela
    html += '<tbody>'
    for item in data:
        html += '<tr>'
        for value in item.values():
            html += f'<td style="text-align: left; padding: 8px; border: 1px solid #ddd; background: #f9f9f9;">{value}</td>'
        html += '</tr>'
    html += '</tbody>'
    
    # Fim da tabela
    html += '</table>'
    
    return html

# Exemplo de dados JSON
json_data = inputs['tabela']

# Gerar HTML da tabela
html_table = json_to_html_table(json_data)

# Exibir o HTML (ou você pode salvar em um arquivo)
print(html_table)
