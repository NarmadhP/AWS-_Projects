we will be deploying full stack app to aws with EC2,RDS and S3

STEPS
1. Create EC2 instance and allow https traffic from and to internet
2. note the DNS of instance after launch
3. then move to db creation
4. we will choose free tier for now
5. choose connect to ec2 instance and choose the ec2 instance we created
6. note the endpoint and port as well
7. then we can connect to the instance using instance connect or ssh
8. then we have to execute the following for a basic php page

   sudo dnf update -y
   sudo dnf install -y httpd php php-mysqli mariadb105
   sudo systemctl start httpd
         You can test that your web server is properly installed and started. To do this, enter the public Domain Name System (DNS) name of your EC2 instance in the address bar of a web browser,
         for example: http://ec2-42-8-168-21.us-west-1.compute.amazonaws.com. If your web server is running, then you see the Apache test page.
   sudo systemctl enable httpd

   While still connected to your EC2 instance, change the directory to /var/www and create a new subdirectory named inc.
      cd /var/www
      mkdir inc
      cd inc
   vi dbinfo.inc
       add these
               <?php
                define('DB_SERVER', 'db_instance_endpoint');
                define('DB_USERNAME', 'tutorial_user');
                define('DB_PASSWORD', 'master password');
                define('DB_DATABASE', 'sample');
                ?>
   cd /var/www/html
   SamplePage.php
     add the SamplePage.php script available in the folder
Verify that your web server successfully connects to your DB instance by opening a web browser and browsing to http://EC2 instance endpoint/SamplePage.php,
  for example: http://ec2-12-345-67-890.us-west-2.compute.amazonaws.com/SamplePage.php
