import sys
from PyPDF2 import PdfReader, PdfWriter

def parse_page_numbers(page_numbers_str: str) -> list:
    page_numbers = set()

    for part in page_numbers_str.split(','):

        if '-' in part:
            start, end = map(int, part.split('-'))
            page_numbers.update(range(start, end + 1))

        else:
            page_numbers.add(int(part))

    return [page - 1 for page in page_numbers]

def delete_pages_from_pdf(input_pdf_path: str, 
                          output_pdf_path: str, 
                          pages_to_delete: list) -> None:
    
    pdf_reader = PdfReader(input_pdf_path)
    pdf_writer = PdfWriter()

    for page_num, page in enumerate(pdf_reader.pages):
        if page_num not in pages_to_delete:
            pdf_writer.add_page(page)

    with open(output_pdf_path, 'wb') as out:
        pdf_writer.write(out)


def print_help():
        print("Usage:\n\tpython3 <input file> <output file> <page numbers to delete (comma and dash separated)>")
        print("Использование:\n\tpython3 <входной файл> <выходной файл> <номера страниц для удаления (через запятую и тире)>")

        exit(-1)


if __name__ == "__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        print_help()

    try:
        input_pdf_path = sys.argv[1]
        output_pdf_path = sys.argv[2]
        page_numbers_str = sys.argv[3]

    except Exception:
        print_help()

    try:
        pages_to_delete = parse_page_numbers(page_numbers_str)
    except Exception:
        print("Error parsing the list of numbers to delete.")
        print("Ошибка ввода удаляемых страниц.")
        print_help()

    try:
        delete_pages_from_pdf(input_pdf_path, output_pdf_path, pages_to_delete)
    except Exception:
        print("An error occurred while deleting pages from PDF file.")
        print("Произошла ошибка при удалении страниц из файла PDF.")
