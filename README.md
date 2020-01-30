Extracting text from an image (in png format).

1. Created a .py extension file (image-to-text.py) while takes command line argument as follows     
                    python image-to-text.py "image path"
                    
2. Created the server using django. Run the server using the following command line argument
                    manage.py runserver
                    
3. HTML page was created (mysite/mysite/templates/upload.html) in templates folder. Accepting the image and clicking on the submit button.

4. Created views.py, urls.py to pass the uploaded file to image-to-text.py file. As well returning the result from .py file to html page.

Note: Run the python file : /.../.../ python image-to-text.py "image path"
      Run html page       : /.../.../mysite  manage.py runserver
      
image-to-text.py : run seperately then file available on code session image-to-text.py "file path".
image-to-text.py : run with html file then /mysite/mysite/python image-to-text.py "file name inside the folder only".
      
