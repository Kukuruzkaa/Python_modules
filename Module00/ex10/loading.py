import time

def ft_progress(list):
    start_time = time.time()
    total = len(list)
    length = 20
    eta = 0
    
    if total == 0:
        total = 1
    for index in range(total):
        elapsed_time = time.time() - start_time
     
        percentage = ((index + 1) / total) * 100
        if percentage > 0:
            eta = (elapsed_time * 100) / percentage
        progress = int((percentage * length) / 100)
        yield index
        
        c_bar = (f"ETA:{eta:.2f}s [{int(percentage):3d}%][{'=' * progress + '>':{length}s}] {index + 1:4d}/{total} | elapsed time {elapsed_time:.2f}s")
        print(c_bar, end="\r")
      
# if __name__ == "__main__":
    
#         listy = range(0, -100, -1)
#         ret = 0
#         for elem in ft_progress(listy):
#             ret += (elem + 3) % 5
#             time.sleep(0.01)
#         print()
#         print(ret)
