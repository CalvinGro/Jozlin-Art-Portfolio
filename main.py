"""
Title: Jozlin's Art Portfolio
Author: Calvin Gross
Date: 12/17/2024
Description: This website is an art portfolio for Jozlin. It was programmed in html, css, python, and used flask. 
It consists of 4 pages: an about me page, a contact page, a gallery page, and a home page. In each page there is 
a identical navbar which is sticky, meaning it stays at the top of the screen when you scroll down the page. In 
the navbar there are links to each of the other pages. In the gallery page each image darkens and grows when you
hover over it and when clicked on, it takes you to a new page with only the image. I was planning to be able to 
send email from the contact page, however I tried flask-mail and flask-mailman and neither of them worked. After
some research I realized I pretty much need to pay for an account with Mailgun or Mailtrap if I wanted to send 
emails, which I decide against.
"""


from website import create_app

# Initialize the Flask app
app = create_app()

# Ensure this code runs only if the file is executed directly
if __name__ == '__main__':
    app.run(debug=True)
