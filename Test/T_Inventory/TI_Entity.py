from Inventory.Items.Item import Item


def main():
    test_PlayerInventory()

def test_PlayerInventory():

    from Entity.Player import Player
    def test_hold():
        p1 = Player(CN_Ship=1)
        p2 = Player(CN_Ship=1)

        assert p1.inventory.Hold.max

        i1 = Item(CN=50, wear=200)

        p1.inventory += i1

        assert p1.inventory.Hold == round(i1['wear'] * i1['size'])

        p1.inventory.send_item(p2, guid=i1['guid'], wear=40)

        assert p1.inventory.Hold == round((i1['wear']) * i1['size'])
        assert p2.inventory.Hold == round(40 * i1['size'])
        print("Success: Player hold")
    test_hold()
    print("Success: test_PlayerInventory")

if __name__ == '__main__':
    main()