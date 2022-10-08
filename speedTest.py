import speedtest

test = speedtest.Speedtest(secure=1)
download = test.download()
upload = test.upload()
print(f'Download: {download / 1024:.2f}')
print(f'Upload: {upload / 1024:.2f}')
