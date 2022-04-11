## This application presents a solution for using the flask api for video data management

# Steps to follow :
1- Cone the repository : git clone https://github.com/BouchraABIDAR/video-SRD.git

2- cd video-SRD

3- ./startup_script.sh

4- Once the message "Running on http://127.0.0.1:5000/" appears in your terminal click on this link http://127.0.0.1:5000/ to visualize the application ([link to application](https://github.com/BouchraABIDAR/video-SRD/blob/main/images/application.PNG))

5- Architecture schema that illustrates a solution to cretae an analytics OLAP on GCP that is synchronozied the OLTP ([link to architecture ](https://github.com/BouchraABIDAR/video-SRD/blob/main/images/archi.PNG))

--> a- Create Cloud Function to export a Cloud SQL(OLTP) database. The function will be triggered by pubsub topic

--> b- The process export of that database to Cloud Storage

--> c- Dataproc(dataflow) job if transformation is needed

--> d- Ingesting data into bigquery(OLAP)

--> e- Cloud Scheduler Job to trigger the Cloud Function


 





