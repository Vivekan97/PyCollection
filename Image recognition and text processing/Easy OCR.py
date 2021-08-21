import easyocr
from prettytable import PrettyTable
from tabulate import tabulate


print(1, "  Running successfully")

IMAGE_PATH = (
    r"C:\Users\Vivekan.Sam\Desktop\RIGELSOFT\OCR Python\easyocr\IMAGES\invoice.jpg"
)

reader = easyocr.Reader(["en"])
result = reader.readtext(IMAGE_PATH, detail=True, paragraph=False)
# if detail=True we get confidence, co-ordinates
# if paragraph=True confidence level won't appear, also accuracy is lower than false method...
### Access from URL
# result1 = reader.readtext("https://i.ytimg.com/vi/bE31y5HbukA/maxresdefault.jpg")
# print(result1)
mytable = PrettyTable(["S.No", "Text", "Confidence"])
# print(result)

### Capturing the output into a file
with open("main0_result.txt", "w") as op_file:
    index = 0
    for lines in result:
        index += 1
        # op_file.write(lines)
        # print(lines)
        try:
            mytable.add_row([index, lines[1], lines[2]])
        except IndexError:
            mytable.add_row([index, lines[1], "Error"])
        # print( len(lines), len(result))
        # op_file.writelines(f"{index}) {lines[1]}\n")
        op_file.writelines(f"{index}) {lines}\n")
    op_file.write(tabulate(mytable))
print(mytable)

### TO draw bounding boxes """SINGLE BOX"""

# top_left = tuple(result[0][0][0])
# bottom_right = tuple(result[0][0][2])
# text = result[0][1]
# font = cv2.FONT_HERSHEY_SIMPLEX

# img = cv2.imread(IMAGE_PATH)
# img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
# img = cv2.putText(img, text, top_left, font, 0.5, (161, 0, 1), 2, cv2.LINE_AA)
# plt.imshow(img)
# plt.show()

### To draw multiple bounding boxes

# img = cv2.imread(IMAGE_PATH)
# spacer = 100
# for detection in result:
#     top_left = tuple(detection[0][0])
#     bottom_right = tuple(detection[0][2])
#     print(top_left, bottom_right)
#     text = detection[1]
#     img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
#     img = cv2.putText(img, text, (20, spacer), font, 0.8, (161, 0, 1), 2, cv2.LINE_AA)
#     # img = cv2.putText(img, text, top_left, font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
#     spacer += 15

# plt.imshow(img)
# plt.show()
