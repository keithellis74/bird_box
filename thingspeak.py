# -*- coding: utf-8 -*-

import requests

thingspeak_url = 'https://api.thingspeak.com/'


class Channel(object):
    """ThingSpeak channel object"""
    def __init__(self, id, api_key=None, write_key=None, fmt='json'):
        self.id = id
        self.api_key = api_key
        self.write_key = write_key
        self.fmt = ('.' + fmt) if fmt in ['json', 'xml'] else ''

    def get(self, options=dict()):
        """Get a channel feed.

        Full reference:
        https://de.mathworks.com/help/thingspeak/get-a-channel-feed.html
        """
        if self.api_key is not None:
            options['api_key'] = self.api_key
        url = '{ts}/channels/{id}/feeds{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            fmt=self.fmt,
        )
        r = requests.get(url, params=options)
        return self._fmt(r)

    def get_field(self, field=None, options=dict()):
        """Get particular field

        Full reference:
        https://de.mathworks.com/help/thingspeak/get-channel-field-feed.html
        """
        if self.api_key is not None:
            options['api_key'] = self.api_key
        url = '{ts}/channels/{id}/fields/{field}{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            field=field,
            fmt=self.fmt,
        )
        r = requests.get(url, params=options)
        return self._fmt(r)

    def get_field_last_text(self, field=None, options=dict()):
        """Get last result from particular field in text format

        Full reference:
        https://de.mathworks.com/help/thingspeak/get-channel-field-feed.html
        """
        self.field=field
        if self.api_key is not None:
            options['api_key'] = self.api_key
        url = '{ts}/channels/{id}/fields/{field}/last{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            field=self.field,
            fmt='.txt'
        )
        r = requests.get(url, params=options)
        return self._fmt(r)


    def view(self):
        """View a Channel"""
        options = dict()
        if self.api_key is not None:
            options['api_key'] = self.api_key
        url = '{ts}/channels/{id}{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            fmt=self.fmt,
        )
        r = requests.get(url, params=options)
        return self._fmt(r)
    # def view

    def update(self, data):
        """Update channel feed.

        Full reference:
        https://de.mathworks.com/help/thingspeak/update-channel-feed.html
        """
        if self.write_key is not None:
            data['api_key'] = self.write_key
        url = '{ts}/update{fmt}'.format(
            ts=thingspeak_url,
            id=self.id,
            fmt=self.fmt,
        )
        r = requests.post(url, params=data)
        return self._fmt(r)

    def _fmt(self, r):
        r.raise_for_status()
        if self.fmt == 'json':
            return r.json()
        else:
            return r.text
