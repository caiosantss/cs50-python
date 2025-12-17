from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting a font
        self.set_font("Helvetica", "", 40)

        # Setting text
        self.cell(0, 20, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align='C')

        # Espace btween the body
        self.ln(10)


pdf = PDF("p", "mm", "a4")

pdf.add_page()

# 1. Desenha a imagem centrada
top_img_y = pdf.get_y()
img_w = 190

pdf.image("shirtificate.png", x="C", w=img_w)

# captura altura final
bottom_img_y = pdf.get_y()
img_h = bottom_img_y - top_img_y

# 2. Texto a 40% da altura
text = input("Name: ")

pdf.set_font("Helvetica", "", 24)
pdf.set_text_color(255, 255, 255)

text_y = top_img_y + img_h * 0.40

# 3. Centralização dentro da imagem
page_w = pdf.w - pdf.l_margin - pdf.r_margin
img_x = pdf.l_margin + (page_w - img_w) / 2

text_full = f"{text} took CS50"
text_w = pdf.get_string_width(text_full)

text_x = img_x + (img_w - text_w) / 2   # centro da imagem

pdf.set_xy(text_x, text_y)
pdf.cell(text_w, 10, text_full)

pdf.output(f"shirtificate.pdf")
