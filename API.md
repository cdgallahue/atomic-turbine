**Read Turbine Sensor**
----
  Returns json data of the requested sensor for a given turbine.

* **URL**

  /api/turbines/:turbine_id/sensors/:sensor_id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `turbine_id=[integer]` <br />
   `sensor_id=[string]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ value : 1.5, timestamp : 1498713475 }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : err }`



**Post Turbine Data**
----
  Posts json data of the requested sensor for a given turbine.

* **URL**

  /api/turbines/:turbine_id/sensors/:sensor_id

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   `turbine_id=[integer]` <br />
   `sensor_id=[string]`

* **Data Params**

  * **Headers:**
    `{"password": "passwordhere"}`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `OK`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{"Error": "Invalid password."}`
    


**Get Turbine Heartbeat**
----
  Returns online/offline status of turbine specified

* **URL**

  /api/turbines/:turbine_id/heartbeat

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `turbine_id=[integer]`

* **Data Params**

  None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ "status": "ONLINE" }`
 
* **Error Response:**

  * **Code:** 200 <br />
    **Content:** `{ "status": "OFFLINE" }`
    
    

**Post Turbine Heartbeat**
----
  Returns online/offline status of turbine specified

* **URL**

  /api/turbines/:turbine_id/heartbeat

* **Method:**

  `POST`
  
*  **URL Params**

   **Required:**
 
   `turbine_id=[integer]`

* **Data Params**

  * **Headers:**
    `{"password": "passwordhere"}`

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `OK`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{"Error": "Invalid password."}`
