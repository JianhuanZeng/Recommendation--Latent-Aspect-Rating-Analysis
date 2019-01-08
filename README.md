# HotelReview_LatentAspectAnalysis
• To improve the customers’ experience of using online hotel recommendation system by developing a latent aspect rating analysis algorithm based on reviews.<br/>
• In our designed system, users could input any keywords they are interested in and their preferred weights on tags. Our system will generate a hotel recommendation map, which may help them find the best hotel according to their personalized need.<br/>
• Transfer the reviews into normalized feature matrices and a normalized rate vector with Pandas& NumPy.<br/>
• Apply Bayesian Model to hotel rates and do mathematic calculation. Specifically, apply and run VI<br/>
algorithm in MATLAB. Getting aspect rates, analyze and visualize results in Python (matplotlib).<br/>

# The Designed Model
see https://github.com/JianhuanZeng/Recommendation--Latent-Aspect-Rating-Analysis/blob/master/Latent%20Rating%20Regression%20Model.pdf

# Data processing
Text to feature<br/>
clean data at https://github.com/JianhuanZeng/Recommendation--Latent-Aspect-Rating-Analysis/tree/master/clean_data<br/>
1. The input X:<br/>
5 files of hotel feature matrix are too large to be uploaded<br/>
good_aspect_feature_matrix_1 :location<br/>
good_aspect_feature_matrix_2 :price<br/>
good_aspect_feature_matrix_3 :amenities<br/>
good_aspect_feature_matrix_4 :service<br/>
good_aspect_feature_matrix_5 :safety<br/>
2. The true y:<br/>
good_rate: normalized rates

# Result
test result at https://github.com/JianhuanZeng/Recommendation--Latent-Aspect-Rating-Analysis/tree/master/results <br/>
avg_rate.txt: the avg rate dictionary to recover real rates for the final recomendation.<br/>
testing_result.csv: the testing result from model<br/>
demo at https://github.com/JianhuanZeng/Recommendation--Latent-Aspect-Rating-Analysis/blob/master/results/demo_aspect_rates.png <br/>
and https://github.com/JianhuanZeng/Recommendation--Latent-Aspect-Rating-Analysis/blob/master/results/demo_presented2.png

