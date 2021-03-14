# A demonstration of classes using the exercises from chapter 9 of Python Crash Course by Eric Matthes

class User:
    """users and their attributes"""

    def __init__(self, username, email, team):
        """user basics"""
        self.username = username
        self.email = email
        self.team = team
        self.login = 0

    def describeUser(self):
        """summary of user's info in a formatted string"""
        print(f"User {self.username}'s e-mail address is {self.email} and belongs to team {self.team}")

    def greetUser(self):
        """personalised greeting for the user"""
        print(f"Hi {self.username}, you are now logged in")

    def login_attempts(self):
        """limits login attempts to 3 attempts"""
        if self.login < 3:
            self.login += 1
            print(f"login attempt {self.login}")
        else:
            print(f'LOGIN ATTEMPTS EXCEEDED')

    def reset_login_attemps(self):
        """replenishes 3 login attempts"""
        self.login = 0
        print("*** login attempts reset ***")


class Admin(User):
    """a user with privileges"""

    def __init__(self, username, email, team):
        super().__init__(username, email, team)
        self.privileges = Privileges()


class Privileges():
    """the privileges an admin user has stored here"""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """privileges user may have"""
        print("User privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(f"> {privilege}")
        else:
            print('*No privileges assigned*')


# instantiations of standard users (no admin or privileges)
user001 = User("blueboy1966", "blueboy66@gmail.com", "blue")
user002 = User("redgirl100", "suzie@yahoo.com", "red")
user003 = User("bananaman", "bananarama@bananas.com", "yellow")

# calling the methods individually
user001.describeUser()
user003.greetUser()

# simulate failed login attempts
user002.login_attempts()
user002.login_attempts()
user002.login_attempts()
user002.login_attempts()
user002.login_attempts()
user002.login_attempts()

# simulate reset of attempts using reset_login_attempts method
user002.reset_login_attemps()

# re-simulate failed logins
user002.login_attempts()
user002.login_attempts()
user002.login_attempts()
user002.login_attempts()
print("")

# create and test new Admin class user
user004 = Admin("john55", "admin_john@company.com", "admin")

# check to see if Admin User has any privileges
user004.privileges.show_privileges()
print("")
# testing Privilege class by adding some privileges
print('adding privileges..')
print("")
# new temp attribute required
user004_privileges = ['delete users',
                      'add users',
                      'modify users']

# re-check privileges
user004.privileges.privileges = user004_privileges
user004.privileges.show_privileges()
