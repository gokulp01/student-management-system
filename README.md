
<img src="https://github.com/gokulp01/slcm_api/blob/master/mages/mahelogo.png?raw=true" height="200" /> 			
# SLCM API(With Captcha Support)
The SLCM API is simple,secure web application based on Flask that allows for retrieving attendance and marks data from the [SLcM Website](https://slcm.manipal.edu) .

### Usage
#### CLI
``` bash
  curl -X POST \
  -H "Content-Type: application/json" \
  -d@./request.json \
  https://slcm-api.ml/api/v1/get
```
### Request Format 
The server expects requests to be in the following format: 

``` JSON
{
      "username":"<USERNAME>",
      "password":"<PASSWORD>"
      "type":"<TYPE>"
}
```
Type can be set to ```ATTENDANCE``` , ```MARKS``` or ```ALL``` depending on what is required.

### Response Format

For Attendance: 
``` 
{
    "attendance": [
        {
            "Academic Year": "<ACADEMIC-YEAR>",
            "Attendance(%)": "<PERCENTAGE>",
            "Days Absent": "<AB>",
            "Days Present": "<PR>",
            "Semester": "VI",
            "Subject": "ENGINEERING ECONOMICS AND FINANCIAL MANAGEMENT",
            "Subject Code": "HUM 4002",
            "Total Class": "25"
        },
        {
            "Academic Year": "2019-2020",
            "Attendance(%)": "<PERCENTAGE>",
            "Days Absent": "<AB>",
            "Days Present": "<PR>",
            "Semester": "VI",
            "Subject": "DISTRIBUTED SYSTEMS",
            "Subject Code": "ICT 3201",
            "Total Class": "19"
        },
        .
        .
        .
        .
        {
            "Academic Year": "2019-2020",
            "Attendance(%)": "<PERCENTAGE>",
            "Days Absent": "<AB>",
            "Days Present": "<PR>",
            "Semester": "VI",
            "Subject": "INTRODUCTION TO POLISH LANGUAGE AND CULTURE",
            "Subject Code": "IIE 3209",
            "Total Class": "0"
        }
    ]
}
```
For Marks:
``` 
{
    "marks": [
        {
            "Internal": "Internal Sessional 1",
            "Marks Obtained": "15.00",
            "Maximum Marks": "15.00",
            "sub_code": "HUM 4002",
            "sub_name": "ENGINEERING ECONOMICS AND FINANCIAL MANAGEMENT",
            "type": "Internal"
        },
        .
        .
        .
        .
        {
            "Assignment": "Total Marks",
            "Marks Obtained": "10.00",
            "Maximum Marks": "10.00",
            "sub_code": "ICT 4012",
            "sub_name": "NEURAL NETWORK AND FUZZY LOGI",
            "type": "Assignment"
        }
    ]
}
```

Incase both marks and attendance are requested, they are concatenated into a single JSON Object.

[![Maintenance](https://img.shields.io/maintenance/yes/2020?color=green&logo=github)](https://github.com/L3thal14)
[![Maintenance](https://img.shields.io/maintenance/yes/2020?color=green&logo=github)](https://github.com/gokulp01)


![built with love](https://forthebadge.com/images/badges/built-with-love.svg)

