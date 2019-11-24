[![Build Status](https://travis-ci.org/skincare-deep-learning/Skincare-backend.svg?branch=master
)](https://travis-ci.org/skincare-deep-learning/Skincare-backend.svg?branch=master
)


# Skincare Backend
Flask Rest Api to classify skin diseases images

## Usage

### Docker

```bash
$ sudo docker-compose up --build
```
```
Access: localhost:5000
```

### Remote
```
 https://skincare-deep-learning.herokuapp.com
```

### Endpoints

#### Send an image to classification

**Definition**

`POST /classifier`

**Arguments**

- `"files":` image to be sent 
- `"name":file` the image's name must be 'file' 
- `"enctype="multipart/form-data"` how the image must be encoded

The image will get a list of the possible and its probabilities. The image classification is related to the greater probability among all provided.

**Response**

- `200 Ok` on success

```json
{
    "data": "List of diseases with its probabilities"
}
```