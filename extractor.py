from pdftextract import XPdf


def extract(file_path):
    try:
        pdf = XPdf(file_path)
        txt = pdf.to_text()
        return txt
    except:
        return "An error occurred while trying to extract the pdf"
