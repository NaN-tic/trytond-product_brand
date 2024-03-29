# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, DeactivableMixin, fields
from trytond.pool import PoolMeta


class Brand(DeactivableMixin, ModelSQL, ModelView):
    'Brand'
    __name__ = 'product.brand'
    name = fields.Char('Name', required=True, translate=True)
    description = fields.Text('Description', translate=True)
    products = fields.One2Many('product.template', 'brand', 'Products')

    @classmethod
    def copy(cls, brands, default=None):
        if default is None:
            default = {}
        else:
            default = default.copy()
        default.setdefault('products', None)
        return super().copy(brands, default)


class Model(ModelSQL, ModelView):
    'Model'
    __name__ = 'product.brand.model'
    name = fields.Char('Name', required=True)
    brand = fields.Many2One('product.brand', 'Brand', required=True)


class Template(metaclass=PoolMeta):
    __name__ = 'product.template'
    brand = fields.Many2One('product.brand', 'Brand')


class Product(metaclass=PoolMeta):
    __name__ = 'product.product'
