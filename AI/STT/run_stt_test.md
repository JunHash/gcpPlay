# STT 测试Demo
## 设置Service Account
```
 export GOOGLE_APPLICATION_CREDENTIALS=/Users/***/mywork/gcpServiceAccount/service-account-all.json
```
## Audio 转码
https://cloud.google.com/speech-to-text/docs/base64-encoding#linux   
Linux
```
base64 source_audio_file -w 0 > dest_audio_file
```
```
{
    "config": {
    "encoding":"FLAC",
    "sampleRateHertz":16000,
    "languageCode":"en-US"
    },
    "audio": {
    "content": "ZkxhQwAAACIQABAAAAUJABtAA+gA8AB+W8FZndQvQAyjv..."
    }
}
```
## Restful 请求
```
curl  -s -H "Content-Type: application/json"     -H "Authorization: Bearer "$(gcloud auth application-default print-access-token)     https://speech.googleapis.com/v1/speech:recognize     -d @audio_test.json


________________
{
  "results": [
    {
      "alternatives": [
        {
          "transcript": "5月26日零到20 45新增境外输入确诊病例截止5月26日24时累计报告境外输入确诊病例22例均已出院单日和新增本的确诊病例截止5月26日24时累计报告本的确诊病例631例均已出院担任吴昕真无症状感染",
          "confidence": 0.97102386
        }
      ]
    }
  ]
```
```
curl   -w "time_total: %{time_total}"  -s -H "Content-Type: application/json"     -H "Authorization: Bearer "$(gcloud auth application-default print-access-token)     https://speech.googleapis.com/v1/speech:recognize     -d @audio_test.json


{
  "results": [
    {
      "alternatives": [
        {
          "transcript": "5月26日零到二十四十五星村境外输入确诊病例截止5月26日24时累计报告境外输入确诊病例22例均已出院单日和新增本的确诊病例截止5月26日24时累计报告本的确诊病例631例均已出院担任吴昕真无症状感染",
          "confidence": 0.9030035
        }
      ]
    }
  ]
}
time_total: 7.044044

```