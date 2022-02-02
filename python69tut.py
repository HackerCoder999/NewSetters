class Empolyee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname} @Coderashlaan.com"

    def explane(self):
        return f"This is Empolyee {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is Delated"
        return f"{self.fname}.{self.lname}@Coderarshlaan.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.lname = names.split(".")[0]
        self.fname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

hind_suppoter = Empolyee("Hind", "Tati")
arshlaan = Empolyee("arshlaan", "Cool")

hind_suppoter.email = "This.that@Coderarshlaan.com"
print(hind_suppoter.email)
print(hind_suppoter.email)

del hind_suppoter.email
print(hind_suppoter.email)
