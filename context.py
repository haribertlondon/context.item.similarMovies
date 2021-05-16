# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Arne Svenson
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

from __future__ import absolute_import, division, print_function, unicode_literals
import xbmc
import xbmcgui
import sys


#------------------------------------------------------------------------------
# MAIN
#------------------------------------------------------------------------------

if __name__ == '__main__':
    
    message = "Clicked on '{}'".format(sys.listitem.getLabel())
    
    id = sys.listitem.getUniqueID("imdb")
    if len(id)==0:
        id = "tmdb"+sys.listitem.getUniqueID("tmdb")
    
    message2 = "IMDB:{}".format(id)
    xbmcgui.Dialog().notification("Hello context items!", message2 + message)
    
    
    #cmd2 = 'ActivateWindow(10025,"plugin://plugin.video.smartfilter/",return)' #works
    cmd2 = 'ActivateWindow(10025,"plugin://plugin.video.smartfilter/?action=listing&category=__SimilarTo__'+id+'",return)' #works
    xbmc.executebuiltin(cmd2)
    
    #cmd= "plugin://plugin.video.smartfilter/?action=listing&category=__SimilarTo__"+id
    #xbmc.executebuiltin('RunPlugin('+cmd+')')
    
    #xbmc.executebuiltin('RunPlugin()' )
    #xbmc.executebuiltin("RunAddon("+cmd+", True)")
    #xbmc.executebuiltin("ActivateWindow(10025,'"+cmd+"',return)")
    

