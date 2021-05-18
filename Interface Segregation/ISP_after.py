"""
Solution: separating the  User interfaces into more specific interfaces
"""

# Type of users example
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.staff = False
        self.auth = True  
    
    def get_username(self):
        return f"Hi {self.username}!"
    

class ClientUser(User):
    @abstractmethod
    def renew_subscription(self):
        pass

    @abstractmethod
    def cancel_subscription(self):
        pass

class StaffMember(User):
    @abstractmethod
    def lock_user(self, username):
        pass

    @abstractmethod
    def unlock_user(self, username):
        pass


class Buyer(ClientUser):
    def renew_subscription(self):
        # logic
        return "Your subscription has been successfully renewed"

    def cancel_subscription(self):
        # logic
        return "Your subscription has been successfully cancelled"

class Seller(ClientUser):
    def renew_subscription(self):
        # logic
        return "Your subscription has been successfully renewed"

    def cancel_subscription(self):
        # logic
        return "Your subscription has been successfully cancelled"


class Admin(StaffMember):
    def lock_user(self, username):
        # A staff member have the privilage to lock any user's account
        return f"{username}' account locked successfully"

    def unlock_user(self, username):
        # A staff member have the privilage to unlock any user's account
        return f"{username}' account unlocked successfully"


"""
We can see that different User types are no more forced to implement methods they don't really need!
"""

if __name__ == "__main__":

    staff_amany = Admin("admin_amany", "amany@admin.com")
    seller_xyz = Seller("seller_xyz", "xyz10@example.com")
    print(seller_xyz.renew_subscription())

    print(staff_amany.lock_user(seller_xyz.username))
