from googletrans import Translator
t = Translator()
print("Welcome to CLI Translator\n")
while True:
 i = input("Enter text for translation(type 'exit' for quit): \n")
 if i=="exit":
  break
 tl = input("Enter target language: ")
 try:
  td = t.translate(i, dest=tl)
  print(f"Translated: {td.text}")
 except Exception as e:
  print(f"Invalid input: {e}")


