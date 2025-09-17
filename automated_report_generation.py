import csv
from fpdf import FPDF

# Define a function to generate the PDF report
def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=24)
    pdf.cell(200, 10, txt="Automated Report Generation", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Summary", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    for key, value in data['summary'].items():
        pdf.cell(200, 10, txt=f"{key}: {value}", ln=True, align='L')
    pdf.ln(10)

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Details", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    for row in data['details']:
        for item in row:
            pdf.cell(200, 10, txt=str(item), ln=True, align='L')
        pdf.ln(10)

    pdf.output("report.pdf")

# Define a function to analyze the data
def analyze_data(data):
    summary = {}
    details = []
    for row in data:
        summary['Total Records'] = summary.get('Total Records', 0) + 1
        summary['Total Sales'] = summary.get('Total Sales', 0) + float(row[1])
        details.append(row)
    summary['Average Sales'] = summary['Total Sales'] / summary['Total Records']
    return {'summary': summary, 'details': details}

# Read data from the CSV file
def read_data(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data 

# Main function
def main():
    file_name = 'data.csv'
    data = read_data(file_name)
    analyzed_data = analyze_data(data)
    generate_pdf_report(analyzed_data)

if __name__ == "__main__":
    main()


