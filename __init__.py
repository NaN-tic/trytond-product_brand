# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from . import product


def register():
    Pool.register(
        product.Brand,
        product.Model,
        product.Template,
        product.Product,
        module='product_brand', type_='model')
