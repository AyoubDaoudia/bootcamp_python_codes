class GotCharacter:
    def __init__(self,first_name,is_alive=True):
        if type(first_name)!=str or first_name=="" :
            raise ValueError
        self.first_name=first_name
        self.is_alive=is_alive


class Stark(GotCharacter):
    """This family is a Got Family, and since I haven't watched it, I know nothing about them, but hey, at least some of them survive till the end right ?"""
    def __init__(self,first_name=None,is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    def print_house_words(self):
        return self.house_words
    def die(self):
        self.is_alive=False