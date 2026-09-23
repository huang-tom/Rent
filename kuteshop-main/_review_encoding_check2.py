# -*- coding: utf-8 -*-
import binascii

def show(path, needle_utf8):
    with open(path, 'rb') as f:
        data = f.read()
    # find 商品不存在 or similar by searching unicode encode
    needle = needle_utf8.encode('utf-8')
    print(path.split('\\')[-1], 'contains', needle_utf8, ':', needle in data)
    # print first chinese-looking multibyte sequence after 'ErrorException'
    idx = data.find(b"ErrorException('")
    if idx >= 0:
        chunk = data[idx:idx+40]
        print('  first err bytes:', binascii.hexlify(chunk))
        print('  decoded:', chunk.decode('utf-8', errors='replace'))

base = r'd:\oms代码\Rent\kuteshop-main\modules\Pt\Services\\'
show(base + 'NewProductService.php', '商品不存在')
show(base + 'NewProductCommentService.php', '评论不存在')
show(base + 'NewProductPromoService.php', '推广分类不存在')
show(base + 'NewProductRentPeriodService.php', '租期档位不存在')
show(base + 'NewProductPromoCateService.php', '推广分类不存在')
