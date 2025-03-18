from django.shortcuts import render
import datetime
from django.http import HttpResponse
import subprocess
import getpass
def htop_view(request):
    name = "Sheik Rizwan"
    username = getpass.getuser()
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    
    try:
        process_output = subprocess.run(["top", "-b","-n","1"],capture_output=True,text=True).stdout  # Fetch all processes
    except Exception as e:
        process_output = f"Error fetching processes: {str(e)}"
    
    html_content = f"""
    <h1>HTOP Endpoint</h1>
    <p><strong>Name:</strong> {name}</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time (IST):</strong> {server_time}</p>
    <pre>{process_output}</pre>
    """

    return HttpResponse(html_content)
