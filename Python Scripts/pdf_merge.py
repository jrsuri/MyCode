import PyPDF2

merger = PyPDF2.PdfMerger()

path = 'C:/Users/jrsur/OneDrive/Documents/Documentos/WEG/Documentos/'
pdfs = ['Certidão Graduação.pdf',
        'Histórico.pdf',
        'Protocolo.pdf']

# Iterar através dos arquivos e adicioná-los ao objeto merger
for pdf in pdfs:
    pdf = path + pdf
    with open(pdf, 'rb') as file:
        merger.append(file)

# Escrever o PDF combinado em um novo arquivo
with open(path + 'out.pdf', 'wb') as file:
    merger.write(file)

# Fechar o objeto merger
merger.close()