from speedtest import Speedtest

wifi = Speedtest()

print("Getting download speed...")
download = wifi.download()
print(f"Download: {download / 1024 /1024:.2f}mb/s")


print("Getting upload speed...")
upload = wifi.upload()
print(f"Upload: {upload / 1024 / 1024:.2f}mb/s")
