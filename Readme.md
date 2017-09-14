## Instructions to follow Run as Server

1. wget http://www.festvox.org/flite/packed/flite-2.0/
2. tar -zvxf flite-2.0.0-release.tar.gz
3. cd flite-2.0.0-release/
4. ./configure --enable-shared
5. make
6. make install
7. wget http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_indic_knr_te.flitevox
8. wget http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_indic_slp_mr.flitevox
9. wget http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_indic_sxs_hi.flitevox
10. wget http://www.festvox.org/flite/packed/flite-2.0/voices/cmu_indic_sxv_ta.flitevox
11. sudo python run.py

## Client {Curl - request}

## Generate Speech Output

### Request
curl -X POST \
  http://url:port/tts/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: f3cdeafc-bd51-b710-495a-2a0048cd9366' \
  -d '{
	"input" : "சென்று வருகிறேன்",
	"language": "tamil"
}'

### Response
{
    "language": "tamil",
    "message": "success",
    "output_file": "tamil_4.wav",
    "status": "success"
}

## Download output

### Request
curl -X POST \
  http://urk:port/download/ \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 61cd6d80-919b-ade6-61b7-a382980cb7e6' \
  -d '{
	"filename" : "tamil_4.wav"
}'

### Supported Languages
-   English, Tamil, Telugu, Marathi and Hindi