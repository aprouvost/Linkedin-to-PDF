from flask import Flask
from util import toPDF, getCandidateInfo, getCandidatesLinkedIn

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'api running !'

@app.route('/resume',methods=['POST'])
def resume():
    """
    POST method that accepts a resume in request's body
    uses
    :return: candidate's PDF from linked in
    """
    ResumePDF = request.files[0]
    LinkedInURL = getCandidatesLinkedIn(ResumePDF)
    CandidatesInfos = getCandidateInfo(LinkedInURL)
    returnPDF = toPDF(CandidatesInfos)

    raise NotImplementedError

@app.route('/linkedin/<linkedinURL>')
def linkedin(LinkedInURL):
    """
    GET download the
    :return: candidate's PDF from linked in
    """
    LinkedInURL = request.args.get('linkedinURL')
    CandidatesInfos = getCandidateInfo(LinkedInURL)
    returnPDF = toPDF(CandidatesInfos)

    raise NotImplementedError


if __name__ == '__main__':
    app.run()
