"""Classes for melon orders."""
class MelonOrder:

    def __init__(self, name, species, qty, tax):
        self.name = name
        self.species = species  
        self.qty = qty
        self.shipped = False
        self.tax = tax
        # self.order_type = order_type
        
        # tax = None, order_type = None, country_code = None
        # if country_code:
        #     self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + int(self.tax)) * int(self.qty) * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True




class DomesticMelonOrder(MelonOrder):
    """A melon order within the USA."""
    order_type = "Domestic"
    tax = 0.08



    
    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(MelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17



    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
