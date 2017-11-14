#!/usr/bin/env python3
'''
 ██████╗██╗     ██╗██████╗ ██████╗  ██████╗  █████╗ ██████╗ ██████╗                            
██╔════╝██║     ██║██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔══██╗██╔══██╗                           
██║     ██║     ██║██████╔╝██████╔╝██║   ██║███████║██████╔╝██║  ██║                           
██║     ██║     ██║██╔═══╝ ██╔══██╗██║   ██║██╔══██║██╔══██╗██║  ██║                           
╚██████╗███████╗██║██║     ██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝                           
 ╚═════╝╚══════╝╚═╝╚═╝     ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝                            
                                                                                               
        ███████╗███╗   ██╗ █████╗ ████████╗ ██████╗██╗  ██╗███████╗██████╗    ██████╗ ██╗   ██╗
        ██╔════╝████╗  ██║██╔══██╗╚══██╔══╝██╔════╝██║  ██║██╔════╝██╔══██╗   ██╔══██╗╚██╗ ██╔╝
        ███████╗██╔██╗ ██║███████║   ██║   ██║     ███████║█████╗  ██████╔╝   ██████╔╝ ╚████╔╝ 
        ╚════██║██║╚██╗██║██╔══██║   ██║   ██║     ██╔══██║██╔══╝  ██╔══██╗   ██╔═══╝   ╚██╔╝  
        ███████║██║ ╚████║██║  ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║██╗██║        ██║   
        ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝        ╚═╝  

Little Python script that pulls email addresses from the clipboard.

Warning.  If you are using Debian based OS, you may get this error:
"pyperclip could not find a copy/paste mechanism for your system."
If you do, make sure you install xsel (sudo apt install xsel) and this should fix it.

TO USE - It doesn't matter what the source of the data is (doc, txt, pdf, xls, web page, whatever).
just Ctrl + A and then Ctrl + C that bad boy... the entire thing.  A copy of everything will be held on the clipboard. Next, run clipboardSnatcher.py to extract emails from the clipboard.  No need to do anything else, just enter ./clipboardSnatcher.py and it will pull emails from the clipboard and output them to the terminal.  But wait, there's more.  It will also automatically put the snatched emails back onto the clipboard for you to paste into a text file.  Based on the work by Al Sweigart (he does good work).

Why use? - This tool isn't dependant on the what type of format the data is stored in.  For example, you could run across the online employee directory for company MegaCorpOne.  You could simply Ctrl + A and Ctrl + C the entire directory and run clipboardSnatcher to extract the emails.  This tool is perfect for those times when you have access to data, but for one reason or another, don't have the ability to access the data directly as a file.  If you can highlight and copy the entire thing, you're golden.

This script depends on Pyperclip to run.

This Python script was written by James Russell.

Usage:  ./clipboardSnatcher.py

'''


import pyperclip, re


#Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)


#Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in emailRegex.findall(text):
    matches.append(groups[0])

#Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Emails found!  Ready to paste!")
    print("")
    print('\n'.join(matches))
else:
    print("No email addresses found.")