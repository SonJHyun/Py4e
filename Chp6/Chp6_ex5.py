str = 'X-DSPAM-Confidence: 0.8475 '

atPos = str.find('0')
print(atPos)

lastPos = str.find(' ', atPos)
print(lastPos)

floatToFind = str[atPos:lastPos]
print(floatToFind)

finalFloat = float(floatToFind)
print(finalFloat)
print(type(finalFloat))