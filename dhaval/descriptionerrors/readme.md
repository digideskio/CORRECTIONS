# Abnormal ngrams in description

See https://github.com/sanskrit-lexicon/CORRECTIONS/issues/309 for details

# Usage

`python ngramdescription.py vcp yat`

Here the first dictionary (vcp) is base dictionary, against which test dictionary (yat) is compared.

Reason for choosing VCP as base is that this dictionary has largest bigrams and trigrams when it comes to Sanskrit words / sentences.

# TODO (Pending dictionaries)

	handleddictlist = ['ap90','ap','bor','pd','vcp','pw','pwg','bop','gst','mwe','shs','yat','wil','skd']

All dictionaries other than these are pending to be handled.

Reasons are multifarious, e.g. description not in SLP1, very specific dictionaries like INM / SNP etc.