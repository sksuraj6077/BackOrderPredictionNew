# Back Order Prediction




## About The Project 

The "Back Order Prediction" project aims to forecast and anticipate instances of back orders within a given inventory system. Back orders occur when a company's demand for a particular product exceeds the available supply, resulting in unfulfilled orders. The significance lies in the ability to preemptively identify and manage potential back orders, allowing businesses to optimize inventory management, minimize stockouts, and enhance customer satisfaction.


# Objectives:

Prediction Focus: 
    This project focuses on leveraging machine learning or statistical models to predict the likelihood of back orders for specific products or SKUs (Stock Keeping Units) within a defined timeframe.

Significance: 
    Predicting back orders facilitates proactive decision-making in inventory management, enabling businesses to:

        Allocate resources efficiently by anticipating demand surges.
        Minimize lost sales and revenue due to stockouts.
        Optimize stock levels, reducing excess inventory and associated costs.
        Enhance customer satisfaction by ensuring timely order fulfillment.

## About the Dataset

This dataset gives information related to Back Order. The dataset contains 22 columns, target is the class variable which is affected by the other 21 columns. Here the aim is to classify the target variable to (yes\no) using different machine learning algorithms and find out which algorithm is suitable for this dataset.
<br><be>

<h3>Attributes:</h3>

 - national_inv
 - lead_time
 - in_transit_qty
 - forecast_3_month
 - forecast_6_month
 - forecast_9_month
 - sales_1_month
 - sales_3_month
 - sales_6_month
 - sales_9_month
 - min_bank
 - potential_issue
 - pieces_past_due
 - perf_6_month_avg
 - perf_12_month_avg
 - local_bo_qty
 - deck_risk
 - oe_constraint
 - ppap_risk
 - stop_auto_buy
 - rev_stop

## Built With

 - Pandas
 - Numpy
 - Scikit-Learn
 - Seaborn
 - Matplotlib
 - Flask

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Option 1: Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
        git clone https://github.com/sksuraj6077/BackOrderPredictionNew.git

2. **Create a Virtual Environment** (Optional but recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```
     conda create -p <Environment_Name> python==<python version> -y
     ```

3. **Activate the Virtual Environment** (Optional)
   - Activate the virtual environment based on your operating system:
       ```
       conda activate <Environment_Name>/
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```
     cd [project_directory]
     ```
   - Run the following command to install project dependencies:
     ```
     pip install -r requirements.txt
     ```

5. **Run the Project**
   - Start the project by running the appropriate command.
     ```
     python app.py
     ``

6. **Access the Project**
   - Open a web browser or the appropriate client to access the project.
  
<br><br>

## Contributing

Contributions are what makes the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request


## Support or Contact

Aniket Patil - [@patil8624972776@gmail.com] (patil8624972776@gmail.com)

Suraj Kawathale - [@surajkawathale0122@gmail.com] (surajkawathale0122@gmail.com)

Ankita yetale - [@ankiyetale7997@gmail.com] (ankiyetale7997@gmail.com)


## Acknowledgements

We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.
