import fpdf


class PDF(fpdf.FPDF):
    """
    Default template of a PDF
    :param police: the font of pdf, inherited values of fpdf lib (system font) ex 'Courier', 'Arial' or 'Times'
    :param name: the first and last name of the candidates
    """

    def __init__(self, police: str, name: str):
        super(PDF, self).__init__()
        self.name = name
        self.police = police
        self.alias_nb_pages()  # To have the total number of PDF
        self.add_page()
        self.set_title(self.name)

    def header(self):
        """
        Set header of the PDF
        :return None
        """
        self.set_font(self.police, 'B', 15)
        self.cell(w=0, h=10, txt=f"CV de {self.name}", border=1, ln=1, align='C')

    def footer(self):
        """
        Set footer of the PDF
        :return: None
        """
        self.set_y(-15)
        self.set_font(self.police, 'I', 8)
        self.cell(w=0, h=10, txt=f"Page {self.page_no()}" + '/{nb}', border='B', ln=0, align='R')

    def contact(self, contactInfos: dict):
        self.cell(w=0, h=10, txt="Contact section", border='B', ln=1)
        for key, values in contactInfos.items():
            if key == "tel":
                self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1, link=f"tel:{values}")
            elif key == "mail":
                self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1, link=f"mailto:{values}")
            else:
                self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1)

    def certification(self, certification: dict):
        self.cell(w=0, h=10, txt="Certification section", border='B', ln=1)
        for key, values in certification.items():
            if key == "start-date" or key == "end-date":
                self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1, link=f"date:{values}")
            if key == "id" or key == "number":
                # we don't use id for the certificate or The license number for this certification.
                pass
            else:
                self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1)

    def languages(self, languages: dict):
        self.cell(w=0, h=10, txt="Languages section", border='B', ln=1)
        for key, values in languages.items():
            self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1)

    def educations(self, educations: dict):
        self.cell(w=0, h=10, txt="Education section", border='B', ln=1)
        for key, values in educations.items():
            self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1)

    def currentposition(self, three_current_positions: dict):
        self.cell(w=0, h=10, txt="Current position section", border='B', ln=1)
        for key, values in three_current_positions.items():
            self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1)

    def pastPosition(self, three_past_positions):
        self.cell(w=0, h=10, txt="Past position section", border='B', ln=1)
        for key, values in three_past_positions.items():
            self.cell(w=0, h=5, txt=f"{key} : {values}", ln=1)
        


def toPDF(Infos):
    """
    create a PDF from the the candidates Info
    :param Infos: dictionnary with all the infos of the candidates
    :return: PDF
    """

    returnPDF = PDF("Courier", Infos.get("name"))
    if Infos.get('contact'):
        returnPDF.contact(Infos.get("contact"))
    returnPDF.output("result.pdf", 'F')


if __name__ == '__main__':
    toPDF(
        {
            "name": "John doe",
            "contact":
                {'tel': "phone exemple",
                 "address": "exmaple addr",
                 "mail": "example@domaine.com"
                 }
        }
    )
