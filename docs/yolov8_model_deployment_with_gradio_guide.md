## Gradio bilan YOLOv8 Obyekt Aniqlash

Ushbu repozitoriy YOLOv8 obyekt aniqlash modelini Gradio doirasida qurilgan ilovani o'z ichiga oladi. Ushbu ilova sizga video yuklash va yuklangan vidyo natijalarni o'ng panelda ko'rish imkoniyatini beradi.

## Talablar
Boshlashdan oldin quyidagi kerakli kutubxonalarni o'rnatilganiga ishonch hosil qiling:

Python 3.6 yoki undan yuqori versiya
pip paket boshqaruvchisi

## O'rnatish

pip install gradio

## Foydalanishdan oldin

Siz talablaringizga muvofiq ilovaning turli qismlarini moslashtirishingiz mumkin:

Model: app.py fayldagi "model = YOLO("../output/weights/best.pt")" qatorni o'zizda mavjud bo'lgan YOLOv8ning kerakli model fayliga o'zgartiring. Ozgartirayotkanda modelni direktoriyasiga e'tibor bering.

## Foydalanish

1. Bu repozitoriyani o'z kompyuteringizga klonlang:
   'https://github.com/cradle-uz/traffic_laws.git'
2. Loyiha branchiga o'ting: 'git checkout gradio-model-deployment'
3. Loyiha direktoriyasiga o'ting: 'cd gradio'
4. Gradio ilovasini ishga tushiring: terminal orqali gradio python app.py yoki PyCharmda 'Run app.py'
5. Veb-brauzeringizni oching va http://127.0.0.1:7860 manziliga o'ting.
   ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/e68c4d70-dabc-40a0-84cc-49cb6853a5a5)
6. Veb interfeysida fayl yuklash tugmasini topasiz. Ustiga bosing va obyekt aniqlamoqchi bo'lgan video faylini tanlang.
   ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/b63c8744-23fd-42f3-bbad-af6ffc3d77cf)
7. Vidyo yuklandikdan so'ng, protses boshlanishi uchun "Submit" tugmasini bosing. 
   ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/bfcceb5e-9f79-4d95-86c8-11ad2b002520)
8. Video yuklandikdan so'ng, YOLOv8 modeli video kadrlarida obyektlarni aniqlaydi. Aniqlangan obyektlar o'ng panelda ko'rsatiladi.
9. Muxim: Vidyo protsess jarayonida protses ketayotkanliga ishonch xosil qiling. Vidyo protsess yuklangan vidyo hajmiga qarab bir necha daqiqani oladi.
   
   ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/746900dd-d123-485c-8c2e-c9c31097790b)
10. Vidyo protses tugagandan so'ng "Gradio" direktoriyasida 2ta yangi fayl yaratilishi kerak. Birinchisi - output.mp4 fayl bu obyektlarni aniqlagan kadrlardan tashkil topgan vidyo. Ikkinchisi, annotated_frames.csv fayl bo'lib ichida muammoli framelarni raqamlarini va xar bir aniqlangan frameni vaqtlari yozilgan bo'ladi.
12. Vidyoni natijasini vidyo korinishida Veb-brauserni ozida ko'rsa ham bo'ladi. Yoki output.mp4 ni vidyo o'qidigan ilova yordamida oching.
