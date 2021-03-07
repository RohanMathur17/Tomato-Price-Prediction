import pickle
import streamlit as st



 
model = pickle.load(open('model.pkl' , 'rb'))

html_temp = """
			<body style= "background-color:lightblue;">
			<div style = "background-color:lightblue;padding:10px">
			<h2 style = "color:white;text-align:center;">Modal Price Prediction</h2>
			</div>
			</body>
			"""

#st.markdown(bg , unsafe_allow_html = True)
st.markdown(html_temp , unsafe_allow_html = True)




st.markdown('### Choose your Max Price & Min Price')



Max_Price= st.number_input("Max Price") 
Min_Price = st.number_input("Min Price")

if st.button("Predict"): 
	result = model.predict([[Max_Price , Min_Price]])

	st.success('Your Modal Price is {} Rs'.format(result))

	st.balloons()

