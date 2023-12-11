openssl ecparam -genkey -name prime256v1 -noout -out ec_private.pem
openssl ec -in ec_private.pem -pubout -out ec_public.pem
# careful! this will output your private key in terminal
cat ec_private.pem | base64

curl -s -I "http://$INGRESS_HOST:$INGRESS_PORT/headers" -H "Authorization: Bearer eyJhbGciOiJFUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjQ2ODU5ODk3MDAsImZvbyI6ImJhciIsImlhdCI6MTUzMjM4OTcwMCwiaXNzIjoiZm9yY2UwLmNvcmFsd29ybGQuY28wIiwic3ViIjoiZm9yY2UwLmNvcmFsd29ybGQuY28ifQ.VPXuLpEh9gXhkxcTmjlwZdFH8VauTArnJWnRDrJ_DL587YJqh9ZeTzC07PUnzif3LwZ_mctbwk9RcKRgbMBY8g" 