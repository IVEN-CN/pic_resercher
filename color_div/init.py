"""将颜色识别信息储存到文件
color   0：红色；   1：绿色；   2：蓝色
save    0：不保存；  1：保存"""
import cv2
import numpy as np


def callback(x) -> None:
    """trackbar回调空函数"""
    pass


def save_color(x) -> None:
    """保存颜色信息的函数"""
    global low_color, up_color, color
    if x == 1:
        data = np.vstack((low_color, up_color))
 
        np.save(f'{color}.npy', data)
    else:
        pass


def save_area(x) -> None:
    """保存面积的函数"""
    global arr
    if x == 1:
        np.save('area.npy', arr)
    else:
        pass

def main(path):
    global low_color, up_color, color, arr
    # 创建窗口
    cv2.namedWindow('test',cv2.WINDOW_NORMAL)
    cv2.namedWindow('test1', cv2.WINDOW_NORMAL)
    cv2.namedWindow('test2', cv2.WINDOW_NORMAL)
    
    img = cv2.imread(path)

    # region 创建trackbar
    L_H = 0
    H_H = 180
    L_S = 0
    H_S = 255
    L_V = 0
    H_V = 255
    cv2.createTrackbar('lower_H', 'test', L_H, 180, callback)
    cv2.createTrackbar('upper_H', 'test', H_H, 180, callback)
    cv2.createTrackbar('lower_S', 'test', L_S, 255, callback)
    cv2.createTrackbar('upper_S', 'test', H_S, 255, callback)
    cv2.createTrackbar('lower_V', 'test', L_V, 255, callback)
    cv2.createTrackbar('upper_V', 'test', H_V, 255, callback)
    # 创建颜色选项
    cv2.createTrackbar('color', 'test', 0, 7, callback)

    cv2.createTrackbar('area', 'test', 1200*800, 1200*800, callback)
    # 保存文件的trackbar
    cv2.createTrackbar('save_color', 'test', 0, 1, save_color)
    # 保存面积的trackbar
    cv2.createTrackbar('save_area', 'test', 0, 1, save_area)
    # endregion

    # 转换色彩空间
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    while True:
        img = cv2.imread(path)
        # region 获取trackbar
        L_H = cv2.getTrackbarPos('lower_H', 'test')
        H_H = cv2.getTrackbarPos('upper_H', 'test')
        L_S = cv2.getTrackbarPos('lower_S', 'test')
        H_S = cv2.getTrackbarPos('upper_S', 'test')
        L_V = cv2.getTrackbarPos('lower_V', 'test')
        H_V = cv2.getTrackbarPos('upper_V', 'test')
        _color = cv2.getTrackbarPos('color', 'test')
        area = cv2.getTrackbarPos('area', 'test')
        # endregion

        dist = {0:'白色',
                1:'黑色',
                2:'浅紫',
                3:'粉红',
                4:'浅蓝',
                5:'浅绿',
                6:'杏色',
                7:'浅黄'}
        color = dist.get(_color)

        low_color = np.array([L_H, L_S, L_V])
        up_color = np.array([H_H, H_S, H_V])
        arr = np.array(area)

        mask = cv2.inRange(img1, low_color, up_color)

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            # 对每个轮廓进行矩形拟合
            x, y, w, h = cv2.boundingRect(contour)
            brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
            if w * h >= area:
                cv2.drawContours(img, [brcnt], -1, (0, 255, 0), 2)
                # brcnt是矩形的四个顶点坐标，-1表示画出矩形，（255,255,255）是颜色，2是线宽

        cv2.imshow('test2', img)
        cv2.imshow('test1', mask)

        if cv2.waitKey(1) == 27:
            break

    # 摧毁窗口
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main('1200(9).jpg')

