### Maqshinalar davlat raqamini aniqlash uchun report

1. Bajarilgan ishlar :
    - `assets` fayl ichidagi `images` faylga test qilinadigan rasmlarni yuklab olamiz.
    - `assets` fayl ichida `result_imgs` nomli bosh fayl ochib olamiz
    - `../scripts/alpr/run_subprocess.py` filega `license_plate_recognizer.py` kodni joyini berib olami
    - terminalda `python run_subprocess.py` codi joylashgan filega borib olib `python run_subprocess.py` buyrug'i orqali
      kodimizni ishlatib olamiz
    - natijalar `result_imgs` bosh faylimizga yuklanadi
2. Natija va statistika :
<<<<<<< HEAD

    -

   | asli                                                              | result_imgs                                                           | aniqligi | 
   |-------------------------------------------------------------------|-----------------------------------------------------------------------|----------|
   | ![00073kvswj8fz.jpg](..%2Fdata%2F839_problem%2F00073kvswj8fz.jpg) | ![00073kvswj8fz.jpg](..%2Fdata%2F839_result_imgs%2F00073kvswj8fz.jpg) |          |
   | ![00074jj5vdan1.jpg](..%2Fdata%2F839_problem%2F00074jj5vdan1.jpg) | ![00074jj5vdan1.jpg](..%2Fdata%2F839_result_imgs%2F00074jj5vdan1.jpg) |          |
   | ![00075q2vveg27.jpg](..%2Fdata%2F839_problem%2F00075q2vveg27.jpg) | ![00075q2vveg27.jpg](..%2Fdata%2F839_result_imgs%2F00075q2vveg27.jpg) |          |
   | ![00077il4rc3bw.jpg](..%2Fdata%2F839_problem%2F00077il4rc3bw.jpg) | ![00077il4rc3bw.jpg](..%2Fdata%2F839_result_imgs%2F00077il4rc3bw.jpg) |          |
   | ![00078pihdz6tb.jpg](..%2Fdata%2F839_problem%2F00078pihdz6tb.jpg) | ![00078pihdz6tb.jpg](..%2Fdata%2F839_result_imgs%2F00078pihdz6tb.jpg) |          |
   | ![00088llkwsnsi.jpg](..%2Fdata%2F839_problem%2F00088llkwsnsi.jpg) | ![00088llkwsnsi.jpg](..%2Fdata%2F839_result_imgs%2F00088llkwsnsi.jpg) |          |
   | ![00089nn8imc04.jpg](..%2Fdata%2F839_problem%2F00089nn8imc04.jpg) | ![00089nn8imc04.jpg](..%2Fdata%2F839_result_imgs%2F00089nn8imc04.jpg) |          |
   | ![00093qo8xi56e.jpg](..%2Fdata%2F839_problem%2F00093qo8xi56e.jpg) | ![00093qo8xi56e.jpg](..%2Fdata%2F839_result_imgs%2F00093qo8xi56e.jpg) |          |
   | ![00096qepofi22.jpg](..%2Fdata%2F839_problem%2F00096qepofi22.jpg) | ![00096qepofi22.jpg](..%2Fdata%2F839_result_imgs%2F00096qepofi22.jpg) |          |
   | ![00097qwcyifgf.jpg](..%2Fdata%2F839_problem%2F00097qwcyifgf.jpg) | ![00097qwcyifgf.jpg](..%2Fdata%2F839_result_imgs%2F00097qwcyifgf.jpg) |          |
   | ![00098f4u_m6op.jpg](..%2Fdata%2F839_problem%2F00098f4u_m6op.jpg) | ![00098f4u_m6op.jpg](..%2Fdata%2F839_result_imgs%2F00098f4u_m6op.jpg) |          |
   | ![00099nd3g5jkl.jpg](..%2Fdata%2F839_problem%2F00099nd3g5jkl.jpg) | ![00099nd3g5jkl.jpg](..%2Fdata%2F839_result_imgs%2F00099nd3g5jkl.jpg) |          |
   | ![00101ymjuinsb.jpg](..%2Fdata%2F839_problem%2F00101ymjuinsb.jpg) | ![00101ymjuinsb.jpg](..%2Fdata%2F839_result_imgs%2F00101ymjuinsb.jpg) |          |
   | ![00103yb0vwd6d.jpg](..%2Fdata%2F839_problem%2F00103yb0vwd6d.jpg) | ![00103yb0vwd6d.jpg](..%2Fdata%2F839_result_imgs%2F00103yb0vwd6d.jpg) |          |
   | ![00104svpaqox7.jpg](..%2Fdata%2F839_problem%2F00104svpaqox7.jpg) | ![00104svpaqox7.jpg](..%2Fdata%2F839_result_imgs%2F00104svpaqox7.jpg) |          |
   | ![00105e3350eqx.jpg](..%2Fdata%2F839_problem%2F00105e3350eqx.jpg) | ![00105e3350eqx.jpg](..%2Fdata%2F839_result_imgs%2F00105e3350eqx.jpg) |          |
   | ![00106dvs1iic0.jpg](..%2Fdata%2F839_problem%2F00106dvs1iic0.jpg) | ![00106dvs1iic0.jpg](..%2Fdata%2F839_result_imgs%2F00106dvs1iic0.jpg) |          |
   | ![00109mbw8xq8u.jpg](..%2Fdata%2F839_problem%2F00109mbw8xq8u.jpg) | ![00109mbw8xq8u.jpg](..%2Fdata%2F839_result_imgs%2F00109mbw8xq8u.jpg) |          |
   | ![00111rt_fi8hu.jpg](..%2Fdata%2F839_problem%2F00111rt_fi8hu.jpg) | ![00111rt_fi8hu.jpg](..%2Fdata%2F839_result_imgs%2F00111rt_fi8hu.jpg) |          |
   | ![00113isgf5tz6.jpg](..%2Fdata%2F839_problem%2F00113isgf5tz6.jpg) | ![00113isgf5tz6.jpg](..%2Fdata%2F839_result_imgs%2F00113isgf5tz6.jpg) |          |
   | ![00114b3qgjv2j.jpg](..%2Fdata%2F839_problem%2F00114b3qgjv2j.jpg) | ![00114b3qgjv2j.jpg](..%2Fdata%2F839_result_imgs%2F00114b3qgjv2j.jpg) |          |
   | ![00115p_ka7ffu.jpg](..%2Fdata%2F839_problem%2F00115p_ka7ffu.jpg) | ![00115p_ka7ffu.jpg](..%2Fdata%2F839_result_imgs%2F00115p_ka7ffu.jpg) |          |
   | ![00124p2l8m5hj.jpg](..%2Fdata%2F839_problem%2F00124p2l8m5hj.jpg) | ![00124p2l8m5hj.jpg](..%2Fdata%2F839_result_imgs%2F00124p2l8m5hj.jpg) |          |
   | ![00125vf7lhzca.jpg](..%2Fdata%2F839_problem%2F00125vf7lhzca.jpg) | ![00125vf7lhzca.jpg](..%2Fdata%2F839_result_imgs%2F00125vf7lhzca.jpg) |          |
   | ![00129jk6rzyl8.jpg](..%2Fdata%2F839_problem%2F00129jk6rzyl8.jpg) | ![00129jk6rzyl8.jpg](..%2Fdata%2F839_result_imgs%2F00129jk6rzyl8.jpg) |          |
   | ![00130ar4inr8d.jpg](..%2Fdata%2F839_problem%2F00130ar4inr8d.jpg) | ![00130ar4inr8d.jpg](..%2Fdata%2F839_result_imgs%2F00130ar4inr8d.jpg) |          |
   | ![00272f_66x6gi.jpg](..%2Fdata%2F839_problem%2F00272f_66x6gi.jpg) | ![00272f_66x6gi.jpg](..%2Fdata%2F839_result_imgs%2F00272f_66x6gi.jpg) |          |
   | ![00273dhj4ebx0.jpg](..%2Fdata%2F839_problem%2F00273dhj4ebx0.jpg) | ![00273dhj4ebx0.jpg](..%2Fdata%2F839_result_imgs%2F00273dhj4ebx0.jpg) |          |
   | ![00275e4tcssqi.jpg](..%2Fdata%2F839_problem%2F00275e4tcssqi.jpg) | ![00275e4tcssqi.jpg](..%2Fdata%2F839_result_imgs%2F00275e4tcssqi.jpg) |          |
   | ![00276en944zsr.jpg](..%2Fdata%2F839_problem%2F00276en944zsr.jpg) | ![00276en944zsr.jpg](..%2Fdata%2F839_result_imgs%2F00276en944zsr.jpg) |          |
   | ![00277ph03ckjj.jpg](..%2Fdata%2F839_problem%2F00277ph03ckjj.jpg) | ![00277ph03ckjj.jpg](..%2Fdata%2F839_result_imgs%2F00277ph03ckjj.jpg) |          |
   | ![00278mk08niwk.jpg](..%2Fdata%2F839_problem%2F00278mk08niwk.jpg) | ![00278mk08niwk.jpg](..%2Fdata%2F839_result_imgs%2F00278mk08niwk.jpg) |          |
   | ![00279jzo1cz2v.jpg](..%2Fdata%2F839_problem%2F00279jzo1cz2v.jpg) | ![00279jzo1cz2v.jpg](..%2Fdata%2F839_result_imgs%2F00279jzo1cz2v.jpg) |          |
   | ![00280rz_itdw3.jpg](..%2Fdata%2F839_problem%2F00280rz_itdw3.jpg) | ![00280rz_itdw3.jpg](..%2Fdata%2F839_result_imgs%2F00280rz_itdw3.jpg) |          |
   | ![00282zlcrp88w.jpg](..%2Fdata%2F839_problem%2F00282zlcrp88w.jpg) | ![00282zlcrp88w.jpg](..%2Fdata%2F839_result_imgs%2F00282zlcrp88w.jpg) |          |
   | ![00283l3tijomk.jpg](..%2Fdata%2F839_problem%2F00283l3tijomk.jpg) | ![00283l3tijomk.jpg](..%2Fdata%2F839_result_imgs%2F00283l3tijomk.jpg) |          |
   | ![00284wid3seps.jpg](..%2Fdata%2F839_problem%2F00284wid3seps.jpg) | ![00284wid3seps.jpg](..%2Fdata%2F839_result_imgs%2F00284wid3seps.jpg) |          |
   | ![00285_7rlj2ao.jpg](..%2Fdata%2F839_problem%2F00285_7rlj2ao.jpg) | ![00285_7rlj2ao.jpg](..%2Fdata%2F839_result_imgs%2F00285_7rlj2ao.jpg) |          |
   | ![000766l520mqk.jpg](..%2Fdata%2F839_problem%2F000766l520mqk.jpg) | ![000766l520mqk.jpg](..%2Fdata%2F839_result_imgs%2F000766l520mqk.jpg) |          |
   | ![000831_lmtdqr.jpg](..%2Fdata%2F839_problem%2F000831_lmtdqr.jpg) | ![000831_lmtdqr.jpg](..%2Fdata%2F839_result_imgs%2F000831_lmtdqr.jpg) |          |
   | ![000916ows2c8d.jpg](..%2Fdata%2F839_problem%2F000916ows2c8d.jpg) | ![000916ows2c8d.jpg](..%2Fdata%2F839_result_imgs%2F000916ows2c8d.jpg) |          |
   | ![000943tdhm74g.jpg](..%2Fdata%2F839_problem%2F000943tdhm74g.jpg) | ![000943tdhm74g.jpg](..%2Fdata%2F839_result_imgs%2F000943tdhm74g.jpg) |          |
   | ![000953ssw_5kb.jpg](..%2Fdata%2F839_problem%2F000953ssw_5kb.jpg) | ![000953ssw_5kb.jpg](..%2Fdata%2F839_result_imgs%2F000953ssw_5kb.jpg) |          |
   | ![001001omhvgw5.jpg](..%2Fdata%2F839_problem%2F001001omhvgw5.jpg) | ![001001omhvgw5.jpg](..%2Fdata%2F839_result_imgs%2F001001omhvgw5.jpg) |          |
   | ![001081z49adb8.jpg](..%2Fdata%2F839_problem%2F001081z49adb8.jpg) | ![001081z49adb8.jpg](..%2Fdata%2F839_result_imgs%2F001081z49adb8.jpg) |          |
   | ![001101uq67rum.jpg](..%2Fdata%2F839_problem%2F001101uq67rum.jpg) | ![001101uq67rum.jpg](..%2Fdata%2F839_result_imgs%2F001101uq67rum.jpg) |          |
   | ![001195jehn_q4.jpg](..%2Fdata%2F839_problem%2F001195jehn_q4.jpg) | ![001195jehn_q4.jpg](..%2Fdata%2F839_result_imgs%2F001195jehn_q4.jpg) |          |
   | ![001311zm2_17d.jpg](..%2Fdata%2F839_problem%2F001311zm2_17d.jpg) | ![001311zm2_17d.jpg](..%2Fdata%2F839_result_imgs%2F001311zm2_17d.jpg) |          |
   | ![002814hawx6ok.jpg](..%2Fdata%2F839_problem%2F002814hawx6ok.jpg) | ![002814hawx6ok.jpg](..%2Fdata%2F839_result_imgs%2F002814hawx6ok.jpg) |          |
   | ![0009238a8u32y.jpg](..%2Fdata%2F839_problem%2F0009238a8u32y.jpg) | ![0009238a8u32y.jpg](..%2Fdata%2F839_result_imgs%2F0009238a8u32y.jpg) |          |
   | ![0010202zsq8wb.jpg](..%2Fdata%2F839_problem%2F0010202zsq8wb.jpg) | ![0010202zsq8wb.jpg](..%2Fdata%2F839_result_imgs%2F0010202zsq8wb.jpg) |          |
   | ![0010758gmmtu3.jpg](..%2Fdata%2F839_problem%2F0010758gmmtu3.jpg) | ![0010758gmmtu3.jpg](..%2Fdata%2F839_result_imgs%2F0010758gmmtu3.jpg) |          |
   | ![0012843o0xk3v.jpg](..%2Fdata%2F839_problem%2F0012843o0xk3v.jpg) | ![0012843o0xk3v.jpg](..%2Fdata%2F839_result_imgs%2F0012843o0xk3v.jpg) |          |
   | ![0013288khicf7.jpg](..%2Fdata%2F839_problem%2F0013288khicf7.jpg) | ![0013288khicf7.jpg](..%2Fdata%2F839_result_imgs%2F0013288khicf7.jpg) |          |
   | ![00090960bjxba.jpg](..%2Fdata%2F839_problem%2F00090960bjxba.jpg) | ![00090960bjxba.jpg](..%2Fdata%2F839_result_imgs%2F00090960bjxba.jpg) |          |
=======
   - Modelsiz qilingan test
   
      | asli                                           | result_imgs                                         |
      |------------------------------------------------|-----------------------------------------------------|
      | ![image](https://github.com/cradle-uz/traffic_laws/assets/106407386/67951ee9-f871-4aeb-8695-c621912c2599) | ![image](https://github.com/cradle-uz/traffic_laws/assets/106407386/03e481ac-f444-4d3d-8110-9aa89365d399)
 |
      | ![00080.jpg](..%2Fassets%2Fimages%2F00080.jpg) | ![00080.jpg](..%2Fassets%2Fresult_imgs%2F00080.jpg) |
      | ![00114.jpg](..%2Fassets%2Fimages%2F00114.jpg) |   ![00114.jpg](..%2Fassets%2Fresult_imgs%2F00114.jpg)                                                  |
      | ![00153.jpg](..%2Fassets%2Fimages%2F00153.jpg) |   ![00153.jpg](..%2Fassets%2Fresult_imgs%2F00153.jpg)                                                  |
>>>>>>> 8a08684a8c55b37a1404a1b99fef0aa966c9d54f


