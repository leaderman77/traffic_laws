## SWS S3ga fayl yuklash

Qilinadigan ishlar ketma-ketligi:

1. Dastalab `AWS CLI`ni ustanovka qilamiz:
```commandline
sudo apt  install awscli
```
2. `AWS` configuratsiyalarini to'g'irlashimiz kerak, termilaldan quyidagi komanda teriladi: 
```commandline
aws configure
```
enter bosilgandan keyin bazi confilglar so'raladi:
* access key ID
* secret access key
* default region name
* output format

`output format` qismida hech narsa kirtish kerak emas shunchaki `enter` bosilsa bo'ldi.

3. Filelarni terminal orqali yuklashimiz mumkin:
```commandline
aws s3 cp example.txt s3://my-bucket/
```
bu yerda:
* exmaple.txt - yuklamoqchi bo'lgan filemiz bizda `*.zip` bo'ladi.
* my-becket - buketimiz nomi(papka nomi desak ham bo'ladi)