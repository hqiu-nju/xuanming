#directory is /fred/oz002/hqiu/superhero/

#### merge psrfits to consecutive strip using pfits

pfitsUtil_searchmode_combineTime -o test.fits vegas_59556_78365_Ursa_minor_0007_000*.fits

### convert files to filterbank

psrfits2fil.py test.fits -o ursa_minor_test.fil
## use following flags?
# --noweights  Do not apply weights when converting data.
# --noscales   Do not apply scales when converting data.
# --nooffsets  Do not apply offsets when converting data.

### run heimdall on filterbanks


heimdall -f ursa_minor_test.fil -dm 20 1000 -output_dir ursa_minor_test
