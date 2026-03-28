# Premium Activation System for Automod Bot

class PremiumActivation:
    def __init__(self):
        self.premium_users = set()  # Set to store premium users

    def activate_premium(self, user_id):
        """ Activates premium status for a user by their user ID. """
        self.premium_users.add(user_id)
        return f'User {user_id} has been activated with premium status.'

    def is_premium(self, user_id):
        """ Checks if a user has premium status. """
        return user_id in self.premium_users

    def deactivate_premium(self, user_id):
        """ Deactivates premium status for a user. """
        if user_id in self.premium_users:
            self.premium_users.remove(user_id)
            return f'User {user_id} has been deactivated from premium status.'
        return f'User {user_id} does not have premium status.'

# Example usage
if __name__ == '__main__':
    activation_system = PremiumActivation()
    print(activation_system.activate_premium(12345))  # Activating a user
    print(activation_system.is_premium(12345))  # Checking premium status
    print(activation_system.deactivate_premium(12345))  # Deactivating a user
