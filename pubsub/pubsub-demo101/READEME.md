# spring boot pubsub101
https://spring.io/guides/gs/messaging-gcp-pubsub/#initial
https://github.com/spring-cloud/spring-cloud-gcp/blob/master/spring-cloud-gcp-samples/spring-cloud-gcp-pubsub-sample/README.adoc

## Build
### GCP auth 
option 1(推荐)   
SA配置：
```aidl
#spring.cloud.gcp.project-id=local-alignment-284902
#spring.cloud.gcp.credentials.location=file:[LOCAL_FS_CREDENTIALS_PATH]
```
Option 2    
user认证 
```aidl
gcloud auth application-default login
gcloud config set project my-project
```
### Restful Run
http://localhost:8080/swagger-ui.html#/web-controller
创建topic
```aidl
curl -X POST "http://localhost:8080/createTopic?topicName=springboot-test" -H "accept: */*"
```
创建订阅
```aidl
curl -X POST "http://localhost:8080/createSubscription?subscriptionName=springboot-sub-test&topicName=springboot-test" -H "accept: */*"
```
## Code
