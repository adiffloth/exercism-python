def convert(number):
    result = ''
    factored = False
    if number % 3 == 0:
        result = result + 'Pling'
        factored = True
    if number % 5 == 0:
        result = result + 'Plang'
        factored = True
    if number % 7 == 0:
        result = result + 'Plong'
        factored = True
    
    if not factored:
        result = str(number)

    return result