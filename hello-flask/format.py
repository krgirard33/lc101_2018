markup = """
<!DOCTYPE html>
<html>
    <head>
        <titel>{0}</title>
    </head>
    <body>
        <h1>{1}</h1>
    </body>
</html>
"""

other = """
<!DOCTYPE html>
<html>
    <head>
        <titel>{title}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""

markup = markup.format('My Page title', 'Page Heading')
other = other.format(title='2nd Page title', heading='2nd Page Heading')
print(markup, other)