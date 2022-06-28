from paddleocr import PaddleOCR, draw_ocr

# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="chinese_cht", use_gpu=True)  # need to run only once to download and load model into memory
img_path = './images/101acfaf-f525-45f9-93ae-40dab4eb46b40001-1.png'
result = ocr.ocr(img_path, cls=False)
for line in result:
    print(line)

# 显示识别结果，
# from PIL import Image
#
# image = Image.open(img_path)
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='./images/ppocr_img/fonts/chinese_cht.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result_A73RMB-0DSG-KC0004_600ppi.jpg')