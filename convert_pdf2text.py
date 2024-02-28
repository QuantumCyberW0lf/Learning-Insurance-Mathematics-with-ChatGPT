#!/usr/bin/python3.10
# -*- coding: utf-8 -*-

import sys,argparse,os

try:
    import pdftotext
except ImportError as err:
    print("[-] No Module pdftotext {}".format(str(err)))
    sys.exit(1)

class PDFtoTextConverter(object):
    def __init__(self,input_pdf:str,output_text:str)->None:
        self.input_pdf = input_pdf
        self.output_text = output_text

    def convert(self):
        try:
            with open(self.input_pdf,"rb") as input_f:
                pdf_content = pdftotext.PDF(input_f)
            output_content = "".join(pdf_content)
            with open(self.output_text,"w") as output_f:
                output_f.write(output_content)
        except FileNotFoundError as err:
            print("[-] File {} not found".format(self.input_pdf))
            sys.exit(1)

def main():
    parser=argparse.ArgumentParser(description="Convert PDF to Text format.",
                                   epilog="Built by Thi Altenschmidt.")
    parser.add_argument("-i","--in",type=str,dest="input_pdf",
                        help="Input PDF file path.",required=True)
    parser.add_argument("-o","--out",type=str,dest="output",
                        help="Ouput text file path",default="output.txt")

    args = parser.parse_args()
    _, file_extension = os.path.splitext(args.input_pdf)
    if file_extension.lower() != '.pdf':
        print("[-] Input file is not a PDF file.")
        sys.exit(1)

    converter = PDFtoTextConverter(args.input_pdf,args.output)
    converter.convert()
    full_path = os.path.abspath(args.output)
    print("[*] Text file saved at {}".format(str(full_path)))

if __name__ == "__main__":
    main()

