
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
    parser = ArgumentParser(description='Script description', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Be verbose')
    parser.add_argument('-o', '--output',type=str, default="test",help='Output File Name')
    parser.add_argument('--ra',type=float, default=51436.202,help='RA')
    parser.add_argument('--dec',type=float, default=270330.24,help='Dec')
    parser.add_argument('-c','--ch1',type=int, default=0,help='starting channel')
    parser.add_argument('-n','--nchans',type=int, default=8192,help='total channels')
    parser.add_argument('-b','--bin',type=int, default=1,help='tscrunch samples per bin, must be dividend of subintegration?')
    parser.add_argument('--fbin',type=int, default=1,help='fscrunch samples per bin')
    parser.add_argument('-N','--segments',type=int, default=20,help='how many files per filterbank segment')
    parser.add_argument(dest='files', nargs='+')
    parser.set_defaults(verbose=False)
    values = parser.parse_args()
    seg=values.segments
    filname=values.output
    fillength=len(values.files)
    inject_iter=fillength//seg+1
    # print(values.files,fillength,inject_iter)
    for i in range(inject_iter):
        print(f"reading files {values.files[i*seg:(i+1)*seg]}, writing to {filname}_{i}.fil")
        write_filterbanks(values,files=values.files[i*seg:(i+1)*seg],filname=f"{filname}_{i}.fil")




def write_filterbanks(values,files,filname):
    from your.formats.filwriter import make_sigproc_object
    for i,filename in enumerate(files):
        fits= your.Your(filename)
        hdu=fits.fits
        if i ==0:
            print()
            newdata=make_sigproc_object(rawdatafile  = filname,
                                        source_name = "bar",
                                        nchans  = values.nchans,
                                        foff = fits.foff, #MHz
                                        fch1 = fits.fch1+fits.foff*values.ch1, # MHz
                                        tsamp = hdu['SUBINT'].header["TBIN"]*values.bin, # seconds
                                        tstart = fits.tstart, #MJD
                                        src_raj=values.ra, # HHMMSS.SS
                                        src_dej=values.dec, # DDMMSS.SS
                                        machine_id=0,
                                        nbeams=1,
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

        print(filename)
        totaldata=fits.get_data(nstart=0,nsamp=1024*int(fits.nsubints))[:,values.ch1:values.ch1+values.nchans]
        writedata=totaldata.reshape(values.bin,-1,values.nchans).mean(0)
        ### reads out stokes I data
        ### this step reads all subints to merge into one datachunk, can't stop printing subint readouts
        newdata.append_spectra(writedata.astype(np.int8),filname)

if __name__ == '__main__':
    _main()
