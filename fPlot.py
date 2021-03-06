# -*- coding: utf-8 -*-
#
# fPlot.py -- Plotting function for embedded matplotlib widget with Ginga.
#
# Thanks for Eric Jeschke (eric@naoj.org), https://github.com/ejeschke/ginga
# Copyleft, Yücel Kılıç (yucelkilic@myrafproject.org) and Mohammad Niaei Shameoni (mshemuni@myrafproject.org).
# This is open-source software licensed under a GPLv3 license.
import sys

from ginga.mplw.ImageViewCanvasMpl import ImageViewCanvas
from ginga.mplw.FigureCanvasQt import setup_Qt
from ginga.AstroImage import AstroImage
from ginga.misc import log
from ginga import cmap

class FitsPlot(object):
    def __init__(self, chartDev):

        self.chartDev = chartDev
        use_logger = False
        logger = log.get_logger(null=not use_logger, log_stderr=True)
        self.logger = logger
        # create a ginga object and tell it about the figure
        self.chartDev.fig.clf()
        fi = ImageViewCanvas(logger)
        fi.enable_autocuts('on')
        fi.set_autocut_params('zscale')
        fi.set_figure(self.chartDev.fig)
        fi.ui_setActive(True)
        self.fitsimage = fi
        setup_Qt(chartDev, fi)

        # enable all interactive features
        fi.get_bindings().enable_all(True)
        self.fitsimage = fi

    def load(self, fitspath):
        # load an image
        image = AstroImage(self.logger)
        image.load_file(fitspath)
        self.fitsimage.set_image(image)
        
        # plot some example graphics via matplotlib
        # Note adding axis from ginga (mpl backend) object
        #ax = self.fitsimage.add_axes()
        #self.chartDev.draw()




