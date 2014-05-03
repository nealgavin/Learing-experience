
width = input("enter then lenth")

price_wid = 10
item_wid = width - price_wid

header_format = '%-*s%*s'
format = '%-*s%*.2f'
print '='*width
print header_format % (item_wid, 'Item',price_wid,'price')
print '-'*width
print format % (item_wid,'apple',price_wid,0.4)
print '=' * width

