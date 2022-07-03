from YaUploader import YaUploader

if __name__ == '__main__':
    path_to_file = 'C:\API\myfile.txt'
    token = ""

    uploader = YaUploader(token=token)
    result = uploader.upload(path_to_file=path_to_file)
