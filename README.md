# insovio.com

INSOVIO'nun web sitesi. Tek sayfalık, Türkçe ve İngilizce statik bir site.

- `index.html`: sayfanın tamamı (metinler, stiller ve dil değiştirme kodu)
- `img/`: görseller
- `en/index.html`: İngilizce adres (insovio.com/en/). `index.html` her değiştiğinde `python3 tools/build_en.py` ile yeniden üretilir; elle düzenlenmez.

Tek adım `tools/build_en.py`; bunun dışında dosyalar olduğu gibi herhangi bir statik barındırmada yayınlanabilir.
GastroSens ön kayıt bağlantısı: https://forms.gle/f3bLTrSBrMYMptt48
