### Substances
The following items are available
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
  And their number, respectively:
 
  <img width="321" alt="image" src="https://user-images.githubusercontent.com/24993718/232384461-adfa3ee7-4e6f-4f3d-8d9f-bd5db7e18b89.png">


For a more detailed description of the Articles, see [Articles.pdf](Articles.pdf).

### Loading data
Go to: `scripts/download.py`


### Cases
#### '128⁵-2', article of oncoming traffic.

Moving
https://docs.google.com/document/d/1hQ47u96GML-y-UL5LldV7pMsZ22_70RFW9T7E9TF6X0/edit
Fixed
https://docs.google.com/document/d/1q_CcHwMaupQ7Z35s0QLMT4q1cBaGc9Mh0oYKO4xVSZU/edit



**Solution**
- Identifying a continuous line of 1 - 1
- Determination of 2 continuous lines - 1
- We need to know the orientation
   - left - we need to detect the car - 1
   - right - we need to detect the car - 1
- We need to determine the dominance of the line - 1
- We need to know whether it is left or right
   - we compare coordinates: car and line

#### 128-1, code -26 line symbol 'znak'
Fixed
https://docs.google.com/document/d/1pjQoE3kQ12B6210yYEaEiUtRkOpYoJMHO1Ix54tv-Mc/edit
Moving
https://docs.google.com/document/d/1fTk8iSD-h1SqCT95oKWZ8X0fXXKrKMMoQcy1Y1Dh1cg/edit

**Solution**
- We need a model that detects when the car stops: it will be based on tracking
- a model that detects a stop sign is needed
- a model that detects road signs is needed
- The model that determines the types of cars: cargo, light
- Pedestrian detection



### Selected
#### 128-4, 101: Pushing the stop line
Fixed - OK
https://docs.google.com/document/d/1Rmy7jdqJApREYLK5MZJPVOEy-uTCjTPhv5KKYVUJKoM/edit

**Solution**
- We need a model that detects traffic lights
- a line-defining model is needed
- a car identifying model is required
- We need a model that detects when the car is on the line


#### 128-1, 90: The road is a lane
Fixed - OK
https://docs.google.com/document/d/1OH9-WS3OvUhvr5kSULrCb-r7dOGge_abJYOIerBAR44/edit

**Solution**
- 1/2 output model
- a machine-detectable model
- a model of whether the car is on the line is needed
- When making a label, we must take it along with the line, if it does not come out, we will throw it away.


#### 130-1, code - 48: Violation of the rules of crossing railway crossings by drivers of vehicles

Fixed - OK
https://docs.google.com/document/d/1o_h_DN2y4-2o34zLpCYhw6dk6G1Mt69OmbJpf9hXUUk/edit
Moving
https://docs.google.com/document/d/1HV4HNN_P2kfxF9i8apYpPbU1I5RWEOFQQhNqdIvw6K8/edit


**Solution**
- It only lights up red, then you have to stop
- A machine-detectable model is required
- We need a model that detects traffic light
- Need a model that detects the black line
- a model that identifies the railway is needed
- a model that detects a stop sign is needed
