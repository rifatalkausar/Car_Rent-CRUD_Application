# Car Rent CRUD Application
This Car Rent CRUD Application is made as my final project in the first module of 'Programming Fundamental' in my Data Science Bootcamp with Purwadhika. The final project is to create a simple application using Python. In my case, the topic is car rental. Inside the application, it must have four main features that are create, read, update, and delete which will be explained later. Other than the four main features I add one feature to rent the car from choosing the day, car, and payment. The goal of the project is to implement what we learn in the first module which is looping, data types, and function. 

In the application, for the inventory, I have 7 columns to represent the category. The first category is car code which will be the primary key for each car and will act as the main input in all main features. The rest of the columns are car brand, car name, car manufacture year, car capacity, car rental price/day, and car availability day. All the inventory data will be stored in a list data types. 

The features that are in this application are:
1. Read: In the read features it will be divided into two options. The first one is to show all the stocks available. The second one is to show the stock based      on the inputted car code
2. Create: In the create feature is to add stock to the inventory. The rule that I set is the car code must be unique for every car.
3. Update: In the update feature you can update each stock bases on the car code that you have inputted. You can change all the categories including the unique car code itself.
4. Delete: In the delete feature you can delete inventory one by one based on the unique car code that you inputted
5. Car Renting: With this extra feature you're able to rent a car. The process will be choosing the day you want to rent, choosing the car that is available on that day, inputting how many days you want to rent, and payment.
