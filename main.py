#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# main.py -- L.A. Cosmic in PyQt4.
#
# Thanks for Ginga to Eric Jeschke (eric@naoj.org), https://github.com/ejeschke/ginga
# Thanks for cosmics.py to Malte Tewes (mtewes (at) astro.uni-bonn.de), http://obswww.unige.ch/people/malte.tewes/cosmics_dot_py/
# Thanks to https://gist.github.com/Maduranga/ for embedding matplotlibWidget into PyQt4

# Copyleft, Yücel Kılıç (yucelkilic@myrafproject.org).
# This is open-source software licensed under a GPLv3 license.

try:
    # force Qt4 API v2
    import sip
    for cl in ('QString', 'QVariant'):
        sip.setapi(cl, 2)

    import os,  math, ntpath
    os.environ['QT_API'] = 'pyqt'
    # force matplotlib to use Qt4 backend
    import matplotlib
    matplotlib.use('Qt4Agg')
    
    from PyQt4 import QtGui, QtCore
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except:
	print("Can not load PyQT4")
	raise SystemExit


try:
    import cosmics
except:
	print("Can not load cosmics")
	raise SystemExit

from cosmicCleaner import Ui_Form

try:
    import matplotlib.pyplot as plt
except:
	print("Can not load matplotlib")
	raise SystemExit

try:
    from ginga.mplw.ImageViewCanvasMpl import ImageViewCanvas
    from ginga.misc import log
    from ginga.AstroImage import AstroImage
    from ginga import cmap
except:
	print("Can not load Ginga")
	raise SystemExit

try:
    from fPlot import *
except:
	print("Where is fPlot?")
	raise SystemExit

try:
    import numpy as np
except:
	print("Can not load numpy")
	raise SystemExit


class MyForm(QtGui.QWidget, Ui_Form):
  def __init__(self):
    super(MyForm, self).__init__()
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    self.ui.pushButton.clicked.connect(self.add)
    self.ui.pushButton_2.clicked.connect(self.rm)
    self.ui.pushButton_3.clicked.connect(self.cleanCosmics)
    self.ui.listWidget.clicked.connect(self.displayPhot)

    self.plotF = FitsPlot(self.ui.widget.canvas)

  # Images add function
  def add(self, flist):
      
    filename = QtGui.QFileDialog.getOpenFileNames(self ,"Images...","",("Fit or Fits (*.fits *.fit)"))
    flist = self.ui.listWidget
    it = flist.count()-1
    for x in filename:
            it = it+1
            item = QtGui.QListWidgetItem()
            flist.addItem(item)
            item = flist.item(it)
            item.setText(QtGui.QApplication.translate("Form", x, None, QtGui.QApplication.UnicodeUTF8))
    return True

  # Images remove function
  def rm(self, flist):
    
    flist = self.ui.listWidget      
    for x in flist.selectedItems():
            flist.takeItem(flist.row(x))
    fnumber = flist.count()
    return True

  # Images display function
  def displayPhot(self):

	img = self.ui.listWidget.currentItem()
	img = img.text()
	self.plotF.load(str(img))

  # Cosmics clean function
  def cleanCosmics(self):

    if self.ui.listWidget.count() != 0:
        it = 0
        self.ui.progressBar.setProperty("value", 0)
        odir = QtGui.QFileDialog.getExistingDirectory( self, 'Select Directory to Save PNG File(s)')
        if os.path.exists(odir):
            for x in xrange(self.ui.listWidget.count()):
                it = it + 1
                image = self.ui.listWidget.item(x)
                filename = ntpath.basename(image.text())
                basename, extension = os.path.splitext(filename)
                
                # Read the FITS :
                array, header = cosmics.fromfits(image.text())
                # array is a 2D numpy array

                # Build the object :
                c = cosmics.cosmicsimage(array, gain=2.2, readnoise=10.0, sigclip = 5.0, sigfrac = 0.3, objlim = 5.0)
                # There are other options, check the manual...

                # Run the full artillery :
                c.run(maxiter = 4)

                # Write the cleaned image into a new FITS file, conserving the original header :
                cosmics.tofits("%s/%s_clean.fits" %(odir, basename), c.cleanarray, header)

                if self.ui.checkBox.isChecked():
                    # If you want the mask, here it is :
                    cosmics.tofits("%s/%s_mask.fits" %(odir, basename), c.mask, header)
                    # (c.mask is a boolean numpy array, that gets converted here to an integer array)
                
                self.ui.progressBar.setProperty("value", math.ceil(100*(float(float(it)/float(self.ui.listWidget.count())))))
                
app = QtGui.QApplication(sys.argv)
f = MyForm()
f.show()

app.exec_()
