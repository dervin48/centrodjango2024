from weasyprint import HTML

HTML(string='<h1>Hello, World!</h1>').write_pdf('output.pdf')
