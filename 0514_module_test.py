import turtle as tt
tt.TurtleScreen._RUNNING = True  # 启动绘图，在IDE中运行加这句可避免报错
cnt = 0
while cnt < 5:
    tt.forward(200)
    tt.right(144)
    cnt += 1
tt.done()  # 结束绘图，这将不会关闭窗口

