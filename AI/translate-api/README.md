# Translate API
配置环境变量认证
```
export GOOGLE_APPLICATION_CREDENTIALS=" "
```

## translate_demo_v2.py
https://cloud.google.com/translate/docs/simple-translate-call#translate_translate_text-python   
Cloud Translation 基本版 (v2)   
### run  

运行
检测可用语言
```
python3 translate_demo_v2.py list-languages

python3 translate_demo_v2.py detect-language "hello"
Text: hello
Confidence: 1
Language: en

python3 translate_demo_v2.py translate-text  zh-CN  "hello"
Text: hello
Translation: 你好
Detected source language: en
```

## curl POST 提交
本地翻译文件为translate-api/request.json
```
curl -X POST \
-H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
-H "Content-Type: application/json; charset=utf-8" \
-d @request.json \
https://translation.googleapis.com/language/translate/v2
```