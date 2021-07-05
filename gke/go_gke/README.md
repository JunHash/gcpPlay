# Golang 使用demo
https://github.com/googleapis/google-cloud-go

## 环境配置
### golang
```
go mod init go_gke
go mod tidy
```
### Service Key 配置
如果配置好gcloud 忽略一下步骤
```
export GOOGLE_APPLICATION_CREDENTIALS= "*****/devopev-editor.json"
```
## GKE
### list cluster
执行代码
```
go run listgke.go  -project devopev -zone us-central1-c

-----------------------------
Cluster "cluster-test" (RUNNING) master_version: v1.19.9-gke.1900  -> Pool "default-pool" (RUNNING) machineType=e2-medium node_version=v1.19.9-gke.1900 autoscaling=fal
```
