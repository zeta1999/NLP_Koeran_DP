# -*- coding=utf-8 -*-
import sys

kaist_to_sejong = {
    'sp' : 'SP', 'sf' : 'SF',
    'sl' : 'SS', 'sr' : 'SS',
    'sd' : 'SO', 'se' : 'SE',
    'su' : 'SW', 'sy' : 'SW',

    'f' : 'SL',

    'ncpa' : 'NNG', 'ncps' : 'NNG',
    'ncn' : 'NNG', 'nq' : 'NNP',
    'nbu' : 'NNB', 'nbn' : 'NNB',
    'npp' : 'NP', 'npd' : 'NP',
    'nnc' : 'NR', 'nno' : 'NR',

    'pvg' : 'VV', 'pvd' : 'VV',
    'paa' : 'VA', 'pad' : 'VA',
    'px' : 'VX',

    'mma' : 'MM', 'mmd' : 'MM',
    'mag' : 'MAG', 'mad' : 'MAD',    # MAD is UNK1
    'maj' : 'MAJ',

    'ii' : 'IC',

    'jcs' : 'JKS', 'jco' : 'JKO',
    'jcc' : 'JKC', 'jcm' : 'JKG',
    'jcv' : 'JKV', 'jca' : 'JKB',
    'jcj' : 'JC', 'jct' : 'JC',
    'jcr' : 'JKQ', 'jp' : 'JP',    # JP is UNK2
    'jxc' : 'JX', 'jxf' : 'JX',
    'jxt' : 'JX',                   # jxt was not on tagset document

    'ef' : 'EF', 'ep' : 'EP',
    'ecc' : 'EC', 'ecs' : 'EC',
    'ecx' : 'EC', 'etn' : 'ETN',
    'etm' : 'ETM',

    'xp' : 'XPN', 'xsn' : 'XSN',
    'xsv' : 'XSV', 'xsm' : 'XSA',
    'xsa' : 'XSA'                   # XSA is UNK3
}

def sejongfy_corpus(corpus):
    sejongfied_corpus = []
    for line in corpus:
        if line.startswith('#') or len(line.strip()) ==0:
            sejongfied_corpus.append(line)
            continue
        else:
            sejongfied_line = sejongfy_line(line)
            sejongfied_corpus.append(sejongfied_line)
    return sejongfied_corpus

def sejongfy_line(line):
    # line = 5  차지하는    차지+하+는  VERB    ncpa+xsv+etm    _   6   acl _   _
    # idx, tok, morphed, eojeol_tag, morph_tagged, _, arc, dep_rel, _, _ = line.split()
    splitted_line = line.split()
    splitted_line[4] = sejongfy_tagged_morph(splitted_line[4])
    return '\t'.join(splitted_line)

def sejongfy_tagged_morph(morph_tagged):
    # morph_tagged = ncpa+xsv+etm
    tags = morph_tagged.split('+')
    sejongfied_tags = [kaist_to_sejong[tag] for tag in tags]
    return '+'.join(sejongfied_tags)


if __name__ == "__main__":
    infile = sys.argv[1]
    outfile = sys.argv[2]

    print(("infile: ", infile))
    print(("outfile: ", outfile))

    with open(infile, 'r') as f_in:
        corpus = f_in.readlines()
    sejongfied_corpus = sejongfy_corpus(corpus)

    with open(outfile, 'w') as f_out:
        for sejongfied_line in sejongfied_corpus:
            if sejongfied_line.startswith('#') or len(sejongfied_line.strip()) ==0:
                f_out.write(sejongfied_line)
            else:
                f_out.write(sejongfied_line + '\n')



