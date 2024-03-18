from docx import Document

d = Document('qa1.docx')

for p in d.paragraphs:  # 获取每个段落
    # 获取numId
    try:
        print('numId', p._element.pPr.numPr.numId.val, end='  ')
    except:
        pass
    # 获取ilvl的值，注意纯文本段落没有ilvl，其ilvl是None
    try:
        print('ilvl', p._element.pPr.numPr.ilvl.val, end='  ')
    except:
        pass
    # 获取每个段落的文本信息
    print('text', p.text)

# 获取numbering.xml文件中的信息
ct_numbering = d.part.numbering_part._element
numXML = d.part.numbering_part.numbering_definitions._numbering
