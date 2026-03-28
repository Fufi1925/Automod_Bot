# Embed Design Utilities

"""
This module contains utilities for designing embeds.
"""

class EmbedUtils:
    @staticmethod
    def create_embed(title, description, color):
        """
        Create an embed with the given title, description, and color.
        """
        return {
            'title': title,
            'description': description,
            'color': color
        }

    @staticmethod
    def add_field(embed, name, value, inline=False):
        """
        Add a field to the existing embed.
        """
        if 'fields' not in embed:
            embed['fields'] = []
        embed['fields'].append({
            'name': name,
            'value': value,
            'inline': inline
        })
        return embed
