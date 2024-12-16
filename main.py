from website import create_app





app = create_app()

# app.config['SECRET_KEY'] = 'wreoigerwoigiufdpoifjfdewrpoijro cxmvewfiwoiefpo'
# app.config['Mail_SERVER'] = 'smtp.gmail.com'
# app.config['Mail_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'calvingwrestle@gmail.com'
# app.config['MAIL_PASSWORD'] = 'SweetSawfi5h'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True

if __name__ == '__main__':
    app.run(debug=True)
