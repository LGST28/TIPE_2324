import os
import tabula
import pandas as pd
from PyPDF2 import PdfFileReader


def extract_information_from_pdf(pdf_file, start_page, end_page):
    pdf = PyPDF2.PdfFileReader(open(pdf_file, 'rb'))

    data = []
    for page_number in range(start_page - 1, end_page):
        page = pdf.getPage(page_number)
        text = page.extractText()
        lines = text.split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith('Homme_') or line.startswith('Femme_'):
                sport, categorie = line.split('_')
            elif line.startswith('#'):
                continue
            elif line:
                values = line.split('\t')
                date = values[1]
                heure_debut = values[2]
                heure_fin = values[3]
                localisation = values[4]
                nationalites_equipes = values[5]
                data.append([sport, categorie, date, heure_debut, heure_fin, localisation, nationalites_equipes])

    df = pd.DataFrame(data, columns=["Sport", "Catégorie", "Date", "Heure de début", "Heure de fin", "Localisation", "Nationalités / Équipes"])
    return df

def create_excel_file(df, output_file):
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']
    worksheet.autofilter(0, 0, df.shape[0], df.shape[1]-1)
    writer.save()

def main():
    pdf_file = "/Users/lg/Documents/Prépa /TIPE /Organisation jeux olympiques.pdf"
    start_page = 4
    end_page = 95
    output_file = "/Users/lg/Documents/Prépa /TIPE /Fonctions Python/Excels créés/Test fonction.xlsx"

    df = extract_information_from_pdf(pdf_file, start_page, end_page)
    create_excel_file(df, output_file)
    print("Extraction des informations terminée. Le fichier Excel a été créé.")

if __name__ == "__main__":
    main()
