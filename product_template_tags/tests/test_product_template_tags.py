from odoo.tests.common import TransactionCase
from odoo.api import Environment


class TestProductTemplateTag(TransactionCase):
    pre_install = True
    post_install = True

    def setUp(self):
        super(TestProductTemplateTag, self).setUp()
        print('--------------------------------------------------')
        env = Environment(self.registry.test_cr, self.uid, {})
        tag = env['product.template.tag'].create({
            'name': 'test_tag',
        })
        product = env['product.template'].search([], 1).write({
            'tag_ids': [(6, 0, [tag.id])],
        })
        print('--------------------------------------------------')
        print(tag, tag.name)
        print(product, product.tag_ids)
        print('--------------------------------------------------')

    def products_count(self):
        env = Environment(self.registry.test_cr, self.uid, {})
        print('=========================================================')
        tag = env['product.template.tag'].search([('name', '=', 'test_tag')])
        print('=========================================================')
        print(tag, tag.name)
        print('=========================================================')
        self.assertEqual(tag.products_count, 1, 'Error product count does not match')


