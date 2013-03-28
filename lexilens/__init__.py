import logging
import optparse

import gettext
from gettext import gettext as _
gettext.textdomain('lexilens')

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from lexilens import lexilensconfig

class LexilensLens(SingleScopeLens):

    class Meta:
        name = 'lexilens'
        description = 'Lexilens Lens'
        search_hint = 'Search Lexilens'
        icon = 'lexilens.svg'
        search_on_blank=True

    # TODO: Add your categories
    example_category = ListViewCategory("Examples", 'help')

    def search(self, search, results):
        # TODO: Add your search results
        results.append('https://wiki.ubuntu.com/Unity/Lenses/Singlet',
                         'ubuntu-logo',
                         self.example_category,
                         "text/html",
                         'Learn More',
                         'Find out how to write your Unity Lens',
                         'https://wiki.ubuntu.com/Unity/Lenses/Singlet')
        pass
