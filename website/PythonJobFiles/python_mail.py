
# -*- coding: utf-8 -*-
"""
@author: A1507
"""
import traceback
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pytz import timezone
import logging
# This html place in another file

def GetHtml(EmailBodyContent):
  body ='''
  <!DOCTYPE html>
  <html>
    <head>
     
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <link href="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" rel="stylesheet" media="screen">
      <style type="text/css">
        .container {
          float: left;
        }
      </style>
    </head>
   
    <body>
      <div class="container">
   
    <p>Hi,</p>
    <p>
    '''+EmailBodyContent+'''
  </p><br/>
    
    <br/><br/>
    <table cellpadding="0" cellspacing="0" border="0" style="background: none; border-width: 0px; border: 0px; margin: 0; padding: 0;">
      <tbody><tr>
        <td valign="top" style="padding-top: 0px; padding-bottom: 0px; padding-left: 0px; padding-right: 0px; border-top: 0; border-bottom: 0: border-left: 0;">
          <table cellpadding="0" cellspacing="0" border="0" style="background: none; border-width: 0px; border: 0px; margin: 0; padding: 0;">
            <tbody><tr>
              <td align="left"><a href="https://www.axtria.com/" style="border-width:0px; border:0px; text-decoration: none;">
              <img id="preview-image-url" alt="Axtria Logo" style="border: none;" src="https://www.axtria.com/Signature/signature-left-image-option3.png"></a></td>
            </tr>
          </tbody></table>
        </td>
        <td valign="top" style="padding-top: 0px; padding-bottom: 0px; padding-left: 5px; padding-right: 5px; width: 200px; border-right: 2px solid #d9d9d9;">
          <table cellpadding="0" cellspacing="0" border="0" style="width: 200px; background: none; border-width: 0px; border: 0px; margin: 0; padding: 0;">
            <tbody><tr>
              <td colspan="2" style="color: #3ab050; font-size: 14.667px; font-weight: 600; font-family: Calibri; text-transform: uppercase;">
              AXTRIA SALESIQ SUPPORT TEAM
              </td>
            </tr>
            <tr>
              <td colspan="2" style="color: #808080; padding-top: 0px; font-size: 13.333px; font-family: Calibri">
              ethicon_salesiq_support@Axtria.com
              </td>
            </tr>
            <tr>
              <td align="left" colspan="2" style="padding-right: 2px; padding-top: 0px; padding-bottom:0px; color: #808080; font-size: 13.333px; font-family: Calibri"><a href="https://www.axtria.com" style="color: #808080; text-decoration: none;">www.axtria.com</a></td>
            </tr>
          </tbody></table>
        </td>
        <td valign="top" style="padding-top: 0px; padding-bottom: 0px; padding-left: 5px; padding-right: 5px; border-top: 0; border-bottom: 0: border-left: 0;">
          <table class="social-icons" cellpadding="0" cellspacing="0" border="0" style="background: none; border-width: 0px; border: 0px; margin: 0; padding: 0;">  
            <tbody><tr>
              <td align="center">
                <a href="https://twitter.com/axtria" style="border-width:0px; border:0px; text-decoration: none;"><img alt="Twitter Logo" style="border: none; " src="https://www.axtria.com/Signature/signature-twitter-icon.png"></a>
              </td>
              <td align="center">
                <a href="https://www.youtube.com/user/AxtriaINC" style="border-width:0px; border:0px; text-decoration: none; margin-left: 5px;"><img alt="YouTube Logo" style="border: none; " src="https://www.axtria.com/Signature/signature-youtube-icon.png"></a>
              </td>
            </tr>
            <tr>
              <td align="center">
                <a href="https://www.linkedin.com/company/axtria" style="border-width:0px; border:0px; text-decoration: none;"><img alt="LinkedIn Logo" style="border: none;" src="https://www.axtria.com/Signature/signature-linkedin-icon.png"></a>
                </td><td align="center"><a href="https://www.instagram.com/lifeataxtria/" style="border-width:0px; border:0px; text-decoration: none; margin-left: 5px;"><img alt="Instagram Logo" style="border: none; " src="https://www.axtria.com/Signature/signature-instagram-icon.png"></a>
              </td>
            </tr>
            <tr>
              <td align="center">
                <a href="https://www.facebook.com/AxtriaInc" style="border-width:0px; border:0px; text-decoration: none;"><img alt="Facebook Logo" style="border: none;" src="https://www.axtria.com/Signature/signature-facebook-icon.png"></a>
                </td><td align="center"><a href="https://www.glassdoor.com/Overview/Working-at-Axtria-EI_IE641281.11,17.htm" style="border-width:0px; border:0px; text-decoration: none; margin-left: 5px;"><img alt="Glassdoor Logo" style="border: none;" src="https://www.axtria.com/Signature/signature-glassdoor-icon.png"></a>
              </td><td>
            </td></tr>
          </tbody></table>
        </td>
      </tr>
    </tbody></table>
    <p>
    ***This message is automatically generated by Axtria SalesIQ system. If you have any questions, please contact <strong> ethicon_salesiq_support@Axtria.com.</strong>  ***
  </p>
  </div>
     
      <script src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
      <script src="http://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>

    </body>
  </html>
  '''
  return body


def SendMailWithoutAttachment(frommail,subject,password,ReceiverList):

    try:
        message = MIMEMultipart()
        body=GetHtml('Hi, This is new file.')
        message["From"] = frommail
        message["To"] =", ".join(ReceiverList)
        
        message["Subject"] = subject
        
        message.attach(MIMEText(body, "html"))
        
       
        text = message.as_string()
        
        smtpObj = smtplib.SMTP('smtp.office365.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(frommail, password)
        sender = frommail
        receivers = ReceiverList
        smtpObj.sendmail(sender,receivers,text)
        smtpObj.quit()

        return 'SUCCESS'
    except Exception as E:
        
        raise Exception(str(E)+ "Error ")




if __name__=='__main__':  

    SendMailWithoutAttachment('Ethicon_salesiq_team@Axtria.onmicrosoft.com','This is test function',"D9',g[tQcPZfCVx9",['shashi.kundan@axtria.com'])
  