# Amazon S3

## Buckets
objects( files )를 buckets에 저장한다.

### Objects
- Objects는 `s3://my-bucket/my_file.txt`와 같은 형식으로 full path로 key를 소유하고 있다. 
- Objects values는 최대 5TB이지만 5GB 이상은 나눠서 multi-part upload로 올려야 한다.
- key - value 페어로 Metadata가 있다.