from datetime import date
import os.path
import yagmail

def email(path, from, to):
    date = date.today()
    year = date.strftime("%Y")
    if os.path.exists(path + '{}_survey.csv'.format(year)):
        contents = ["The {} Survey has been downloaded!".format(year)]
        return contents

    else:
        contents = ["No new surveys available :("]
        return contents

    yagmail.SMTP(from).send(to, '***SO Survey Download Alert***', contents)





if __name__ == "__main__":
    path = 'home/user/Project/Surveys/'
    from = 'my_secret_mail@gmail.com'
    to = 'my_developer_mail@gmail.com'
    email(path, from, to)
