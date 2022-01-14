from odoo import api, fields, models
from odoo.exceptions import Warning

class Worker(models.Model):
    # properties
    _name = 'waste.worker'
    _description = 'Worker'
    # String fields
    name = fields.Char('Name', required=True)

    '''
    process = fields.Char('生产工序')
    product_code = fields.Char('产品型号')
    material_type = fields.Selection(
        [('涂布/边角铜', 'Tubu'), ('三元级片', 'Sanyuan'), ('静铝箔', 'Lvbo'), ('other', 'Other')], 'Type')
        #[('paper', 'Paperback'), ('hard', 'Hardcover'), ('electronic', 'Electronic'), ('other', 'Other')], 'Type')
    contract = fields.Char('联系人')
    date_published = fields.Date()
    notes = fields.Text('Internal Notes')
    descr = fields.Html('Description')

    # Numeric fields:
    copies = fields.Integer(default=1)
    avg_rating = fields.Float('Average Rating', (3,2))
    price = fields.Monetary('Price', 'currency_id')
    currency_id = fields.Many2one('res.currency') # price helper

    # Date and time fields
    date_published = fields.Date()
    last_borrow_date = fields.Datetime('Last Borrowed On', default=lambda self: fields.Datetime.now())

    # Other fields
    active = fields.Boolean('Active?', default=True)
    image = fields.Binary('Cover')

    # Relational Fields
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    author_ids = fields.Many2many('res.partner', string='Authors')
    publisher_country_id = fields.Many2one('res.country', string='Publisher Country',
                                           compute='_compute_publisher_country')
    
    @api.depends('publisher_id.country_id')
    def _compute_publisher_country(self):
        for book in self:
            book.publisher_country_id = book.publisher_id.country_id
    '''