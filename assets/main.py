from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/login/")
def login():
	return render_template('login.html')

@app.route("/sign/")
def sign():
	return render_template('sign.html')

@app.route("/forpass/")
def forpass():
	return render_template('forpass.html')

@app.route("/marge")
def marge():
	return render_template('01_marge-file.html')

@app.route("/split")
def split():
	return render_template('02_split-pdf.html')

@app.route("/compress")
def compress():
	return render_template('03_compress-pdf.html')

@app.route("/pdf_to_word")
def pdf_to_word():
	return render_template('04_pdf To Word.html')

@app.route("/pdf_to_powerpoint")
def pdf_to_powerpoint():
	return render_template('05_pdf_to_powerpoint.html')

@app.route("/pdf_to_excel")
def pdf_to_excel():
	return render_template('06_pdf_excel.html')

@app.route("/word_to_pdf")
def word_to_pdf():
	return render_template('07_word_pdf.html')

@app.route("/powerpoint_to_pdf")
def powerpoint_to_pdf():
	return render_template('08_powerpoint_pdf.html')

@app.route("/excel_to_pdf")
def excel_to_pdf():
	return render_template('09_excel_pdf.html')

@app.route("/pdf_edit")
def pdf_edit():
	return render_template('10_pdf_edit.html')

@app.route("/pdf_to_jpg")
def pdf_to_jpg():
	return render_template('11_pdf-jpg.html')

@app.route("/jpg_to_pdf")
def jpg_to_pdf():
	return render_template('12_jpg-pdf.html')

@app.route("/sign_pdf")
def sign_pdf():
	return render_template('13_sign-pdf.html')

@app.route("/watermark")
def watermark():
	return render_template('14_watermark.html')

@app.route("/rotate")
def rotate():
	return render_template('15_rotate-pdf.html')

@app.route("/html_to_pdf")
def html_to_pdf():
	return render_template('16_html-pdf.html')

@app.route("/unlock")
def unlock():
	return render_template('17-unlock-pdf.html')

@app.route("/protect")
def protect():
	return render_template('18_protect-pdf.html')

@app.route("/organize")
def organize():
	return render_template('19_organize-pdf.html')

@app.route("/pdf_pdf_A")
def pdf_pdf_A():
	return render_template('20_pdf-pdf-A.html')

@app.route("/repair")
def repair():
	return render_template('21_repair-pdf.html')

@app.route("/page_number")
def page_number():
	return render_template('22_page-number.html')

@app.route("/scan_pdf")
def scan_pdf():
	return render_template('23_scan-pdf.html')

@app.route("/OCR_PDF_A")
def OCR_PDF_A():
	return render_template('24_OCR-PDF-A.html')

@app.route("/Compare")
def Compare():
	return render_template('25_Compare-pdf.html')


@app.route('/', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		# Here you would handle the form submission
		name = request.form['SignupForm[name]']
		email = request.form['SignupForm[email]']
		password = request.form['SignupForm[password]']
		timezone = request.form['SignupForm[timezone]']

		# Add your logic to process the data (e.g., save to database)

		return redirect(url_for('main'))  # Redirect to login after successful registration

	return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True,port=5002)
