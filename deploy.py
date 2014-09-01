# -*- coding: utf-8 -*-
# Copyright (C) 2012-2014 Mag. Christian Tanzer All rights reserved
# Glasauergasse 32, A--1130 Wien, Austria. tanzer@swing.co.at
# #*** <License> ************************************************************#
# This module is part of the program FFG.
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This module is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this module. If not, see <http://www.gnu.org/licenses/>.
# #*** </License> ***********************************************************#
#
#++
# Name
#    deploy
#
# Purpose
#    Deploy command for FFG
#
# Revision Dates
#    23-May-2012 (CT) Creation
#    31-May-2012 (CT) Remove `lib_dir` from `_defaults`
#     1-Jun-2012 (CT) Remove ancestor `GTW.OMP.deploy`
#     2-Jun-2012 (CT) Replace `config_defaults` by `Config`
#     3-Jun-2012 (CT) Factor `_Base_Command_`, add `App_Config`
#    10-Jul-2014 (CT) Derive `Command` from `CNDB.GTW.deploy.Command`, too
#    ««revision-date»»···
#--

from   __future__  import absolute_import, division, print_function #, unicode_literals

from   _CNDB                    import CNDB
from   _GTW                     import GTW
from   _TFL                     import TFL

import _CNDB._GTW.deploy
import _GTW._Werkzeug.deploy

from   _Base_Command_           import _Base_Command_

class Command \
          ( _Base_Command_
          , CNDB.GTW.deploy.Command
          , GTW.Werkzeug.deploy.Command
          ) :
    """Manage deployment of FFG application."""

    _defaults               = dict \
        ( app_dir           = "www/app"
        , app_module        = "./Command.py"
        , bugs_address      = "tanzer@swing.co.at,ralf@runtux.com"
        , copyright_holder  = "Mag. Christian Tanzer, Ralf Schlatterbeck"
        , languages         = "de,en"
        , project_name      = "FFG"
        )

    class App_Config (_Base_Command_.Config) :
        """Config for application: don't specify, just for internal use."""

        ### avoid auto-loading by redefining `type` to `Rel_Path`
        type                = TFL.CAO.Rel_Path

    # end class App_Config

    class Config (GTW.Werkzeug.deploy.Command.Config) :

        _default  = ".ffg.deploy.config"

    # end class Config

    class _Babel_ (GTW.Werkzeug.deploy.Command._Babel_) :

        _package_dirs       = ["_CNDB", "."]

    # end class _Babel_

# end class Command

command = Command ()

if __name__ == "__main__" :
    command ()
### __END__ deploy