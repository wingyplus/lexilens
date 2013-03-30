import logging
import optparse

import gettext
from gettext import gettext as _
gettext.textdomain('lexilens')

from singlet.lens import SingleScopeLens, IconViewCategory, ListViewCategory

from lexilens import lexilensconfig

import sqlite3 as sqlite
import re  

DB_FILE = '/usr/share/unity/lenses/lexilens/lexite.db'

class LexilensLens(SingleScopeLens):

    class Meta:
        name = 'lexilens'
        description = 'Lexilens Lens'
        search_hint = 'Look word up'
        icon = 'lexilens.svg'
        search_on_blank=True

    con = None
    # TODO: Add your categories
    meaning_category = ListViewCategory("Meaning", 'dialog-information-symbolic')

    def lookup(self, search):
        query = ""
        try:
            if re.match("^[aA-zZ]", search):
                query = "SELECT et_tentry,et_cat FROM et_lex WHERE et_search LIKE '%s'" % (search)
            else:
                query = "SELECT te_eentry,te_cat FROM te_lex WHERE te_search LIKE '%s'" % (search)

            con = sqlite.connect(DB_FILE)
            cur = con.cursor()
            cur.execute(query)
            
            data = cur.fetchall()
            return data
        except sqlite.Error, e:
            print "Error : Unable to lookup : %s" % (e)
            return []

    def search(self, search, results):
        for meaning in self.lookup(search):
            results.append('',
                         '/usr/share/unity/lenses/lexilens/unity-lens-lexilens.png',
                         self.meaning_category,
                         "text/html",
                         meaning[0],
                         meaning[1],
                         '')
        pass
