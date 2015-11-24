# November 13, 2015
1. Idea conceived
2. Idea = collect corresponding author(s) email(s) from papers across fields, and send them an email. Check whether they bounce, or conceive some other form of automated reply as criterium for no longer in use.
3. Separate the authors' email addreses per year, and see whether there is an increase in bounces over the years.
4. Note that one email might be prevalent across multiple years, such that i would have to think about how to handle it by sending only one email and incorporating that result across the data.
5. this would be a authors x years matrix
6. as such, if same author email is in e.g., 2006 and 2010, note both as bounced if it bounced.
7. odds would be computed per year
8. and these would be plottable.

# november 20, 2015
1. met with it-department, suggested using swaks to probe emails instead of actually delivering message to inbox.

# november 22, 2015
1. might be useful code later `swaks -f someone@example.net -t liquidat@example.com --quit-after RCPT`
2. seems like this would work `swaks --t chjh@protonmail.com --server smtp.gmail.com/587 -tls -a LOGIN --quit-after RCPT`
3. now just need to find a loop and write out the emails that (do not) bounce
4. `for E in 'cat /path/to/email/file'
do
     swaks --to $E --server test-server.example.com --quit-after RCPT --hide-all
     [ $? -ne 0 ] && echo $E
done`
5. need to add -au [ausername] and -ap [apassword]
6. need to figure out the server and protocol to use uni mail
7. results in
`for E in 'corresponding_emails'
do
     swaks --to $E --server [test-server.example.com] -tls -au [user] -ap [password] --quit-after RCPT --hide-all
     [ $? -ne 0 ] && echo $E >> tested_email
done`
8. would first need to run `touch tested_email`
9. 
