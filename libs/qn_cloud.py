from qiniu import Auth, put_file

from swiper import config


def upload_to_qiniu(filename, filepath):
    '''上传到七牛云'''
    # 构建鉴权对象
    qn_auth = Auth(config.QN_AK, config.QN_SK)
    # 要上传的空间
    bucket_name = config.QN_BUCKET_NAME
    # 上传后保存的文件名
    key = filename
    # 生成上传 Token, 可以指定过期时间等
    token = qn_auth.upload_token(bucket_name, key, 3600)

    # 要上传文件的本地路径
    put_file(token, key, filepath)

    url = '%s/%s' % (config.QN_BASE_URL, key)

    return url
