str_input = """
g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""

alph_in = 'abcdefghijklmnopqrstuvwxyz'
alph_out = 'cdefghijklmnopqrstuvwxyzab'

trans = str.maketrans(alph_in, alph_out)
result = str_input.translate(trans)

print(result)

#so what we need is to change the url to http://www.pythonchallenge.com/pc/def/ocr.html