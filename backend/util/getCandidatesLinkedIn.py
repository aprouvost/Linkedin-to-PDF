import pikepdf
import PyPDF2


def getCandidateLinkedIn(resume):
    """
    scrape the candidates resume to get his linked in
    :param resume: PDF file
    :return:
    """
    if resume.endswith("pdf"):
        PDFFile = open(resume, 'rb')
        URL = []
        PDF = PyPDF2.PdfFileReader(PDFFile)
        pages = PDF.getNumPages()
        key = '/Annots'
        uri = '/URI'
        ank = '/A'

        for page in range(pages):

            # print("Current Page: {}".format(page))
            pageSliced = PDF.getPage(page)
            pageObject = pageSliced.getObject()
            if key in pageObject.keys():
                ann = pageObject[key]
                for a in ann:
                    u = a.getObject()
                    if uri in u[ank].keys():
                        URL.append(u[ank][uri])

        for elem in URL:
            if "linkedin" not in elem:
                URL.remove(elem)
        if len(URL) > 0:
            return URL
        else:
            print("Warning, no URL found")
            return URL

    else:
        print("Warning, you must provide a PDF")
        return


if __name__ == "__main__":
    # execute only if run as a script
    print(getCandidateLinkedIn("cv.pdf"))
