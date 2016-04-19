# Copyright (c) 2016  Adam Coldrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Classes for handling actions a user can take."""


from adventurelib.exceptions import MissingFieldsError


required_fields = [
    'action',
    'type'
]


class Action(object):

    """Class to represent a basic action.

    A basic action is something like looking around. Actions
    with more complex behaviour can be subclassed from here.

    """

    def __init__(self, definition):
        try:
            # Attempt to parse the action definition
            self.action = definition['action']
            self.aliases = definition.get('aliases', [])
            self.type = definition['type']
            self.content = definition.get('content', '')
        except KeyError:
            # At least one required field was missing
            missing = [field for field in required_fields
                       if field not in definition]
            raise MissingFieldsError(missing)
        except Exception as e:
            # Something unexpected happened
            raise

    def __repr__(self):
        return '<adventurelib.action.Action: %s>' % self.action
