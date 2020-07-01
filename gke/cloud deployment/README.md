# run cloud deployment
## 配置service account
```
export GOOGLE_APPLICATION_CREDENTIALS=/Users/***/mywork/gcpServiceAccount/service-account-all.json
```
##启动服务
```
gcloud deployment-manager deployments create gke-test  --config gke-cluster.yaml

__________________
The fingerprint of the deployment is b'TVb7n-ZBK1dOdTR68tmvog=='
Waiting for create [operation-1593595469140-5a95ddbda9226-11394e95-52594850]...⠏ 
```