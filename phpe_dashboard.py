st. set_page_config(layout="wide")

# Getting Secrets from Streamlit Secret File
username=st.secrets['AWS_RDS_username']
password=st.secrets['AWS_RDS_password']
Endpoint=st.secrets['Endpoint']
# username=st.secrets['AWS_RDS_username']
# password=st.secrets['AWS_RDS_password']
# Endpoint=st.secrets['Endpoint']

# CONNECTED TO (AWS)Amazon-Web-Services ----> (RDS)Relational-Database-Service 
conn=pymysql.connect(
    host=Endpoint,
    user=username,
    password=password
)
# # CONNECTED TO (AWS)Amazon-Web-Services ----> (RDS)Relational-Database-Service 
# conn=pymysql.connect(
#     host=Endpoint,
#     user=username,
#     password=password
# )

# USING PhonepeDB I HAVE CREATED IN DATABASE-INSTANCE OF RDS
mycursor=conn.cursor()
sql='''USE PhonepeDB'''
mycursor.execute(sql)
# # USING PhonepeDB I HAVE CREATED IN DATABASE-INSTANCE OF RDS
# mycursor=conn.cursor()
# sql='''USE PhonepeDB'''
# mycursor.execute(sql)

# RETRIEVING DATA FROM CLOUD DATABASE
query = 'select * from Longitude_Latitude_State_Table'
Indian_States = pd.read_sql(query, con = conn)
# # RETRIEVING DATA FROM CLOUD DATABASE
# query = 'select * from Longitude_Latitude_State_Table'
# Indian_States = pd.read_sql(query, con = conn)

# DATASETS
Data_Aggregated_Transaction_df= pd.read_csv(r'data/Data_Aggregated_Transaction_Table.csv')
@@ -37,7 +37,7 @@
Coropleth_Dataset =  pd.read_csv(r'data/Data_Map_IndiaStates_TU.csv')
Data_Map_Transaction_df = pd.read_csv(r'data/Data_Map_Transaction_Table.csv')
Data_Map_User_Table= pd.read_csv(r'data/Data_Map_User_Table.csv')
#Indian_States= pd.read_csv(r'data/Longitude_Latitude_State_Table.csv')
Indian_States= pd.read_csv(r'data/Longitude_Latitude_State_Table.csv')
colT1,colT2 = st.columns([2,8])
with colT2:
    st.title(':red[PhonePe Pulse Data Analysis:signal_strength:]')
