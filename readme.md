## This application presents a solution for using the flask api for video data management

# To test the application:
1- Cone the repository : https://github.com/BouchraABIDAR/video-SRD.git

2- cd api-video

3- ./startup_script.sh

4- copy this link http://127.0.0.1:5000/ in the chrome browser <centre>[link to application](https://github.com/BouchraABIDAR/video-SRD/blob/main/images/application.PNG) </centre>

5- Architecture schema that illustrates a solution to cretae an analytics OLAP on GCP that is synchronozied the OLTP

--> a- Create Cloud Function to export a Cloud SQL(OLTP) database. The function will be triggered by pubsub topic

--> b- The process export of that database to Cloud Storage

--> c- Dataproc(dataflow) job if transformation is needed

--> d- Ingesting data into bigquery(OLAP)

--> e- Cloud Scheduler Job to trigger the Cloud Function

<centre>[link to architecture ](https://github.com/BouchraABIDAR/video-SRD/blob/main/images/archi.PNG) </centre>
 





