"""
the Interface Segregation Principle means separating the interfaces.
The principle states that many client-specific interfaces are better than one general-purpose interface. 
Clients should not be forced to implement a function they do no need.
Interface Segregation Principle "sometimes" could be considered as a solution of LSP violation. 
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
    
    @abstractmethod
    def renew_subscription(self):
        pass

    @abstractmethod
    def cancel_subscription(self):
        pass

    @abstractmethod
    def lock_user(self, username):
        pass


class Customer(User):
    def renew_subscription(self):
        # logic
        return "Your subscription has been successfully renewed"

    def cancel_subscription(self):
        # logic
        return "Your subscription has been successfully cancelled"

    # A customer should not have the privilage to lock other user's account,
    # so this should be left unimplemented!
    def lock_user(self, user_ID):
        pass

class Staff(User):
    def renew_subscription(self):
        # A staff user account doesn't have subscription option, they only do administrative work
        pass

    def cancel_subscription(self):
        # A staff user account doesn't have subscription option, they only do administrative work
        pass 

    def lock_user(self, username):
        # A staff member have the privilage to lock any user's account
        return f"{username}' account locked successfully"


"""
In this example, we can see that different User types had to implement methods they don't require!
"""

if __name__ == "__main__":

    staff_amany = Staff("admin_amany", "amany@admin.com")
    user_xyz = Customer("user_xyz", "xyz10@example.com")
    print(user_xyz.renew_subscription())

    print(staff_amany.lock_user(user_xyz.username))
