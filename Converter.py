from PyPDF2 import PdfReader
from enum import Enum
from docx import Document
from odf.opendocument import OpenDocumentText
from odf.text import P

class FileTypes(Enum):
    DOCX = 1
    ODT = 2


def extractContent(filePath: str) -> str:
    """Extracts the content from the PDF file"""
    text = ""
    with open(filePath, "rb") as file:
        reader = PdfReader(file)
        for pageNumber in range(len(reader.pages)):
            page = reader.pages[pageNumber]
            text += page.extract_text()
    return text


def createDOCX(content: str, customPath: str) -> None:
    """Generates a DOCX file"""
    doc = Document()
    doc.add_paragraph(content)
    doc.save(customPath)


def createODT(content: str, customPath: str) -> None:
    """Generates a ODT file"""
    paragraph = P(text = content)
    doc = OpenDocumentText()
    doc.text.addElement(paragraph)
    doc.save(customPath)


def convert(content: str, customPath: str, type: FileTypes) -> None:
    """Converts the file to the defined type"""
    if type == FileTypes.DOCX:
        createDOCX(content, customPath)
    else:
        createODT(content, customPath)


if __name__ == "__main__":
    filePath = input("Insert path to pdf file:\n")
    content = extractContent(filePath)
    convert(content, ".\\ConvertedFile.odt", FileTypes.ODT)