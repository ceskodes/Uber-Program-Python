class Account:

    # Constructor

    def __init__(self, id, name, document, email, password):
        self.id = id
        self.name = name
        self.document = document
        self.email = email
        self.password = password

    # Setters

    def set_name(self, name):
        self.name = name

    def set_document(self, document):
        self.document = document

    def set_email(self, email):
        self.email = email

    def set_password(self, password):
        self.password = password

    # Getters

    def get_name(self):
        return self.name

    def get_document(self):
        return self.document

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password