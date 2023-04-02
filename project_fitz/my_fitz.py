import fitz


class ReaderPDF:
    fields = ["PN", "SN", "DESCRIPTION", "LOCATION", "CONDITION", "RECEIVER#", "UOM", "EXP DATE", "PO", "CERT SOURCE",
              "REC.DATE", "MFG", "BATCH#", "DOM", "REMARK", "LOT#", "TAGGED BY", "Qty", "NOTES"]

    def __init__(self, pdf_path: str, file_txt_nane: str):
        self.doc = fitz.open(pdf_path)
        self.write_data_to_file(self.doc, file_txt_nane)
        self.lines = self.read_data_from_file_inline(file_txt_nane)
        self.result_dict = self.get_dict_with_data(self.lines)

    @staticmethod
    def write_data_to_file(doc_pdf, file_name: str) -> None:
        page_pdf = doc_pdf.load_page(0)
        page1text = page_pdf.get_text("text")
        with open(file_name, "w") as file:
            file.write(page1text)

    @staticmethod
    def read_data_from_file_inline(file_name: str):
        with open(file_name, "r") as file:
            lines = file.readlines()
        return lines

    @staticmethod
    def get_dict_with_data(lines) -> dict:
        pairs_list = [line.split(":") for line in lines]
        dict_result = {elem[0].strip(): elem[1].strip() for elem in pairs_list if len(elem) == 2}
        return dict_result

    def check_structure(self, dict_with_data: dict) -> bool:
        """
                It validates the structure of pdf document according to the sample
                and returns the True or False
                :param dict_with_data: the schema to validate against
                :return: bool
                """
        counter = 0
        for num, val in enumerate(dict_with_data.items()):
            if num == 0 and val[0] == self.fields[num] and type(val[1]) is str:
                counter += 1
            if num == 1 and val[0] == self.fields[num] and val[1].isdigit():
                counter += 1
            if num == 2 and val[0] == self.fields[num] and type(val[1]) is str:
                counter += 1
            if num == 3 and val[0] == self.fields[num] and val[1].isdigit():
                counter += 1
            if num == 4 and val[0] == self.fields[num] and type(val[1]) is str:
                counter += 1
            if num == 5 and val[0] == self.fields[num] and val[1].isdigit():
                counter += 1
            if num == 6 and val[0] == self.fields[num] and type(val[1]) is str:
                counter += 1
            if num == 7 and val[0] == self.fields[num] and val[1][:2].isdigit() and val[1][3:5].isdigit() \
                    and val[1][-4:].isdigit() and val[1][2] == "." and val[1][5] == ".":
                counter += 1
            if num == 8 and val[0] == self.fields[num] and val[1].isalnum():
                counter += 1
            if num == 9 and val[0] == self.fields[num] and type(val[1]) is str:
                counter += 1
            if num == 10 and val[0] == self.fields[num] and val[1][:2].isdigit() and val[1][3:5].isdigit() \
                    and val[1][-4:].isdigit() and val[1][2] == "." and val[1][5] == ".":
                counter += 1
            if num == 11 and val[0] == self.fields[num] and type(val[1]) is str:
                counter += 1
            if num == 12 and val[0] == self.fields[num] and val[1].isdigit():
                counter += 1
            if num == 13 and val[0] == self.fields[num] and val[1][:2].isdigit() and val[1][3:5].isdigit() \
                    and val[1][-4:].isdigit() and val[1][2] == "." and val[1][5] == ".":
                counter += 1
            if num == 14 and val[0] == self.fields[num]:
                counter += 1
            if num == 15 and val[0] == self.fields[num] and val[1].isdigit():
                counter += 1
            if num == 16 and val[0] == self.fields[num]:
                counter += 1
            if num == 17 and val[0] == self.fields[num] and val[1].isdigit():
                counter += 1
            if num == 18 and val[0] == self.fields[num]:
                counter += 1
        if counter == 19:
            print("The document is matched of the sample")
            return True
        else:
            print(counter)
            print("The document is not matched of the sample")
            return False


if __name__ == "__main__":
    pdf = ReaderPDF("../test_task.pdf", "data_from_pdf.txt")
    received_dict = pdf.result_dict
    pdf.check_structure(received_dict)











