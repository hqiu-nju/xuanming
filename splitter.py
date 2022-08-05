import your
### a short implementation to convert filterbank to psrfits
your.__version__

from your import Your, Writer
import os
import numpy as np


def _main():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description='Script description', formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Be verbose')
    parser.add_argument('-o', '--output',type=str, default="_cutout",help='Output File Name')
    parser.add_argument('-d', '--outdir',type=str, default="./",help='Output Directory')
    parser.add_argument('-f','--fch1',type=int, default=0,help='split band start (freq)')
    parser.add_argument('-c','--nchan',type=int, default=336,help='number of channels')
    parser.add_argument('-x','--tstart',type=int, default=0,help='split band start (time)')
    parser.add_argument('-s','--samples',type=int, default=-1,help='number of samples -1 for entire length')
    parser.add_argument('-m', '--mode',type=int, default=0,help='Output File Format, 0 -- filterbank ; 1 -- fits')

    parser.add_argument(dest='files', nargs='+')
    parser.set_defaults(verbose=False)
    values = parser.parse_args()
    for fil in values.files:
        original_file=Your(fil)
        length=original_file.your_header.nspectra
        if values.samples==-1:
            cut_L=length
        else:
            cut_L=values.samples
        writer_object = Writer(
            original_file,
            nstart=values.tstart,
            nsamp=cut_L,
            c_min=values.fch1,
            c_max=values.fch1+values.nchan,
            outdir=values.outdir,
            outname=values.output)
        print(f"writing cutout from {fil} to new file")
        if values.mode == 0:
            writer_object.to_fil()
        elif values.mode == 1:
            writer_object.to_fits()




if __name__ == '__main__':
    _main()
