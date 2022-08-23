from translate import Translator
trns=  Translator(from_lang = "Italian", to_lang="Dutch")
trns_text = trns.translate("Buongiorno!")
print(trns_text)