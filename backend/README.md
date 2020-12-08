# LINKEDIN 2 PDF - BACKEND

## Overview
 
the backend is runs on flask and has 3 main routes 

## Architecture
![](https://github.com/aprouvost/Linkedin-to-PDF/blob/main/backend/doc/Backend_architecture.png)

## Routes

> /resume 

`POST` request, with the resume in the body of the request as (must be a .pdf file)
returns the output PDF with all the candidate's infos 

> /linkedin/<url>

`POST`

Parameter :
 - url: candidate's linkedin url 

return pdf as  `/resume` 
