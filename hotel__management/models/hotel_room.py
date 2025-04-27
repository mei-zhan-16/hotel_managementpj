from odoo import fields,models

class HotelRoom(models.Model):
    _name="hotel.room"

    roomname=fields.Char(string="Room Name")
    roomtype=fields.Char(string="Room Type")
    rent=fields.Char(string="Rent")
    floor=fields.Char(string="Floor")


