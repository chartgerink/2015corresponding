# Materials

The materials folder is destined to include all materials used in the research, such as stimuli or copies of the survey used. This folder can be extended by adding subfolders when there are multiple studies, to provide better oversight. 

The email files were collected from Web of Science, 2005-2015, topic "psychology". The search resulted in 21,116 results (collected on 6 July 2016), after further refining the search to "Research Area: Psychology"; "Type: Article"; "Language: English". This was done using the collect_emails.py (it required some manual work, so if you want to do it note that the script sucks).

To concatenate the files from `raw_wos` the following script was used (`pwd` was set to the materials folder)

```bash
cat raw_wos/* | grep -A 10 "^EM " | grep "^EM " | cut -c 4- > emails

cat raw_wos/* | grep -A 10 "^EM " | grep "^PY " | cut -c 4- > years
```

Emails and years is manually combined in spreadsheet program and saved to csv. Unique email list subsequently created with the following R code

```R
x <- read.csv(file = 'collated_emails_years.csv', header = FALSE, stringsAsFactors = FALSE)

x <- unique(unlist(strsplit(x$V1, '; ', fixed = TRUE)))

write.table(x, 'emails_uniq.csv', row.names = FALSE, col.names = FALSE)
```