# -*- coding: utf-8 -*-
'''
 brutifus: a set of Python modules to process datacubes from integral field spectrographs.\n
 Copyright (C) 2018,  F.P.A. Vogt
 
 -----------------------------------------------------------------------------------------
 
 This file contains general tools for the brutifus routines to fit the stellar continuum and 
 the emission lines in an IFU data cube.

 Created November 2018, F.P.A. Vogt - frederic.vogt@alumni.anu.edu.au
'''
# ----------------------------------------------------------------------------------------

import numpy as np
import signal 
from astropy.constants import c

from .brutifus_metadata import __version__ as version
 
 # ----------------------------------------------------------------------------------------      
  
def init_worker():
   '''Handles KeyboardInterrupt during multiprocessing.
   
   :Notes:
      See https://noswap.com/blog/python-multiprocessing-keyboardinterrupt
   '''
   signal.signal(signal.SIGINT, signal.SIG_IGN)

# ----------------------------------------------------------------------------------------      
  
def hdu_add_brutifus(hdu,procstep):
   '''Adds dedicated brutifus keywords to a FITS file header.
    
   :Args:
      hdu: FITS hdu
           The destination hdu to which the brutifus keywords must be added.
      procstep: string
                The name of the processing step creating the FITS file.
    
   :Returns:
      out: FITS header
           The newheader with brutifus info included.   
   '''
    
   hdu.header['BRUTIFUS'] = (version, 'brutifus version')
   hdu.header['B_STEP'] = (procstep, 'brutifus processing step')
    
   return hdu
    
# ----------------------------------------------------------------------------------------      
  
def hdu_add_wcs(newhdu,refheader):
   '''Adds the WCS coordinates from a reference header to a new hdu.
    
   :Args:
      newheader: FITS hdu
                 The destination hdu to which the WCS keywords must be added.
      refheader: FITS header
                 The reference header, from which to transer the WCS keywords.
    
   :Returns:
      out: FITS hdu
           The new hdu with WCS info included.   
   :Notes:
      Keywords transfered are  'CRPIX1', 'CD1_1', 'CTYPE1', 'CUNIT1', 'CRPIX2', 'CD2_2',
      'CTYPE2', 'CUNIT2', 'CD1_2', 'CD2_1', 'CRVAL1' and 'CRVAL2'.
   '''
    
   newhdu.header['CRPIX1'] = refheader['CRPIX1']
   newhdu.header['CD1_1'] = refheader['CD1_1']
   newhdu.header['CTYPE1'] = refheader['CTYPE1']
   newhdu.header['CUNIT1'] = refheader['CUNIT1']
   newhdu.header['CRPIX2'] = refheader['CRPIX2']
   newhdu.header['CD2_2'] = refheader['CD2_2']
   newhdu.header['CTYPE2'] = refheader['CTYPE2']
   newhdu.header['CUNIT2'] = refheader['CUNIT2']
   newhdu.header['CD1_2'] = refheader['CD1_2']
   newhdu.header['CD2_1'] = refheader['CD2_1']
   newhdu.header['CRVAL1'] = refheader['CRVAL1']
   newhdu.header['CRVAL2'] = refheader['CRVAL2']
   
   return newhdu
# ----------------------------------------------------------------------------------------      
    
def hdu_add_lams(newhdu,refheader):
   '''Adds the wavelength information from a reference header to a new hdu.
    
   :Args:
      newhdu: FITS hdu
              The destination hdu to which the wavelength keywords must be added.
      refheader: FITS header
                 The reference header, from which to transer the wavelength keywords.
    
   :Returns:
      out: FITS hdu
           The newheader with wavelength info included.   
   :Notes:
      Keywords transfered are 'CTYPE3', 'CUNIT3', 'CD3_3', 'CRPIX3', 'CRVAL3', 'CD1_3', 
      'CD2_3', 'CD3_1' and 'CD3_2'.
   '''
    
   newhdu.header['CTYPE3'] = refheader['CTYPE3'] 
   newhdu.header['CUNIT3'] = refheader['CUNIT3']   
   newhdu.header['CD3_3'] = refheader['CD3_3']
   newhdu.header['CRPIX3'] = refheader['CRPIX3']
   newhdu.header['CRVAL3'] = refheader['CRVAL3']
   newhdu.header['CD1_3'] = refheader['CD1_3']
   newhdu.header['CD2_3'] = refheader['CD2_3']
   newhdu.header['CD3_1'] = refheader['CD3_1']
   newhdu.header['CD3_2'] = refheader['CD3_2']
 
   return newhdu    
 
# ----------------------------------------------------------------------------------------

def inst_resolution(inst = 'MUSE', get_ff = False, show_plot=False):
    '''Returns the functional resolution of an instrument as a function of the wavelength.
    
    Returns a callable function of the wavelength (in Angstroem !).
    
    :Args:
        inst: string [default: 'MUSE']
              The name tag referring to a given instrument.
        get_ff: bool [default: False]
                Whether to recompute the given function from a reference dataset or not.
                Only valid with inst = 'MUSE'.
        show_plot: bool [default: False]
                   Whether to make a plot of the function.
    
    :Returns:
        R(lambda): function
                   A function that takes a float (lambda in Angstroem, and returns the 
                   corresponding value of the chosen instrument resolution.
    
    :Notes:
        Supported instruments: 'MUSE'
    
    '''
     
    if inst == 'MUSE':
       if get_ff:
          this_fn_path = os.path.dirname(__file__)
          ref_fn = 'MUSE_specs/MUSE_spectral_resolution.txt'
          R_lam = np.loadtxt(os.path.join(this_fn_path,ref_fn),
                           skiprows = 1)
                           
          # Fit a polynomial to this. Deg 3 works well.
          z = np.polyfit(R_lam[:,0]*10.,R_lam[:,1],3)
          p = np.poly1d(z)
          
          if show_plot:
             plt.close(99)
             plt.figure(99)
             
             lams = np.arange(4500,10000.,1)
             
             plt.plot(lams,p(lams), 'b-')            
             plt.plot(R_lam[:,0]*10.,R_lam[:,1], 'k.')
             
             plt.show()
          
       else:
           #Fit on 02.2016:
           p = np.poly1d([ -8.27037043e-09, 1.40175196e-04, -2.83940026e-01, 7.13549344e+02])
           
       return p    
                    
    else:
        sys.exit('Unknown instrument...') 
 
 
        