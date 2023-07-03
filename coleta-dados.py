import json 

dictionary =[
    { 
        "ticker" : "BOVA11", 
        "ultimo" : 114.32, 
        "strike" : 8.6, 
        "vencimento" : "2023-12-15"
    },
    { 
        "ticker" : "BOVAG105", 
        "ultimo" : 10.98, 
        "strike" : 105.00, 
        "vencimento" : "2023-07-21"
    },
    { 
        "ticker" : "BOVAH950", 
        "ultimo" : 21.33, 
        "strike" : 95.00, 
        "vencimento" : "2023-08-15"
    }
] 

texto=""
for linha in dictionary:
    texto += f"<p>{linha['ticker']}; {linha['ultimo']}; {linha['strike']}; {linha['vencimento']}</p>\n"

with open("cotacoes-b3/index.html", "w") as outfile: 
    text  = '<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8"/>\n<title>Extraindo dados da B3</title>\n</head\n>'
    text += f'<body>\n{texto}</body>\n</html>'
    outfile.write(text)