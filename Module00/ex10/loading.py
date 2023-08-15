import time
import sys

# def ft_progress(lst):
#     start_time = time.time()
#     total = len(lst)
#     length = 10
#     for elem, index in enumerate(lst):
#         progress = (index + 1) / total
#         elapsed_time = time.time() - start_time
#         eta = (elapsed_time / progress) - elapsed_time
#         yield elem
        
#         bar = f"ETA: {eta:5.2f}s [{int(progress * 100):3d}%][{int(progress * length) * '=' + '>':{length}s}] {index:4d}/{total} | elapsed time {elapsed_time:.2f}s"
#         sys.stdout.write(bar)
#         sys.stdout.flush()
#         sys.stdout.write("\r")
    

def ft_progress(list):
    start_time = time.time()
    start = list[0]
    end = list[len(list) - 1]
    total = end - start
    length = 20
    eta = 0
    
    for index in range(start,end):
        progress = (index / total) * 100
        pr_bar = round((progress / 100) * length) 
        yield index
        
        c_bar = (f"ETA:{eta:5.2f}s [{int(progress):3d}%][{'=' * pr_bar}]")
        print(c_bar, end="\r")
      
        
        
if __name__ == "__main__":
    
        listy = range(1000)
        ret = 0
        for elem in ft_progress(listy):
            ret += (elem + 3) % 5
            time.sleep(0.01)
        print()
        print(ret)
