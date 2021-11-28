'''
Pythonista Show in folder
===========================

Notices
-------

Copyright 2021 couplelongnecks.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

For a full copy of the GNU General Public License, see
<http://www.gnu.org/licenses/>.

Description
-----------

Implements a "Show script in folder" function for Ole Zorn's "Pythonista"
iPad app.


Usage
-----
- Add as Action Script
- Tap the Action Menu
- Tap Show in Files!
'''

import os
import _pythonista
import shortcuts
import editor


def main():
	get_url = editor.get_path()
	get_url = _pythonista.make_url(get_url)
	get_url = get_url.split('/')
	get_url.pop()
	get_url = "/".join(get_url)
	shortcuts.open_url(get_url)

if __name__=='__main__':
	main()


