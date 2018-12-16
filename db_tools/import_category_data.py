# -*- coding: utf-8 -*-
__author__ = 'XiaoWei'

# 独立使用Django的model
import os
import sys
import django
pwd = os.path.dirname(os.path.realpath(__file__))
# 将db_tools 添加到环境目录
sys.path.append(pwd + '../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MxShop.settings')
django.setup()

from goods.models import GoodsCategory
from db_tools.data.category_data import row_data

for lev1_cat in row_data:
    lev1_intance = GoodsCategory()
    lev1_intance.code = lev1_cat['code']
