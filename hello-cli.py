import argparse

languages_dict = {
                 'english': 'Hello', 'russian': 'Привет', 'bashkirian': 'Һаумыһығыҙ', 
                 'tatarian':'Исәнмесез', 'spanish':'Hola', 'vietnamian': 'Xin chào'
                 }

parser = argparse.ArgumentParser(
                    prog='hello cli',
                    description='Writes "hi" in 3 languages')

parser.add_argument('-n', '--name', help='write your name')

parser.add_argument('-sl', '--setlanguage',
                     action='extend',
                     help='set 3 languages', 
                     default=[]
                   )

parser.add_argument('-ll', '--languagelist', 
                    action='store_true', 
                    help='write all language', 
                   )


args = parser.parse_args()
name = args.name
language = args.setlanguage
if args.languagelist:
    for i in languages_dict.keys():
        print(i)

for i in language:
    print(languages_dict[i], name)
