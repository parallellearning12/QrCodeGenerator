
# from flask import Flask, render_template, request, send_from_directory
# import qrcode
# from PIL import Image, ImageDraw, ImageFont
# import os
#
# app = Flask(__name__)
# QR_FOLDER = 'generated_qr'
# FONT_PATH = 'static/font/Roboto-Bold.ttf'
# DPI = 300  # Dots Per Inch for mm-to-pixels conversion
#
# def mm_to_px(mm):
#     return int((mm / 25.4) * DPI)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         try:
#             qr_width_mm = float(request.form['width'])
#             qr_height_mm = float(request.form['height'])
#             start = int(request.form['start'])
#             end = int(request.form['end'])
#         except ValueError:
#             return "Invalid input. Please enter valid numbers."
#
#         qr_width_total = mm_to_px(qr_width_mm)
#         qr_height = mm_to_px(qr_height_mm)
#         qr_extra_side_padding = mm_to_px(2)  # 2mm padding on both sides inside the QR box
#         qr_width = qr_width_total - (qr_extra_side_padding * 2)  # Adjust QR image size only
#
#         label_height = mm_to_px(16)
#         padding_px = mm_to_px(3)
#         label_spacing = mm_to_px(2)
#         border_thickness = 1
#         corner_radius = 20
#         border_color = (18, 55, 115)
#
#         canvas_width = qr_width_total + padding_px * 2  # Keep total canvas size same
#         canvas_height = padding_px + qr_height + label_spacing + label_height
#
#         for i in range(start, end + 1):
#             qr_number = f'B{str(i).zfill(4)}'
#             data = qr_number
#
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=10,
#                 border=0
#             )
#             qr.add_data(data)
#             qr.make(fit=True)
#             qr_img = qr.make_image(fill_color="#123773", back_color="white").convert('RGB')
#             qr_img = qr_img.resize((qr_width, qr_height))
#
#             content_img = Image.new('RGB', (canvas_width, canvas_height), 'white')
#
#             qr_x = padding_px + qr_extra_side_padding  # Place QR with 2mm internal margin
#             qr_y = padding_px
#             content_img.paste(qr_img, (qr_x, qr_y))
#
#             label_top = qr_y + qr_height + label_spacing
#             draw = ImageDraw.Draw(content_img)
#             draw.rectangle([(0, label_top), (canvas_width, canvas_height)], fill=border_color)
#
#             try:
#                 font_large = ImageFont.truetype(FONT_PATH, int(label_height * 0.3))
#                 font_small = ImageFont.truetype(FONT_PATH, int(label_height * 0.16))
#             except:
#                 return "Font not found. Make sure Roboto-Bold.ttf is in static/font."
#
#             def center_text_x(text, font):
#                 return (canvas_width - font.getlength(text)) // 2
#
#             line1 = qr_number
#             line2 = "This belongs to"
#             line3 = "Forbes Marshall Pvt. Ltd. Chakan"
#
#             line_spacing = 2
#             line1_y = label_top + 2
#             line2_y = line1_y + font_large.size + line_spacing
#             line3_y = line2_y + font_small.size + line_spacing
#
#             draw.text((center_text_x(line1, font_large), line1_y), line1, font=font_large, fill='white')
#             draw.text((center_text_x(line2, font_small), line2_y), line2, font=font_small, fill='white')
#             draw.text((center_text_x(line3, font_small), line3_y), line3, font=font_small, fill='white')
#
#             # Create bordered image with rounded corners on the entire outer image
#             bordered_width = canvas_width + 2 * border_thickness
#             bordered_height = canvas_height + 2 * border_thickness
#             bordered_img = Image.new('RGBA', (bordered_width, bordered_height), (0, 0, 0, 0))
#
#             draw_border = ImageDraw.Draw(bordered_img)
#             draw_border.rounded_rectangle(
#                 [(0, 0), (bordered_width, bordered_height)],
#                 radius=corner_radius + border_thickness,
#                 fill=border_color + (255,)
#             )
#
#             # Paste content image into the center with same corner shape
#             mask = Image.new('L', (canvas_width, canvas_height), 0)
#             draw_mask = ImageDraw.Draw(mask)
#             draw_mask.rounded_rectangle(
#                 [(0, 0), (canvas_width, canvas_height)],
#                 radius=corner_radius,
#                 fill=255
#             )
#
#             content_img.putalpha(mask)
#             bordered_img.paste(content_img, (border_thickness, border_thickness), content_img)
#
#             filename = f"{qr_number}.png"
#             filepath = os.path.join(QR_FOLDER, filename)
#             bordered_img.save(filepath)
#
#         return render_template('success.html', count=end - start + 1)
#
#
#     return render_template('index.html')
#
# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory(QR_FOLDER, filename)
#
# if __name__ == '__main__':
#     if not os.path.exists(QR_FOLDER):
#         os.makedirs(QR_FOLDER)
#     app.run(debug=True)








#
# from flask import Flask, render_template, request, send_from_directory
# import qrcode
# from PIL import Image, ImageDraw, ImageFont
# import os
#
# app = Flask(__name__)
# QR_FOLDER = 'generated_qr'
# FONT_PATH = 'static/font/Roboto-Bold.ttf'
# DPI = 300  # Dots Per Inch for mm-to-pixels conversion
#
# def mm_to_px(mm):
#     return int((mm / 25.4) * DPI)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         try:
#             qr_width_mm = float(request.form['width'])
#             qr_height_mm = float(request.form['height'])
#             start = int(request.form['start'])
#             end = int(request.form['end'])
#         except ValueError:
#             return "Invalid input. Please enter valid numbers."
#
#         qr_width_total = mm_to_px(qr_width_mm)
#         qr_height = mm_to_px(qr_height_mm)
#         qr_extra_side_padding = mm_to_px(2)  # 2mm padding on both sides inside the QR box
#         qr_width = qr_width_total - (qr_extra_side_padding * 2)  # Adjust QR image size only
#
#         label_height = mm_to_px(16)
#         padding_px = mm_to_px(3)
#         label_spacing = mm_to_px(2)
#         border_thickness = 1
#         corner_radius = 30
#         border_color = (18, 55, 115)
#
#         canvas_width = qr_width_total + padding_px * 2  # Keep total canvas size same
#         canvas_height = padding_px + qr_height + label_spacing + label_height
#
#         for i in range(start, end + 1):
#             qr_number = f'B{str(i).zfill(4)}'
#             data = qr_number
#
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=10,
#                 border=0
#             )
#             qr.add_data(data)
#             qr.make(fit=True)
#             qr_img = qr.make_image(fill_color="#123773", back_color="white").convert('RGB')
#             qr_img = qr_img.resize((qr_width, qr_height))
#
#             content_img = Image.new('RGB', (canvas_width, canvas_height), 'white')
#
#             qr_x = padding_px + qr_extra_side_padding  # Place QR with 2mm internal margin
#             qr_y = padding_px
#             content_img.paste(qr_img, (qr_x, qr_y))
#
#             label_top = qr_y + qr_height + label_spacing
#             draw = ImageDraw.Draw(content_img)
#             draw.rectangle([(0, label_top), (canvas_width, canvas_height)], fill=border_color)
#
#             try:
#                 font_line1 = ImageFont.truetype(FONT_PATH, int(label_height * 0.18))  # QR number
#                 font_line2 = ImageFont.truetype(FONT_PATH, int(label_height * 0.14))  # main label
#                 font_line3 = ImageFont.truetype(FONT_PATH, int(label_height * 0.14))  # footer
#             except:
#                 return "Font not found. Make sure Roboto-Bold.ttf is in static/font."
#
#             def center_text_x(text, font):
#                 return (canvas_width - font.getlength(text)) // 2
#
#             line1 = qr_number
#             line2 = "This belongs to"
#             line3 = "Forbes Marshall Pvt. Ltd. Chakan"
#
#             line_spacing = 18
#             line1_y = label_top + 8
#             line2_y = line1_y + font_line1.size + line_spacing
#             line3_y = line2_y + font_line2.size + line_spacing
#
#             draw.text((center_text_x(line1, font_line1), line1_y), line1, font=font_line1, fill='white')
#             draw.text((center_text_x(line2, font_line2), line2_y), line2, font=font_line2, fill='white')
#             draw.text((center_text_x(line3, font_line3), line3_y), line3, font=font_line3, fill='white')
#
#             # Create bordered image with rounded corners on the entire outer image
#             bordered_width = canvas_width + 2 * border_thickness
#             bordered_height = canvas_height + 2 * border_thickness
#             bordered_img = Image.new('RGBA', (bordered_width, bordered_height), (0, 0, 0, 0))
#
#             draw_border = ImageDraw.Draw(bordered_img)
#             draw_border.rounded_rectangle(
#                 [(0, 0), (bordered_width, bordered_height)],
#                 radius=corner_radius + border_thickness,
#                 fill=border_color + (255,)
#             )
#
#             # Paste content image into the center with same corner shape
#             mask = Image.new('L', (canvas_width, canvas_height), 0)
#             draw_mask = ImageDraw.Draw(mask)
#             draw_mask.rounded_rectangle(
#                 [(0, 0), (canvas_width, canvas_height)],
#                 radius=corner_radius,
#                 fill=255
#             )
#
#             content_img.putalpha(mask)
#             bordered_img.paste(content_img, (border_thickness, border_thickness), content_img)
#
#             filename = f"{qr_number}.png"
#             filepath = os.path.join(QR_FOLDER, filename)
#             bordered_img.save(filepath)
#
#         return render_template('success.html', count=end - start + 1)
#
#     return render_template('index.html')
#
# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory(QR_FOLDER, filename)
#
# if __name__ == '__main__':
#     if not os.path.exists(QR_FOLDER):
#         os.makedirs(QR_FOLDER)
#     app.run(debug=True)
#
# from flask import Flask, render_template, request, send_from_directory
# import qrcode
# from PIL import Image, ImageDraw, ImageFont
# import os
#
# app = Flask(__name__)
# QR_FOLDER = 'generated_qr'
# FONT_PATH = 'static/font/Roboto-Bold.ttf'
# DPI = 300  # Dots Per Inch for mm-to-pixels conversion
#
# def mm_to_px(mm):
#     return int((mm / 25.4) * DPI)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         try:
#             qr_width_mm = float(request.form['width'])
#             qr_height_mm = float(request.form['height'])
#             start = int(request.form['start'])
#             end = int(request.form['end'])
#         except ValueError:
#             return "Invalid input. Please enter valid numbers."
#
#         qr_width_total = mm_to_px(qr_width_mm)
#         qr_height = mm_to_px(qr_height_mm)
#         qr_extra_side_padding = mm_to_px(2)  # 2mm padding on both sides inside the QR box
#         qr_width = qr_width_total - (qr_extra_side_padding * 2)  # Adjust QR image size only
#
#         label_height = mm_to_px(16)
#         padding_px = mm_to_px(3)
#         label_spacing = mm_to_px(2)
#         border_thickness = 1
#         corner_radius = 20
#         border_color = (18, 55, 115)
#
#         canvas_width = qr_width_total + padding_px * 2  # Keep total canvas size same
#         canvas_height = padding_px + qr_height + label_spacing + label_height
#
#         for i in range(start, end + 1):
#             qr_number = f'B{str(i).zfill(4)}'
#             data = qr_number
#
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=10,
#                 border=0
#             )
#             qr.add_data(data)
#             qr.make(fit=True)
#             qr_img = qr.make_image(fill_color="#123773", back_color="white").convert('RGB')
#             qr_img = qr_img.resize((qr_width, qr_height))
#
#             content_img = Image.new('RGB', (canvas_width, canvas_height), 'white')
#
#             qr_x = padding_px + qr_extra_side_padding  # Place QR with 2mm internal margin
#             qr_y = padding_px
#             content_img.paste(qr_img, (qr_x, qr_y))
#
#             label_top = qr_y + qr_height + label_spacing
#             draw = ImageDraw.Draw(content_img)
#             draw.rectangle([(0, label_top), (canvas_width, canvas_height)], fill=border_color)
#
#             try:
#                 # KEEP original sizes for line2 and line3
#                 font_line2 = ImageFont.truetype(FONT_PATH, int(label_height * 0.16))  # default size
#                 font_line3 = ImageFont.truetype(FONT_PATH, int(label_height * 0.16))  # default size
#                 # Make QR number smaller
#                 font_line1 = ImageFont.truetype(FONT_PATH, int(label_height * 0.20))
#             except:
#                 return "Font not found. Make sure Roboto-Bold.ttf is in static/font."
#
#             def center_text_x(text, font):
#                 return (canvas_width - font.getlength(text)) // 2
#
#             line1 = qr_number
#             line2 = "This belongs to"
#             line3 = "Forbes Marshall Pvt. Ltd. Chakan"
#
#             line_spacing = 5  # Add space between lines
#             line1_y = label_top + 4
#             line2_y = line1_y + font_line1.size + line_spacing
#             line3_y = line2_y + font_line2.size + line_spacing
#
#             draw.text((center_text_x(line1, font_line1), line1_y), line1, font=font_line1, fill='white')
#             draw.text((center_text_x(line2, font_line2), line2_y), line2, font=font_line2, fill='white')
#             draw.text((center_text_x(line3, font_line3), line3_y), line3, font=font_line3, fill='white')
#
#             # Create bordered image with rounded corners on the entire outer image
#             bordered_width = canvas_width + 2 * border_thickness
#             bordered_height = canvas_height + 2 * border_thickness
#             bordered_img = Image.new('RGBA', (bordered_width, bordered_height), (0, 0, 0, 0))
#
#             draw_border = ImageDraw.Draw(bordered_img)
#             draw_border.rounded_rectangle(
#                 [(0, 0), (bordered_width, bordered_height)],
#                 radius=corner_radius + border_thickness,
#                 fill=border_color + (255,)
#             )
#
#             # Paste content image into the center with same corner shape
#             mask = Image.new('L', (canvas_width, canvas_height), 0)
#             draw_mask = ImageDraw.Draw(mask)
#             draw_mask.rounded_rectangle(
#                 [(0, 0), (canvas_width, canvas_height)],
#                 radius=corner_radius,
#                 fill=255
#             )
#
#             content_img.putalpha(mask)
#             bordered_img.paste(content_img, (border_thickness, border_thickness), content_img)
#
#             filename = f"{qr_number}.png"
#             filepath = os.path.join(QR_FOLDER, filename)
#             bordered_img.save(filepath)
#
#         return render_template('success.html', count=end - start + 1)
#
#     return render_template('index.html')
#
# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory(QR_FOLDER, filename)
#
# if __name__ == '__main__':
#     if not os.path.exists(QR_FOLDER):
#         os.makedirs(QR_FOLDER)
#     app.run(debug=True)
#

#
#
# from flask import Flask, render_template, request, send_from_directory
# import qrcode
# from PIL import Image, ImageDraw, ImageFont
# import os
#
# app = Flask(__name__)
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# QR_FOLDER = os.path.join(BASE_DIR, 'generated_qr')
# FONT_PATH = os.path.join(BASE_DIR, 'static', 'font', 'Roboto-Bold.ttf')
# DPI = 300  # Dots Per Inch for mm-to-pixels conversion
#
# def mm_to_px(mm):
#     return int((mm / 25.4) * DPI)
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         try:
#             qr_width_mm = float(request.form['width'])
#             qr_height_mm = float(request.form['height'])
#             start = int(request.form['start'])
#             end = int(request.form['end'])
#         except ValueError:
#             return "Invalid input. Please enter valid numbers."
#
#         qr_width_total = mm_to_px(qr_width_mm)
#         qr_height = mm_to_px(qr_height_mm)
#         qr_extra_side_padding = mm_to_px(2)
#         qr_width = qr_width_total - (qr_extra_side_padding * 2)
#
#         label_height = mm_to_px(16)
#         padding_px = mm_to_px(3)
#         label_spacing = mm_to_px(2)
#         border_thickness = 1
#         corner_radius = 30
#         border_color = (18, 55, 115)
#
#         canvas_width = qr_width_total + padding_px * 2
#         canvas_height = padding_px + qr_height + label_spacing + label_height
#
#         if not os.path.exists(QR_FOLDER):
#             os.makedirs(QR_FOLDER)
#
#         for i in range(start, end + 1):
#             qr_number = f'B{str(i).zfill(4)}'
#             data = qr_number
#
#             qr = qrcode.QRCode(
#                 version=1,
#                 error_correction=qrcode.constants.ERROR_CORRECT_H,
#                 box_size=10,
#                 border=0
#             )
#             qr.add_data(data)
#             qr.make(fit=True)
#             qr_img = qr.make_image(fill_color="#123773", back_color="white").convert('RGB')
#             qr_img = qr_img.resize((qr_width, qr_height))
#
#             content_img = Image.new('RGB', (canvas_width, canvas_height), 'white')
#
#             qr_x = padding_px + qr_extra_side_padding
#             qr_y = padding_px
#             content_img.paste(qr_img, (qr_x, qr_y))
#
#             label_top = qr_y + qr_height + label_spacing
#             draw = ImageDraw.Draw(content_img)
#             draw.rectangle([(0, label_top), (canvas_width, canvas_height)], fill=border_color)
#
#             try:
#                 font_line1 = ImageFont.truetype(FONT_PATH, int(label_height * 0.18))
#                 font_line2 = ImageFont.truetype(FONT_PATH, int(label_height * 0.14))
#                 font_line3 = ImageFont.truetype(FONT_PATH, int(label_height * 0.14))
#             except:
#                 return "Font not found. Make sure Roboto-Bold.ttf is in static/font."
#
#             def center_text_x(text, font):
#                 return (canvas_width - font.getlength(text)) // 2
#
#             line1 = qr_number
#             line2 = "This belongs to"
#             line3 = "Forbes Marshall Pvt. Ltd. Chakan"
#
#             line_spacing = 18
#             line1_y = label_top + 8
#             line2_y = line1_y + font_line1.size + line_spacing
#             line3_y = line2_y + font_line2.size + line_spacing
#
#             draw.text((center_text_x(line1, font_line1), line1_y), line1, font=font_line1, fill='white')
#             draw.text((center_text_x(line2, font_line2), line2_y), line2, font=font_line2, fill='white')
#             draw.text((center_text_x(line3, font_line3), line3_y), line3, font=font_line3, fill='white')
#
#             bordered_width = canvas_width + 2 * border_thickness
#             bordered_height = canvas_height + 2 * border_thickness
#             bordered_img = Image.new('RGBA', (bordered_width, bordered_height), (0, 0, 0, 0))
#
#             draw_border = ImageDraw.Draw(bordered_img)
#             draw_border.rounded_rectangle(
#                 [(0, 0), (bordered_width, bordered_height)],
#                 radius=corner_radius + border_thickness,
#                 fill=border_color + (255,)
#             )
#
#             mask = Image.new('L', (canvas_width, canvas_height), 0)
#             draw_mask = ImageDraw.Draw(mask)
#             draw_mask.rounded_rectangle(
#                 [(0, 0), (canvas_width, canvas_height)],
#                 radius=corner_radius,
#                 fill=255
#             )
#
#             content_img.putalpha(mask)
#             bordered_img.paste(content_img, (border_thickness, border_thickness), content_img)
#
#             filename = f"{qr_number}.png"
#             filepath = os.path.join(QR_FOLDER, filename)
#             bordered_img.save(filepath)
#
#         return render_template('success.html', count=end - start + 1)
#
#     return render_template('index.html')
#
# @app.route('/download/<filename>')
# def download(filename):
#     return send_from_directory(QR_FOLDER, filename)
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request, send_from_directory
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
QR_FOLDER = os.path.join(BASE_DIR, 'generated_qr')
FONT_PATH = os.path.join(BASE_DIR, 'static', 'font', 'Roboto-Bold.ttf')
DPI = 300  # Dots Per Inch for mm-to-pixels conversion

def mm_to_px(mm):
    return int((mm / 25.4) * DPI)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            qr_width_mm = float(request.form['width'])
            qr_height_mm = float(request.form['height'])
            start = int(request.form['start'])
            end = int(request.form['end'])
        except ValueError:
            return "Invalid input. Please enter valid numbers."

        qr_width_total = mm_to_px(qr_width_mm)
        qr_height = mm_to_px(qr_height_mm)
        qr_extra_side_padding = mm_to_px(2)
        qr_width = qr_width_total - (qr_extra_side_padding * 2)

        label_height = mm_to_px(16)
        padding_px = mm_to_px(3)
        label_spacing = mm_to_px(2)
        border_thickness = 1
        corner_radius = 30
        border_color = (18, 55, 115)

        canvas_width = qr_width_total + padding_px * 2
        canvas_height = padding_px + qr_height + label_spacing + label_height

        if not os.path.exists(QR_FOLDER):
            os.makedirs(QR_FOLDER)

        for i in range(start, end + 1):
            qr_number = f'B{str(i).zfill(4)}'
            data = qr_number

            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=0
            )
            qr.add_data(data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="#123773", back_color="white").convert('RGB')
            qr_img = qr_img.resize((qr_width, qr_height))

            content_img = Image.new('RGB', (canvas_width, canvas_height), 'white')

            qr_x = padding_px + qr_extra_side_padding
            qr_y = padding_px
            content_img.paste(qr_img, (qr_x, qr_y))

            label_top = qr_y + qr_height + label_spacing
            draw = ImageDraw.Draw(content_img)
            draw.rectangle([(0, label_top), (canvas_width, canvas_height)], fill=border_color)

            try:
                font_line1 = ImageFont.truetype(FONT_PATH, int(label_height * 0.18))
                font_line2 = ImageFont.truetype(FONT_PATH, int(label_height * 0.14))
                font_line3 = ImageFont.truetype(FONT_PATH, int(label_height * 0.14))
            except:
                return "Font not found. Make sure Roboto-Bold.ttf is in static/font."

            def center_text_x(text, font):
                return (canvas_width - font.getlength(text)) // 2

            line1 = qr_number
            line2 = "This belongs to"
            line3 = "Forbes Marshall Pvt. Ltd. Chakan"

            line_spacing = 18
            line1_y = label_top + 8
            line2_y = line1_y + font_line1.size + line_spacing
            line3_y = line2_y + font_line2.size + line_spacing

            draw.text((center_text_x(line1, font_line1), line1_y), line1, font=font_line1, fill='white')
            draw.text((center_text_x(line2, font_line2), line2_y), line2, font=font_line2, fill='white')
            draw.text((center_text_x(line3, font_line3), line3_y), line3, font=font_line3, fill='white')

            bordered_width = canvas_width + 2 * border_thickness
            bordered_height = canvas_height + 2 * border_thickness
            bordered_img = Image.new('RGBA', (bordered_width, bordered_height), (0, 0, 0, 0))

            draw_border = ImageDraw.Draw(bordered_img)
            draw_border.rounded_rectangle(
                [(0, 0), (bordered_width, bordered_height)],
                radius=corner_radius + border_thickness,
                fill=border_color + (255,)
            )

            mask = Image.new('L', (canvas_width, canvas_height), 0)
            draw_mask = ImageDraw.Draw(mask)
            draw_mask.rounded_rectangle(
                [(0, 0), (canvas_width, canvas_height)],
                radius=corner_radius,
                fill=255
            )

            content_img.putalpha(mask)
            bordered_img.paste(content_img, (border_thickness, border_thickness), content_img)

            filename = f"{qr_number}.png"
            filepath = os.path.join(QR_FOLDER, filename)
            bordered_img.save(filepath)

        return render_template('success.html', count=end - start + 1)

    return render_template('index.html')


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(QR_FOLDER, filename)


@app.route('/list_qr')
def list_qr():
    if not os.path.exists(QR_FOLDER):
        return "No QR codes generated yet."

    files = sorted(f for f in os.listdir(QR_FOLDER) if f.lower().endswith('.png'))
    if not files:
        return "No QR codes found."

    links_html = ''.join(
        f'<li><a href="/download/{f}" target="_blank">{f}</a></li>' for f in files
    )

    page = f"""
    <h1>Generated QR Codes</h1>
    <ul>{links_html}</ul>
    <a href="/">Go back to Home</a>
    """
    return page


if __name__ == '__main__':
    app.run(debug=True)
