from Website import create_app

app = create_app()

if __name__ == '__main__':

    app.run(debug = True)

    #last line: If we change any of our python code it will automatically rerun the web server.

    
