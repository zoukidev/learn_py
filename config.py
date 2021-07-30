import configparser

def load():
    parser = configparser.ConfigParser()
    parser.read('./test.ini')
    print('backoffice_url:', parser['SQL'].get('backoffice_url'))