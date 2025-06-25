from googletrans import Translator;

translator = Translator()

out = translator.translate('my name is ayush', dest='hi')
print(out.text)

