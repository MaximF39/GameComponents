from Inventory.Items.Item import Item


class Device(Item):

    def use(self):
        super().use()   

    def unuse(self):
        super().unuse()