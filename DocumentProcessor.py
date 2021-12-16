try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re


class DocumentProcessor:

    def retrieveContractNumber(self, filename):
        ocr_txt = pytesseract.image_to_string(Image.open(filename))

        # print(ocr_txt.split())

        contract_number = self.findContractNumberV2(ocr_txt.split())

        corr_contract_number = self.correct_contract_number(contract_number)

        return corr_contract_number

    def findContractNumber(self, ocr_txt_lst):

        keywords = [
            'Contractnummer',
            'Contractnummer:'
            'contractnummer',
            'contractnummer:',
            'INGnummer',
            'INGnummer:',
            'Leningnummer',
            'Leningnummer:'
        ]

        for token_index in range(len(ocr_txt_lst)):
            if ocr_txt_lst[token_index] in keywords:

                return ocr_txt_lst[token_index + 1]
        return "i give up"

    def findContractNumberV2(self, ocr_txt_lst):

        datum_list = [
            'datum',
            'Datum',
            'datum:',
            'Datum:'
        ]

        for token_index in range(len(ocr_txt_lst)):
            if ocr_txt_lst[token_index] in datum_list:
                return ocr_txt_lst[token_index - 1]
            if ocr_txt_lst[token_index] == 'Dear':
                return ocr_txt_lst[token_index - 1]
        return "i give up"

    def correct_contract_number(self, contract_number):

        for i in range(len(contract_number.split())):
            if contract_number[i] == 'O' or contract_number[i] == 'o':
                contract_number[i] = 0

        return ''.join(contract_number)
