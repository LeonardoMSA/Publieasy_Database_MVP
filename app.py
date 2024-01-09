import os
from DatabaseProject import app, db
from DatabaseProject.models import Count

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
