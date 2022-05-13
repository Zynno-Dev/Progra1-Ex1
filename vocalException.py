def vocalCounter(palabra):
    vocal = 0
    try:
        for letra in palabra:
            if letra in "aeiouAEIOU":
                vocal += 1
        return vocal
    except:
        return "Error"

print(vocalCounter("hola"))