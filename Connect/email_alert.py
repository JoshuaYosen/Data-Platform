import yagmail

contents = ["test"]


yagmail.SMTP('joshuayosen@gmail.com').send('joshuayosen@gmail.com', '**Stack Overflow Download Alert**', contents)
