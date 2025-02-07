# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SpeckleQGIS
                                 A QGIS plugin
 SpeckleQGIS Description
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-08-04
        copyright            : (C) 2021 by Speckle Systems
        email                : alan@speckle.systems
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

import os
import sys
path = os.path.dirname(os.path.abspath(__file__))
if(path not in sys.path):
    sys.path.insert(0, path)

from plugin_utils.installDependencies import setup
from speckle.logging import logger

from qgis.core import Qgis
# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SpeckleQGIS class from file SpeckleQGIS.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """

    # Set qgisInterface to enable logToUser notifications
    logger.qgisInterface = iface
    iface.pluginToolBar().setVisible(True)
    
    # Ensure dependencies are installed in the machine
    from speckle.utils import enable_remote_debugging
    enable_remote_debugging()
    setup()
    from speckle_qgis import SpeckleQGIS
    from specklepy.logging import metrics
    
    version = Qgis.QGIS_VERSION.encode('iso-8859-1', errors='ignore').decode('utf-8').split(".")[0]
    metrics.set_host_app("QGIS", f"QGIS {version}")
    return SpeckleQGIS(iface)
