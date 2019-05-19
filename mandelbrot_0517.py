"""xiter_mandelbrot.pyw 绘制曼德布罗分形图
"""
import tkinter as tk
import time


def mandelbrot_pixel(c):
    """返回曼德布罗平面像素点对应索引号
    """
    maxiter = 256
    z = complex(0.0, 0.0)
    for i in range(maxiter):
        z = z * z + c
        if abs(z) >= 2.0:
            return i
    return 256


def mandelbrot_image(xa, xb, ya, yb, x, y):
    """返回曼德布罗平面图像字符串
    """
    clr = ["#%02x%02x%02x" % (  # 索引号0-255对应不同颜色
            int(255 * ((i / 255) ** 8)) % 64 * 4,
            int(255 * ((i / 255) ** 8)) % 128 * 2,
            int(255 * ((i / 255) ** 8)) % 256) for i in range(255, -1, -1)]
    clr.append("#000000")  # 索引号256对应黑色
    # 计算复平面坐标对应的像素点
    xm = [xa + (xb - xa) * kx / x for kx in range(x)]
    ym = [ya + (yb - ya) * ky / y for ky in range(y)]
    # 生成图像字符串
    return " ".join((("{" + " ".join(clr[mandelbrot_pixel(complex(i, j))]
                    for i in xm)) + "}" for j in ym))


def main():
    """绘制曼德布罗分形图
    """
    # 复数取值范围
    xa = -2.25
    xb = 0.75
    ya = -1.25
    yb = 1.25
    # 显示窗口大小
    x = 600
    y = 500
    window = tk.Tk()
    canvas = tk.Canvas(window, width=x, height=y, bg="#000000")
    canvas.pack()
    t1 = time.process_time()
    img = tk.PhotoImage(width=x, height=y)
    canvas.create_image((0, 0), image=img, state="normal", anchor=tk.NW)
    # 计算并显示图像
    pixels = mandelbrot_image(xa, xb, ya, yb, x, y)
    img.put(pixels)
    print("运行耗时：{}秒。".format(time.process_time() - t1))
    tk.mainloop()


if __name__ == "__main__":
    main()