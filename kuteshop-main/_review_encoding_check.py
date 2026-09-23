# -*- coding: utf-8 -*-
import re
import os

files = [
    r'd:\oms代码\Rent\kuteshop-main\modules\Pt\Services\NewProductCommentService.php',
    r'd:\oms代码\Rent\kuteshop-main\modules\Pt\Services\NewProductPromoService.php',
    r'd:\oms代码\Rent\kuteshop-main\modules\Pt\Services\NewProductRentPeriodService.php',
    r'd:\oms代码\Rent\kuteshop-main\modules\Pt\Services\NewProductService.php',
    r'd:\oms代码\Rent\kuteshop-main\modules\Pt\Services\NewProductPromoCateService.php',
]

out = []
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        text = fh.read()
    out.append('=== ' + os.path.basename(f) + ' ===')
    out.append('replacement_ufffd: ' + str('\ufffd' in text))
    msgs = re.findall(r"ErrorException\('([^']*)'\)", text)
    for m in msgs:
        out.append('  err: ' + m)
    # sample const comments
    for m in re.finditer(r'/\*\*\s*(.+?)\s*\*/\s*\n\s*const ', text):
        out.append('  const_comment: ' + m.group(1))

# also php -l syntax check via tokenize-ish: look for odd quotes
dest = r'd:\oms代码\Rent\kuteshop-main\_review_encoding_out.txt'
with open(dest, 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out))
print('wrote', dest)
