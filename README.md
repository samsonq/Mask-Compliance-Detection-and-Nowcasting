# Mask-Compliance-Detection-and-Nowcasting


## Objective
<todo>

## Summary
<todo>

## Processes
1. <b>Build Computer Vision Detector </b>\
We implement a YOLO detection model to accurately and consistently identify individuals not following social-distancing guidelines. The strictness of the guidelines can be adjusted accordingly.
2. <b>Incorporate Blockchain Storage </b>\
The use of blockchain ledgers and smart contracts preserve the integrity of the data and allows for easy analysis of social distancing practices throughout different locations.
3. <b>Deploy and Monitor Social Distancing </b>\
Deploying the detection model to video feed of webcams and record social distancing. The detections made by the model are flowing through the blockchain and good/bad distancing are recorded.

## Screenshots
![detector](./screenshots/detector.png)

## Run Guide
Navigate to the src folder and run main.py (Use --help to see the full list of options): 
```
python main.py
```
The application will be running on: http://localhost:8000

## TODO
Host application with Heroku
