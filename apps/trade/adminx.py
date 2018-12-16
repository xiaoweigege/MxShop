# -*- coding: utf-8 -*-
__author__ = 'bobby'

import xadmin
from .models import Shopping, OrderInfo, OrderGoods


class ShoppingCartAdmin(object):
    list_display = ["user", "goods", "goods_num", ]


class OrderInfoAdmin(object):
    list_display = ["user", "order_sn",  "trade_no", "pay_staus", "post_script", "order_mount", "pay_time", "add_time"]

    class OrderGoodsInline(object):
        model = OrderGoods
        exclude = ['add_time', ]
        extra = 1
        style = 'tab'

    inlines = [OrderGoodsInline, ]


xadmin.site.register(Shopping, ShoppingCartAdmin)
xadmin.site.register(OrderInfo, OrderInfoAdmin)
