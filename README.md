# Computer Location Tool

A Django-based command-line tool that retrieves a computer's geographic coordinates using the Windows Location Service.

## Features

- Retrieves the computer's current latitude.
- Retrieves the computer's current longitude.
- Uses the Windows Location Service.
- Does not depend on public-IP geolocation.
- Runs from the terminal using a Django management command.

## Technologies

- Python
- Django
- Windows Location API
- WinRT
- PowerShell / Command Prompt

## Project Structure

```text
computer_location/
│
├── manage.py
├── README.md
├── config/
│
└── location/
    └── management/
        └── commands/
            └── get_location.py
```
### Run the Django location command:
```python
python manage.py get_location
python test_location.py
