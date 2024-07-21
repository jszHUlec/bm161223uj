"""
zrob dekodowanie i kodowanie tekst do formatu base64
"""
import base64

tekst = b"Hellow World"

print(base64.b64encode(tekst))

tekst2 = "SGVsbG93IFdvcmxk"
print(base64.b64decode(tekst2))

