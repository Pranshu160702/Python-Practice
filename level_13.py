import re

pattern = r"[a-z]+he"
text = '''Air pollution is contamination of the indoor or outdoor environment by any chemical, physical or biological agent that modifies the natural characteristics of the atmosphere. Household combustion devices, motor vehicles, industrial facilities and forest fires are common sources of air pollution.'''

match = re.search(pattern, text)
print(match)
matches = re.finditer(pattern, text)
for match in matches:
    print(match)
    
# import asyncio

# async def func():
#     await asyncio.sleep(1)
#     print("Async")
    
# async def main():
#     task = asyncio.create_task(func())
#     await func()
    
# asyncio.run(main())

# Threads -> Threading is used to perform actions parallely in the background

import threading
import time 

def new_func(seconds):
    print(f"We slept for {seconds} minutes")
    time.sleep(seconds)
    return seconds
    
# start_time = time.perf_counter()
# # Without Threading
# new_func(3)
# new_func(2)
# new_func(1)
# end_time = time.perf_counter()
# print(int(end_time - start_time))
    
# start_time = time.perf_counter()
# # Without Threading
# t1 = threading.Thread(target=new_func, args=[3])
# t2 = threading.Thread(target=new_func, args=[2])
# t3 = threading.Thread(target=new_func, args=[1])
# t1.start()
# t2.start()
# t3.start()
# t1.join()
# t2.join()
# t3.join()
# end_time = time.perf_counter()
# print(int(end_time - start_time))

# Multiprocessing as the name suggests does the task of doing various process at once
import multiprocessing
import requests

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"files/file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")

if __name__ == '__main__':
    url = "https://picsum.photos/2000/3000"
    pros = []
    for i in range(5):
        # downloadFile(url, i)
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
