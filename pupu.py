d=[ord(c)-47 for c in 'V?_;d8g7i6j5l4n3n3n3n3E6:5?4C1616070<5B0905080:6@090409097>090409079>090409079>180508079?071507098@131813298B2>2<8c9b9`:_;]<[=W?UB9163GFC9<LD:<LE99OH77QH`H_:0;_23<_<_:`9a6b']
n=0x3ffc84210842109ff2abaf
r=''
while d:r+=' '*d.pop()+'*'*d.pop()+n%2*'\n';n//=2
print(r)