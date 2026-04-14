from weasyprint import HTML

def generar_pdf(html):
    return HTML(string=html).write_pdf()