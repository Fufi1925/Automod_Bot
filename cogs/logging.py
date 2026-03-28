import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('moderation.log'),
                        logging.StreamHandler()
                    ])

logger = logging.getLogger('ModerationLogger')


def log_moderation_event(event_type, user, details):
    """Log moderation events such as kick, ban, mute, etc."""
    logger.info(f'Event: {event_type}, User: {user}, Details: {details}')


def log_user_action(action_type, user, details):
    """Log user actions such as message edits, deletions, etc."""
    logger.info(f'Action: {action_type}, User: {user}, Details: {details}')


# Example usage
# log_moderation_event('ban', 'User123', 'Banned for spamming')
# log_user_action('edit', 'User456', 'Edited message: <old_message> to <new_message>')