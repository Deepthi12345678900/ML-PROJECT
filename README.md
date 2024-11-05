SOCIAL MEDIA USER CLASSIFICATION  

In my project, I developed a Flask-based web application designed to classify social media users 
from platforms like Instagram and Twitter into categories such as regular users, bots, influencers, 
or fake accounts. The project starts with the user providing a social media profile URL as input. I 
chose Flask because it’s lightweight and efficient for web development, making it easy to handle 
user requests and manage inputs. Flask facilitated the connection between the user’s input and 
the back-end processing where the data was fetched and analyzed. 
To extract the necessary data from Instagram and Twitter profiles, I integrated Instaloader for 
Instagram and Tweepy for Twitter. These tools were selected because they allow for seamless 
access to public profile information like follower counts, posts, and whether the account is 
verified. For example, Instaloader helps scrape Instagram data like the number of followers, 
engagement metrics, and account verification status. Tweepy, on the other hand, handles similar 
tasks for Twitter by using its API to retrieve follower and following counts, tweet activity, and 
account metadata. Both tools are well-documented and popular for these tasks, making them 
reliable choices for data extraction. 
Once the data is fetched, it is passed through a preprocessing phase where libraries like Pandas 
and NumPy are used to clean and structure it. Pandas is particularly useful here for organizing 
the data into a format that the machine learning model can work with, while NumPy efficiently 
handles numerical operations such as normalizing the follower and engagement metrics. This 
step ensures that all the input data is ready for the next stage: classification. 
For the classification task, I implemented a neural network model using Keras with a 
TensorFlow backend. This deep learning model was selected because of its ability to handle 
complex data relationships and its flexibility with numerical inputs like follower counts and 
engagement rates. The neural network is a fully connected architecture that includes several 
layers and dropout layers to prevent overfitting, which helps improve the model's generalization 
to unseen data. The model was trained on a dataset of labeled social media profiles, with each 
profile categorized as a regular user, bot, influencer, or fake account. After tuning the model, I 
achieved an impressive 96% classification accuracy. The neural network was particularly well
suited for this task because it can capture subtle patterns in the data, such as engagement trends 
and user activity, which are important for differentiating between real and fake accounts. 
One of the main challenges in this project was handling API rate limits, especially since both 
Instagram and Twitter impose restrictions on how many requests can be made in a certain time 
frame. To address this, I implemented a custom API request handler. This handler monitored 
the number of requests being made to both platforms, ensuring that the app didn’t exceed the 
API rate limits. For example, each time Instaloader or Tweepy made a request to Instagram or 
Twitter, the handler would log it. If the request count was nearing the limit, the handler would 
enforce a timed delay to prevent overloading the API. This delay ensured that the app remained 
functional even when handling large amounts of data, preventing it from being blocked by the API. 
This was crucial for maintaining the app’s performance and ensuring that users could still receive 
classifications without interruptions, even when multiple requests were made simultaneously. 
Once the data was classified, the results were displayed back to the user in an intuitive and user
friendly interface. For this, I used a combination of HTML, CSS, and JavaScript to create the 
front-end. Flask handled the routing of data between the machine learning model and the front
end, while HTML and CSS were used to design the interface, making it easy for users to input their 
profile URLs and view the results in real-time. 
Another challenge was dealing with imbalanced data since the majority of users in the dataset 
were regular users, and bots or fake accounts were underrepresented. To solve this, I used 
resampling techniques to balance the dataset and also adjusted class weights in the neural 
network to ensure that the model didn’t favor the majority class. This allowed the model to 
perform well across all categories and not just classify most profiles as regular users. 
In summary, this project successfully integrated multiple tools and technologies to build a 
functional application. Flask was used for web development, Instaloader and Tweepy for data 
extraction, Pandas and NumPy for preprocessing, and Keras with TensorFlow for classification. 
Each tool was chosen for its ability to efficiently handle specific tasks, and the result was a robust 
application capable of classifying social media profiles with high accuracy. The project not only 
demonstrated technical skills in web development and machine learning but also tackled real
world challenges like API rate limits and imbalanced data effectively.
