from tool.employee_dao import EmployeeDAO
from openai import OpenAI
import json
client = OpenAI()

class FinanceChatbot:
    def __init__(self):
        pass

    def get_employee_salary(self, employee_name):
        tools = [
            {
            "type": "function",
            "function": {
                "name": "get_employee_salary",
                "description": "Get employee salary from MySQL database",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Employee name"
                        }
                    },
                    "required": ["name"]
                }
            }
            }
            ]
        response = client.chat.completions.create(
            model="gpt-5",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant for finance department. You can get employee salary information from MySQL database. The employee table has two columns: name and salary."},
                {"role": "user", "content": f"Get salary for employee: {employee_name}"}
            ],
            tools=tools
        )
        tool_calls = getattr(response.choices[0].message, "tool_calls", None)
        if tool_calls:
            tool_call = tool_calls[0]
            arguments = json.loads(tool_call.function.arguments)
            employee_name = arguments["name"]
            dao = EmployeeDAO()
            salary = dao.get_employee_salary(employee_name)
            return f"The salary of {employee_name} is {salary}"
        else:
            return "No tool call returned by the model."
    
    def get_employee_details(self, query):
        tools = [
            {
            "type": "function",
            "function": {
                "name": "execute_query",
                "description": "Execute SQL query on onlineedu database",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "SQL query to execute"
                        }
                    },
                    "required": ["query"]
                }
            }
            }
            ]
        response = client.chat.completions.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are a data assistant. Generate SQL queries for the employees table."},
                {"role": "user", "content": f"Execute SQL query: {query}"}
            ],
            tools=tools
        )
        tool_calls = getattr(response.choices[0].message, "tool_calls", None)
        if tool_calls:
            tool_call = tool_calls[0]
            arguments = json.loads(tool_call.function.arguments)
            sql_query = arguments["query"]
            dao = EmployeeDAO()
            result = dao.execute_query(sql_query)
            
            messages = [
            {"role":"user","content":query},
            response.choices[0].message,
            {
            "role":"tool",
            "tool_call_id": tool_call.id,
            "content": result
            }
            ]
            final = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
            )
            return final.choices[0].message.content
        else:           
            return "No tool call returned by the model."