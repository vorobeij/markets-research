from src.data import tradingeconomics_data


def tradingeconomics_report():
    body = "".join(tradingeconomics_data())

    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        $body
    </body>
    </html>""".replace('$body', body)

    text_file = open("output/tradingeconomics.html", "w")
    text_file.write(template)
    text_file.close()
