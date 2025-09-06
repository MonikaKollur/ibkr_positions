1. Start IBKR proxy  if not already running
   cd ibportal
   ./runDocker

2. login to proxy ( once every week)

    from browser https://localhost:5000/

3. Setup Client
   //one time setup AWS access keys
   export AWS_ACCESS_KEY_ID=<your_access_key>
   export AWS_SECRET_ACCESS_KEY=<your secret access key>
   create a d3 bucket "portfolio-data" in aws

4. Run Client

   cd ibportal_client 
  ./createDockerClientImage
  ./runDockerClient

   
52. If you need to clean up all docker images/procceses
   cd ibportal
   ./cleanDocker
   cd ibportal_client
   ./cleanDocker

