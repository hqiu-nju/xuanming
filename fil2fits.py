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
    parser.add_argument('-o', '--output',type=str, default="test",help='Output File Name')
    # parser.add_argument('--ra',type=float, default=51436.202,help='RA')
    # parser.add_argument('--dec',type=float, default=270330.24,help='Dec')
    # parser.add_argument('-c','--ch1',type=int, default=0,help='starting channel')
    # parser.add_argument('-n','--nchans',type=int, default=8192,help='total channels')
    # parser.add_argument('-b','--bin',type=int, default=1,help='tscrunch samples per bin, must be dividend of subintegration?')
    # parser.add_argument('--fbin',type=int, default=1,help='fscrunch samples per bin')
    # parser.add_argument('-N','--segments',type=int, default=20,help='how many files per filterbank segment')
    parser.add_argument(dest='files', nargs='+')
    parser.set_defaults(verbose=False)
    values = parser.parse_args()
    for fil in values.files:
        original_file=Your(fil)
        length=original_file.your_header.nspectra
        writer_object = Writer(
            original_file,
            nstart=0,
            nsamp=length,
            # c_min=0,
            # c_max=100,
            outdir=".",
            outname=values.output)
        writer_object.to_fits()





if __name__ == '__main__':
    _main()
