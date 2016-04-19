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

"""Classes and utility functions for handling locations in a game world."""

from adventurelib.actions import Action
from adventurelib.exceptions import MissingFieldsError


required_fields = [
    'name',
    'actions'
]


class Location(object):

    """A location as defined in a YAML file.

    A location is a single place in the game world. It has a list of actions
    that are possible, and any metadata that may be useful, such as an image
    to display or the type of location it is (if such a thing is useful).

    The YAML should be of the form:

    $id:
      name: $name
      type: $type # optional
      image: path/to/image # optional
      actions:
        - action: $command
          output:
            type: $output_type
            content: |
                Some example content string.

    See the Action class for full documentation of actions

    """

    def __init__(self, id, definition):
        """Instantiate a Location.

        :param definition: A dictionary from a YAML location definition.

        """
        self.id = id
        try:
            # Attempt to parse the location definition.
            self.name = definition['name']
            self.type = definition.get('type', None)
            self.image = definition.get('image', None)
            self.actions = [Action(a) for a in definition['actions']]
        except KeyError:
            # At least one required field was missing
            missing = [field for field in required_fields
                       if field not in definition]
            raise MissingFieldsError(missing)
        except Exception as e:
            # Something unexpected went wrong
            raise
