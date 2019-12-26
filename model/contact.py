class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, adress=None, mobilephone=None, email=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.adress = adress
        self.mobilephone = mobilephone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

