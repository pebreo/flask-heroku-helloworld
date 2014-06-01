Overview
-------
This is a simple Hello World Flask app that can be run in Heroku.

Here are the steps:

.. code:: bash
   
   # Setup Heroku keys
   $ cd ~/.ssh
   $ ssh-keygen -t rsa
   # Copy the .pub file contents and paste it to Heroku keys section
   # Then add heroku.com to ~/.ssh/config like this:
   Host heroku.com
     IdentityFile ~/.ssh/heroku-macbook
   
   $ heroku keys:add mykey.pub
   $ heroku keys
   
   # Create files
   $ touch app.py config.py requirements.txt .gitignore Procfile

   # CREATE GIT REPO
   $ git init
   $ git add .
   $ git commit -m "initial commit"
   
   # Create heroku app and associate with repo
   $ heroku create helloworld-stage1 (the url will be: http://helloworld-stage1.herokuapp.com )
   $ git remote add stage1 git@heroku.com:helloworld-stage1.git
   $ heroku config:set APP_SETTINGS=config.StagingConfig --remote stage1
   # Deploy
   $ git push stage1 master

   # Heroku commands
   $ heroku ps:scale web=1
   $ heroku ps
   $ heroku open
   $ heroku logs

Sources
------
Flask by Example part 1 and 2
http://www.realpython.com/blog/python/flask-by-example-part-1-project-setup
http://www.realpython.com/blog/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
