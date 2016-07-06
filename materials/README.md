# Materials

The materials folder is destined to include all materials used in the research, such as stimuli or copies of the survey used. This folder can be extended by adding subfolders when there are multiple studies, to provide better oversight. 

The email files were collected from Web of Science, 2005-2015, topic "psychology". The search resulted in 21,116 results (collected on 6 July 2016), after further refining the search to "Research Area: Psychology"; "Type: Article"; "Language: English". This was done using the collect_emails.py (it required some manual work, so if you want to do it note that the script sucks).

To concatenate the files from `raw_wos` the following script was used (`pwd` was set to the materials folder)

```bash
x=PT,AU,BA,BE,GP,AF,BF,CA,TI,SO,SE,BS,LA,DT,CT,CY,CL,SP,HO,DE,ID,AB,C1,RP,EM,RI,OI,FU,FX,CR,NR,TC,Z9,U1,U2,PU,PI,PA,SN,EI,BN,J9,JI,PD,PY,VL,IS,PN,SU,SI,MA,BP,EP,AR,DI,D2,PG,WC,SC,GA,UT,PM

cat raw_wos/* | sed 's/\t/,/g' > concatenated_raw.csv
echo $x > temp
cat temp concatenated_raw > wos_info.csv
rm temp concatenated_raw
```