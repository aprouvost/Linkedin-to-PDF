# LINKEDIN 2 PDF - BACKEND

the backend is runs on flask and has 3 main routes 

> /resume 

`POST` request, with the resume in the body of the request as (must be a .pdf file)
returns the output PDF with all the candidate's infos 

> /linkedin/<url>

`POST`

Parameter :
 - url: candidate's linkedin url 

return pdf as  `/resume` 
