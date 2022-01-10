
"""
Code to move psrfits search files into filterbank files using astropy/your,
pure python header transport
you can also try and fix the headers yourself

"""
import your
import numpy as np
import os
__author__ = "Harry Qiu"


def _main():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    from your.formats.filwriter import make_sigproc_object
    parser = ArgumentParser(description='Script description', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Be verbose')
    parser.add_argument('-o', '--output',type=str, default="test.fil",help='Output File Name')
    parser.add_argument('--ra',type=float, default=51436.202,help='RA')
    parser.add_argument('--dec',type=float, default=270330.24,help='Dec')
    parser.add_argument(dest='files', nargs='+')
    parser.set_defaults(verbose=False)
    values = parser.parse_args()
    filname=values.output
    print(values.files)
    for i,filename in enumerate(values.files):
        fits= your.Your(filename)
        print(filename)
        totaldata=fits.get_data(nstart=0,nsamp=1024*np.int(fits.nsubints))
        ### reads out stokes I data
        ### this step reads all subints to merge into one datachunk, can't stop printing subint readouts

        hdu=fits.fits
        if i ==0:
            newdata=make_sigproc_object(rawdatafile  = filname,
                                        source_name = "bar",
                                        nchans  = fits.nchan,
                                        foff = fits.foff, #MHz
                                        fch1 = fits.fch1, # MHz
                                        tsamp = hdu['SUBINT'].header["TBIN"], # seconds
                                        tstart = fits.tstart, #MJD
                                        src_raj=values.ra, # HHMMSS.SS
                                        src_dej=values.dec, # DDMMSS.SS
                                        machine_id=0,
                                        nbeams=0,
                                        ibeam=0,
                                        nbits=fits.nbits,
                                        nifs=1,
                                        barycentric=0,
                                        pulsarcentric=0,
                                        data_type=0,
                                        az_start=-1,
                                        za_start=-1,
                                        )
            newdata.write_header(filname)
        newdata.append_spectra(totaldata,filname)

if __name__ == '__main__':
    _main()
