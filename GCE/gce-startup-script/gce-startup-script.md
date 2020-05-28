# GCE Startup 启动脚本
## gcloud 创建GCE   
[google 文档参考 启动脚本](https://cloud.google.com/compute/docs/startupscript?_ga=2.52840296.-1966959884.1579600848#gcloud)

[gcloud compute 命令 ](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create)
```
gcloud compute instances create  nginx-instance-script \
    --metadata-from-file startup-script=nginx_startup.sh

——————————————————
Created [https://www.googleapis.com/compute/v1/projects/devopev/zones/us-central1-b/instances/nginx-instance-script].
NAME                   ZONE           MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP   EXTERNAL_IP   STATUS
nginx-instance-script  us-central1-b  n1-standard-1               10.128.13.68  34.70.33.146  RUNNING
```
登陆GCE，验证运行进程
```
~$ ps -ef | grep nginx

____________________________________
root      2206     1  0 Mar14 ?        00:00:00 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
www-data  2207  2206  0 Mar14 ?        00:03:49 nginx: worker process
junsong  11149 11124  0 12:03 pts/0    00:00:00 grep nginx

curl -I localhost
________________________________
HTTP/1.1 200 OK
Server: nginx/1.10.3
Date: Thu, 28 May 2020 12:04:21 GMT
Content-Type: text/html
Content-Length: 625
Last-Modified: Sat, 14 Mar 2020 21:00:27 GMT
Connection: keep-alive
ETag: "5e6d45eb-271"
Cache-Control: public, max-age=604800
Accept-Ranges: bytes
```