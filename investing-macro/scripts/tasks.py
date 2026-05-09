import argparse
import datetime
import os.path
import sys
from dateutil import parser as date_parser

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/tasks"]

def get_credentials():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    token_path = os.path.join(os.path.dirname(__file__), "token.json")
    creds_path = os.path.join(os.path.dirname(__file__), "credentials.json")

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(creds_path):
                print(f"Error: {creds_path} not found.")
                print("Please follow the setup instructions to download your credentials.json file.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_path, "w") as token:
            token.write(creds.to_json())
    return creds

def list_task_lists(service):
    results = service.tasklists().list(maxResults=20).execute()
    items = results.get("items", [])
    if not items:
        print("No task lists found.")
    else:
        print(f"{'Title':<30} {'ID':<20}")
        print("-" * 50)
        for item in items:
            print(f"{item['title']:<30} {item['id']:<20}")

def list_tasks(service, list_id):
    results = service.tasks().list(tasklist=list_id, showCompleted=True, showHidden=True).execute()
    items = results.get("items", [])
    if not items:
        print("No tasks found in this list.")
    else:
        print(f"{'Status':<8} {'Title':<40} {'ID':<20} {'Due':<20}")
        print("-" * 90)
        for item in items:
            status = " [x] " if item.get('status') == 'completed' else " [ ] "
            due = item.get('due', 'N/A')
            print(f"{status:<8} {item['title']:<40} {item['id']:<20} {due:<20}")

def create_task(service, list_id, title, notes=None, due=None):
    task = {'title': title}
    if notes:
        task['notes'] = notes
    if due:
        try:
            # Parse the date and format it as RFC 3339 timestamp
            dt = date_parser.parse(due)
            # Google Tasks API requires Zulu time (Z) and no offset
            task['due'] = dt.strftime('%Y-%m-%dT00:00:00.000Z')
        except ValueError:
            print(f"Error: Invalid date format for due date: {due}")
            return

    result = service.tasks().insert(tasklist=list_id, body=task).execute()
    print(f"Task created: {result['title']} (ID: {result['id']})")

def update_task_status(service, list_id, task_id, status):
    # Fetch the current task first as we need to pass the whole body back for updates
    task = service.tasks().get(tasklist=list_id, task=task_id).execute()
    task['status'] = status
    if status == 'completed':
        # Removing completed date if it exists, API will set it
        task.pop('completed', None)
    else:
        # If marking as needsAction, we must remove the completed date
        task['status'] = 'needsAction'
        task.pop('completed', None)

    result = service.tasks().update(tasklist=list_id, task=task_id, body=task).execute()
    print(f"Task updated: {result['title']} status set to {status}")

def delete_task(service, list_id, task_id):
    service.tasks().delete(tasklist=list_id, task=task_id).execute()
    print(f"Task deleted: {task_id}")

def main():
    parser = argparse.ArgumentParser(description="Google Tasks CLI Tool")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # list-lists
    subparsers.add_parser("list-lists", help="List all task lists")

    # list-tasks
    list_tasks_parser = subparsers.add_parser("list-tasks", help="List tasks in a list")
    list_tasks_parser.add_argument("list_id", help="The ID of the task list (use 'list-lists' to find it, or '@default')")

    # create-task
    create_task_parser = subparsers.add_parser("create-task", help="Create a new task")
    create_task_parser.add_argument("list_id", help="The ID of the task list")
    create_task_parser.add_argument("title", help="The title of the task")
    create_task_parser.add_argument("--notes", help="Notes for the task")
    create_task_parser.add_argument("--due", help="Due date (e.g., '2026-04-10' or 'tomorrow')")

    # complete-task
    complete_task_parser = subparsers.add_parser("complete-task", help="Mark a task as completed")
    complete_task_parser.add_argument("list_id", help="The ID of the task list")
    complete_task_parser.add_argument("task_id", help="The ID of the task")

    # reopen-task
    reopen_task_parser = subparsers.add_parser("reopen-task", help="Mark a task as needs action")
    reopen_task_parser.add_argument("list_id", help="The ID of the task list")
    reopen_task_parser.add_argument("task_id", help="The ID of the task")

    # delete-task
    delete_task_parser = subparsers.add_parser("delete-task", help="Delete a task")
    delete_task_parser.add_argument("list_id", help="The ID of the task list")
    delete_task_parser.add_argument("task_id", help="The ID of the task")

    args = parser.parse_parser_args() if hasattr(parser, 'parse_parser_args') else parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    creds = get_credentials()
    try:
        service = build("tasks", "v1", credentials=creds)

        if args.command == "list-lists":
            list_task_lists(service)
        elif args.command == "list-tasks":
            list_tasks(service, args.list_id)
        elif args.command == "create-task":
            create_task(service, args.list_id, args.title, args.notes, args.due)
        elif args.command == "complete-task":
            update_task_status(service, args.list_id, args.task_id, 'completed')
        elif args.command == "reopen-task":
            update_task_status(service, args.list_id, args.task_id, 'needsAction')
        elif args.command == "delete-task":
            delete_task(service, args.list_id, args.task_id)

    except HttpError as err:
        print(f"An HTTP error occurred: {err}")

if __name__ == "__main__":
    main()
