import os
from fpdf import FPDF

class PdfFile:
    OUTPUT_FOLDER = "FilesPDF"

    @staticmethod
    def _next_name():
        files = os.listdir(PdfFile.OUTPUT_FOLDER)
        max_file = 0
        for file in files:
            current_file_number = int(file.title().upper().replace("DATABASE_(", "").replace(").PDF", ""))
            max_file = max(max_file, current_file_number)
        max_file = max_file + 1
        return 'Database_(%s).pdf' % max_file

    @staticmethod
    def save(results):
        if not os.path.exists(PdfFile.OUTPUT_FOLDER):
            os.mkdir(PdfFile.OUTPUT_FOLDER)

        pdf = FPDF('P', 'mm', 'A4')
        filename = PdfFile.OUTPUT_FOLDER + "/" + PdfFile._next_name()
        pdf.add_font("timesnewromanpsmt", "", "timesnewromanpsmt.ttf", uni=True)
        pdf.set_font('timesnewromanpsmt', '', 13)
        pdf.add_page()
        for result in results:
            (book_id, book) = result
            formatted_book = "%s: %s, %s, %s год" % (book_id, book.author, book.title, book.year)
            print(formatted_book)
            pdf.write(8, formatted_book)
            pdf.ln(8)
        pdf.output(filename, 'F')
        pdf.close()

    @staticmethod
    def save_pdf(result):
        PdfFile.save([result])