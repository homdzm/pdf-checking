import pytest

from project_fitz.my_fitz import ReaderPDF


@pytest.fixture
def get_dict_from_pdf():
    pdf = ReaderPDF("test_task.pdf", "data_from_pdf.txt")
    received_dict = pdf.result_dict
    pdf.check_structure(received_dict)
    return pdf.check_structure(received_dict)
