import torch, gc

gc.collect()
torch.cuda.empty_cache()

# import torch
# import time
#
# # gpu = torch.device('cuda')
# # 如果用cpu测试那么注释掉上面的代码, 用下面的
# gpu = torch.device('cpu')
#
# beginTime = time.time()
#
# a = torch.rand(2048, 2048)
# b = torch.rand(2048, 2048)
# c = torch.rand(2048, 2048)
#
# x = a.to(gpu)
# y = b.to(gpu)
#
# z = c.to(gpu)
#
# initTime = time.time()
# print("ok")
#
# i = 0
#
# while i < 10000:
#     z = (z + x + y)
#     i += 1
#
# endTime = time.time()
#
# print(z)
#
# print("运行结束, 初始化使用了 {} 秒, 循环用了 {} 秒".format(initTime - beginTime, endTime - beginTime))