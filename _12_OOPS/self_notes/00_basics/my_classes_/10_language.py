class Language:
    def __init__(self, local_lang, national_lang, Int_national_lang):
        self.local_lang = local_lang
        self.national_lang = national_lang
        self.Int_national_lang = Int_national_lang

    def my_lang(self):
        print("Language details ", self.local_lang, self.national_lang, self.Int_national_lang)


lang = Language("Bhojpuri", "Hindi", "English")
lang.my_lang()
