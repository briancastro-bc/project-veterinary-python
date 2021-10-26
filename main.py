from src.app import Application

def main():
    app = Application.init_app()
    app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'], load_dotenv=True)

if __name__ == '__main__':
    main()