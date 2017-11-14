#A collection of scripts for gathering email addresses. Different scripts depending on the situation. 

For right now, it is just clipboardSnatcher, more will come soon.  Stay tuned.



clipboardSnatcher.py - Little Python script that pulls email addresses from the clipboard.


TO USE - It doesn't matter what the source of the data is (doc, txt, pdf, xls, web page, whatever).
just Ctrl + A and then Ctrl + C that bad boy... the entire thing.  A copy of everything will be held on the clipboard. Next, run clipboardSnatcher.py to extract emails from the clipboard.  No need to do anything else, just enter ./clipboardSnatcher.py and it will pull emails from the clipboard and output them to the terminal.  But wait, there's more.  It will also automatically put the snatched emails back onto the clipboard for you to paste into a text file.  Based on the work by Al Sweigart (he does good work).

Why use? - This tool isn't dependant on the what type of format the data is stored in.  For example, you could run across the online employee directory for company MegaCorpOne.  You could simply Ctrl + A and Ctrl + C the entire directory and run clipboardSnatcher to extract the emails.  This tool is perfect for those times when you have access to data, but for one reason or another, don't have the ability to access the data directly as a file.  If you can highlight and copy the entire thing, you're golden.
