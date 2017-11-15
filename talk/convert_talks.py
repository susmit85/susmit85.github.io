import sys
lines = []
with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
for talk in lines:
    print(talk.strip('\n'))
    fields = talk.strip().split('.')
    filename = fields[1].strip().replace(' ','-') +'.md'
    string = '+++\ndate = '+ fields[0] + '\ntitle ="'+fields[1]+'"\nlocation ="'+ fields[2] +'"\n'
    print filename, string
    with open(filename, 'w') as w:
        w.write(string)
        w.write('''
                # Is this a selected talk? (true/false)
selected = false

# Projects (optional).
#   Associate this talk with one or more of your projects.
#   Simply enter the filename (excluding '.md') of your project file in `content/project/`.
projects = ["deep-learning"]

# Links (optional).
url_pdf = ""
url_slides = ""
url_video = ""
url_code = ""

# Does the content use math formatting?
math = true

# Does the content use source code highlighting?
highlight = true

+++
''')
