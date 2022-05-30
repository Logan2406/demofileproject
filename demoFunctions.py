from distutils.command.config import config
from PyPDF2 import PdfFileReader,PdfFileWriter
from pdf2image import convert_from_path
import os

conf=os.path.join(os.getcwd(),"static","files")


pdf_files=[]
img_files=[]

def checkOrientation(ur_x,ul_x,ul_y,ll_y):
    if ((ur_x-ul_x)>(ul_y-ll_y)):
        return('Landscape')
    else:
        return('Portrait')

def pdfToImages(base):
    images = convert_from_path(conf+"/"+'rotated_pdf.pdf')
    for i in range(len(images)):
        images[i].save(conf+"/"+base+"/"+'Img_page_' + str(i+1) + '.jpg', 'JPEG')
        img_files.append(conf+"\\"+base+"\\"+'Img_page_' + str(i+1) + '.jpg')



def print_hi(filename):

    img_files.clear()
    pdf_files.clear()

    print('Welcome the Application')
    try:
        pdf = PdfFileReader(conf+"/"+filename)
    except:
        print('Error occured while importing')
        return 0

    writer = PdfFileWriter()


    base = filename.split(".")[0]
    if(not os.path.isdir(conf+"/"+base)):
        os.makedirs(conf+"/"+base)

    for i in range(pdf.numPages):
        page = pdf.getPage(i).mediaBox
        ori = checkOrientation(page.getUpperRight_x(),page.getUpperLeft_x(),page.getUpperLeft_y(),page.getLowerLeft_y())
        pageDemo = pdf.getPage(i)
        if(ori=='Landscape'):
            pageDemo.rotateCounterClockwise(90)
        writer.addPage(pageDemo)
    out_file = open(conf+"/"+'rotated_pdf.pdf','wb')
    writer.write(out_file)
    out_file.close()

    try:
        pdf = PdfFileReader(conf+"/"+'rotated_pdf.pdf')
    except:
        print('Error occured while importing')
        return 0

    for i in range(pdf.numPages):
        page = pdf.getPage(i)
        out_file = open(conf+"/"+base+"/"+f'Pdf_page_{i+1}.pdf', 'wb')
        pdf_files.append(conf+"\\"+base+"\\"+f'Pdf_page_{i+1}.pdf')
        writer = PdfFileWriter()
        writer.addPage(page)
        writer.write(out_file)
        out_file.close()

    pdfToImages(base)
    os.remove(conf+"/"+'rotated_pdf.pdf')

    return [pdf_files,img_files]