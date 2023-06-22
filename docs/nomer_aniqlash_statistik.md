### Maqshinalar davlat raqamini aniqlash uchun report

1. Bajarilgan ishlar :
    - `assets` fayl ichidagi `images` faylga test qilinadigan rasmlarni yuklab olamiz.
    - `assets` fayl ichida `result_imgs` nomli bosh fayl ochib olamiz
    - `../scripts/alpr/run_subprocess.py` filega `license_plate_recognizer.py` kodni joyini berib olami
    - terminalda `python run_subprocess.py` codi joylashgan filega borib olib `python run_subprocess.py` buyrug'i orqali
      kodimizni ishlatib olamiz
    - natijalar `result_imgs` bosh faylimizga yuklanadi
2. Natija va statistika :
   - Modelsiz qilingan test
   
      | asli                                           | result_imgs                                         |
      |------------------------------------------------|-----------------------------------------------------|
      | ![00059.jpg](..%2Fassets%2Fimages%2F00059.jpg) | ![00059.jpg](..%2Fassets%2Fresult_imgs%2F00059.jpg) |
      | ![00080.jpg](..%2Fassets%2Fimages%2F00080.jpg) | ![00080.jpg](..%2Fassets%2Fresult_imgs%2F00080.jpg) |
      | ![00114.jpg](..%2Fassets%2Fimages%2F00114.jpg) |   ![00114.jpg](..%2Fassets%2Fresult_imgs%2F00114.jpg)                                                  |
      | ![00153.jpg](..%2Fassets%2Fimages%2F00153.jpg) |   ![00153.jpg](..%2Fassets%2Fresult_imgs%2F00153.jpg)                                                  |

