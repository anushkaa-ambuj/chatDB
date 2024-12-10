import os
import mysql.connector
from dotenv import load_dotenv
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define prompt
PROMPT = [
    """
    You are an expert in converting English Questions to SQL Query!
    The SQL database is named STUDENT and has the following columns: NAME, YEAR, SECTION, MARKS, DEPARTMENT, and CITY.
    
    \n\n For Example,
    \n Example 1 - How many records are present in the database?,
    the SQL command will be something like SELECT COUNT(*) FROM STUDENT;
    
    \n Example 2 - What is the total number of students in each year?,
    the SQL command will be something like SELECT YEAR, COUNT(*) AS total_students
                                            FROM STUDENT
                                            GROUP BY YEAR;
    
    \n Example 3 - How many students belong to each department?,
    the SQL command will be something like SELECT DEPARTMENT, COUNT(*) AS total_students
                                            FROM STUDENT
                                            GROUP BY DEPARTMENT;
    
    \n Example 4 - Tell me about all the students studying in the Computer Science department.,
    the SQL command will be something like SELECT * FROM STUDENT
                                            WHERE DEPARTMENT = 'Computer Science';
                                            
    \n Example 5 - What is the average marks scored by students in each city?,
    the SQL command will be something like SELECT CITY, AVG(MARKS) AS average_marks
                                            FROM STUDENT
                                            GROUP BY CITY;
                                            
    \n Example 6 - Which students are from Bengaluru?,
    the SQL command will be something like SELECT * FROM STUDENT
                                            WHERE CITY = 'Bengaluru';

    Also, the SQL code should not have ``` in the beginning or end and SQL word in the output.
    """
]


# Function to load Google Gemini model and get SQL query
def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([PROMPT[0], question])
    return response.text

# Function to retrieve query results from MySQL database
def get_sql_response(query):
    # Establish connection to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',        # Replace with your MySQL server host
        user='root',    # Replace with your MySQL username
        password='Khushi!2005', # Replace with your MySQL password
        database='class'         # Replace with your MySQL database name
    )
    cursor = connection.cursor()
    
    try:
        # Execute the query
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    finally:
        # Commit and close the connection
        connection.commit()
        cursor.close()
        connection.close()

# API view
class TextToSQLAPIView(APIView):
    def post(self, request):
        question = request.data.get('question')
        if not question:
            return JsonResponse({"error": "Question is required"}, status=400)
        
        # Generate SQL query from question
        sql_query = get_gemini_response(question)
        
        try:
            # Retrieve data from MySQL database
            result = get_sql_response(sql_query)
            return JsonResponse({"query": sql_query, "result": result}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# Home view for root URL
def home_view(request):
    return HttpResponse("Welcome to the Text-to-SQL API")
