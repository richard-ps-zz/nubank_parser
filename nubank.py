import pdfquery
import sys

pdf = pdfquery.PDFQuery(sys.argv[1])
pdf.load()

label = pdf.pq('LTTextLineHorizontal:contains("Valor")')
x1 = float(label.attr('x0'))
y1 = float(label.attr('y0'))

nome = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' % (x1, y1, x1+300, y1+60)).text()
print nome

label =  pdf.pq('LTTextLineHorizontal:contains("Vencimento")')
x1 = float(label.attr('x0'))
y1 = float(label.attr('y0'))

vencimento =  pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' %  (x1, y1, x1+300, y1+20)).text()
print vencimento

count = 0

while True:
    x1 = 148.648
    y1 = 524.118 - (35.9030*count)
    count += 1
    despesa = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' %  (x1, y1, x1+300, y1+20)).text()
    valor = pdf.pq('LTTextLineHorizontal:in_bbox("%s, %s, %s, %s")' %  (x1+200, y1, x1+600, y1+20)).text()
    if despesa == "" or valor == "":
        break
    print despesa, valor
