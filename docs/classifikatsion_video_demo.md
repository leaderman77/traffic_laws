## Berilgan videoni clasifikatsiya moduli orqali muammoli joylarni aniqlash

1. Videoni biz classifikatsiya modulidan foydalanib [kod](https://github.com/cradle-uz/traffic_laws/blob/video_demo_classification/scripts/classificatsion_video_demo.py)
   
   kod orqali videoni fremnlarga o'tqazib, undagi muaamoli rasmlarni yuklab oldik va natijani va
   👉 [bu](https://drive.google.com/drive/folders/1TyijJpv5I1dOFQlUJkKayGSAhYv015n4) yerga yuklandi

2. olingan videolarni video ko'riinshiga [kod](https://github.com/cradle-uz/traffic_laws/blob/video_demo_classification/scripts/frame_do_video.py)
  
   codan foydalanib keltirdik va bu 👉 [bu](https://drive.google.com/drive/folders/1lPyXneWOwdVV4Qq-eP9mFpMcaoo-McxF)
   yerga yuklandi

## Xulosa:

| Nomi               | asli | problem | good |
|--------------------|------|---------|------|
| vid_39_1284-2_1174 | 117  | 117     | 0    |
| vid_39_1284-2_1202 | 149  | 38      | 111  |
| vid_39_1284-2_1204 | 199  | 76      | 123  |
| vid_39_1284-2_1207 | 149  | 50      | 99   |
| vid_39_1284-2_1215 | 249  | 93      | 156  |
| vid_39_1284-2_1220 | 326  | 104     | 222  |
| vid_39_1284-2_1237 | 133  | 39      | 94   |
| vid_39_1284-2_1250 | 199  | 52      | 147  |
| vid_39_1284-2_1254 | 249  | 67      | 182  |
| vid_39_1284-2_1293 | 952  | 386     | 566  |



## Model qilingan videolar

| Nomi                       | asli | problem                       | good |
|----------------------------|------|-------------------------------|------|
| vid_39_1284-2_1174_problem | 117  | 1(99 - rasm)                  | 116  |
| vid_39_1284-2_1202_problem | 38   | 18(12 - 30 rasmlar)           | 20   |
| vid_39_1284-2_1204_problem | 76   | 24(13 - 37 rasmlar)           | 52   |
| vid_39_1284-2_1207_problem | 50   | 22(8 - 30 rasmlar)            | 28   |
| vid_39_1284-2_1215_problem | 93   | 68(25 - 93 rasmlar)           | 25   |
| vid_39_1284-2_1220_problem | 104  | 7(77 - 84 rasmlar)            | 97   |
| vid_39_1284-2_1237_problem | 39   | 30(1 - 15 va 23 - 39 rasmlar) | 9    |
| vid_39_1284-2_1250_problem | 52   | 20(4 - 24 rasmlar)            | 32   |
| vid_39_1284-2_1254_problem | 67   | 47(8 - 55 rasmlar)            | 20   |
| vid_39_1284-2_1293_problem | 386  | 358(2 - 360                   | 28   |

Eng ko’p framelar soni `vid_39_1284-2_1293`da 386ta

Eng kam framelar soni `vid_39_1284-2_1202`da 38ta

Eng ko’p problem framelar `vid_39_1284-2_1293`da 358ta

Eng kam problem framelar `vid_39_1284-2_1174`da 1ta

Eng ko’p good framelar `vid_39_1284-2_1174`da 116ta

Eng kam good framelar `vid_39_1284-2_1237`da 9ta

Ba'zi xatoliklar ham aniqlandi ,videodagi problem qilib olingan lekin bular good uchunn misol boladi

`vid_39_1284-2_1202` 
![img.png](..%2Fdata%2Frasm%2Fimg.png)

`vid_39_1284-2_1220` 

![img_1.png](..%2Fdata%2Frasm%2Fimg_1.png)
![img_2.png](..%2Fdata%2Frasm%2Fimg_2.png)

Modul asosan qoida buzarlikdan oldinroq ya'ni aynan chiziq ustida emas undan oldinroq yoki keyinroqdan boshlamoqda