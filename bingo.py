#! /usr/bin/python

################################################################################
# This file is part of dr-bingo
# Copyright (C) 2016 Bert Vandenbroucke (bert.vandenbroucke@gmail.com)
#
# dr-bingo is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Shadowfax is distributed in the hope that it will be useful,
# but WITOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Shadowfax. If not, see <http://www.gnu.org/licenses/>.
#
# Poorly forked Finnish version for Eurovision Song Contest 2018 
# by mucla (github.com/mucla).
################################################################################

import numpy as np

# list of words that are likely to be mentioned during the presentation
# mind the manual hyphenation, which is necessary to ensure every word fits
likely = ["Tuulikone", "Suomen lippu katsomossa", "Asun\\-vaihdos", 
        "Pakko laulaa mukana", "Ylireippaat tanssijat", "Laahus tai liehukkeet",
         "Modulaatio","Wtf-hetki", "Suomi saa 12 pistetta", "Vilkutus kameraan",
        "Balladi", "Maailman\\-parannus\\-biisi", "Joku ylosalaisin", "Vanhus lavalla",
        "Siansaksaa lyriikoiden joukossa", "Lento\\-suukko", 
        "Pisteiden antaja jaa juttelemaan liian pitkaan juontajan kanssa", 
        "Valtava laahus, jota esiintyja ei pysty (itse) liikuttamaan", 
        "Laulaja iskee silmaa kameralle", "Mies laulaa sakeistot, nainen laulaa kertsit",
        "Juontajat vitsailevat ennalta sovitusti ja eparennosti", "Juontajat \"piilo\"\\-mainostaa oheiskraasaa",
        "Haviaja yrittaa hymyilla reippaasti", 
        "Joku viime vuosien voittajista nakyy muualla kuin esityksessa",
        "Juontaja kertoo, etta artisti on itse suunnitellut pukunsa"]
likely = np.array(likely)

# list of words that are less likely to be mentioned
unlikely = ["Tukka totterolla", "Koskettava kohtalo", "Disko\\-humppa", 
            "Artisti on alle 18-vuotias ja se mainitaan erikseen juonnossa",
            "Laulajalla on rooliasu, (ammatti, hahmo, tms.)",
            "Naislaulaja riisuu pitkan mekon tai takin", "Mieslaulaja riisuu takin",
            "Tanssijat nostavat laulajan ilmaan", 
            "Laulaja soittaa pari savelta jollain instrumentilla ja sitten hylkaa sen loppubiisin ajaksi",
            "Laulajan kaula-aukko ulottuu napaan asti"]
unlikely = np.array(unlikely)

file = open("bingo.tex", "w")

file.write(r"""\documentclass[10pt]{letter}
\usepackage{a4wide}
\usepackage{tabularx}
\usepackage{graphicx}
\begin{document}""")

# the number of iterations sets the number of bingo squares
# they are put on separate a4 pages
for i in range(8):
    file.write(r"""
    \thispagestyle{empty}
    \begin{center}
    \Huge{}
    \bf{}
    {Viisubingo 2018}\\[18pt]
    \end{center}
    
    \Small
    \begin{tabularx}{\textwidth}{| >{\centering{}\arraybackslash}X | 
    >{\centering{}\arraybackslash}X | >{\centering{}\arraybackslash}X |
    >{\centering{}\arraybackslash}X | >{\centering{}\arraybackslash}X |
    @{}m{0pt}@{}}
    \hline
    """)
    
    # make sure every line and column contains an unlikely word
    specials = np.random.permutation([0, 1, 2, 3, 4])

    likely = np.random.permutation(likely)
    unlikely = np.random.permutation(unlikely)

    li = 0
    ui = 0
    words = []
    for i in range(5):
        for j in range(5):
            if specials[i] == j:
                words.append(unlikely[ui])
                ui += 1
            else:
                words.append(likely[li])
                li += 1

    words = np.array(words)

    count = 0
    for word in words:
        file.write("{word}".format(word = word))
        count += 1
        if count%5 == 0:
            file.write(" & \\\\[44pt]\\hline\n")
        else:
            file.write(" & ")

    file.write("\\end{tabularx}\\clearpage{}\n")

file.write("\\end{document}")