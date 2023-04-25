### Moddalar
Quyidagi moddlar mavjud
```python
 '123',
 '128-1',
 '128¹-1',
 '128⁴-1',
 '128⁴-2',
 '128⁵-1',
 '128⁵-2',
 '128⁶-1',
 '129-1',
 '130-1',
 '137',
 '147-1',
 '147-2'
 ```
 Va ularning soni mos ravishda:
 
 <img width="321" alt="image" src="https://user-images.githubusercontent.com/24993718/232384461-adfa3ee7-4e6f-4f3d-8d9f-bd5db7e18b89.png">


Moddalar kengroq tavsifi uchun quyidagini qarang: [Moddalar.pdf](Moddalar.pdf).

### Datani yuklash
Quyidagiga boring: `scripts/yuklash.py`


### Holatlar
#### '128⁵-2', qarama qarshi yo’ldan harakatlanish moddasi.

Moving
https://docs.google.com/document/d/1hQ47u96GML-y-UL5LldV7pMsZ22_70RFW9T7E9TF6X0/edit
Fixed
https://docs.google.com/document/d/1q_CcHwMaupQ7Z35s0QLMT4q1cBaGc9Mh0oYKO4xVSZU/edit



**Yechim**
- 1-talik uzluksiz chiziqni aniqlash - 1 
- 2-talik uzluksiz chiziqni aniqlash - 1
- Orientatsiyasini bilishimiz kerak 
  - chap - mashinani detect qilishimiz kerak - 1
  - o’ng - mashinani detect qilishimiz kerak - 1
- Chiziq ustudaligini aniqlashimiz kerak - 1
- Chap yoki o’ng tomondaligini bilishimiz kerak
  - kordinatalarni solishtiramiz: mashina va chiziq

#### 128-1, kod -26 yo’l belgi ‘znak’
Fixed
https://docs.google.com/document/d/1pjQoE3kQ12B6210yYEaEiUtRkOpYoJMHO1Ix54tv-Mc/edit
Moving
https://docs.google.com/document/d/1fTk8iSD-h1SqCT95oKWZ8X0fXXKrKMMoQcy1Y1Dh1cg/edit

**Yechim**
- Mashinani to’xtab turishini aniqlaydigan model kerak: tracking asosida bo’ladi
- stop belgini aniqlaydigan model kerak
- yo’l belgilarini aniqlaydigan model kerak
- Mashina xillarini aniqlaydigan model: yuk, yengil
- Pedestrian detection



### Tanlanganlar
#### 128-4, 101:To’xtash chizig’ini bosish
Fixed - OK
https://docs.google.com/document/d/1Rmy7jdqJApREYLK5MZJPVOEy-uTCjTPhv5KKYVUJKoM/edit

**Yechim**
- Svetaforni aniqlaydigan model kerak
- chiziqni aniqlaydigan model kerak
- mashinani aniqlaydigan model kerak
- Mashina chiziq uztidaligini aniqlaydigan model kerak


#### 128-1, 90: Yo'l chiziq polosa  
Fixed - OK
https://docs.google.com/document/d/1OH9-WS3OvUhvr5kSULrCb-r7dOGge_abJYOIerBAR44/edit

**Yechim**
- 1/2-talik chiqizni aniylaydigan model
- mashina aniqlaydigan model
- mashina chiziq ustidami degan model kerak
- Label qilyotganda chiziq bilan birga olishimiz kerak, chiqiz bo’lmasa tashlab ketamiz.


#### 130-1,  kod - 48: Transport vositalari haydovchilarining temir yo’lni o’tish joylaridan o’tish qoidalarini buzishi

Fixed - OK
https://docs.google.com/document/d/1o_h_DN2y4-2o34zLpCYhw6dk6G1Mt69OmbJpf9hXUUk/edit
Moving
https://docs.google.com/document/d/1HV4HNN_P2kfxF9i8apYpPbU1I5RWEOFQQhNqdIvw6K8/edit


**Yechim**
- Faqat qizil yonadi, shunda to’xtash kerak
- Mashina aniqlaydigan model kerak
- Traffic light aniqlaydigan model kerak
- Qora chiziqni aniqlaydigan model kerak
- temir yo’lni aniqlaydigan model kerak
- stop belgini aniqlaydigan model kerak











