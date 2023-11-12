## Identifying problem areas through the given video classification module

1. We use the video classification module [code](https://github.com/cradle-uz/traffic_laws/blob/video_demo_classification/scripts/classificatsion_video_demo.py)
   
    We transferred the video to frames using the code and downloaded the corresponding pictures, the result and
    👉 [this](https://drive.google.com/drive/folders/1TyijJpv5I1dOFQlUJkKayGSAhYv015n4) uploaded to earth

2. convert the received videos into a video viewer [code](https://github.com/cradle-uz/traffic_laws/blob/video_demo_classification/scripts/frame_do_video.py)
  
    co and this 👉 [this](https://drive.google.com/drive/folders/1lPyXneWOwdVV4Qq-eP9mFpMcaoo-McxF)
    loaded on the ground

## Summary:

### The result of dividing the model into good and problem

| Name | originally | problem | good |
|-------------------|------|---------|------|
| vid_39_1284-2_1174 | 117 | 117 | 0 |
| vid_39_1284-2_1202 | 149 | 38 | 111 |
| vid_39_1284-2_1204 | 199 | 76 | 123 |
| vid_39_1284-2_1207 | 149 | 50 | 99 |
| vid_39_1284-2_1215 | 249 | 93 | 156 |
| vid_39_1284-2_1220 | 326 | 104 | 222 |
| vid_39_1284-2_1237 | 133 | 39 | 94 |
| vid_39_1284-2_1250 | 199 | 52 | 147 |
| vid_39_1284-2_1254 | 249 | 67 | 182 |
| vid_39_1284-2_1293 | 952 | 386 | 566 |



### Goods were identified in the problem frames separated by the model

| Name | originally | problem | good |
|--------------------------|------|------------ ------------------|------|
| vid_39_1284-2_1174_problem | 117 | 1(99 - picture) | 116 |
| vid_39_1284-2_1202_problem | 38 | 18(12 - 30 pictures) | 20 |
| vid_39_1284-2_1204_problem | 76 | 24(13 - 37 pictures) | 52 |
| vid_39_1284-2_1207_problem | 50 | 22(8 - 30 pictures) | 28 |
| vid_39_1284-2_1215_problem | 93 | 68(25 - 93 pictures) | 25 |
| vid_39_1284-2_1220_problem | 104 | 7 (pictures 77 - 84) | 97 |
| vid_39_1284-2_1237_problem | 39 | 30 (pictures 1 - 15 and 23 - 39) | 9 |
| vid_39_1284-2_1250_problem | 52 | 20(4 - 24 pictures) | 32 |
| vid_39_1284-2_1254_problem | 67 | 47(8 - 55 pictures) | 20 |
| vid_39_1284-2_1293_problem | 386 | 358(2 - 360 | 28 |

The highest number of frames is 386 in `vid_39_1284-2_1293`

The minimum number of frames is 38 in `vid_39_1284-2_1202`

The most problem frames are 358 in `vid_39_1284-2_1293`

The least problem frames are 1 in `vid_39_1284-2_1174`

The most good frames are 116 in `vid_39_1284-2_1174`

The least good frames are 9 in `vid_39_1284-2_1237`

Some errors were also detected, they were considered problems in the video, but these are good examples

`vid_39_1284-2_1202`
![vid_39_1284-2_1202.png](..%2Fdata%2Frasm%2Fvid_39_1284-2_1202.png)

`vid_39_1284-2_1220`

![vid_39_1284-2_1220.png](..%2Fdata%2Frasm%2Fvid_39_1284-2_1220.png)
![vid_39_1284-2_1220_1.png](..%2Fdata%2Frasm%2Fvid_39_1284-2_1220_1.png)

The module is basically starting before or after the violation, not exactly on the line
