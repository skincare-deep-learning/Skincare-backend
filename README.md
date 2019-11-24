[![Build Status](https://travis-ci.org/skincare-deep-learning/Skincare-backend.svg?branch=master
)](https://travis-ci.org/skincare-deep-learning/Skincare-backend.svg?branch=master
)


# Skincare Backend
Flask Rest Api to classify skin diseases images 

## Run

### Docker

```bash
$ sudo docker-compose up --build
```

### Endpoints

```
localhost:5000/classifier
```
- POST: Accept an image, with the name's parameter "file", and return its name.
